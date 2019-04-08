# Your Name
# OCEAN 340A
# Problem Set #4: Writing Files
# Winter 2019

"""
NOTE: As this is a problem set that is done with no in class instruction, please take notice of
the following differences from a normal 340A problem set:
    1. You're given a head start on this assignment - some of it is already done for you (or at
       least the problem has been started) and some helpful comments are included.
    2. Some tutorials are given that are links to websites. Also, be sure to google around, come to
       office hours this week, and email Patrick (patold@uw.edu) if you need any help or desire
       to meet outside of office hours if that time does not work well for you.
    3. The due date on this assignment has changed to Saturday night (2/16/19) at 11:59 PM, as
       we will talk about some of this material on Friday in class for a short period of time.
       Please start the assignment before class Friday, and only some more minor questions will
       be addressed in class at that time.


In this assignment we will examine writing netCDF and CSV files using Python. Please resort to
the following documentation for basic help on this assignment:

Working with and writing netCDF files: 
http://www.ceda.ac.uk/static/media/uploads/ncas-reading-2015/11_create_netcdf_python.pdf

Working with and writing CSV files:
https://www.programiz.com/python-programming/working-csv-files#existing-files


I recommend you read all of the questions before you begin. You may decide you want to work on 
the questions out of order, and reading it all will help guide you in your approach to this
assignment as a whole.

Problem 1: When writing netCDF files, you will notice that if you write the file once, then
try to replace that file by writing to the same filepath again, you will get an error that
states something along the lines of "PermissionError: Permission Denied". This is because the
file already exists, so you cannot write it again to that same location.

One way to deal with this is to check if the file exists, and if it does, delete that file.
Please visit the following Stack Overflow page to see how to do this:
https://stackoverflow.com/questions/10840533/most-pythonic-way-to-delete-a-file-which-may-not-exist

Turn this code into a function that takes in a filepath and deletes the file at the given filepath
if it exists. Then, you will want to call this function inside of your function that creates a 
netCDF file (question 2) to avoid the permissions error mentioned above.
*** 15 points ***


Problem 2: There are two appropriate ways to write this function, which vary on the number
of parameters you wish to pass it. This function must take in profiles of salinity, temperature,
pressure, depth, and potential density. These can be passed to this function in a dictionary, 
or all as separate parameters. These profiles should come in the form of numpy arrays. Additionally, 
this function must take in a filepath. This function then writes a netCDF file to the given 
filepath, creating a depth dimension (the only dimension of this netCDF file), variables with data 
for all of the profiles, a description you write for the data (doesn't have to be very descriptive, 
can be very short), and a source for the data (again can be very short). These last two steps will
provide the dataset some attributes, forms of metadata.

Please use the comments provided to you in the function and the tutorial above to complete this
function.
*** 30 points ***


Problem 3: Similar to question 2, except now with a CSV file. Create a function that either takes 
in a filepath and a dictionary containing all of the following profiles, or a filepath and a
salinity profile, temperature profile, depth profile, pressure profile, and 
potential density profile as separate parameters. These profiles should come in the form of numpy 
arrays. This function then writes a CSV file to the given filepath. This file should 
contain appropriate column names, and the profiles of each variable given in the parameters.
Ideally, depth should be the first column, but you will not be graded on this.

Please remember to use the CSV tutorial, linked above.
*** 30 points ***


Problem 4: In the main function, you'll notice some data is given. However, not all data
required for questions 2 and 3 are present. Create this data using the seawater package. Next,
call your functions created in questions 2 and 3, either passing in a filepath and a dictionary or
a filepath and all of the profiles as separate parameters using the data provided and the data
you calculate with the seawater package.
*** 10 points ***


Before submitting, please check that the files you created have the contents you desire. No need
to submit the files you create, just submit the script that creates them (this script).

*** 15 points will be used to grade code style and logic ***

"""

from netCDF4 import Dataset
import numpy as np



def createNetCDF(fp, profileDict):
    """This function takes in a filepath to a new netCDF file, a depth profile, a 
    salinity profile, and a temperature profile. It creates a new netCDF file with the only
    dimension being depth, and creates the variables of lev, temp, sal, pres, and pden with 
    the correct data assigned to those variables. Last, a description is added to the netcdf 
    file, as well as a source.
    """
    # Call question 1 function to delete file if it exists. You must create this function.
    
    # Write netCDF file, which is what the 'w' indicates
    nc_ocean_data = Dataset(fp,'w',format='NETCDF4_CLASSIC')
    
    # creates only dimension, depth level
    # 1. nc_ocean_data.createDimension('lev', lengthOfDimension))
    
    # For all variables...
    # 2. nc_ocean_data.createVariable('variableName', dataType, (dimension,))
    # 3. nc_ocean_data.variables['variableName'][:] = variableData
    
    
    # 4. create attributes
    
def createCSV(fp, profileDict):
    """This function takes in a filepath, a salinity profile, temperature profile, depth profile,
    pressure profile, and potential density profile. It creates a CSV file with all of these
    profiles as the data.
    """
    
    with open(fp, mode='w') as ocean_file:  # note that the 'w' mode means 'write'.
        ocean_writer = csv.writer(ocean_file)
        # more...


def main():
    depthData = np.array([5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 
                      125, 150, 175, 200, 300, 400, 500, 750, 1000])
    salData = np.array([25.5086, 25.5084, 25.5292, 28.8857, 28.9132, 29.0884, 29.1017, 29.111, 
                        29.118, 29.7642, 29.7731, 29.8756, 29.883, 29.9072, 29.916, 30.2831, 
                        30.2838, 30.295, 30.3118, 30.313])
    tempData = np.array([9.3109, 9.3104, 8.9506, 8.9452, 8.4689, 8.4648, 8.4003, 8.4002, 8.4754, 
                         8.4755, 8.487, 8.4865, 8.4865, 8.4867, 8.4888, 8.4885, 6.4914, 5.0916, 
                         4.6729, 4.4918])
    # 1. do calculations for other variables
    
    
    # 2. add all to a dictionary if you desire
    
    
    # 3. change the name of these files to your_name_nc_file.nc or your_name_csv_file.csv
    newNcFp = "testncfile.nc"
    newCsvFp = "testcsvfile.csv"
    
    # 4. Call functions and pass in a filepath and either all profiles as different parameters or a
    # profile dictionary.


if __name__ == "__main__":
    main()