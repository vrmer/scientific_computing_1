"""
Generated using ChatGPT on 10/07/2025
"""

import numpy as np
import matplotlib.pyplot as plt

# Lorenz system parameters
sigma = 10.0
beta = 8.0 / 3.0
rho = 6

# Time settings
dt = 0.01         # Time step
num_steps = 50_000 # Number of steps

# Initialize arrays
x = np.zeros(num_steps)
y = np.zeros(num_steps)
z = np.zeros(num_steps)

# Initial conditions
x[0], y[0], z[0] = 0, 1, 1.05

# Euler's method to solve the Lorenz system
for i in range(num_steps - 1):
    dx = sigma * (y[i] - x[i])
    dy = x[i] * (rho - z[i]) - y[i]
    dz = x[i] * y[i] - beta * z[i]
    
    x[i+1] = x[i] + dt * dx
    y[i+1] = y[i] + dt * dy
    z[i+1] = z[i] + dt * dz

# Plot the Lorenz attractor
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, lw=0.5)
ax.set_title("Lorenz Attractor using Euler's Method")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
