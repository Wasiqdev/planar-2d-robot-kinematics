import numpy as np

def jacobian(theta1, theta2, l1, l2):
    j11 = -l1*np.sin(theta1) - l2*np.sin(theta1 + theta2)
    j12 = -l2*np.sin(theta1 + theta2)
    j21 =  l1*np.cos(theta1) + l2*np.cos(theta1 + theta2)
    j22 =  l2*np.cos(theta1 + theta2)

    return np.array([[j11, j12],
                     [j21, j22]])
