# Ripple Effect Animation with Manim

The motivation for this project start while I was walking back from work. On a day of heavy overcast and light rain, I was walking over a bridge that stood tall over a calm river. I noticed the subtle ripples in the water, and was curious on how one would simulate that. Here's my attempt of trying to simulate the effect in Python Manim.

This Python script utilizes the Manim library to create a visually appealing ripple effect animation. The animation simulates raindrops falling onto a surface, creating ripples that expand and fade over time. The script is structured into a class RippleEffect that inherits from Manim's Scene class, providing a framework for generating the animation.

_NOTE: This code is not very well optimized. This is the best way I could come up with to do something like this in Manim. Perhaps another framework or language is would be better suited for a task like this one._

### Features
__Customizable Parameters__: The script includes several parameters that can be adjusted to modify the appearance and behavior of the ripple effect. These include the damping factor, resolution, number of batches, and runtime for each animation frame.
__Dynamic Raindrop Generation__: Raindrops are generated in batches with random positions and intensities, simulating a natural rain effect.
Efficient Ripple Simulation: The ripple effect is achieved by calculating pixel values based on the surrounding pixels, creating a realistic water surface disturbance.
## Key Components
initializeVariables(): Initializes variables and sets up the parameters for the ripple algorithm. It also prepares the initial state of the animation with two arrays representing the current and previous states of the water surface.
construct(): Orchestrates the overall animation process, including generating raindrops in batches and animating the resulting ripples.
animateRaindrop(dropCut): Simulates the ripple effect for a given number of frames (dropCut). It updates the water surface state and creates a transition between the current and previous states.
## Usage
To use this script, you must have Manim installed in your Python environment. Once Manim is set up, you can run the script to generate the ripple effect animation. The script is highly customizable, allowing you to experiment with different parameters to achieve various visual effects.

### Installation
Ensure you have Python installed on your system.
Install Manim using pip:
```bash
pip install manim
Run the script with Manim:
manim -p -ql your_script_name.py RippleEffect
```
## Customization
You can customize the animation by modifying the parameters in the initializeVariables() method. For example, changing the damping value will affect how quickly the ripples fade. Adjusting the batches and runTime can alter the density and speed of the raindrops.

### Note
This script is designed for educational and entertainment purposes. Feel free to explore and modify the code to create your own unique animations with Manim.

## Additional Resources
 - [The Coding Train: Coding Challenge #102](https://youtu.be/BZUdGqeOD0w?si=NoatKlIv-sW-UUr7)
 - [Original Article](https://web.archive.org/web/20160418004149/http://freespace.virgin.net/hugo.elias/graphics/x_water.htm)
 - [Manim Community Library](https://www.manim.community)

