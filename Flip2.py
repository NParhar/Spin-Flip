import matplotlib.pyplot as plt
import math
import copy
import os
import numpy as np 
import pandas as pd
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from Flip import to_flip
from Flip3 import to_flip_3
#This constant comes from 'Monte Carlo tests of renormalization-group predictions for critical phenomena in Ising models,K Binder et al'
constant = 0.221654
#This formila comes from 'CHAPTER 15. MONTE CARLO SIMULATIONS OF THERMAL SYSTEMS, H Gould et al'
bond_prob = 1 - np.exp(-2*constant)
class to_flip_2:
    """ This class is used to simulate the simultaneous spin flip. The algorithm idea is from: CHAPTER 15. MONTE CARLO SIMULATIONS OF THERMAL SYSTEMS, H Gould et al.  
    """
    def __init__(self):
        """ There is 1 variable for this simulation. It is the maximum random value possible. This is to observe the behaviour. 
        """
        self.number_a = 0

    def _flip_b(self, number_a):
        """ This is method used to determine which parrticles flip."""
        #To convert the arrays from Flip.py into neat lists
        list_of_2 = to_flip()._flip_a(number_a)
        sample_size_a = list_of_2[0]
        list_of_points = []
        for i in range(0,len(list_of_2[1])):
            xyz=[]
            for j in range(0,len(list_of_2[1][i])):
                xyz.append(list_of_2[1][i][j])
            list_of_points.append(xyz)
        #print(list_of_points)
        #plot before spin flip graph using Flip3's method _graph_before()
        to_flip_3()._graph_before(list_of_points)
        #######
        list_of_particles_to_be_flipped_in_graph = []
        #randomly chosen spin
        random_seed_spin = np.random.randint(0,sample_size_a -1, size=None)
        seed_perimenter_flipped = to_flip_3()._list_neighbours_a(list_of_points,random_seed_spin)
        #make a copy to edit later
        copy_of_all = copy.deepcopy(list_of_points)
        copy_of_all.remove(list_of_points[random_seed_spin])
        list_of_particles_to_be_flipped_in_graph.append(list_of_points[random_seed_spin])
        #To flip randomly chosen seed
        if len(seed_perimenter_flipped)>=1:
            for i in seed_perimenter_flipped:
                list_of_particles_to_be_flipped_in_graph.append(list_of_points[i])
                for y in copy_of_all:
                    if y==list_of_points[i]:
                        copy_of_all.remove(list_of_points[i])
                #To flip randomly chosen seed's perimeters        
                sub=to_flip_3()._list_neighbours_a(copy_of_all,i)
                if len(sub)>=1:
                    for x in sub:
                        for y in copy_of_all:
                            if y==list_of_points[x]:
                                copy_of_all.remove(list_of_points[x])
                        list_of_particles_to_be_flipped_in_graph.append(list_of_points[x])                  
        #print("TO FLIP IN NEW GRAPH:",list_of_particles_to_be_flipped_in_graph)
        #print("TO STAY IN NEW GRAPH:",copy_of_all)
        #####
        #plot after spin flip graph using Flip3's method _graph_after()
        to_flip_3()._graph_after(copy_of_all,list_of_particles_to_be_flipped_in_graph)       
       