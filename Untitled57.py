#!/usr/bin/env python
# coding: utf-8

# # Least Square Fit Method:

# In[2]:


import matplotlib.pyplot as plt
F=[2,4,6,8,10]
a=[6,9,12,15,18]
[sumx,sumy,sumxy,sumxx]=[0,0,0,0]
for i in range(0,len(F)):
    sumx+=a[i]
    sumy+=F[i]
    sumxy+=F[i]*a[i]
    sumxx+=a[i]*a[i]
B=(len(F)*sumxy-sumx*sumy)/(len(F)*sumxx-sumx**2)
A=(sumy-B*sumx)/len(F)
print(A,B)
Fnew=[]
for i in range(0,len(F)):
    Fnew.append(A+a[i]*B)
plt.plot(a,F,'o')
plt.plot(a,Fnew)


# In[ ]:





# In[ ]:


S=[2,4,6,8,10]
t=[6,9,12,15,18]
n=len(S)
sumX = 0
sumY = 0
sumXY = 0
sumX2 = 0
for i in range(0,n):
    sumX=sumX+t[i]
    sumY=sumY+S[i]
    sumXY=sumXY+S[i]*t[i]
    sumX2=sumX2+t[i]*t[i]
m=(n*sumXY-sumX*sumY)/(n*sumX2-sumX**2)
f=(sumY-m*sumX)/n
print("For the given data, the values of parameters m and f in equation F=ma+f on which SSE is minimum are: \n m=", m, "\n f=", f)
print("Therefore, the least square fit is:\n F=",m,"a", "{:+}".format(f))

