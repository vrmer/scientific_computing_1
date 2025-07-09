import numpy as np
from euler_solver import solver, Parameters


params = Parameters(
    x=1,
    y=1,
    z=1,
    sigma=1,
    beta=1,
    rho=1,
    t_delta=0.01,
    N=10
)


class TestEulerSolver:
    
    def test_solver_return_type(self):
        """
        Test if the solver returns the appropriate type.
        
        Inspiration from ChatGPT.
        """
        result_tuple = solver(params)
        assert all(isinstance(result, np.ndarray) for result in result_tuple)
        
    def test_solver_return_shape(self):
        """
        Test if the solver returns the appropriate type.
        
        Inspiration from ChatGPT.
        """
        result_tuple = solver(params)
        assert all(result.shape[0] == params.N for result in result_tuple)
