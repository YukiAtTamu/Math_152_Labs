#!/usr/bin/env python
# coding: utf-8

# Double-click to insert team members' names here: Yuki Janvier, Daniel J McCabe III, Yada C Van Noort, Cole Bailey

# In[1]:


from sympy import *
from sympy.plotting import (plot, plot_parametric)
import math


# #1a Evaluate expression

# In[2]:


# Defining variables x and y
x = 6.5
y = 3.2

# Equation from 1a
a = (x**2 + y**2)**(1/2) + ((x*y)/(y-x))

# Output
print("The answer to 1a is",a)


# #1b Evaluate expression

# In[2]:


# Equation from 1b
b = x + y + ((x*y)/(y-x))

# Output
print("The answer to 1b is",b)


# #1c Equality and implications

# In[ ]:


''' 
    *Reason for why a and b aren't equal*
    Just because there is a square root on the outside does not mean
    it will cancel the squares on the inside    
'''


# #2a Trig value at pi/6

# In[4]:


# Defining variable x
x = symbols('x')

# Equations
rightSide = .5*(1+cos(2*x))
leftSide = (cos(x))**2

# Subbing pi/6 for both sides of the eqn
rightSub = rightSide.subs(x,pi/6)
leftSub = leftSide.subs(x,pi/6)

# Output
print("The difference between the left and the right side is",str(rightSub - leftSub),"meaning the identity holds true.")


# #2b Trig value at 1.25

# In[5]:


# Equations
rightSide = .5*(1+cos(2*x))
leftSide = (cos(x))**2

# Subbing 1.25 for both sides of eqn
rightSub = rightSide.subs(x,1.25)
leftSub = leftSide.subs(x,1.25)

# Output
print("The difference between the left and the right side is",str(rightSub - leftSub),"meaning the identity holds true.")


# #2c graph on [0, 2pi]

# In[6]:


matplotlib notebook


# In[20]:


# Equation
eqn = (cos(x))**2 - .5*(1+cos(2*x))

# Plotting eqn
plot(eqn,(x,0,2*pi))

'''
    *Explanation for y does not equal 0 on plot*
    The y-axis shows a few peaks at approx 1 and -1 with the scale
    being set to 1e-16 meaning that the dips are probably invisible when
    set on a normal one-to-one scale
'''


# #3a plot of "non-identity"

# In[21]:


matplotlib notebook


# In[23]:


# Equation
eqn = sin(2*x) - 2*sin(x)

# Plotting eqn
plot(eqn,(x,0,2*pi))


# #3b Solve equations to find roots and critical values

# In[27]:


# Place where f(x) (eqn) equals 0
eqnSoln = solve(eqn-0,x)
eqnSolnApprox = [i.evalf() for i in eqnSoln]

# First Output
print("The values of x where f(x) = 0 are",eqnSolnApprox)

# Critical numbers (places where f'(x) equals 0)
eqnPrime = diff(eqn,x)
critVal = solve(eqnPrime-0,x)

# Second Output
print("The critical values are",critVal)


# #4 Definite integral using FTC

# In[29]:


# Integral of sqrt(1 + x**2)
eqn = .5*asin(x) + ((x * (1-x**2)**.5))/2

# Subbing in values 1/2 and 0 for eqn
eqnHalf = eqn.subs(x,.5)
eqnZero = eqn.subs(x,0)

# Output is the fundamental theorem F(b) - F(a)
print("The answer is", str(eqnHalf - eqnZero))


# In[ ]:




