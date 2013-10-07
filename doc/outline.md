# Introduction to Python Workshop

This is the outline of the workshop. These are not intended to be detailed lecture notes.

The tweet dataset for the exercises is available at: http://people.cs.uchicago.edu/~borja/upload/tweets.zip [41MB]

## Introduction to Python

We start by showing a piece of Python code. The goal is to highlight that, if you know C/C++/Java/etc., you probably know how to read Python.

    a = [10, 1, 2, 76, 20, 3, 20, 49, 98, 5]
    n = 0
    for i in a:
        if i > 5:
            print i
        else:   
            n += 1
    
    print "n is " + str(n)
    
Students should submit the output here: http://bit.ly/hackpyw

The correct output it:

    10
    76
    20
    20
    49
    98
    n is 4
    
We use this code to highlight some of the main differences between Python and other languages. We will show the equivalent C code, since most students who have signed up have either a C or Java background.

The equivalent C code is:

    #include<stdio.h>

    int main()
    {
        int a[] = {10, 1, 2, 76, 20, 3, 20, 49, 98, 5};
        int n = 0;
    
        for(int i=0; i < 10; i++)
        {
            if(a[i] > 5)
                printf("%i\n", a[i]);
            else
                n++;
        }
    
        printf("n is %i\n", n);
    }

Main differences:

 - Dynamically typed
 - Blocks delimited using tabs
 - Lists are a first-class citizen
 - You can loop directly on the values of the list, no need to use an index variable
 - No need for a main() function 
 
Now, show the same code in the interpreter.


### Exercise

Make sure that you are able to run the intro.py file from the command line. Next, try running that same code from the interpreter.


## Lists

At this point, we're going to go through a lot of short examples on the IPython notebook.

Explain that we are not going to "lecture" about all the language features. Instead, we are going to show multiple examples (which students will have access to). When we get to the exercises, students will need to extrapolate from the various features that are highlighted in the examples.

For lists, cover at least the following:

 - TODO
 - TODO
 - TODO
 
### Twitter example

Load N tweets (as list of strings). Write a script that prints the length of the tweets.

### Twitter exercise

1. Write a script that computes the average length of a list of tweets.

2. Modify it so it will also compute the standard deviation.

## Dictionaries

### Twitter example

Play around with the load_tweets() function (which returns a list of dictionaries).

### Twitter exercise

Write a script that computes the frequency of lengths of tweets.

## List Comprehensions

TODO

Maybe use list comprehensions to do "queries" on the dataset?

## Functions

TODO

## Simple visualizations

Take the length frequencies and plot them with matplotlib.

## Extra Topics

Only if we have time:

 - Object Orientation
 - Packages and Modules
 - Functional programming
 - Python Standard Library
 - NumPy

