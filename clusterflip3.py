import matplotlib.pyplot as plt
import math
import copy
import os
import numpy as np 
import pandas as pd
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import heapq
import operator as op
class apply:
    """ This class is used to apply the single cluste flip algorithm.   
    """
    def __init__(self):
        """ There is 1 variable that will be input in the test file. 
        """
        self.x = []
        self.y = []
        self.z = []
        self.spins = []
        self.index_a = 0

    def _list_neighbours(self,x,y,z,spins, index_a):
        """This is to work out the neighbours of a spin. ****It has been tested"""
        list_of_indices_with_distances=[]
        for i in range(len(x)):
            index_distance = []
            index_distance.append(i)
            index_distance.append(np.sqrt( (x[i]-x[index_a])**2 + (y[i]-y[index_a])**2 + (z[i]-z[index_a])**2 ) )
            list_of_indices_with_distances.append(index_distance)
        #print(list_of_indices_with_distances)
        return(list_of_indices_with_distances)

    def _four(self,x,y,z,spins, index_a):
        """This is to work out the 4 nearest neighbours of a spin.*** tested and now corrected"""
        list_of_indices_with_distances = apply()._list_neighbours(x,y,z,spins,index_a)
        list_of_indices = []
        list_of_distnaces = []
        for i in range(len(list_of_indices_with_distances)):
            list_of_indices.append(list_of_indices_with_distances[i][0])
            list_of_distnaces.append(list_of_indices_with_distances[i][1])
        list_of_five_in_lattice = heapq.nsmallest(5, zip(list_of_indices, list_of_distnaces), key=op.itemgetter(-1))
        #print(list_of_five_in_lattice)
        return(list_of_five_in_lattice)
    
    def _perimeter_spins(self,x,y,z,spins, index_a):
        """This is to get the parallel perimeter spins"""
        list_of_five_in_lattice = apply()._four(x,y,z,spins,index_a)
        seed_spin_index = list_of_five_in_lattice[0][0]
        seed_spin = (-1)**spins[seed_spin_index]
        parallel_to_seed = []
        for i in range(len(list_of_five_in_lattice)):
            if (-1)**spins[i]==seed_spin:
                parallel_to_seed.append(list_of_five_in_lattice[i][0])
        #print(parallel_to_seed)
        return(parallel_to_seed)

    def _bondprobability(self,x,y,z,spins, index_a):
        """This is to see if the parallel spins have suitable bond energy to be added to the cluster"""
        parallel_to_seed = apply()._perimeter_spins(x,y,z,spins,index_a)
        #This constant comes from 'Monte Carlo tests of renormalization-group predictions for critical phenomena in Ising models,K Binder et al'
        constant = 0.221654
        #This formila comes from 'CHAPTER 15. MONTE CARLO SIMULATIONS OF THERMAL SYSTEMS, H Gould et al'
        bond_prob = 1 - np.exp(-2*constant)
        parallel_to_seed.pop(0)
        #new_parallel_to_seed = [parallel_to_seed[-1]]
        parallel_to_seed.insert(0, parallel_to_seed[-1])
        parallel_to_seed.pop(-1)
        cluster=[]
        for i in parallel_to_seed:
            #new_parallel_to_seed.append(i)       
            r_value=np.random.random()
            if r_value<=bond_prob:
                cluster.append(i)
        #print("SEED CLUSTER",cluster)
        return(cluster)
    
     