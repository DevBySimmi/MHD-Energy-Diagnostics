import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ==========================================
# PARAMETERS
# ==========================================

nx = 1000
dx = 0.1
dt = 0.01

B0 = 1.0
rho0 = 1.0
mu0 = 1.0

# ==========================================
# INITIAL CONDITIONS
# ==========================================

x = np.linspace(0, (nx - 1) * dx, nx)

v = np.sin(2 * np.pi * x / (nx * dx))

B = B0 + 0.1 * np.sin(
    2 * np.pi * x / (nx * dx)
)

rho = rho0 + 0.05 * np.sin(
    2 * np.pi * x / (nx * dx)
)

# Initial Alfvén speed
vA = B / np.sqrt(mu0 * rho)

# ==========================================
# UPDATE FUNCTION
# ==========================================

def update_wave(v, B, rho, dt, dx):

    vA = B / np.sqrt(mu0 * rho)

    dv = -vA * np.gradient(B, dx) * dt
    dB = -vA * np.gradient(v, dx) * dt

    v += dv
    B += dB

    return v, B

# ==========================================
# FIGURE SETUP
# ==========================================

fig, axs = plt.subplots(
    4,
    2,
    figsize=(16, 12)
)

fig.suptitle(
    "Advanced MHD Wave Simulator",
    fontsize=18
)

# ------------------------------------------
# Velocity
# ------------------------------------------

line_v, = axs[0, 0].plot(
    x,
    v,
    color='blue',
    label='Velocity'
)

axs[0, 0].set_title("Velocity Profile")
axs[0, 0].grid()
axs[0, 0].legend()

# ------------------------------------------
# Magnetic Field
# ------------------------------------------

line_B, = axs[0, 1].plot(
    x,
    B,
    color='red',
    label='Magnetic Field'
)

axs[0, 1].set_title("Magnetic Field Profile")
axs[0, 1].grid()
axs[0, 1].legend()

# ------------------------------------------
# Density
# ------------------------------------------

line_rho, = axs[1, 0].plot(
    x,
    rho,
    color='orange',
    label='Density'
)

axs[1, 0].set_title("Density Profile")
axs[1, 0].grid()
axs[1, 0].legend()

# ------------------------------------------
# Alfvén Speed
# ------------------------------------------

line_vA, = axs[1, 1].plot(
    x,
    vA,
    color='purple',
    label='Alfvén Speed'
)

axs[1, 1].set_title("Alfvén Speed")
axs[1, 1].grid()
axs[1, 1].legend()

# ------------------------------------------
# Kinetic Energy
# ------------------------------------------

Ek = 0.5 * rho * v**2

line_Ek, = axs[2, 0].plot(
    x,
    Ek,
    color='green',
    label='Kinetic Energy'
)

axs[2, 0].set_title("Kinetic Energy Density")
axs[2, 0].grid()
axs[2, 0].legend()

# ------------------------------------------
# Magnetic Energy
# ------------------------------------------

Em = B**2 / (2 * mu0)

line_Em, = axs[2, 1].plot(
    x,
    Em,
    color='magenta',
    label='Magnetic Energy'
)

axs[2, 1].set_title("Magnetic Energy Density")
axs[2, 1].grid()
axs[2, 1].legend()

# ------------------------------------------
# Total Energy
# ------------------------------------------

Etotal = Ek + Em

line_Et, = axs[3, 0].plot(
    x,
    Etotal,
    color='black',
    label='Total Energy'
)

axs[3, 0].set_title("Total Energy Density")
axs[3, 0].grid()
axs[3, 0].legend()

# ------------------------------------------
# Phase Space
# ------------------------------------------

phase_line, = axs[3, 1].plot(
    v,
    B,
    color='cyan'
)

axs[3, 1].set_title("Phase Space (v vs B)")
axs[3, 1].set_xlabel("Velocity")
axs[3, 1].set_ylabel("Magnetic Field")
axs[3, 1].grid()

plt.tight_layout()

# ==========================================
# ANIMATION
# ==========================================

def animate(frame):

    global v, B

    v, B = update_wave(
        v,
        B,
        rho,
        dt,
        dx
    )

    vA_local = B / np.sqrt(mu0 * rho)

    Ek = 0.5 * rho * v**2
    Em = B**2 / (2 * mu0)
    Etotal = Ek + Em

    shock = np.abs(
        np.gradient(v, dx)
    )

    line_v.set_ydata(v)
    line_B.set_ydata(B)
    line_rho.set_ydata(rho)

    line_vA.set_ydata(vA_local)

    line_Ek.set_ydata(Ek)
    line_Em.set_ydata(Em)

    line_Et.set_ydata(Etotal)

    phase_line.set_data(v, B)

    axs[3, 0].set_title(
        f"Total Energy Density | "
        f"Max Shock = {shock.max():.3f}"
    )

    return (
        line_v,
        line_B,
        line_rho,
        line_vA,
        line_Ek,
        line_Em,
        line_Et,
        phase_line
    )

ani = FuncAnimation(
    fig,
    animate,
    frames=1000,
    interval=20,
    blit=True
)

plt.show()