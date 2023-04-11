# -*- coding: utf-8 -*-
"""hw6_Brendan_Sullivan_ex2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t74E0LJMX27Ozzn7hZ2PR-r45Jgps4st
"""

"""
Homework 6, Exercise 2
Brendan Sullivan
4/11/2023
This program provides a cache function decorator for a fibonacci sequence. The decorator has
a function attribute dictionary that stores calculated values from the fibonacci sequence
so that they don't have to be recalculated.
Without using the cache and just using the normal function, I ran fibonacci(20) and it took 20 seconds
and called the function 21,891 times. Then I tried it using the deccorator, and it took 1 second and called
the function 39 times, making it significantly quicker than no using the cache.
"""

import functools
def cache(func):
    @functools.wraps(func)
    def wrapperCache(*args, **kwargs):
        wrapperCache.numCalls += 1
        print("Call {} of {}".format(wrapperCache.numCalls, func.__name__))         ## see the number of function calls to compare to when not using the dictionary
        return func(*args, **kwargs)
    wrapperCache.numCalls = 0
    wrapperCache.dictionary={}
    return wrapperCache

@cache
def fibonacci(num):
    fibonacci.dictionary
    if num in fibonacci.dictionary:         #if it the num was already calculated
        return fibonacci.dictionary[num]
    elif num < 2:                                           # if the num is 1 or 0
        fibonacci.dictionary[num]= num
        return num
    else:                                                                 # if the num is not already calculated
      newValue = fibonacci(num - 1) + fibonacci(num - 2)
      fibonacci.dictionary[num]= newValue                        #save the new value to the dictionary
      return newValue 


  
print(fibonacci(20)) 
print(fibonacci.dictionary) # 2