# MHD-Energy-Diagnostics
A Python-based advanced Magnetohydrodynamic (MHD) wave simulator featuring animated plasma wave propagation, Alfvén speed analysis, energy diagnostics, shock detection, and phase-space visualization.

Overview

Advanced MHD Wave Simulator is a Python-based scientific visualization project that demonstrates the propagation of Magnetohydrodynamic (MHD) waves in a plasma medium.

The simulator numerically evolves velocity and magnetic field perturbations using finite-difference methods while providing real-time visualization of important plasma quantities such as:

- Velocity Profile
- Magnetic Field Profile
- Density Distribution
- Alfvén Speed
- Kinetic Energy Density
- Magnetic Energy Density
- Total Energy Density
- Shock Detection
- Phase Space Dynamics

The project is designed for students, educators, and physics enthusiasts interested in computational plasma physics and magnetohydrodynamics.

---

Features

Wave Propagation

Simulates coupled evolution of velocity and magnetic field perturbations.

Alfvén Speed Analysis

Computes local Alfvén velocity:

v_A = B / √(μ₀ρ)

Energy Diagnostics

Kinetic Energy Density

E_k = ½ρv²

Magnetic Energy Density

E_B = B² / (2μ₀)

Total Energy Density

E_total = E_k + E_B

Shock Detection

Detects steep gradients in the velocity field:

Shock = |∂v/∂x|

Phase Space Visualization

Displays velocity versus magnetic field dynamics.

Real-Time Animation

Animated evolution of MHD waves using Matplotlib's FuncAnimation.

---

Physics Background

Magnetohydrodynamics (MHD) studies the interaction between electrically conducting fluids and magnetic fields.

Applications include:

- Solar Physics
- Space Weather
- Fusion Reactors
- Astrophysical Jets
- Interstellar Plasma Dynamics
- Magnetospheres

This simulator demonstrates simplified Alfvén-wave-like behavior in a one-dimensional plasma.

---

Technologies Used

- Python 3
- NumPy
- Matplotlib

---

Move into the project directory:

cd Advanced-MHD-Wave-Simulator

Install dependencies:

pip install numpy matplotlib

---

Running the Simulation

python mhd_wave_simulator.py

---

Visual Outputs

The simulator generates:

- Velocity Profile
- Magnetic Field Profile
- Density Profile
- Alfvén Speed Plot
- Kinetic Energy Density
- Magnetic Energy Density
- Total Energy Density
- Phase Space Diagram

All quantities evolve dynamically during the simulation.

---

Future Improvements

- 2D MHD Simulations
- Plasma Density Heatmaps
- Magnetic Field Line Tracing
- Magnetosonic Wave Modes
- Magnetic Reconnection Models
- GPU Acceleration
- Data Export to CSV/HDF5
- MP4 and GIF Export Support

---

Educational Value

This project can be used for:

- Computational Physics
- Plasma Physics Courses
- Numerical Methods Education
- Scientific Visualization Projects
- Undergraduate Research Demonstrations

---

License

MIT License

---

Author

Developed as a computational plasma physics and scientific visualization project using Python.
