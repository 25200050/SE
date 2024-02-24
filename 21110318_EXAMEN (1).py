# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 20:21:13 2023

@author: isisa
"""
#Isabel Ortiz Corona 21110318  EXAMEN IA 2023
def prim(w,n,s):
    v=[]
    while(len(v)!= n):
        v.append(0)
    v[s] = 1
    E = []
    suma = 0
    for i in range(0,n-1):
        minimo = 9 
        agregar_vertice = 0
        e = []
        for j in range(0,n):
            if(v[j] == 1):
                for k in range(0,n):
                    if(v[k]==0 and w[j][k] < minimo):
                         agregar_vertice = k
                         e = [j,k]
                         minimo = w[j][k]
        suma += w[e[0]][e[1]]    
        
        v[agregar_vertice] = 1
        E.append([e[0]+1,e[1]+1])
    return [E,suma]
n=6
s=0
w=[
   [9,4,2,9,3,9],
   [4,9,9,5,9,9],
   [2,9,9,1,6,3],
   [9,5,1,9,9,6],
   [3,9,6,9,9,2],
   [9,9,3,6,2,9]
   
   ]

print("El arbol de expansion mınima es:", prim (w, n, s), ":)")

