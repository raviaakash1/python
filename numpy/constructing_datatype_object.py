import numpy as np
 
# Integer datatype
x = np.array([1, 2])  
print(x.dtype)         
 
# Float datatype
x = np.array([1.0, 2.0]) 
print(x.dtype)  
 
# Forced Datatype
x = np.array([1, 2], dtype = np.int64)   
print(x.dtype)