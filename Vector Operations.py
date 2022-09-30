#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#09/29/2022
#This programs function is to perform operations on two given vectors, where each list corresponds to a reading of sounds, one will be amplified and one will be attenuated
import numpy as np #importing the numpy module which allows for numbers to be represented as vectors
list1=[-9167,-7857,-6548,-5238,-3928,-2619,-1309,2,1293,2623] #first ordered pair of numbers
list2=[649,14,-659,-1318,-1977,-2636,-3295,-3954,-4613,-5272] #second ordered pair of numbers
x=np.array(list1) #equating x to the vector that corresponds to the first ordered list
y=np.array(list2) # equating y to the vector that corresponds to the second ordered list
print((2*x)+(0.5*y)) #computing an operation on each vector and then adding the results

