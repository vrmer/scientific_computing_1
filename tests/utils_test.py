import numpy as np
from euler_solver import euclidean_distances


array_1 = np.array([0, 0])
array_2 = np.array([1, 0])

distance = euclidean_distances(array_1, array_2)


class TestUtils:
    
    def test_euclidean_distance_type(self):
        assert isinstance(distance, np.ndarray)
        
    def test_euclidean_distance_value(self):
        assert distance == 1
