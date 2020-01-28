# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 21:04:24 2019

@author: VIKKU
"""
z=int(input("enter the no.: "))

for i in range(0,2*z,2):
    n=int(i/2)
    for j in range(0,2*z-i-1):
        print(end=" ")
    
    for j in range(0,i+1):
        
        print(n+1,end=" ")
        if(j<int(i/2)):
            n=n-1
        else:
            n=n+1
    print()
for i in range(2*z-1,1,-2):
    n=int(i/2)
    print(end=" ")
    for j in range(2*z-i+1,0,-1):
        print(end=" ")
    
    for j in range(i,2,-1):
        print(n,end=" ")
        if(j>int((i+3)/2)):
            n=n-1
        else:
            n=n+1
    print()
