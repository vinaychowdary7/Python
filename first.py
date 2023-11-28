# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 22:49:51 2023

@author: vinay
"""
import random
import pandas as pd
[w1,w2,w3,w4,w5,w6,w7]=[0.367,-0.0327,0.509,0.491,-0.226,1.142,0.169]
val=[]
for i in range(1000):
    x1=random.randint(1,10)
    x2=random.randint(1,5)
    x3=random.randint(1,100)
    x4=random.randint(1,70)
    x5=random.randint(1,2)
    x6=random.randint(1,10)
    x7=random.randint(1,2)
    eq=w1*x1+w2*x2+w3*x3+w4*x4+w5*x5+w6*x6+w7*x7
    val.append([x1,x2,x3,x4,x5,x6,x7,eq])
df=pd.DataFrame(val,columns=["SKILLS","WORK_CULTURE","FINANCE","LEARNING","TECHNOLOGY","HEALTH","POLICIES","PRODUCTIVITY"])
df.to_csv("employee.csv",index=False)