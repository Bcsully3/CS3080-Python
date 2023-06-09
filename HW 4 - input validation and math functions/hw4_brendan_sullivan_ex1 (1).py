# -*- coding: utf-8 -*-
"""HW4_Brendan_Sullivan_ex1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OKfIGZI-T-VilEclIzBi67bpx-YwoSDB
"""

""""
Homework 4, Exercise 1
Brendan Sullivan
3/9/2022 
This program creates classes for Circles, Squares, and Rectangles, and gives them methods
to calculate their areas, perimeters, and diagonals. Then, at the end, it calculates  the perimeter 
of a circle with a radius that’s half  of  the  diagonal  of  a  rectangle  with  a  length  of  20  and  
width  10
"""


import math

# Circle class
class circle:

  def __init__(self, radius):     # init
    self.radius = radius

  def findArea(self):     #methods
    return (math.pi * self.radius * self.radius)

  def findDiameter(self):
    return (2 * self.radius)

  def findCircumference(self):
    return (2 * math.pi * self.radius)


# Square Class
class square:

  def __init__(self, side):     # init
    self.side = side

  def findArea(self):          #methods
    return (self.side*self.side)

  def findDiagonal(self):
    return (math.sqrt( (self.side*self.side) *2 ))

  def findPerimeter(self):
    return (self.side*4)


#rectangle class
class rectangle:
 
  def __init__(self, width, length):     # init
    self.length = length
    self.width = width

  def findArea(self):                   #methods
    return (self.width*self.length)

  def findDiagonal(self):
    return int((math.sqrt( (self.width*self.width) + (self.length*self.length) )))

  def findPerimeter(self):
    return ((self.width*2)+(self.length*2))

circle1 = circle(2)
square1 = square(2)
rect1=rectangle(10,20)


#  calculate the perimeter of a circle with a radius that’s 
# half  of  the  diagonal  of  a  rectangle  with  a  length  of  20  and  width  10


diagonal = rectangle(10,20).findDiagonal()
circle1=(circle(.5*diagonal))
print(circle1.findCircumference())