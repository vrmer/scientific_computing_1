"""
Equations of the Euler ODE solver.
"""


def equation_x(
    x: int|float,
    y: int|float,
    sigma: int|float,
    t_delta: int|float
    ):
    r"""
    Euler approximation of the $x$ value at time step $t$.
    
    Parameters:
        x: value of $x_{t-1}$ (integer or float)
        y: value of $y_{t-1}$ (integer or float)
        sigma: value of model parameter $\sigma$ (integer or float)
        t_delta: unit of time step ($t_delta$) (integer or float)
        
    Output:
        value of $x_{t}$
    
    Formula:
        $x[n+1] \cong t_{\delta} \sigma(y[n]-x[n]) + x[n]$
    """
    return x + t_delta * sigma * (y - x)


def equation_y(
    x: int|float,
    y: int|float,
    z: int|float,
    rho: int|float,
    t_delta: int|float
    ):
    r"""
    Euler approximation of the $y$ value at time step $t$.
    
    Parameters:
        x: value of $x_{t-1}$ (integer or float)
        y: value of $y_{t-1}$ (integer or float)
        z: value of $z_{t-1}$ (integer or float)
        rho: value of model parameter $\rho$ (integer or float)
        t_delta: unit of time step ($t_delta$) (integer or float)
        
    Output:
        value of $y_{t}$
        
    Formula:
        $y[n+1] \cong \t_{\delta} (x (\rho - z) - y)$
    """
    return y + t_delta * (x * (rho - z) - y)


def equation_z(
    x: int|float,
    y: int|float,
    z: int|float,
    beta: int|float,
    t_delta: int|float
    ):
    r"""
    Euler approximation of the $y$ value at time step $t$.
    
    Parameters:
        x: value of $x_{t-1}$ (integer or float)
        y: value of $y_{t-1}$ (integer or float)
        z: value of $z_{t-1}$ (integer or float)
        beta: value of model parameter $\beta$ (integer or float)
        t_delta: unit of time step ($t_delta$) (integer or float)
        
    Output:
        value of $z_{t}$
        
    Formula:
        $z + \t_delta (xy - \beta z)$
    """
    return z + t_delta * (x * y - beta * z)
