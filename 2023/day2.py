import numpy as np

a = np.array(
    [
        #7,banan,citron,bell,orange,bar,cherry,plum,wm
        [3,0,0,0,0,0,0,0,0],
        [0,1,1,1,0,0,0,0,0],
        [1,1,1,0,0,0,0,0,0],
        [0,0,0,2,1,0,0,0,0],
        [1,0,0,0,1,1,0,0,0],
        [0,0,2,0,0,1,0,0,0],
        [0,2,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,2,1],
        [0,0,0,0,0,1,1,0,1],
    ])
b = np.array([63, 76, 72, 105, 164, 124, 130, 231, 199])
x = np.linalg.solve(a, b)
print(x)
print(x[4],x[6],x[7])