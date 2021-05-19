import matplotlib.pyplot as plt
import math
import copy
import os
import numpy as np 
import pandas as pd 
import numpy
import matplotlib
from Ising_magnet import ising_magnet_2d
from Ising_magnet_functions import ising_magnet_2d_Function


#plots a graph showing the behviour of the spins that flip in the ising magnet
#varie the value '_' to change the range of 99 values to be plotted in: ising_magnet_2d()._plot(-)

ising_magnet_2d()._plot(101)
####################
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