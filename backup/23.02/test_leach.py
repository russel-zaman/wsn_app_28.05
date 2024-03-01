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
STATISTICS = {
    'DEAD': np.zeros((1, rmax+1)),
    'ALLIVE': np.zeros((1, rmax+1)),
    'COUNTCHS': np.zeros((1, rmax+1)),
    'PACKETS_TO_BS': np.zeros((1, rmax+1)),
    'PACKETS_TO_CH': np.zeros((1, rmax+1)),
    'PACKETS_TO_BS_PER_ROUND': np.zeros((1, rmax+1)),
    'THROUGHPUT': np.zeros((1, rmax+1))
}

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

    packets_TO_BS = 0
    packets_TO_CH=0
    packets_TO_BS_per_round=0
   
    #########################################
    for r in range(rmax+1):
        packets_TO_BS_per_round=0
        dead = 0
        countCHs = 0
        cluster = 1  
        C = []     
        X = []
        Y = []
        PACKETS_TO_BS = np.zeros((1, rmax+1))  
        
        if (r % round(1/p) == 0):
            for i in range(n):
                S[i]['G'] = 0
                S[i]['cl'] = 0

        for i in range(n):
            if S[i]['E'] <= 0:
                dead += 1
                if dead == 1:
                    if flag_first_dead == 0:
                        first_dead = r
                        flag_first_dead = 1

                if dead == 0.5*n:
                    if flag_half_dead == 0:
                        half_dead = r
                        flag_half_dead= 1

                if dead == n:
                    if flag_all_dead == 0:
                        all_dead = r
                        flag_all_dead = 1
           
            if S[i]['E'] > 0:
                S[i]['type'] = 'N'

        STATISTICS['DEAD'][h, r] = dead
        STATISTICS['ALLIVE'][h, r] = allive - dead
        
        for i in range(n):
            if S[i]['E'] > 0:
                temp_rand = np.random.rand()
                if S[i]['G'] <= 0:
                    if temp_rand <= (p / (1 - p * (r % int(round(1/p))))):
                        countCHs += 1
                        packets_TO_BS += 1
                        packets_TO_BS_per_round += 1
                        PACKETS_TO_BS[0] [r] = packets_TO_BS
                        S[i]['type'] = 'C'
                        S[i]['G'] = round(1/p) - 1
                        C.append({
                            'xd': S[i]['xd'],
                            'yd': S[i]['yd'],
                            'distance': np.sqrt((S[i]['xd'] - S[n]['xd']) ** 2 + (S[i]['yd'] - S[n]['yd']) ** 2),
                            'id': i,
                        })
                        X.append(S[i]['xd'])
                        Y.append(S[i]['yd'])
                        cluster += 1
                        if distance > do:
                            S[i]['E'] -= ((ETX + EDA) * 8 + Emp * 8 * (distance**4))
                        if distance <= do:
                            S[i]['E'] -= ((ETX + EDA) * 8 + Efs * 8 * (distance**2))
                            
        STATISTICS['COUNTCHS'][h, r] = countCHs

        for i in range(n):
            if (S[i]['type'] == 'N' and S[i]['E'] > 0):
                if (cluster - 1 >= 1):
                    min_dis = np.sqrt((S[i]['xd'] - S[n]['xd']) ** 2 + (S[i]['yd'] - S[n]['yd']) ** 2)
                    min_dis_cluster = 0
                    for c in range(cluster-1):
                        temp = min(min_dis, np.sqrt((S[i]['xd'] - C[c]['xd']) ** 2 + (S[i]['yd'] - C[c]['yd']) ** 2))
                        if (temp < min_dis):
                            min_dis = temp
                            min_dis_cluster = c

                    if (min_dis_cluster != 0):
                        if (min_dis > do):
                            S[i]['E'] = S[i]['E'] - (ETX * kb + Emp * kb * (min_dis ** 4))
                        if (min_dis <= do):
                            S[i]['E'] = S[i]['E'] - (ETX * kb + Efs * kb * (min_dis ** 2))

                        S[C[min_dis_cluster]['id']]['E'] = S[C[min_dis_cluster]['id']]['E'] - ((ERX + EDA) * kb)
                        packets_TO_CH += 1
                    else:
                        if (min_dis > do):
                            S[i]['E'] = S[i]['E'] - (ETX * kb + Emp * kb * (min_dis ** 4))
                        if (min_dis <= do):
                            S[i]['E'] = S[i]['E'] - (ETX * kb + Efs * kb * (min_dis ** 2))
                            
                        packets_TO_BS += 1
                        packets_TO_BS_per_round += 1
                        PACKETS_TO_BS[0] [r] = packets_TO_BS

                    S[i]['min_dis'] = min_dis
                    S[i]['min_dis_cluster'] = min_dis_cluster
                else:
                    min_dis = np.sqrt((S[i]['xd'] - S[n]['xd']) ** 2 + (S[i]['yd'] - S[n]['yd']) ** 2)    
                    if (min_dis > do):
                        S[i]['E'] = S[i]['E'] - (ETX * kb + Emp * kb * (min_dis ** 4))
                    if (min_dis <= do):
                        S[i]['E'] = S[i]['E'] - (ETX * kb + Efs * kb * (min_dis ** 2))
                    
                    packets_TO_BS += 1
                        
        STATISTICS['PACKETS_TO_CH'][h, r] = packets_TO_CH
        STATISTICS['PACKETS_TO_BS'][h, r] = packets_TO_BS
        STATISTICS['PACKETS_TO_BS_PER_ROUND'][h, r] = packets_TO_BS_per_round
        STATISTICS['THROUGHPUT'][h, r] = STATISTICS['PACKETS_TO_BS'][h, r] + STATISTICS['PACKETS_TO_CH'][h, r]
            
    
plt.show()












