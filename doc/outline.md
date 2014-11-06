# Introduction to Python Workshop

This is the outline of the workshop. These are not intended to be detailed lecture notes.

Workshop website: http://bit.ly/hack-python-workshop (http://hack-at-uchicago.github.io/python-workshop/)

The tweet datasets for the exercises is available at: http://people.cs.uchicago.edu/~borja/upload/tweets.zip [45MB]

The live code will be available at http://bit.ly/pyw-code

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
    
Students should submit the output here: http://bit.ly/hack-python

The correct output is:

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

Make sure that you are able to run the intro.py file from the command line (examples/simple/intro.py). Next, try running that same code from the interpreter.


## Lists

At this point, we're going to go through a lot of short examples on the IPython notebook.

Explain that we are not going to "lecture" about all the language features. Instead, we are going to show multiple examples (which students will have access to). When we get to the exercises, students will need to extrapolate from the various features that are highlighted in the examples.

Go through the following topics:

 - Accessing lists ([], slicing)
 - Extending lists (append, extend, insert)
 - Removing (del, pop)
 - Misc functions: len, min, max, sort
 - Iterating through a list
 
### Twitter example

get_tweet_lengths.py

Explain the workshop.py module

Load N tweets (as list of strings). First on the interpreter, then on a script.

First without sys.argv. Then, add sys.argv.

### Twitter exercise

1. Write a script that computes the average length of a list of tweets.

2. Modify it so it will also compute the standard deviation.

Square root: 

    import math
    
    math.sqrt(N)

## List Comprehensions

Show simple examples.

## More datatypes

 - Strings
 - Tuples
 - Sets

## Dictionaries

 - Explain what a dictionary is (associative array, map of keys to values)
 - Initializing, accessing dictionaries
 - has_key, keys, values, items
 - Misc functions: len, min, max, sort

### Twitter example

Play around with the load_tweets() function (which returns a list of dictionaries).

Dictionary contains values specified here: https://dev.twitter.com/docs/platform-objects/tweets

print_tweet_info.py: Print some basic info

get_length_frequencies.py: A script that computes the frequency of lengths of tweets.


### Twitter exercise

Write a script that computes the frequency of hashtags.

exercise_dict.py

## Functions

 - Writing functions
 - Default parameter values
 - Positional vs. keyword
 - Returning values

### Twitter example

Write a function that returns the lengths of tweets.

functions.py

### Twitter exercise

Write a function that extracts all the values of a field, and a function that generates the frequencies of those values.

We provide get_frequencies.py. They implement exercise_functions.py.





## Simple visualizations

Use the extract_lengths function and the compute_frequencies function to generate a simple plot:

    lengths = functions.extract_lengths("tweets.json", 20000)
    freqs = functions.compute_frequencies(lengths)
    freqs = freqs.items()
    freqs.sort()
    xs = [f[0] for f in freqs]
    ys = [f[1] for f in freqs]
    plot(xs, ys)

and extract_values functions to do hist() visualizations with pylab.

    lengths = functions.extract_lengths(20000, "tweets.json")
    top_lengths = functions.extract_lengths(20000, "top_tweets.json")

    hist(lengths, bins=50)
    hist(top_lengths, bins=50)

    top_retweets = extract_values(20000, "top_tweets.json", "retweet_count")
    hist(top_retweets, bins=50, log=True)

    top_favorite = extract_values(20000, "top_tweets.json", "favorite_count")
    hist(top_favorite, bins=50, log=True)

TODO: Exercise?

## Extra Topics

Only if we have time:

 - Object Orientation
 - Packages and Modules
 - Functional programming
 - Python Standard Library
 - NumPy

