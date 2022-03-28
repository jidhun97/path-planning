



from matplotlib import pyplot as plt
from pointsorting import xvalue
from pointsorting import yvalue
from pointsorting import sample
from math import sqrt
import numpy as np

def main():


    
    def distance_between_points(ln1):
        x1, y1 = ln1[0][0], ln1[0][1]
        x2, y2 = ln1[1][0], ln1[1][1]

        dis = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        return dis



    def visualization2(a, b):
        x1 = []
        y1 = []
        for pt in a:
            x1 += [pt[0]]
            y1 += [pt[1]]
        plt.plot(x1, y1, 'yo')

        m1 = range(len(x1))
        for i in np.arange(0, len(m1) - 1, 1):
            curr_dist = round(distance_between_points([my_list[i], my_list[i + 1]]), 2)
            plt.text(x=np.mean(x1[i:i + 2]), y=np.mean(y1[i:i + 2]), s=curr_dist, ha="right", va="bottom")

    my_list = sample


    plt.plot(xvalue, yvalue, '-o')
    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    visualization2(my_list, 'red')
    plt.axis('equal')
    n = ['START', 'P', 'P', 'P', 'P', 'P', 'P', 'STOP']
    for i, txt in enumerate(n):
        plt.annotate(txt, (xvalue[i], yvalue[i]))
    plt.grid()
    plt.show()




if __name__ == '__main__':
    main()

