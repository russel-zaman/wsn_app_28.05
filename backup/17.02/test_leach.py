import io
import os
import random
import math
from pandas import *
from flask import Response
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Flask
from flask import Flask, render_template, request, url_for, redirect

xm=100
ym=100

sinkx=50
sinky=100

xgrid = np.arange(0, 110, 10)
ygrid = np.arange(0, 110, 10)

n=20

kb=4000
p=0.1
Eo=0.5
ETX=50*0.000000001
ERX=50*0.000000001
Efs=10e-12
Emp=0.0013e-12
EDA=5*0.000000001
rmax=100
do = np.sqrt(Efs/Emp)
Et=0
matricef=[]
matriceh=[]
matricel=[]
resEnergy=[]
S=[]

for h in range(1):
    S = [{'xd': sinkx, 'yd': sinky} for i in range(n+1)]
    Et = 0
    XR = np.zeros(n)
    YR = np.zeros(n)
    for i in range(n):
        S[i]['xd'] = np.random.rand(1)*xm
        XR[i] = S[i]['xd']
        S[i]['yd'] = np.random.rand(1)*ym
        YR[i] = S[i]['yd']
        distance = np.sqrt((S[i]['xd'] - S[n]['xd']) ** 2 + (S[i]['yd'] - S[n]['yd']) ** 2)
        S[i]['distance'] = distance
        S[i]['G'] = 0
        S[i]['type'] = 'N'
        S[i]['E'] = Eo
        Et = Et + S[i]['E']
        plt.figure(h*10)
        plt.plot(S[i]['xd'], S[i]['yd'], 'o', markersize=6, markerfacecolor='b')

        for ngrid in range(len(xgrid)):
            plt.plot([xgrid[ngrid], xgrid[ngrid]], [ygrid[0], ygrid[-1]], 'k-', linewidth = 0.5)
        for ngrid in range(len(ygrid)):
            plt.plot([xgrid[0], xgrid[-1]], [ygrid[ngrid], ygrid[ngrid]], 'k-', linewidth = 0.5)

    plt.plot(S[n]['xd'], S[n]['yd'], 'o', markersize=12, markerfacecolor='r')


    #########################################
    countCHs=0
    cluster=1
    flag_first_dead=0
    flag_half_dead=0
    flag_all_dead=0
    first_dead=0
    half_dead=0
    all_dead=0
    allive=n

    packets_TO_BS=0
    packets_TO_CH=0
    packets_TO_BS_per_round=0
    
    #########################################
    
    
    
plt.show()












