"""
Utility functions
"""

import os
import warnings
import numpy as np
from typing import List
from dataclasses import fields
from matplotlib.collections import LineCollection


def save_arrays(
    target_arrays: List[np.array],
    output_path: str|None,
    ):
    """
    Save arrays to an output path if given.
    
    Parameters:
        target_array: input array (np.array)
        output_path: if given, the array is saved to it (str or None)
    """
    if output_path:
        array_dict = dict()
        os.makedirs(
            os.path.dirname(output_path), exist_ok=True)
        for idx, array in enumerate(target_arrays):
            array_dict[f"arr{idx+1}"] = array
        np.savez(output_path, **array_dict)
        
        
def load_arrays(target_path: str):
    """
    Given a filepath, it returns a tuple of arrays.
    """
    data = np.load(target_path)
    return tuple([data[key] for key in data.files])


def euclidean_distances(array_1, array_2):
    """
    # TODO: docstring
    help from ChatGPT
    """
    assert len(array_1) == len(array_2), "Input arrays have to be the same length"
    
    array_1 = np.asarray(array_1)
    array_2 = np.asarray(array_2)
    
    dx = np.diff(array_1)
    dy = np.diff(array_2)
    
    distances = np.sqrt(dx**2 + dy**2)
    
    return distances


# from https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html
def colored_line_between_pts(x, y, c, ax, **lc_kwargs):
    """
    Plot a line with a color specified between (x, y) points by a third value.

    It does this by creating a collection of line segments between each pair of
    neighboring points. The color of each segment is determined by the
    made up of two straight lines each connecting the current (x, y) point to the
    midpoints of the lines connecting the current point with its two neighbors.
    This creates a smooth line with no gaps between the line segments.

    Parameters
    ----------
    x, y : array-like
        The horizontal and vertical coordinates of the data points.
    c : array-like
        The color values, which should have a size one less than that of x and y.
    ax : Axes
        Axis object on which to plot the colored line.
    **lc_kwargs
        Any additional arguments to pass to matplotlib.collections.LineCollection
        constructor. This should not include the array keyword argument because
        that is set to the color argument. If provided, it will be overridden.

    Returns
    -------
    matplotlib.collections.LineCollection
        The generated line collection representing the colored line.
    """
    if "array" in lc_kwargs:
        warnings.warn('The provided "array" keyword argument will be overridden')

    # Check color array size (LineCollection still works, but values are unused)
    if len(c) != len(x) - 1:
        warnings.warn(
            "The c argument should have a length one less than the length of x and y. "
            "If it has the same length, use the colored_line function instead."
        )

    # Create a set of line segments so that we can color them individually
    # This creates the points as an N x 1 x 2 array so that we can stack points
    # together easily to get the segments. The segments array for line collection
    # needs to be (numlines) x (points per line) x 2 (for x and y)
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = LineCollection(segments, **lc_kwargs)

    # Set the values used for colormapping
    lc.set_array(c)

    return ax.add_collection(lc)


# from ChatGPT
def filter_to_dataclass(dataclass_type, data: dict):
    # TODO: docstring
    valid_keys = {f.name for f in fields(dataclass_type)}
    filtered_data = {k: v for k, v in data.items() if k in valid_keys}
    return dataclass_type(**filtered_data)

