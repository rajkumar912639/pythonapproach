import numpy as np
a = np.arrange(10,22).reshape((3,4))
print("original array :")
print(a)
print("each element of the array is :")
for x in np.nditer(a):
    print(x,end=" ")