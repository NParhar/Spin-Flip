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
from Ising_magnet_functions import ising_magnet_2d_Function
#made using: Chapter 6 Monte Carlo simulations
class ising_magnet_2d:
    """ This class is used to simulate the 2D ising magnet.   
    """
    def __init__(self):
        """ There are 3 variables for this simulation. They are varied to observe the behaviour. int_low, int_high is the range
        of the number (no_of_int) of random values. 
        """
        self.int_low = 0
        self.int_high = 1 
        self.no_of_int = 5
        self.input1 = []

    def _flip(self, int_low, int_high, no_of_int):
        """ This is method used to calcualte if the spins flip or not"""
        #random test.py tests the randomness
        list_of_powers=np.random.random_integers(int_low,int_high, size=(no_of_int))
        list_of_spins_and_counts_a = ising_magnet_2d_Function()._get_spins(list_of_powers)
        list_of_spins= list_of_spins_and_counts_a[0]
        no_of_up = list_of_spins_and_counts_a[1]
        no_of_down = list_of_spins_and_counts_a[2]

        range_J=np.random.randint(1,101, size=None)
        J = np.random.randint(-range_J,range_J, size=None)
        list_of_delta_E = ising_magnet_2d_Function()._get_delta_energy(list_of_spins,J)
        
        list_of_prob_and_new_spins = ising_magnet_2d_Function()._get_probability_to_spin_flip(list_of_spins,list_of_delta_E)
        prob_spin_to_flip=list_of_prob_and_new_spins[0]
        new_list_of_spins=list_of_prob_and_new_spins[1]

        list_of_counts=ising_magnet_2d_Function()._get_counts(new_list_of_spins)
        no_of_up_new = list_of_counts[0]
        no_of_down_new = list_of_counts[1]
        

        no_of_spin = len(prob_spin_to_flip)
        no_of_spin_flipped = 0
        for i in range(len(prob_spin_to_flip)):
            if prob_spin_to_flip[i]=="YES":
                no_of_spin_flipped+=1
        print("ORIGINAL LIST OF SPINS      : ",list_of_spins)
        print("PROBABILITY FOR SPIN TO FLIP: ",prob_spin_to_flip)
        print("NEW LIST OF SPINS           : ",new_list_of_spins)
        print("ORIGINAL UP:DOWN            : ", no_of_up,":",no_of_down)
        print("NEW UP:DOWN                 : ", no_of_up_new,":",no_of_down_new)
        print("FLIPPED SPINS/ SPINS        : ", no_of_spin_flipped,"/", no_of_spin)
        plot_x=0
        plot_y=0
        if no_of_up>=no_of_down:
            plot_x+=no_of_up
            plot_y+=no_of_up_new
        else: 
            plot_x+=no_of_down
            plot_y+=no_of_down_new
        print(plot_x, plot_y)
        return_values = []
        return_values.append(plot_x)
        return_values.append(plot_y)
        return(return_values)

    def _plot(self, input1):
        """ This is method used to plot a graph of the spins"""
        list_of_values_varied = np.random.randint(5,input1, size=99)
        x=[]
        y=[]
        for i in range(len(list_of_values_varied)):
            x.append(ising_magnet_2d()._flip(0,99,list_of_values_varied[i])[0])
            y.append(ising_magnet_2d()._flip(0,99,list_of_values_varied[i])[1])
        print(list_of_values_varied)
        plt.scatter(x,y)
        plt.xlabel("no. of majority spins")
        plt.ylabel("no. of majority spins after flip")
        plt.show()
        return(x,y)