import matplotlib.pyplot as plt
import math
import copy
import os
import numpy as np 
import pandas as pd
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from clusterflip import generate_data
from clusterflip3 import apply

class single_cluster_flip:
    """ This class is used to apply the single cluster flip algorithm.   
    """
    def __init__(self):
        """ There is 1 variable that will be input in the test file. 
        """
        self.sample_size_max = 0

    def _show(self, sample_size_max):
        """ This method is used to generate random data to be used."""
        ######################THIS ORGANIZES THE GENERATED DATA USING PANDAS
        list_of_data = generate_data()._set_max_value(sample_size_max)
        df = pd.DataFrame(list_of_data, columns=['x', 'y', 'z', 'spins'])
        df.to_pickle("Output_Data.csv")
        x=[]
        y=[]
        z=[]
        spins=[]
        for i in df['x']:
            x.append(i)
        for i in df['y']:
            y.append(i)
        for i in df['z']:
            z.append(i)
        for i in df['spins']:
            spins.append(i)
        ####################THIS PLOTS THE DATA BEFORE THE SINGLE CLUSTER FLIP ALGORITHM IS APPLIED    
        x_down=[]
        y_down=[]
        z_down=[]
        x_up=[]
        y_up=[]
        z_up=[]
        for i in range(0,len(spins)):
            if (-1)**(spins[i])==-1:
                x_down.append(x[i])
                y_down.append(y[i])
                z_down.append(z[i])
            else:
                x_up.append(x[i])
                y_up.append(y[i])
                z_up.append(z[i])
        fig = pyplot.figure()
        ax = Axes3D(fig)
        ax.scatter(x_down,y_down,z_down,c="red", marker="v")
        ax.scatter(x_up,y_up,z_up,c="blue", marker="^")
        pyplot.savefig("before.png")
        pyplot.show()

        x_copy=copy.deepcopy(x)
        y_copy=copy.deepcopy(y)
        z_copy=copy.deepcopy(z)
        spins_copy=copy.deepcopy(spins)
        #################DATA AFTER ALGORITHM
        random_number=np.random.randint(0,sample_size_max-1, size=None)
        cluster=apply()._bondprobability(x,y,z,spins,random_number)
        print("SEED CLUSTER:", cluster)
        if len(cluster)>=1:
            for i in cluster:
                print("for", i)
                sub_cluster=apply()._bondprobability(x,y,z,spins,i)               
                if len(sub_cluster)>=1:
                    for j in sub_cluster: 
                        abc=[]                   
                        if j!=i:
                            if len(abc)>=1:
                                for qrs in abc:
                                    if j!=qrs:
                                        abc.append(j)
                        for lmn in abc:
                            cluster.append(lmn)
        print("FINAL CLUSTER: ",cluster)
        ##############################GRAPH AFTER ALGORITHM
               
        x_down_after=[]
        y_down_after=[]
        z_down_after=[]
        x_up_after=[]
        y_up_after=[]
        z_up_after=[]
        x_c=[]
        y_c=[]
        z_c=[]
        for i in cluster:
            x_c.append(x_copy[i])
            y_c.append(y_copy[i])
            z_c.append(z_copy[i])
        all = list(range(len(spins_copy)))
        print(all)
        if len(cluster)>=1:
            for i in cluster:
                all.remove(i)
        print("ALL:", all) 
        if len(all)>1:           
            for i in all:
                if (-1)**(spins[i])==-1:
                    x_down_after.append(x_copy[i])
                    y_down_after.append(y_copy[i])
                    z_down_after.append(z_copy[i])
                else:
                    x_up_after.append(x_copy[i])
                    y_up_after.append(y_copy[i])
                    z_up_after.append(z_copy[i]) 
        if len(all)==1:
            if (-1)**(spins[i])==-1:
                x_down_after.append(x_copy[all[1]])
                y_down_after.append(y_copy[all[1]])
                z_down_after.append(z_copy[all[1]])
            else:
                x_up_after.append(x_copy[all[1]])
                y_up_after.append(y_copy[all[1]])
                z_up_after.append(z_copy[all[1]])
        fig = pyplot.figure()
        ax = Axes3D(fig)
        ax.scatter(x_down_after,y_down_after,z_down_after,c="red", marker="v")
        ax.scatter(x_c,y_c,z_c,c="purple", marker="o")
        ax.scatter(x_up_after,y_up_after,z_up_after,c="blue", marker="^")
        pyplot.show()



        