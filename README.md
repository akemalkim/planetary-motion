# Planetary Motion Simulation

## Project Overview
This project simulates the motion of planets based on classical Newtonian mechanics and gravitational forces. The simulation is designed to model planetary orbits, taking into account the gravitational interactions between celestial bodies. This project provides a visual and computational exploration of planetary motion and can be used to study orbital mechanics, gravitational dynamics, and the behavior of planets in a solar system.

## Objectives
- To simulate the orbits of planets around a star using Newton’s laws of motion and gravity.
- To visualize planetary trajectories and analyze orbital properties such as eccentricity, velocity, and distance from the star.
- To allow for interactive exploration of different planetary systems and initial conditions.

## Features
- Simulation of multiple planets orbiting a central star.
- Interactive adjustment of initial conditions, such as planet mass, velocity, and position.
- Visualization of planetary orbits using 2D or 3D plots.
- Calculation of key orbital parameters such as velocity, acceleration, and angular momentum.

## Results
The simulation demonstrates the stable orbits of planets under gravitational forces, reproducing elliptical and circular trajectories as predicted by Kepler's laws. It can be used to observe phenomena such as orbital resonances and variations in velocity due to the elliptical nature of orbits.

For more detailed information and a discussion of the results, refer to the PDF report in this repository: [Detailed Report](./detailed_report.pdf).

## Methodology
1. **Equations of Motion:** The simulation is based on solving Newton’s second law of motion and the law of universal gravitation. The force acting on each planet is calculated using:
   \[
   F = \frac{G M m}{r^2}
   \]
   where \(F\) is the gravitational force, \(G\) is the gravitational constant, \(M\) is the mass of the star, \(m\) is the mass of the planet, and \(r\) is the distance between the star and the planet.

2. **Numerical Integration:** The equations of motion are solved using numerical methods such as the Euler or Runge-Kutta method to compute the position and velocity of each planet over time.

3. **Visualization:** Matplotlib is used to create plots of the planetary orbits. The simulation can produce both 2D and 3D visualizations, allowing for a detailed study of the motion.

## Installation
To run the simulation, make sure the following Python packages are installed:
- NumPy
- Matplotlib
- SciPy

You can install the required packages using pip:
```bash
pip install numpy matplotlib scipy
