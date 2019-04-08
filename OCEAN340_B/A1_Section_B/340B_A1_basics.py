# Your Name Here
# Winter 2019
# OCEAN 340B


"""
Hello OCEAN 340B class! In the first assignment, we will practice some
basic computing problems in Python to make sure we are able to accomplish
some more complex challenges later in the course that are much more 
exciting than this and relevant to the field of Oceanography.

These problems involve the use of Python syntax, lists, dictionaries, and loops.
These are all very important computer science fundamentals. 
We will utilize these very often in this course to accomplish some incredible tasks 
relevant to oceanography. However, for now, we will mostly just focus on programming, as 
refreshing this is likely a necessary step before we "dive" into applying these in 
an oceanographic setting.

Please use proper style, as discussed in class.


### IMPORTANT ###
Please submit this assignment with your first and last name, followed by the original
assignment name, like this:

Ex. Patrick_Old_340B_A1_basics.py


*** 90 points total listed. An additional 10 for style will be graded. ***
"""


"""
This question involves slicing lists in Python. This is a handy skill to know,
and is very commonly used.

Please note this as a good reference for how to conduct list slicing:

a[start:end:step] # where the variable a is of type list.
Citation: https://stackoverflow.com/questions/509211/understanding-pythons-slice-notation

*** Each part is worth 2.5 points, 10 points total. ***
"""

numList = list(range(1, 11)) # list function used to ensure entire range is printed
print (numList)


# Question 1a
"""Slice numList to get every other number, starting from the 0th index.
Assign the result to a new variable with a proper name, and print that variable.
"""

everyOther = numList[::2]
print (everyOther)


# Question 1b
"""Slice numList to get every other number starting from the 1st index.
Assign the result to a new variable with a proper name, and print that variable.
"""

everyOtherFirst = numList[1::2]
print (everyOtherFirst)


# Question 1c
"""Slice numList so that you reverse the list.
Assign the result to a new variable with a proper name, and print that variable.
"""

reverse = numList[::-1]
print (reverse)


# Question 1d
"""Slice numList so that you get every 3rd element, starting from the
second index and ending on the 8th index. 
Assign the result to a new variable with a proper name, and print that variable.
"""

everyThird = numList[2:8:3]
print (everyThird)


# Question 2
"""
Below, you're provided a list of integers, assigned to the variable someNums.
Work with each number in the list. If the number is less than 5, print "small". If less than 
10, print "medium", and for anything else, print "large". Print only one statement per integer.

*** 10 points ***
"""

someNums = [3, 6, 5, 10, 11]


# Question 3
"""You were out at sea collecting data, and received six density and depth measurements from 
a sparse profile cast you took. However, you made a mistake when working with the data, and
you think you may have accidentally changed the order of the density measurements, meaning
they no longer correspond to the correct depths in the profile.

However, you decide that you still want to work with the data. Do your best to put the density
measurements back in their original order using a built-in Python function (don't write one - 
if you're confused about this, please ask an instructor or google it!). Write a comment 
explaining your thought process on how to do this correctly.

You are given the following list of densities (kg/m^3):

[1024.121, 1022.347, 1024.001, 1023.771, 1016.21, 1023.85]

And the following list of depths (m):

[5, 25, 75, 100, 400, 700]

*** 10 points ***
"""



# Question 4
"""Building off question 4, calculate the average change in density per meter 
(this is the vertical component of the density gradient) between each data point. 
Round values to the 4th digit and print them in a list.

ex. In the following situation, given these simpler densities and depths to work with:

dens = [1025.0, 1025.1, 1025.2] # kg/m^3
depths = [100, 150, 250] # meters

You would receive this output:
    
output: [0.002, 0.001]

*** 15 points ***
"""



# Question 5
"""Create a dictionary with keys of 'sal' (salinity, PSU), 'temp' (temperature, Celsius),
and 'z' (depth, meters) that each map to the given values below, which is from a profile cast.
Print the dictionary.

*** 5 points ***
"""

sal = [26.1, 28.4, 29.3, 30.2, 30.0] # PSU
temp = [8.5, 7.8, 6.5, 6.4, 6.1] # Celsius
z = [10, 50, 100, 300, 500] # Meters



# Question 6
"""Building off of question 5, generate 5 more salinity, temperature, and depth values for the 
surface ocean (which we will define as being the range of depths from our most shallow 
depth up to 100 meters) using Python's 'random' module. Please keep in mind that this means there
should not be any values outside of the maximum values of the salinity and temperatures found in 
the current surface ocean. Update the dictionary you created by adding these new values to the 
dictionary's old values (each key now corresponds to one list, holding 10 elements).

### Helpful functions ###
random int: random.randint()
random float: random.uniform()

Remember, this data is supposed to represent an oceanic profile. You just added new, random
data points in no particular order. Think about how this will look when plotted, and do what you 
can to make the casts appear more realistic.

*** 20 points ***
"""



# Question 7
"""Next, prompt the user for user input (using Python's built in input() function), asking 
them which variable (salinity or temperature) they would like to plot. Then, plot based off of 
their input, show their desired plot. 

Please label the axis, add an appropriate title to the graph,
and invert the y-axis. No need to submit the plots that you create, just 
submitting the code you write will suffice!

This should look similar to an actual profile cast. If it does not, please refer back to question 
three to manipulate your data to make it more realistic.

*** 20 points ***
"""



# BONUS PROBLEM (If you're bored / interested...sorry, no extra credit)
"""Given the two dimensional array below, find the values within the top-left to
bottom-right diagonal, append them to a list, and print the list.


two_d = [[1, 2, 3, 4], 
         [5, 6, 7, 8], 
         [9, 10, 11, 12], 
         [13, 14, 15, 16]]

HINT: Output should be [1, 6, 11, 16]

*** NO points ***
"""