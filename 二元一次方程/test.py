import numpy as np
##x,y
a = np.array([[-1/7,1/2],[1,-1]])
b = np.array([27/14,-1])
##x z
c = np.array([[-1/7,-1/10],[1,1]])
d = np.array([9/70,-3])
##yz
e = np.array([[-1/2,-1/10],[1,1]])
f = np.array([9/70-27/14,-2])
print(np.linalg.solve(a,b))
print(np.linalg.solve(c,d))
print(np.linalg.solve(e,f))