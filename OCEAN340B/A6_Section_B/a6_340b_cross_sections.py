# Your Name
# Problem Set #6: Cross Sections & Interpolation
# OCEAN 340B, Winter 2019

"""In this OCEAN 340B assignment we will examine how to create cross section plots. Part of this
process will involve interpolation, which is an estimation of a value between two given values.
Interpolation is very common in oceanographic computer programming, and cross sections are a very 
common way to represent oceanographic data. You will also be using the function given to you to
calculate the distance between two points (specifically within question 3). Please read the 
docstring and examine the code of this function to learn more about it.

The data you will be working with after you complete the functions (and should keep in mind while
writing the functions) is CNV data found on Canvas. These are profiles from around the Puget Sound.
You will read in the data using the fCNV function in your main function, which is created in 
question 5.

                                             
_________________________________________ QUESTIONS ________________________________________________
____________________________________________________________________________________________________ 

Question 1: This question asks you to write a function that interpolates data. Please use the
following example, courtesy of SciPy documentation:
    
https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp1d.html


Create a function that takes in an profile of variable data (ex. temperature),
a profile of depths, and a profile of new depths. All of these profiles should be
numpy arrays. This function should then interpolate the variable data relative to the new depths 
given, and return this new interpolation of the variable data in the form of a numpy array.

*** 10 points ***


Question 2: This function will create a 2-D array of vertical profiles.

Create a function that takes in a variable name, a list of fCNV datasets (NOT filepaths), and a  
numpy array of depths for data to be interpolated to. This function returns a 2-D numpy array of 
data from the given datasets. The data returned should be that of the given variable name, 
interpolated to the depths given, and returned in the form of a numpy array.

*** 20 points ***


Question 3: Create a function that takes in a list of latitudes and a list of longitudes. This 
function should then calculate the distance between two consecutive latitudes and longitudes
in the given lists. The output is a numpy array with the first value being zero, and the following
values being the distances between the given latitudes and longitudes.

Example:
    latList = [40, 40.5, 41]
    lonList = [120, 120.2, 120.4]
    calculate distance between point 1 (40, 120) and point 2 (40.5, 120.2)...
    calculate distance between point 2 (40, 120) and point 3 (40.5, 120.2)...
    OUTPUT:[  0., 58.13064838, 116.22461932]
    
*** 20 points ***


Question 4: Create a function that takes in a 2-D depths array, a 2-D distance array, a 2-D
variable data array, and a figure number. This function should create a filled contour plot of the 
variable data array with respect to the depths and distance arrays given. 
Be sure to use the figure number when plotting.

*** 15 points ***


Question 5: Create a main function that plots the given data for this assignment by doing the
            following:
    1. Open all of the data given for this assignment using the fCNV function from the seabird
        package and put the datasets in a list.
    2. Create a numpy array of new depths to interpolate to. This should be, for this problem set,
        the depths 5 - 100, inclusive. HINT: Try using the np.arange function for this.
    3. Create 2-D array of variable data, in this case both salinity and temperature, using 
        createTwoDimData function.
    4. Create a list of all latitudes from the CNV datasets and a list of all longitudes from the
        CNV datasets.
    5. Get the distance between each latitude and longitude pair. HINT: Use function from question 3.
    6. Create a 2-D array of distances and a 2-D array of new depths. HINT: Use np.meshgrid
    7. Plot the cross sections using contourf of both salinity and temperature from each of the
        three given CNV files.

*** 20 points ***

Please complete the following problems. There are 100 points total, with 15 points being used to 
grade code style/logic.
"""


import matplotlib.pyplot as plt
import numpy as np
from seabird import fCNV
from scipy import interpolate
from math import asin, sin, cos, sqrt, radians


def main():
    # Create and put all CNV datasets into a list
    prof1 = fCNV("/path/to/cnv1")
    prof2 = fCNV("/path/to/cnv2")
    prof3 = fCNV("/path/to/cnv3")



if __name__ == "__main__":
    main()
