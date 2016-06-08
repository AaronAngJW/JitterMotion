# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 10:42:07 2016

@author: Aaron
"""
#Import relevant modules 
import os
import numpy as np
import csv
from matplotlib.pyplot import *

C1adaptS = 0
CN2adaptS = 0
N3adaptS = 0
NS4adaptS = 0
S5adaptS = 0
C1adaptC = 0
CN2adaptC = 0
N3adaptC = 0
NS4adaptC = 0
S5adaptC = 0

#Paste filename to be analysised here (The .csv file)
filename = 'PartID_AA_20160302_1332.csv'

#Change directory to file's location (Gaussian)
#os.chdir('C:\Users\Aaron\Dropbox\JitterAdapt\Dotty Simplified (Gaussian Edition)\Dotty Simplified (Full Experiment Folder)')
#Change directory to file's location (Plausible)
os.chdir('C:\Users\Aaron\Dropbox\JitterAdapt\Dotty Simplified (Gaussian Edition)\Dotty Simplified (Full Experiment Folder)')


loadcsv = open(filename, 'r')
for line in loadcsv.readlines():
    line = line.strip()
    #Split the words within the line
    trialnum, stimulus, stimulus_location, response, more_sin_like, sin_adapt = line.split(',')
    if stimulus == 'C1' and more_sin_like == '1' and sin_adapt == '1':
        C1adaptS += 1
    elif stimulus == 'CN2' and more_sin_like == '1' and sin_adapt == '1':
        CN2adaptS += 1
    elif stimulus == 'N3' and more_sin_like == '1' and sin_adapt == '1':
        N3adaptS += 1
    elif stimulus == 'NS4' and more_sin_like == '1' and sin_adapt == '1':
        NS4adaptS += 1
    elif stimulus == 'S5' and more_sin_like == '1' and sin_adapt == '1':
        S5adaptS += 1
    elif stimulus == 'C1' and more_sin_like == '1' and sin_adapt == '0':
        C1adaptC += 1
    elif stimulus == 'CN2' and more_sin_like == '1' and sin_adapt == '0':
        CN2adaptC += 1
    elif stimulus == 'N3' and more_sin_like == '1' and sin_adapt == '0':
        N3adaptC += 1
    elif stimulus == 'NS4' and more_sin_like == '1' and sin_adapt == '0':
        NS4adaptC += 1
    elif stimulus == 'S5' and more_sin_like == '1' and sin_adapt == '0':
        S5adaptC += 1
        
print C1adaptS
print CN2adaptS
print N3adaptS
print NS4adaptS
print S5adaptS
print C1adaptC
print CN2adaptC
print N3adaptC
print NS4adaptC
print S5adaptC

SinAdaptList = [C1adaptS, CN2adaptS, N3adaptS, NS4adaptS, S5adaptS]
ConsAdaptList = [C1adaptC, CN2adaptC, N3adaptC, NS4adaptC, S5adaptC]

plot (SinAdaptList)
plot (ConsAdaptList)

xlim(0, 4)
ylim(0, 20)

xticks([0,1,2,3,4], ['C1','CN2','N3','CN4','S5'])

xlabel('Conditions')
ylabel('No. of Trials perceived as more Sin-like')

legend(['Adapted to Sin','Adapted to Constant'])


    