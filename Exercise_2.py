import numpy as np

T_b = np.array([[0.0, 0.9, 0.1, 0.0],
                [0.9, 0.1, 0.0, 0.0],
                [0.0, 0.0, 0.1, 0.9],
                [0.9, 0.0, 0.0, 0.1]])

T_c = np.array([[0.0, 0.1, 0.9, 0.0],
                [0.9, 0.1, 0.0, 0.0],
                [0.0, 0.0, 0.1, 0.9],
                [0.9, 0.0, 0.0, 0.1]])

Rsc = np.array([[0, 1, 0, 2]])

Vp_0 = np.array([[0.0, 0.0, 0.0, 0.0]])

Vp_1 = Rsc

Vp_2 = Rsc + Rsc @ T_c.T

print("Exercise 2A:", Vp_0.tolist())
print("Exercise 2B: ", Vp_1.tolist())
print("Exercise 2C:", Vp_2.tolist())
