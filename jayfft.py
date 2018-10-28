#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 11:32:06 2018

@author: Jay
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

 
SAMPLE_RATE = 44100
N=4096
 
def fourier_transform(x):
    data_list = list()
    count =1
    for k in range(0, N):
        window = 1 # np.sin(np.pivalue * (k+0.5)/N)**2
        data_list.append(np.complex(x[k] * window, 0))
        count+=1
    fourier_transform_rec(data_list)
    return data_list
 
def fourier_transform_rec(data_list):
    N = len(data_list)
    if N <= 1:
        return
 
    evennum = np.array(data_list[0:N:2])
    oddnum = np.array(data_list[1:N:2])
 
    fourier_transform_rec(evennum)
    fourier_transform_rec(oddnum)
 
    for k in range(0, N//2):
        t = np.exp(np.complex(0, -2 * np.pi * k / N)) * oddnum[k]
        data_list[k] = evennum[k] + t
        data_list[N//2 + k] = evennum[k] - t
 
 
 
df = pd.read_csv('/Users/Jay/Downloads/jay.dat', sep='\s+', header=None)
x1=df[1]
xlist1=[]
for i in x1:
    xlist1.append(i)
xlist1=xlist1[:1024]


data_list = fourier_transform(x1)
 
 
# Plotting of values 
_, plots = plt.subplots(2)
 
 
# Plot in frequent-domain to time-domain graph

powers_all = np.abs(np.divide(data_list, N//2))
powers = powers_all[0:N//2]
frequencies = np.divide(np.multiply(SAMPLE_RATE, np.arange(0, N/2)), N)
plots[1].plot(frequencies, powers)
 
 
# view plots
plt.show()

