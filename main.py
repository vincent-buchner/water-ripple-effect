from manim import *
from random import randint, random


class RippleEffect(Scene):

    # Set resolution of the video
    config.pixel_width = 500
    config.pixel_height = 500

    def initializeVariables(self):

        # Setting up the parameters for the ripple algorithm to work
        self.damping = 0.95
        self.width = config.pixel_width
        self.height = config.pixel_width
        self.currentArray = np.zeros((self.width, self.height))
        self.previousArray = np.zeros((self.width, self.height))
        self.batches = 10
        self.runTime = 0.01
        self.resolutionScale = 250

        # Array -> Image -> Transition(Image1, Image2)
        self.currentImage = ImageMobject(
            self.currentArray, scale_to_resolution=2).set_resampling_algorithm(RESAMPLING_ALGORITHMS["box"])
        self.previousImage = ImageMobject(
            self.previousArray, scale_to_resolution=2).set_resampling_algorithm(RESAMPLING_ALGORITHMS["box"])

    def construct(self):

        # Initialize the variables
        self.initializeVariables()

        # Takes the raindrops through in batches
        for _ in range(self.batches):

            # Random amount of drops for the batch
            for _ in range(randint(5, 20)):

                # Create a drop at a random position on screen
                self.previousArray[randint(
                    0, self.width - 1), randint(0, self.height - 1)] = randint(100, 255)

            # Starts the animation and lets it go until the random time
            self.animateRaindrop(randint(25, 50))

        # Finishes off the remaining bit
        self.animateRaindrop(65)

    def animateRaindrop(self, dropCut):

        # GAME LOOP - per say
        for _ in range(dropCut):

            # Loop over each pixel in the matrix
            for i in range(self.width - 1):
                for j in range(self.height - 1):

                    # Calculates the value of the current pixel relative to surrounding previous pixels
                    self.currentArray[i][j] = (
                        self.previousArray[i-1][j] +
                        self.previousArray[i+1][j] +
                        self.previousArray[i][j-1] +
                        self.previousArray[i][j+1]
                    ) / 2 - self.currentArray[i][j]

                    # Apply damping
                    self.currentArray[i][j] *= self.damping

            # Create the images from the calculate arrays and perform a transition
            self.currentImage = ImageMobject(
                self.currentArray, scale_to_resolution=self.resolutionScale).set_resampling_algorithm(RESAMPLING_ALGORITHMS["box"])
            self.previousImage = ImageMobject(
                self.previousArray, scale_to_resolution=self.resolutionScale).set_resampling_algorithm(RESAMPLING_ALGORITHMS["box"])
            self.play(Transform(self.previousImage,
                      self.currentImage), run_time=self.runTime)

            # Update and swap the values for next loop
            self.previousArray, self.currentArray = self.currentArray, self.previousArray
