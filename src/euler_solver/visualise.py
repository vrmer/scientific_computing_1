"""
Scripts for visualising the Lorenz attractor simulations.
"""

from typing import Tuple
import matplotlib.pyplot as plt
from .utils import load_arrays, euclidean_distances, colored_line_between_pts


def plot_2d_arrays(
    target_path: str,
    dimensions: Tuple[str],
    output_path: str = None
    ):
    """
    Plots two dimensions of the points of the Lorenz attractor.
    
    Parameters:
        target_path: input path to the positions (str)
        dimensions: two from 'x', 'y', or 'z' (tuple)
        output_path: output path to save the plot to (str)
    """
    assert len(dimensions) == 2, "Make sure to provide only two dimensions to the function."
    x_array, y_array, z_array = load_arrays(target_path)
    array_dict = {"x": x_array, "y": y_array, "z": z_array}
    
    target_arrays = array_dict[dimensions[0]], array_dict[dimensions[1]]
    
    fig, ax1 = plt.subplots()
    
    # colour based on Euclidean distance
    distances = euclidean_distances(*target_arrays)
    lines = colored_line_between_pts(*target_arrays, distances, ax1, linewidth=4, cmap="plasma")
    fig.colorbar(lines)
    
    ax1.set_xlabel(f"Positions in dimension {dimensions[0]}")
    ax1.set_ylabel(f"Positions in dimension {dimensions[1]}")
    ax1.plot(*target_arrays)
    
    if output_path:
        plt.savefig(output_path)
    else:
        plt.show()
    
    
def plot_3d_arrays(
    target_path: str,
    output_path: str = None
    ):
    """
    Plots three dimensions of the points of the Lorenz attractor.
    
    Parameters:
        target_path: input path to the positions (str)
        output_path: output path to save the plot to (str)
    """
    x_array, y_array, z_array = load_arrays(target_path)
    ax = plt.figure().add_subplot(projection="3d")
    
    ax.plot(x_array, y_array, z_array, lw=0.5)
    ax.set_xlabel(f"Positions in dimension x")
    ax.set_ylabel(f"Positions in dimension y")
    ax.set_zlabel(f"Positions in dimension z")
    
    if output_path:
        plt.savefig(output_path)
    else:
        plt.show()
