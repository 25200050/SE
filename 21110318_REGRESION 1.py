# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:30:18 2023

@author: isisa
"""
#ISABEL ORTIZ CORONA  21110318

import numpy as np
import matplotlib.pyplot as plt

 

x=np.array([-2,-1,0,1,2])
y=np.zeros((5,1))
y=x*2
w=0
y_e=w*x
m=5
e=np.zeros(5)

for x in range(5):
    y_e=w*x
    e[w]=np.sum(np.power(y_e-y,2))/(2*m)


w=np.array([0,1,2,3,4])    
plt.plot(w,e)    