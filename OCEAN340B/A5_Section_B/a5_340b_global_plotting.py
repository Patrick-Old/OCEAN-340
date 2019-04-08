# Your Name
# Problem Set #5: Creating Global Maps
# OCEAN 340B, Winter 2019

"""Hello OCEAN 340B! In this assignment we will be using matplotlib's contourf
function to plot real oceanographic data on a global map. The data comes from
the world ocean atlas 2013 (WOA13), found below. No need to download the data from there,
as the data you should work with is already found in the Canvas assignment.
     WOA13 Data: https://www.nodc.noaa.gov/cgi-bin/OC5/woa13/woa13.pl?parameter=t

To give you an idea of what we will be creating today, check out the following figure on
Canvas:
WOA13 Summer Temp Plot: https://canvas.uw.edu/courses/1270532/files/folder/Misc?preview=54072593

NOTE: For the problems below, open each dataset just once in your main() function, and pass each
open dataset to each function as needed.

NOTE #2: You will see that for questions 1 and 2 we are setting up our data in a 2-D format. This
is because our function to put our data on a map, contourf, needs 2-D lat, lon and data. Please
see example here: https://scitools.org.uk/cartopy/docs/v0.5/matplotlib/introductory_examples/03.contours.html

Notice how the above example uses the Cartopy package to create the map. Cartopy is now seen
as the official replacement for Basemap, as seen below, and therefore we will be using it in 
this course: https://matplotlib.org/basemap/users/intro.html#cartopy-new-management-and-eol-announcement

To install Cartopy on Anaconda, please do the following:
    conda install -c conda-forge cartopy

Cartopy actually already comes with Canopy, so no need to install it on the Canopy terminal / 
command prompt. Please let Patrick know if you have any installation issues.


Question 1: Because our goal for this assignment is to map data on a global map, we will need
our data in two dimensions: latitude and longitude. Additionally, we will need both our longitude
and latitude to be in the SAME 2-D shape as well in order to call the contourf plotting function 
on our data. If you check out the shape of the longitude data or latitude data from one of the 
datasets (dataset.variables['lat'][:]), you will notice that the longitude and latitude are each 
stored as 1-D arrays. However, as mentioned above, in order to create our maps, we need the 
latitude and longitude to be 2-D. 

Create a function that takes in a WOA netCDF dataset, and returns the longitude and latitude in 2-D 
form using the np.meshgrid function (google this to find documentation if it is unclear).

I encourage you to mess around with the result of np.meshgrid, switching around inputs as well, to
see how it effects the function output.

*** 10 points ***


Question 2: Next, we will need to change our data from four dimensions to two dimensions in
order to plot it on our map. After all, a map is two dimensional, so this makes sense. For our
purposes, this will mean averaging (get it...mean...averaging...) out time and selecting a depth at 
which we are interested in seeing the global temperature at. We will be creating temperature maps 
of the ocean at 100 meters depth and the surface (0 meters) in our main function.

Create a function that takes in a WOA13 netCDF dataset and a depth, extracts the temperature data 
from the dataset, averages out time, and selects the depth plane to examine based on the depth
parameter this function takes in. 

HINT: To find the index at which a value occurs in a list, you can use list.index(value), which 
will return the index at which the value occurs first in a list.

*** 25 points ***


Question 3: Finally, write a function to put the data on a map. It should take in the following 
parameters: 2-D lats, 2-D lons, 2-D variable data (in our case temperature), a figure number, and a 
figure title. The tutorial on contourf at the top of the page should be helpful in creating
this function. In this tutorial, notice how a projection is setup, then the latitudes, longitudes, 
and data are set to variables, and then the plt.contourf function is used to plot the data on the 
projection defined above it. Once you have created your map, use ax.set_title to set the title and 
add a colorbar as is done in the following example (specifically look at the plt.contourf, how 
they set that to a variable, and then how they reference this variable when creating the colorbar):
https://goo.gl/LoLp9c

Be sure to add coastlines and gridlines to your plot. Choose either the PlateCarree, Robinson,
Mollweide or Orthographic projection for your maps. Additionally, I recommend (but do not require) 
passing in an optional parameter to your plt.figure function, as follows: 
    
    plt.figure(figsize=(20, 10))

This will make the figures very large. This is not required but it is sometimes nice to make 
the plots larger.

*** 30 points ***


Question 4: Last, write a main function that performs the following steps:
    1.  Opens both the winter woa data and summer woa data as netCDF datasets and saves them to 
         variables.
    2.  Creates 2-D longitude and latitude data and saves them to variables.
    3.  Creates 2-D temperature data of the surface and at 100m depth for the summer, and
         creates 2-D temperature data for just the surface in the winter.
    4a. Find the difference between the summer surface temps and winter surface temps and save it
         to a variable. Should calculate by doing summer minus winter.
    4b. Find the difference between summer surface temps and summer temps at 100m depth and save it
         to a variable. Should calculate by doing surface minus 100m depth.
    5.  Create maps of the following:
         5a. Temperature at the surface in the summer.
         5b. Temperature difference between summer and winter at the surface.
         5c. Temperature difference between 100m and the surface in the summer.

*** 20 points ***

*** An additional 15 points will be used to grade code style / logic ***
"""

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from netCDF4 import Dataset
import numpy as np

# Other functions go here


def main():
    sum_dataset = Dataset('summer_woa13_decav.nc', 'r')
    wint_dataset = Dataset('winter_woa13_decav.nc', 'r')
    
    
if __name__ == "__main__":
    main()