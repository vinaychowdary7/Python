# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 12:49:07 2023

@author: vinay
"""
import random
import pandas as pd
[p1,p2,p3,p4,p5,p6,p7]=[1.111,1.172,1.607,1.712,1.422,1.688,1.476]
vals=[]
for i in range(1000):
    x1=random.randint(1,10)
    x2=random.randint(1,10)
    x3=random.randint(1,10)
    x4=random.randint(1,5)
    x5=random.randint(1,5)
    x6=random.randint(1,5)
    x7=random.randint(1,25)
    eq=p1*x1+p2*x2+p3*x3+p4*x4+p5*x5+p6*x6+p7*x7
    cs=""
    if eq>60:
        cs="Useful"
    else:
        cs="Not Useful"
    vals.append([x1,x2,x3,x4,x5,x6,x7,eq,cs])
data=pd.DataFrame(vals,columns=["BOWLING","BATTING","FEILDING","TEAMWORK","HEALTH","GAME_IQ","MONEY","WINNING_PERCENTAGE","WINNER"])
data.to_csv("Palyer.csv",index=False)