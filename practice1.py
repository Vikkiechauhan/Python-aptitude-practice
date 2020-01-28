# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 13:26:16 2019

@author: VIKKU
"""

z=input("enter any alphabet: ")
t=ord(z)
def ab(f):
    count=0
    
    for i in range (f,t+1):
        for j in range(0,t-i):
            print(end=" ")
        
        if(i==65 or i==97):
            print(chr(i))
        else:
            print(chr(i),end="")
            for j in range(0,2*count):
                print(end=" ")
            print(chr(i))
            
        count=count+1
    return count
def cd(f,count):
        
        
        for i in range (t-1,f-1,-1):
            for j in range(0,t-i):
                print(end=" ")
        
            if(i==65 or i==97):
                print(chr(i))
            else:
                count=count-1
                print(chr(i),end="")
                for j in range(2*count-1,1,-1):
                    print(end=" ")
                print(chr(i))

if(int(z.isupper())==1):  
    y=ab(65)
    cd(65, y)
else:
    y=ab(97)
    cd(97,y)