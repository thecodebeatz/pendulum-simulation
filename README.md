# Pendulum Simulation: Solving Differential Equations with Python
This repository contains a Python script that models the motion of a pendulum by solving its second-order differential equation. Using numerical methods from SciPy and visualization tools from Matplotlib, this simulation explores how different initial angles affect the pendulum's motion over time.

## Context

This project illustrates a practical application of Python for solving and visualizing differential equations, specifically for modeling a pendulum. It showcases the difference in behavior for various starting angles, demonstrating how a pendulum's period varies with amplitude.

## How it Works

The pendulum's motion is modeled as a system of first-order differential equations derived from the original second-order equation. Using the `scipy.integrate.ode` solver, the script computes the motion for different initial angles and plots the results over time. The script uses numerical integration to solve the system of equations with the Runge-Kutta 4,5 method (`dopri5`). The results are then visualized using Matplotlib, where each pendulum's motion, starting from a different angle, is shown in unique colors. The simulation assumes Earth's gravity (9.8 m/s²) and a pendulum length of 1 meter.

## Installation

First, install Python if you haven't done so already. You can download Python from the official website. Afterward, you will need to install the required libraries for the simulation, which are NumPy, SciPy and Matplotlib. You can do this via pip by running `pip install scipy` and `pip install matplotlib`.

## Running the Simulation

Once you have the necessary dependencies installed, clone this repository. After cloning, navigate to the directory where the project is stored and run the simulation script using Python. For example:

```bash
cd pendulum-simulation
python pendulum_simulation.py
```

Running the script will generate a plot that shows the motion of the pendulum for several initial angles. The plot visualizes how the pendulum behaves when dropped from angles such as 5°, 10°, 15°, 30°, 45°, 60°, and 90°.

## Output

The main output of the simulation is a graph that shows how the angle of the pendulum (θ) changes over time for different initial angles. As the initial angle increases, the pendulum’s period also increases, deviating from the simple harmonic motion approximation that holds for small angles.

## License

This project is licensed under the Creative Commons Attribution 3.0 Unported License. More information about the license can be found at http://creativecommons.org/licenses/by/3.0/.

## Author

This project was created by Tomás Jaramillo Quintero. For more context and a detailed explanation of the pendulum problem, feel free to visit Code Beats.