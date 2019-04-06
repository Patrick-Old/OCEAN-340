# Your Name
# Problem Set #5: Mapping Points
# OCEAN 340A, Winter 2019

"""In this assignment you will learn how to plot points on a map using Python. Similar to past
mapping assignments, we will be using Cartopy, which you now have installed with your IDE 
(Canopy or Spyder). The data you will be plotting comes from past problem sets (CNV data from
the Puget Sounds, prof1.cnv, prof2.cnv, prof3.cnv, each found in the Canvas files page.) You
can either redownload them from the files page in Canvas, or just use what you downloaded 
previously.

Question 1: Create a function that takes in a list of CNV datasets (not filepaths). This function
returns a list of tuples, each tuple containing a latitude-longitude pair from a specific CNV
dataset from the list passed in.

*** 25 points ***


Question 2: Create a function that takes in a list of tuples that are latitude-longitude pairs and
plots them on a map. This function should also take in the following optional parameters:
    1. Figure size (tuple), default of (12, 16)
    2. Map resolution (string), default of '10m'
    3. Region of the world to be plotted (string), default of 'PS' (which stands for Puget Sound)
    4. Matplotlib colormap (string), default of 'rainbow'

This function creates a map that plots the latitude-longitude pairs from the given list,
and use the optional parameters to format the map. The colormap parameter should be used to
ensure that the points plotted are different colors. The map should contain the following:
    1. Legend
    2. Colored land
    3. Title
    
NOTE: You must use the I the eval() function to create the colormap based on the given parameter.

*** 40 points ***


Question 3: Create a main function that does the following:
    1. Obtains the filepaths to the CNV files via the os.listdir function
    2. Creates a list of tuples containing latitude-longitude pairs of the CNV datasets
    3. Plots these latitude-longitude pairs
    
*** 20 points ***


*** An additional 15 points will be used to grade code style / logic ***
"""

