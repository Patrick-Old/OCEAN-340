# Your Name
# OCEAN 340B
# Problem Set #4: netCDF Files
# Winter 2019


"""In this assignment, we will be investigating how to use netCDF files. Write all of your
code at the global scope (not in functions) for this assignment. This assignment will be more of an
investigation into netCDF files than writing complex functions.

IMPORTANT: When you're asked to print something, please state the question before it and add
an empty print statement after your answer. Example:
    
    print ("Question 1")
    print ("Here is my answer")
    # OR
    print (answer) # where answer is saved to a variables
    
    print () # Add print statement like this to separate out the parts.
    
NOTE: Be sure to complete all answers to questions just below where the question is stated, keeping
a good amount of space between each question (making sure the document doesn't get messy).

Data source: http://ncss.hycom.org/thredds/ncss/grid/GOMl0.04/expt_32.5/2014/hrly/dataset.html
    
*** An additional 15 points will be used to evaluate code style / logic. ***
"""


"""Question 1
Let's spend 15 minutes looking into netCDF files and reconvene with what we find. 
Try: Opening the file, finding python packages to work with the data, types of datasets
that use netCDF, what the file extension name is, etc.
Please explain what you find / your experience in 2-3 sentences.

*** 10 points ***

Answer: 
    
"""



"""Question 2
Now, let's open up our dataset and examine some metadata found within it. Metadata describes
important information about the dataset, but does not contain the data we are interested in
for our analysis. For example, we can find the conventions used when creating the file, and
information like who was the cheif scientist (which was found in the metadata of our netCDF
file on Friday). Write your code just below this question and put your answer within the same
multi-line comment this question is written in.

Please install the netCDF4 module using the following command on the terminal or command prompt: 
    - pip install netCDF4 

Answer the following:
1. What institution created this netCDF file?
2. What conventions were used in the creation of this file?
3. What are the latitudinal max and min in the file? How about the longitudinal max and min? Find
this by iterating through the metadata, not the actual data.

*** 10 points ***

"""




"""Question 3
Now, let's investigate some characteristics of the data found within the file. For each of the
variables in the file, print the variable's name on one line, and on the next line, print 
the variable's information (which will contain several lines of valuable information). Add an 
additional print statement after printing a variable's information to keep things separated. 

*** 10 points ***
"""



"""Question 4
Answer the following three questions for the mld (mixed layer depth), salinity,
and depth variables.

a. How many dimensions are there for this variable?
b. What are the dimensions?
c. What are the units for the variable?

*** 10 points ***
"""

q4 = """
    MLD
    a. Answer 1
    b. answer 2
    c. answer 3
"""





"""Question 5
Now, lets determine how to examine the data within each variable of the netCDF file. Below,
assign the data for salinity, temperature, mixed layer depth, latitude, longitude, depth, and time
to variables. Then, print the data of three variables of your choice with a blank line 
inbetween them. After you've confirmed that your printing code works, comment out just the
printing code, as the output will take up a lot of unnecessary space in the console. Be sure to
not comment out the variables assigned to the data.

*** 10 points ***
"""



"""Question 6
To help us conceptualize our data, please visit the two maps below:
    - http://mrkash.com/activities/images/map.jpg
    - https://canvas.uw.edu/courses/1270526/files/folder/Class%20Notes?preview=53810557
    
Now that we can see the exact area of the globe we are working in, let us do some calculations on
the data to extract some meaningful information. 

Find the average salinity and temperature in the region. Print these values as follows:
print ("Temperature mean:", tempAvg) # where you define tempAvg
print ("Salinity mean:", salAvg) # where you define salAvg

Last, write a sentence or two (and print it) describing what taking the mean of this data does.
In your response, please relate it back to the region and depths you're analyzing.

*** 5 points ***
"""



"""Question 7
Next, average all of the days together in the temperature and salinity variables. This will 
eliminate the time dimension of our data, and leave us with just geospatial data (depth, lat, lon).
Reassign your temperature and salinity variables to these new values. Last, print the
new shape of these variables.

*** 5 points ***
"""


"""Question 8
Now, create the average vertical profiles of salinity and temperature for this region. Do this by
averaging the latitude and longitude out for each depth level, leaving us with one data point for
each depth in our region, which represents the 2-D space and time averaged vertical profile. The
temperature and salinity vertical profiles must be numpy arrays.

*** 15 points ***
"""


"""Question 9
Last, lets import your plotVar function and plot both temperature and salinity versus depth using
our calculations from question 8.

*** 10 points ***
"""
