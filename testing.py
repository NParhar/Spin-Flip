import unittest
from Ising_magnet import ising_magnet_2d
from Ising_magnet_functions import ising_magnet_2d_Function
from Flip import to_flip
from Flip2 import to_flip_2
from Flip3 import to_flip_3
from clusterflip import generate_data
from clusterflip2 import single_cluster_flip
from clusterflip3 import apply
########################################FOR Ising_magnet.py:#################################################################
#FOR Ising_magnet_2d_Function()._get_spins([0,1,2,3,4]):
def test__get_spins():
    assert ising_magnet_2d_Function()._get_spins([0,1,2,3,4]) == [[1,-1,1,-1,1],3,2], "Should be [[1,-1,1,-1,1],3,2]"
if __name__ == "__main__":
    test__get_spins()
    print("Everything passed")
############
#FOR Ising_magnet_2d_Function()._get_delta_energy(list_of_spins,J):
def test__get_delta_energy():
    assert ising_magnet_2d_Function()._get_delta_energy([1,-1,1,-1,1], 5) == [0,-20,0,-20,0], "Should be [0,-20,0,-20,0]"
if __name__ == "__main__":
    test__get_delta_energy()
    print("Everything passed")
#############
#FOR Iising_magnet_2d_Function()._get_probability_to_spin_flip(list_of_spins, list_of_delta_E):
def test__get_probability_to_spin_flip():
    assert ising_magnet_2d_Function()._get_probability_to_spin_flip([1,-1,1,-1,1], [0,-20,0,-20,0]) == [["NO","YES","NO","YES","NO"],[1,1,1,1,1]], "Should be all the same"
if __name__ == "__main__":
    test__get_probability_to_spin_flip()
    print("Everything passed")
###########
#FOR Iising_magnet_2d_Function()._get_counts(new_list_of_spins):
def test__get_counts():
    assert ising_magnet_2d_Function()._get_counts([1,1,1,1,1]) == [5,0], "Should be [5,0]"
if __name__ == "__main__":
    test__get_counts()
    print("Everything passed")
######################################################################
#FOR THE clusterflip3.py functions
#FOR apply()._list_neighbours([0,1,2],[0,1,2],[0,1,2],[0,1,2], 0)
def test__list_neighbours():
    assert apply()._list_neighbours([0,1,2],[0,1,2],[0,1,2],[0,1,2], 0) == [[0, 0.0], [1, 1.7320508075688772], [2, 3.4641016151377544]], "CHECK apply()._list_neighbours"
if __name__ == "__main__":
    test__list_neighbours()
    print("Everything passed")

#FOR apply()._four([0,3,5,1,4,2],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1], 0)
def test__four():
    assert apply()._four([0,3,5,1,4,2],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1], 0) == [(0, 0.0), (3, 1.0), (5, 2.0), (1, 3.0), (4, 4.0)], "CHECK apply()._four"
if __name__ == "__main__":
    test__four()
    print("Everything passed")
