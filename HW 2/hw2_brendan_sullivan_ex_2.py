# -*- coding: utf-8 -*-
"""hw2_BrendanSulliva_ex_2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18Mz1DhS4QaJluJ4-Uy_GhZ0UI0mIZmjU
"""

''' 
Homework 2, Exercise 2
Brendan Sullivan
2/16
This program performs the collatz sequence on a number provided by the user, but makes sure that the user entered a valid interger
'''
def collatz2(number) :
  returnValue = 0
  try:
    if (number % 2 == 0):
      returnValue = number // 2
    
    else :
      returnValue = 3*number+1

    return returnValue

  except:
    print("Error. Make sure that you entered an integer")

inputNum = input()

try:
  result = collatz2(int(inputNum))
  print(result)

  while (result != 1):
    result = collatz2(result)
    print(result)
except:
      print("Error. Make sure that you entered an integer")