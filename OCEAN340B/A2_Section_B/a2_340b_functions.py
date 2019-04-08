# Your Name
# OCEAN 340B
# Winter 2019
# Assignment 2: Functions

"""
Welcome to 340B, Assignment #2! Please read all of the instructions before beginning.

In this assignment, we will be working with multiple scripts to accomplish our task. This will
build off of assignment #2 from 340A (Monday's assignment). We will be adding to that script,
and also will be adding to this script, creating some functions from scratch!

The new script (this file) will contain two functions that we need to create from scratch:
    1. A function called getTotalChange, which calculates the total change of a variable
    throughout it's profile and the average change per meter throughout the entire profile, and
    returns these values. The values should be a maximum of four digits after the decimal place.
    *** 20 points ***
    
    2. A function called vertGradVals, which calculates the ABSOLUTE VALUE of the maximum and 
    minimum changes between two continuous depths. The values should also be a maximum of 
    four digits after the decimal place.
    *** 20 points ***
    
    Ex.
        t = [10, 9, 8]
        z = [5, 10, 20]
        output: max = 0.2
                min = 0.1
                
    HINT: This is similar to a question from your homework last Friday.
    HINT #2: I recommend having your output be a dictionary for both of these functions!
    
Please create these functions, adding appropriate parameters and a docstring that follows
the style guide on Canvas in 340A.

Next, please edit your script from Monday to include the following:
    1. Only allow valid input from a user when they state how many plots they would like
    to plot, and the names of the variables they would like to plot.
    *** 30 points ***
    
    Ex. When the user is asked to provide a number of plots, if they respond with an invalid
    response (ex. any string that cannot be cast to an integer, like the word 'two'), 
    repeat the question and state that they provided an invalid response.
    
    Ex. When the user is asked for a variable to plot, if it is not an expected response
    (ex. you want them to type in 's' instead of the word 'salinity'), repeat the question and
    state that they provided an invalid response.
    
    Realistically, you would want to tell the user what type of input is valid
    (ex. explain that you're expecting s, t, p, or d for variables, or that you're expecting
    an integer when specifying the number of plots). You're encouraged to do this!
    
    This will be done by using while loops, and may require a try/except block. We will discuss
    these in class. For further assistance:
        
        User input with while, try/except block: https://www.youtube.com/watch?v=22UnNK8TOPI
        While loop help: https://www.youtube.com/watch?v=jSs58VZVLw8
    
    
    2. In your plotting function, create and use an inner function that returns a plot description 
    that puts all information from the functions you created in this script. You will create
    an appropriate function header (name and parameters if needed) for this function, and add an 
    appropriate docstring.
    *** 20 points ***
    
    Do this by:
        1. importing this script into the other script
        2. Creating a function named getPlotSubtitle that returns the description in the form
        of a string.
        3. Using plt.figtext() in the outer function to put the description in the plot. Please use 
        the command plt.figtext? in the console to learn more about this function.
        
        HINT: Because there is quite a bit of information to put in the inner plot description
        function, break it down into different lines, and assign each line to a variable, adding 
        a "new line character" to the end of each statistic to start the next stat on a new line. 
        Then, combine them all into one variable and return it. This should make this function
        easier to create the correct output.
        
        Ex. firstStat = "Total change: 3.1 \n"
            secondStat = "Avg change: 0.006 \n"
            thirdStat = "Gradient max: 0.05 \n"
            fourthStat = "Gradient min: 0.0"
            allText = firstStat + secondStat + thirdStat + fourthStat # use this as description
            return allText
        
        
        The result of the above code is a figure with a description that is broken into multiple
        lines. This should fill the 's' parameter of the plt.figtext function. Try using
        x = 0 and y = -0.2 for the other parameters (placing the description in the lower
        left hand side of the figure).

    Please submit BOTH scripts for your 340B problem set this week!
    
    There are a total of 90 points here. An additional 10 points will be used to grade code style.
    
"""
