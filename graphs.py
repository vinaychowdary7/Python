# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 14:20:24 2023

@author: vinay
"""

import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

data=pd.read_csv("Authenticity_of_Knowledge.csv")
print(data.head())
print(data.describe())
X = data[["BIAS","SOURCE","CONTRADITIONS","THEORY","EVIDENCE","OBSERVED"]]
Y = data["AUTHENTICITY_OF_KNOWLEGDE"]
Y_= data["TRUSTABLE"]

plt.scatter(X['BIAS'], Y, color='b')
plt.xlabel='BIAS'  
plt.ylabel='TRUSTABLE' 
plt.show()

inp = [[1,10,9,4,4,1]]

#LINEAR REGRESSION
mdl = LinearRegression()
mdl.fit(X,Y)
pred = mdl.predict(inp)
print("Predicted value (LR): ",pred[0])
print("Accuracy (LR): ",mdl.score(X[:100], Y[:100])*100)


plt.scatter(X['BIAS'], Y, color='red')
plt.plot(X['BIAS'], mdl.predict(X),color='black',linewidth=3)
plt.xlabel='BIAS'  
plt.ylabel='AUTHENTICITY_OF_KNOWLEDGE' 
plt.show()


#LOGISTIC REGRESSION
from sklearn.linear_model import LogisticRegression
mdl = LogisticRegression() 
mdl.fit(X,Y_)
pred = mdl.predict(inp)
print("Predicted Value (longstic Regression):",pred[0])
print("Accuracy (LGR): ",mdl.score(X[:100],Y[:100])*100)

plt.scatter(X["BIAS"],Y_,color="red")
plt.plot(X['BIAS'],mdl.predict(X),color='black',linewidth=3)
plt.xlabel='BIAS'  
plt.ylabel='TRUSTABLE'
plt.show()

#SVR
from sklearn.svm import SVR
mdl = SVR(kernel='rbf')
mdl.fit(X,Y)
pred = mdl.predict(inp)
print("Predicted Value (SVR): ",pred[0])
print("Accuracy (SVR): ",mdl.score(X[:100], Y[:100])*100)
 
plt.scatter(X['BIAS'],Y,color="red")
plt.plot(X['BIAS'],mdl.predict(X),color="black",linewidth=3)
plt.xlabel="BIAS"
plt.ylable="AUTHENTICITY_OF_KNOWLEDGE"
plt.show()

#SVC
from sklearn.svm import SVC
mdl = SVC(kernel='poly')
mdl.fit(X,Y_)
pred = mdl.predict(inp)
print("Predicted Value (SVC): ",pred[0])
print("Accuracy (SVC): ",mdl.score(X[:100], Y[:100])*100)
 
plt.scatter(X['BIAS'],Y_,color="red")
plt.plot(X['BIAS'],mdl.predict(X),color="black",linewidth=3)
plt.xlabel="BIAS"
plt.ylable="TRUSTABLE"
plt.show()

#NB
from sklearn.naive_bayes import GaussianNB
mdl = GaussianNB()
mdl.fit(X,Y_)
pred = mdl.predict(inp)
print("Predicted Value (NB): ",pred[0])
print("Accuracy (NB): ",mdl.score(X[:100], Y[:100])*100)

plt.scatter(X['BIAS'],Y_,color='red')
plt.plot(X['BIAS'],mdl.predict(X),color='black',linewidth=3)
plt.xlabel='BIAS'
plt.ylabel='TRUSTABLE'
plt.show()

#KNN
from sklearn.neighbors import KNeighborsClassifier
mdl = KNeighborsClassifier()
mdl.fit(X, Y_)
pred = mdl.predict(inp)
print("Predicted value (KNN): ",pred[0])
print("Accuracy (KNN): ",mdl.score(X[:100], Y_[:100])*100)

plt.scatter(X['BIAS'], Y_, color='red')
plt.plot(X['BIAS'], mdl.predict(X),color='black',linewidth=3)
plt.xlabel='BIAS'  
plt.ylabel='TRUSTABLE' 
plt.show()