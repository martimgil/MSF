import numpy as np


def minimos_quadrados(x,y):

    N = x.size


    sum_x = np.sum(x)
    sum_y= np.sum(y)
    sum_x2 = np.sum(x**2)
    sum_y2 = np.sum(y**2)
    sum_xy = np.sum(x*y)

    m = (N*sum_xy -sum_x*sum_y)/(N*sum_x2 - sum_x**2)


    b = (sum_x2*sum_y - sum_x*sum_xy)/(N* sum_x2 - sum_x**2)

    r2 = (N*sum_xy - sum_x*sum_y)**2/((N*sum_x2 - sum_x**2)*(N*sum_y2))


    dm = np.absolute(m)*np.sqrt((1/r2-1)/(N-2))

    db = dm*np.sqrt((sum_x2)/N)

    return m,b,r2,dm,db



