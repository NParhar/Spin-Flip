The files used are divided into groups below m=based on how they're used.
######
*******randomness test
random test.py:
It plots a graph to test how random the numbers generated are that will be used. 
The graph should show no correlation between consecutive generated numbers to be
truly random.
#####
******Ising model
Ising_magnet.py:Used in Ising_magnet_test.py. It contains a class that simulates the process
 of spin flip in the Ising model. A method produces the data, the other plots.
Ising_magnet_Functions.py:The class contains functions that are used in Ising_magnet.py and are tested in Ising_magnet_test.py.
Ising_magnet_test.py:Plots a graph of the majority of spins (either up or down) in their initial state
against the final spin state.

The lines expected are horizontal (0 gradient) and 2 diagonal (gradient 1 and gradient>1) which is
seen.
input is max value that 1 of 99 particles can have.
Also contains the testing functions for the Ising_magnet_Functions.py
#####
***single cluster flip algorithm files:
flip.py: get values
flip2.py: Gets the data to plot
flip3.py: to plot before flip and after flip graph as well as determining which 
particles flip.
test_formulae.py: To simulate the spin flip using 1 input (max number of particles).
####
*****Second single cluster flip algorithm files:
clusterflip.py:generated the data
clusterflip2.py:stores the data using panda to be used
clusterflip3.py:contains the functions required for the algorithm used in clusterflip2.py
########
************************
testing.py: contains all of the testing functions for the testing suite