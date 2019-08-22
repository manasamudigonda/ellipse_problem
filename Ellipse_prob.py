import numpy as np
from coeffs import *
import matplotlib.pyplot as plt
import math

V = np.array([[1,0],[0,3]])
#print(V)
t = np.deg2rad(30)

A = np.array([3*math.sqrt(3)/2 , math.sqrt(3)/2  ])
B =	np.array([-3/2 , 3*math.sqrt(3)/2  ])

n1 = V@A 
n2 = V@B 

#print(n1[0],n2[0])

g = (n1[0]*n2[0])+(n1[1]*n2[1])
print(g)

nor_A = norm(A)
nor_B = norm(B)

print(nor_A,nor_B)

beta = math.acos(g/(nor_A*nor_B))

#s = 2*math.tan(beta) * math.sin(2*t)
#sol = 1/s
#print(sol)
