#simulation of the 2D Ising magnet
import matplotlib.pyplot as plt
import math
import copy
import os
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import math
import copy
import os
import numpy as np 
import pandas as pd 
import numpy
#made using: Chapter 6 Monte Carlo simulations
class ising_magnet_2d_Function:
    """ This class is used to make the functions used to simulate the 2D ising magnet.   
    """
    def __init__(self):
        """ There are variables used in the functions. 
        """
        self.list_of_powers = []
        self.J=0.
        self.list_of_spins = []
        self.list_of_delta_E =[]
        self.new_list_of_spins = []

    def _get_spins(self, list_of_powers):
        """ This is method used to calcualte the list of spins with counters for the numbers of ups and downs"""
        list_of_spins = []
        for i in list_of_powers:
            list_of_spins.append((-1)**i)
        no_of_up = 0
        no_of_down = 0
        for i in range(len(list_of_spins)):
            if list_of_spins[i] == 1:
                no_of_up+=1
            else:
                no_of_down+=1
        list_of_spins_and_counts = [list_of_spins, no_of_up, no_of_down]
        #print(list_of_spins_and_counts)
        return(list_of_spins_and_counts)
    
    def _get_delta_energy(self,list_of_spins, J):
        """ This is method used to calcualte the delta_energy. """
        list_h_i =[]
        for i in range(0,len(list_of_spins)):
            h_i = 0.
            for j in range(0,len(list_of_spins)):
                if j!=i:
                    h_i += list_of_spins[j]
            list_h_i.append(h_i)
        list_of_delta_E = []
        for i in range(len(list_of_spins)):
            list_of_delta_E.append(2*J*list_of_spins[i]*list_h_i[i])
        #print(list_of_delta_E)
        return(list_of_delta_E)
    
    def _get_probability_to_spin_flip(self,list_of_spins,list_of_delta_E):
        """ This is method used to calcualte the probabillity for spin to flip. """
        new_list_of_spins= []
        prob_spin_to_flip=[]
        for i in range(len(list_of_spins)):
            if list_of_delta_E[i] < 0:
                prob_spin_to_flip.append("YES")
                new_list_of_spins.append(-list_of_spins[i])
            else:
                prob_spin_to_flip.append("NO")
                new_list_of_spins.append(list_of_spins[i])
        list_of_both = [prob_spin_to_flip,new_list_of_spins]
        #print(list_of_both)
        return(list_of_both)
    
    def _get_counts(self,new_list_of_spins):
        """ This is method used to calcualte the probabillity for spin to flip. """
        no_of_up_new = 0
        no_of_down_new = 0
        for i in range(len(new_list_of_spins)):
            if new_list_of_spins[i] == 1:
                no_of_up_new+=1
            else:
                no_of_down_new+=1
        up_and_down_count = [no_of_up_new, no_of_down_new]
        #print(up_and_down_count)
        return(up_and_down_count)
        