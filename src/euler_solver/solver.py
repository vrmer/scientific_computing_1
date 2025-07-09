"""
Simulates values of the Lorenz model of atmospheric convection
using the Euler ODE solver.
"""

import numpy as np
from .utils import save_arrays
from .parameters import Parameters
from .equations import equation_x, equation_y, equation_z

# TODO: write tests


def solver(
    params: Parameters,
    output_path: str|None = None):
    """
    Euler solver algorithm.
    
    Parameters:
        params: contains the necessary parameters for the Euler solver algorithm
        
        output_path: if it is filled, it saves arrays to the target path
        
    Output:
        x_array: array of positions in dimension x during simulation (np.array)
        y_array: array of positions in dimension y during simulation (np.array)
        z_array: array of positions in dimension z during simulation (np.array)
    """
    # Define output arrays
    x_array = np.zeros(params.N)
    y_array = np.zeros(params.N)
    z_array = np.zeros(params.N)
    
    # define the initial positions
    x, y, z = params.x, params.y, params.z
    
    # Simulate over N time steps
    for i in range(params.N):
        x = equation_x(x, y, params.sigma, params.t_delta)
        y = equation_y(x, y, z, params.rho, params.t_delta)
        z = equation_z(x, y, z, params.beta, params.t_delta)
        
        x_array[i] = x
        y_array[i] = y
        z_array[i] = z
        
    if output_path:
        save_arrays([x_array, y_array, z_array], output_path)
        
    return x_array, y_array, z_array
