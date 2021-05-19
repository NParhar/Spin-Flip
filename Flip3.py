import matplotlib.pyplot as plt
import math
import copy
import os
import numpy as np 
import pandas as pd
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
#This constant comes from 'Monte Carlo tests of renormalization-group predictions for critical phenomena in Ising models,K Binder et al'
constant = 0.221654
#This formila comes from 'CHAPTER 15. MONTE CARLO SIMULATIONS OF THERMAL SYSTEMS, H Gould et al'
bond_prob = 1 - np.exp(-2*constant)
class to_flip_3:
    """ This class is used to plot the before and after spin-flip graphs, and is used to determine which particles flip.   
    """
    def __init__(self):
        """ There are 4 variables. Their values will be substituted from Flip.py being used in Flip2.py.
        """
        self.x_y_z_positions = []
        self.sample_size = 10
        self.random_seed_spin = 0
        self.changed = []

    def _graph_before(self, x_y_z_positions):
        """ This method is used to plot the before spin flip graph."""
        x=[]
        y=[]
        z=[]
        x_up=[]
        y_up=[]
        z_up=[]
        for i in range(0,len(x_y_z_positions)):
            if (-1)**(x_y_z_positions[i][3])==-1:
                x.append(x_y_z_positions[i][0])
                y.append(x_y_z_positions[i][1])
                z.append(x_y_z_positions[i][2])
            else:
                x_up.append(x_y_z_positions[i][0])
                y_up.append(x_y_z_positions[i][1])
                z_up.append(x_y_z_positions[i][2])
        fig = pyplot.figure()
        ax = Axes3D(fig)
        ax.scatter(x,y,z,c="red", marker="v")
        ax.scatter(x_up,y_up,z_up,c="blue", marker="^")
        pyplot.show()

    def _list_neighbours_a(self, x_y_z_positions, random_seed_spin):
        """ This method is used in a loop in Flip2.py to determine the perimeters that flip."""
        list_of_distnaces_from_seed =[]
        for i in range(0,len(x_y_z_positions)):
            new_coord_x = x_y_z_positions[i][0]-x_y_z_positions[random_seed_spin][0]
            new_coord_y = x_y_z_positions[i][1]-x_y_z_positions[random_seed_spin][1]
            new_coord_z = x_y_z_positions[i][2]-x_y_z_positions[random_seed_spin][2]
            distance_from_seed = np.sqrt((np.abs(new_coord_x))**2+(np.abs(new_coord_y))**2+(np.abs(new_coord_z))**2)
            list_of_distnaces_from_seed.append(distance_from_seed)
        ordered_i=[sorted(list_of_distnaces_from_seed).index(i) for i in list_of_distnaces_from_seed]
        seed_neighbour_position_list=[]
        for i in range(1,5):
            for j in range(0,len(ordered_i)):
                if i==ordered_i[j]:
                    xyz=[]
                    xyz.append(x_y_z_positions[j][0])
                    xyz.append(x_y_z_positions[j][1])
                    xyz.append(x_y_z_positions[j][2])
                    xyz.append(x_y_z_positions[j][3])
                    seed_neighbour_position_list.append(xyz)
        list_of_spins = []
        for i in range(0,len(x_y_z_positions)):
            list_of_spins.append(x_y_z_positions[i][3])
        copy_to_flip = copy.deepcopy(seed_neighbour_position_list)
        counter_same_spin_as_seed =0
        same_spin_list =[]
        for i in range(0,len(copy_to_flip)):
            if (-1)**copy_to_flip[i][3]==(-1)**x_y_z_positions[random_seed_spin][3]:
                counter_same_spin_as_seed+=1
                same_spin_list.append(copy_to_flip[i])
        cluster = []
        while same_spin_list:
            if len(same_spin_list)==1:
                r_value=np.random.random()
                if r_value<=bond_prob:
                    cluster.append(same_spin_list[0])
                same_spin_list = []
            if len(same_spin_list)>1:
                r_value=np.random.random()
                if r_value<=bond_prob:
                    cluster.append(same_spin_list[0])
                same_spin_list.pop(0)        
                same_spin_list.insert(0,same_spin_list[len(same_spin_list)-1])
                same_spin_list.pop(len(same_spin_list)-1)
        list_to_be_removed = []
        copy_of_all_particle = copy.deepcopy(x_y_z_positions)
        for i in cluster:
            for j in range(0,len(copy_of_all_particle)):
                if i==copy_of_all_particle[j]:
                    list_to_be_removed.append(j)
        return(list_to_be_removed)
            
    def _graph_after(self, position_a, changed):
        """This method is used to plot the before spin flip graph."""
        x=[]
        y=[]
        z=[]
        x_up=[]
        y_up=[]
        z_up=[]
        x_c=[]
        y_c=[]
        z_c=[]
        for i in range(0,len(position_a)):
            if (-1)**(position_a[i][3])==-1:
                x.append(position_a[i][0])
                y.append(position_a[i][1])
                z.append(position_a[i][2])
            else:
                x_up.append(position_a[i][0])
                y_up.append(position_a[i][1])
                z_up.append(position_a[i][2])
        for i in range(0,len(changed)):
            x_c.append(changed[i][0])
            y_c.append(changed[i][1])
            z_c.append(changed[i][2])
        fig = pyplot.figure()
        ax = Axes3D(fig)
        ax.scatter(x,y,z,c="red", marker="v")
        ax.scatter(x_c,y_c,z_c,c="purple", marker="o")
        ax.scatter(x_up,y_up,z_up,c="blue", marker="^")
        pyplot.show()
            
            
