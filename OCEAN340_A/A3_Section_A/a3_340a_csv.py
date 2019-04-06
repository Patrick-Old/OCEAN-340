# Your Name
# OCEAN 340A
# Problem Set #3: CSV Files
# Winter 2019

"""
In this assignment, we will try to attempt some tasks that are relatively simple in concept, but
are quite difficult if not performed in the correct way. These including finding data, reading in
that data in a way that structures it in an easy to analyze format, and a couple of other
short exercies. These are very realistic tasks for data scientists in oceanography (and just
data scientists in general), and serve as an introductory insight into the rest of the quarter 
for us.

PART 1: Experience Finding Data

Question 1: For about 15-20 minutes, try and find some example oceanographic data online.
You won't be using the data for this assignment specifically, but this may begin to spark
some ideas for your final project. Try searching for very specific data - were you able to find it?
What other data did you find? How about any sites that were confusing to use? Any sites that were
completely shut down? Please write 3-4 sentences answering these questions (don't worry if you
don't address them all, just detail your experience doing this exercise).

*** 10 points ***

PART 2: np.genfromtxt versus csv functions

Question 2: For another 20-25 minutes, try to open the GIVEN file that contains vertical profile 
data and do so by using the np.genfromtxt() function from the numpy module. Do this in a function
of your own. This is a very common way of opening up random data sets, and many of you have used 
this in OCEAN 215. Feel free to lookup the documentation on this function online or by using the 
IPython console in your IDE (Canopy or Spyder). Once opened, try to extract the temperature, 
potential salinity and depths from the dataset and add them to a dictionary for 
you to use. How did this work for you? If you run into any issues, try changing the parameters that 
the function takes in / work with the data to put it in a better format for you to analyze. 
Please write 3-4 sentences describing your experience with this / answering the above questions.
No need to submit your code for this question - feel free to comment the code you write in a 
multi-line comment, or delete it.

*** 10 points ***


NOTE: Save the code from questions 3 - 6 to submit for your homework.

Question 3a: Now, try and use the csv module to open the file and extract the temperature, 
potential salinity and depth from the dataset and add them to a dictionary for you 
to use. Try looking up the documentation for it online / using forums to figure out how to do 
this best.
After about 20 minutes we will go over a fast way to do this together.

Please describe your experience using the documentation in 2-3 sentences, and how far you got on
it before we reconvened.

*** 10 points ***


NOTE: For the problems below, please ask the difference between filepath and filename if 
you're unsure.

Question 3b: Turn question three into a function that takes in a filepath and a list of variables 
(which should be the names of columns in the csv file given). This function opens the data using 
the csv module functions we went over in class, and returns a dictionary with keys of the 
variable names given and values of all of the data in those variable columns.

*** 15 points ***


Question 4: Create a function that returns a list of all of the column headers (variable names) 
found in a given csv file (should take in the filepath).

*** 15 points ***


PART 3: Connect it all (and another script) in main

Question 5: 

NOTE: Please read the entire question before starting to write the code for this question.

Create a main function & use the if __name__ == "__main__" syntax to call it.
In your main function, call your plotVar function you created in the past on the data from your 
dictionary you created today. Your dictionary should have at least three column names 
(PSAL, TEMP, etc.) in it. While you will still likely need to get the depth data from the 
csv file, do not count it toward one of your three column names. Do not copy paste your plotVar 
function into this script. Instead, import it from the script that it is already in. As a 
realistic exercise, make sure this script (where you're importing the plotVar function) and the 
script containing the plotVar functions are in DIFFERENT directories. Try googling how to handle 
this scenario and/or ask for help on it if you're confused!

Last, also in main, call your function to get all of the column names in the given .csv file and
print the list that the function returns.


*** 25 points ***


*** An additional 15 points will be used to grade code style / logic. Please see style guide
on the 340A Canvas page and ask any questions about the guide if you have any. ***

When submitting, please include your name in the filename:
ex. Patrick_Old_a3_340a_csv.py
"""

import csv
import numpy as np
