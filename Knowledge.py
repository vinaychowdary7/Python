# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 22:40:24 2023

@author: vinay
"""

"""
for authenticity of knowledge
BIAS - On a scale of 10
SOURCE - On a scale of 10
CONTRADITIONS - On a scale of 10
THEORY - On a scale of 5
EVIDENCE - On a scale of 5
OBSERVED - On a scale of 10
 
"""
import random
import pandas as pd
[k1,k2,k3,k4,k5,k6]=[2,2,2,2,2,2]
values=[]
for i in range(1000):
    x1=random.randint(1,10)
    x2=random.randint(1,10)
    x3=random.randint(1,10)
    x4=random.randint(1,5)
    x5=random.randint(1,5)
    x6=random.randint(1,10)
    eq=k1*x1+k2*x2+k3*x3+k4*x4+k5*x5+k6*x6
    t=""
    if eq>70:
        t="Highly Trustable"
    elif eq>50:
        t="Lowly Trustable"
    else:
        t="Not Trustable"
    values.append([x1,x2,x3,x4,x5,x6,eq,t])
df=pd.DataFrame(values,columns=["BIAS","SOURCE","CONTRADITIONS","THEORY","EVIDENCE","OBSERVED","AUTHENTICITY_OF_KNOWLEGDE","TRUSTABLE"])
df.to_csv("Authenticity_of_Knowledge.csv",index=False)