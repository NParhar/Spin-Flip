import matplotlib.pyplot as plt
import math
import copy
import os
import numpy as np 
import pandas as pd
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

class generate_data:
    """ This class is used to create the randomly generated data used to simulate simultaneous spin flip used in Flip2.py.   
    """
    def __init__(self):
        """ There is 1 variable that will be input in the test file. 
        """
        self.sample_size_max = 0

    def _set_max_value(self, sample_size_max):
        """Min input must be 6. This method is used to generate random data to be used."""
        sample_size=np.random.randint(5,sample_size_max, size=None)
        x_y_z_positions=np.random.randint(0,1000, size=(sample_size,4))
        list_of_xyz=[]
        for i in x_y_z_positions:
            sub=[]
            for j in i:
                sub.append(j)
            list_of_xyz.append(sub)
        print(list_of_xyz)
        return(list_of_xyz)


    