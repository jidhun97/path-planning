import math
from functools import partial
from point import dct

dis = []
points =[]
xvalue = []
yvalue = []
dist = []
sample = []


def euclidean(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
euc = partial(euclidean, 1,1)

for k in dct.keys():
    d = euc(int(dct[k][0]), int(dct[k][0]))
    dis.append((k, d))

    dis = sorted(dis, key=lambda x: x[1])


for x, y in dis:
    for k in dct.keys():
         if x == k:
            points = dct[k]
            xvalue.append(int(dct[k][0]))
            yvalue.append(int(dct[k][1]))
for i in range(len(dis)):
    dist.append(dis[i][1])
dist.remove(0)
for i in range( len(xvalue)):
    sample.append([xvalue[i],yvalue[i]])
