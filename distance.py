import numpy as np
from scipy.spatial.distance import cdist
from points1 import point,a,b
import math
x = np.array([[4,4]])
y = np.array(point[2:])
d = cdist(x,y)
idx= np.argmin(d)
print(y[idx])


