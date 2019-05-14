# Your Name
# OCEAN 340B
# Problem Set #4: CNV Files 
# Winter 2019


"""
In this assignment, we will complete similar exercises as we did on Monday this week for OCEAN 340A.
However, instead of doing this with a CSV file, we will now complete the exercises with a CNV file.
This file type is very common in oceanography, and specifically profile casts often come in CNV
files. For example, this is what the data originally came in for OCEAN 220 this past year when
we took profile casts out in the Puget Sound, and one of those profile casts is what we will
be working with for this problem set.

Question 1: To make this problem set more realistic, go ahead and investigate how to open CNV files
in Python online. Additionally, you may want to try to open the file by clicking on it. Spend about
20 minutes on this, and detail your experience in 3-4 sentences below.
*** 10 Points ***



NOTE: For the questions below, you're responsible for coming up with the function header names,
parameters, and docstrings.

Question 2: Now that we have reconvened and discussed how to properly work with CNV files, please
write a function that takes in a filepath to a CNV file and a list of desired 
variable profile names you wish to extract the profiles of from that file. You should return a 
dictionary with they keys being the desired variable names and values being the profiles of those
variables.

HINT: This is essentially the same function you wrote on Monday for 340A, except it now needs to
work with CNV files instead of CSV files.
*** 15 Points ***



Question 3: Create a function that takes in a dictionary with the keys being strings representing
variables and the values being the profile of it's corresponding variable in the form of a list. 
Additionally, one of the keys must be depth, and the value must be the depths at which all 
of the profiles occur at. This function then creates multiple plots of all of the profiles versus 
depth, excluding plotting depth versus depth. You should call your plotVar function from another
script you wrote previously to do the plotting.
*** 20 Points ***



Question 4: Create a function that takes in a filepath to a CNV file and returns all of the 
profile variables in that CNV file in the form of a list.
*** 10 Points ***



Question 5: Create a function that takes in a filepath to a CNV file and returns the latitude
and longitude of where the profile was taken, both in the form of floats. Round these to
have a maximum of four digits after the decimal place. Return them in the order 
of latitude, longitude.
*** 10 Points ***



Question 6: Create the main function (being sure to use if __name__ == "__main__" syntax). Call 
your function from question two to create a dictionary of certain variable profiles you're
interested in (at least three not including depth), and then call your function from question 
three to plot all of the profiles. Then, call your functions you created in questions four and 
five, printing the result of each of those functions.
*** 20 Points ***



*** An additional 15 points will be used to grade your problem set's use of style and logic ***

When submitting, add your name to the filename when submitting, ex. Patrick_Old_a3_340a_csv.py


Also, don't forget to submit your final project proposal, due the same time as this problem set
(Thursday, 2/7/19 @ 11:59 PM).

"""


# Your code should start right here! Don't forget, put all of your imports right here, not
# throughout your script... :) 

