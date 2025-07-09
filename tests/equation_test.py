from euler_solver import equation_x, equation_y, equation_z


x = 1
y = 1
z = 1
sigma = 1
beta = 1
rho = 1
t_delta = 0.01


class TestEquations:
    
    def test_equation_x(self):
        assert equation_x(x, y, sigma, t_delta) == 1.0
        
    def test_equation_y(self):
        assert equation_y(x, y, z, rho, t_delta) == 0.99
        
    def test_equation_z(self):
        assert equation_z(x, y, z, beta, t_delta) == 1.0
        
