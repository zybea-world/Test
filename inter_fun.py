from functools import reduce

import numpy as np
list = np.random.randint(5,66,8).tolist()
list = sorted(list,reverse=True)
def f(x,y):
    return x*y
print(reduce(f,list,2))

