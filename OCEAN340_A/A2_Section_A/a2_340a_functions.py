# Your Name
# Winter 2019
# OCEAN 340A
# Assignment 2: Functions


"""Welcome to the second assignment for OCEAN 340A! Here, we will begin investigating
how to properly write functions, create full scripts, and utilize outside modules that contain
functions to create an interactive application that plots oceanographic data.

Please install the seawater module in Canopy by doing the following:
    1. Open the Canopy editor.
    2. Open the tools tab at the top of the page in Canopy.
    3. Select "Canopy Terminal".
    4. Type the command "pip install seawater"
    
Or in Anaconda by running this command in your command prompts (Windows) or terminal (Mac):
    conda install -c conda-forge seawater
    
If you get a message on the terminal saying the task is done or completed,
congrats! You have just installed an incredibly powerful module for conducting
oceanographic research. We will be using it throughout the quarter in our
problem sets.

Additionally, we can learn more about the module by using these commands in the console.

For general information about the module:
    seawater?

For a list of all functions we can use:
    dir(sw)

For helpful information on a specific function:
    seawater.dens?
    
Below, you will create a Python script that utilizes the main() function, and run it using
the proper format of:
    
if __name__ == "__main__":
    main()
    
    

In this assignment we will prompt the user for a certain number of plots they would
like to make, ask which variables they would like to be plotted, and then plot those plots
accordingly. This is done by breaking this goal into smaller tasks. Each smaller task
is a function that you will write. These functions should then connect in the main
function, which is executed when the program is run and the two lines of code above this
paragraph are included in your script.
    

    
*** There are 90 points in this assignment. An additional 10 will be used to grade style. ***
    
Please complete the following questions, and as always, don't hesistate to ask if something is
confusing!
"""



# Question 1
"""Identify the parameters the density calculation from the seawater package requires. 
Please state the type of data that it uses (list, string, etc.), specifically what 
the data is supposed to be (turbidity, chlorophyll content, salinity, etc.), and what the 
units are of that data. Briefly explain how you found this information.

Answer in the form of a multi-line comment.

*** 10 points ***
"""



# Question 2
"""Create any additional profiles you need in order to calculate density. Save these to a
variable in main.

*** 5 points ***
"""



# Question 3
"""In your main function, calculate the density of seawater in kg/m^3. Save this to a variable 
with an appropriate name.

*** 5 points ***
"""



# Question 4
"""Please complete the function getPlotVars. Be sure to:
    1. Prompt the user with a question asking them how many plots they would like to make.
    2. Prompt them each time asking the name of the variable they would like to plot.
    3. Output the names of the variables they choose in the form of a list.

*** 20 points ***
"""



# Question 5
"""Please complete the function plotVar. Please note that there should not be more than one
profile plotted on the same plot.

*** 20 points ***
"""



# Question 6
""" Connect the functions you just wrote in the main function. Be sure to include the 
boolean statement to run main outside of the main script. If all goes well, you should have 
a fully functioning script that prompts the user for input (question 4) and plots their 
desired plots (question 5).

*** 30 points ***
"""



def getPlotVars():
    """This function prompts the user for how many plots they would like to make,
    and then asks them for the name of the variable they want to plot. It returns all of the
    names of the variables they would like to plot in the form of a list.
    """
    


def plotVar(var, depths, figNum, xlabel):
    """This function takes in a profile of a variable in the form of a list, a depth list,
    the figure number, and the label for the x-axis. It then plots the profile on a 
    specific figure, adding labels, a title, and inverts the y-axis.
    """



def main():
    s = [26.1, 26.2, 26.6, 27.9, 28.2, 28.4, 28.9, 29.3, 30.0, 30.2] # salinities
    t = [8.5, 7.8, 6.5, 6.4, 6.4, 6.4, 6.4, 6.4, 6.3, 6.1] # temps
    z = [10, 32, 41, 50, 54, 64, 82, 100, 300, 500] # depths
    print ("Hello, I am in main!")


if __name__ == "__main__":
    main()