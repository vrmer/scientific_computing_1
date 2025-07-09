from dataclasses import dataclass


@dataclass
class Parameters:
    """
    Dataclass for parameters of the Euler solver algorithm.
    
    x: initial position in dimension x (integer or float)
    y: initial position in dimension y (integer or float)
    z: initial position in dimension z (integer or float)
    sigma: value of parameter $\\sigma$ (integer or float)
    beta: value of parameter $\beta$ (integer or float)
    rho: value of parameter $\rho$ (integer or float)
    t_delta: unit of time step ($t_delta$) (integer or float), default is 0.01
    N: maximum time step (integer), default is 50,000
    """
    x: int|float
    y: int|float
    z: int|float
    sigma: int|float
    beta: int|float
    rho: int|float
    t_delta : int|float = 0.01
    N: int = 50_000
