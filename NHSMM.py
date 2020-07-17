# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 13:10:02 2020

@author: Desktop
"""

from math import*
import numpy as np 

usr1 = [4,5,3] 
usr1f=[4,0,5,3,0]
usr2=[5,4,1]
usr2f=[0,5,0,4,1]
usr3 = [2,1,4,3]
usr3f=[2,1,4,0,3]
usr4 = [3,2,5,4]
usr4f = [3,0,2,5,4]
usr5 = [1,4,2]
usr5f = [1,4,0,2,0]
itm1 = [4,2,3,1]
itm2 = [5,1,4]
itm3=[5,4,2]
itm4=[3,4,5,2]
itm5 = [1,3,4]
meanItm1 = np.mean(itm1)
meanItm2 = np.mean(itm2)
meanItm3 = np.mean(itm3)
meanItm4 = np.mean(itm4)
meanItm5 = np.mean(itm5)
meanusr1 = np.mean(usr1)
meanusr2 = np.mean(usr2)
meanusr3 = np.mean(usr3)
meanusr4 = np.mean(usr4)
meanusr5 = np.mean (usr5)

stdu1 = np.std(usr1, dtype=np.float64)
stdu2 =  np.std(usr2, dtype=np.float64) 
stdu3 =  np.std(usr3, dtype=np.float64)
stdu4 =  np.std(usr4, dtype=np.float64) 
stdu5 =  np.std(usr5, dtype=np.float64)  
   

def jaccard_similarity(x,y):
 
 intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
 multiplication_cardinality = len(set(x))*len( set(y))
 js = round(intersection_cardinality/(multiplication_cardinality),5)
 return js

def URP_similarity(a,b,c,d):
    exponent=abs(a-b)*abs(c-d)
    exponential_value = exp(-exponent)
    urp = round(( 1-(1/(1+exponential_value))),5)
    return urp

def PSS(a,b):
   x = min(len(a),len(b))
   prox_array = [] * x
   significance_array = [] * x
   singularity_array = [] * x
   pss =0
   median1 = np.median(a)
   median2 = np.median(b)
   mir=[2.5,3.33,3.66,3.5,2.66]
   for i in range(x):
   
    if a[i]==0 and b[i]==0:
         continue
    else:
         exponent = abs(a[i]-b[i])
         exponential_value = round(exp(-exponent),5)
         prox= round((1-(1/(1+exponential_value))),5)
         prox_array.append(prox)
         print("proximity", prox_array[i-1])
         exponent_sig = abs(a[i]-median1)* abs(b[i]-median2)
         sig_exponential_value = exp(-exponent_sig)
         sig = (1/(1+sig_exponential_value))
         significance_array.append(sig)
         print("significance" ,significance_array[i-1])
         exponent_sing = abs(((a[i]+b[i])/2) - mir[i-1])
         sing_exponential_value = exp(-exponent_sing)
         singularity = (1-(1/(1+sing_exponential_value)))
         singularity_array.append(singularity)
         print("singularity" ,singularity_array[i-1])
         pss=pss + (prox_array[i-1]*singularity_array[i-1]*significance_array[i-1])
         print ("pss", pss)
   return pss

up12 = PSS(usr1f,usr2f)
up13 = PSS(usr1f,usr3f)
up14 = PSS(usr1f,usr4f)
up15 = PSS(usr1f,usr5f)
up23 = PSS(usr2f,usr3f)
up24 = PSS(usr2f,usr4f)
up25 = PSS(usr2f,usr5f)
up34 = PSS(usr3f,usr4f)
up35 = PSS(usr3f,usr5f)
up45 = PSS(usr4f,usr5f)
print("PSS marrix")
print(up12 , up13, up14, up15)
print(up23, up24, up25)
print(up34, up35)
print(up45)
PSS=[[up12,up13,up14,up15],[0,up23,up24,up25],[0,0,up34,up35],[0,0,0,up45]]    
 


urp12 = URP_similarity(meanusr1, meanusr2, stdu1, stdu2)
urp13 = URP_similarity(meanusr1,meanusr3, stdu1, stdu3)
urp14 = URP_similarity(meanusr1,meanusr4, stdu1, stdu4)
urp15 = URP_similarity(meanusr1,meanusr5, stdu1, stdu5)
urp23 = URP_similarity(meanusr2,meanusr3, stdu2, stdu3)
urp24 = URP_similarity(meanusr2,meanusr4, stdu2, stdu4)
urp25 = URP_similarity(meanusr2,meanusr5, stdu2, stdu5)
urp34 = URP_similarity(meanusr3,meanusr4, stdu3, stdu4)
urp35 = URP_similarity(meanusr3,meanusr5, stdu3, stdu5)
urp45 = URP_similarity(meanusr4,meanusr5, stdu4, stdu5)
print("URP marrix")
print(urp12 , urp13, urp14,urp15)
print(urp23, urp24, urp25)
print(urp34, urp35)
print(urp45)
URP=[[urp12,urp13,urp14,urp15],[0,urp23,urp24,urp25],[0,0,urp34,urp35],[0,0,0,urp45]]   

uj12 = jaccard_similarity(usr1,usr2)
uj13 = jaccard_similarity(usr1, usr3)
uj14 = jaccard_similarity(usr1, usr4)
uj15 = jaccard_similarity(usr1, usr5)
uj23 = jaccard_similarity(usr2, usr3)
uj24 = jaccard_similarity(usr2, usr4)
uj25 = jaccard_similarity(usr2, usr5)
uj34 = jaccard_similarity(usr3, usr4)
uj35 = jaccard_similarity(usr3, usr5)
uj45 = jaccard_similarity(usr4, usr5)
print("jaccard marrix")
print(uj12 , uj13, uj14, uj15)
print(uj23, uj24, uj25)
print(uj34, uj35)
print(uj45)
jac=[[uj12,uj13,uj14,uj15],[0,uj23,uj24,uj25],[0,0,uj34,uj35],[0,0,0,uj45]]

nhsm12 = (uj12*up12) * urp12


nhsm13 = (uj13*up13) * urp13

nhsm14 = (uj14*up14) * urp14
nhsm15 = (uj15*up15) * urp15
nhsm23 = (uj23*up23) * urp23
nhsm24 = (uj24*up24) * urp24
nhsm25 = (uj25*up25) * urp25
nhsm34 = (uj34*up34) * urp34
nhsm35 = (uj35*up35) * urp35
nhsm45 = (uj45*up45) * urp45
print("NHSM marrix")
print(nhsm12 , nhsm13, nhsm14, nhsm15)
print(nhsm23, nhsm24, nhsm25)
print(nhsm34, nhsm35)
print(nhsm45)
NHMS=[[nhsm12,nhsm13,nhsm14,nhsm15],[0,nhsm23,nhsm24,nhsm25],[0,0,nhsm34,nhsm35],[0,0,0,nhsm45]]