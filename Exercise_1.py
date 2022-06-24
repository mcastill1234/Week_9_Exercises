# Problem 1A:
def f_1A(s, x_i):
    return max(s, x_i)


def g_1A(s):
    return s * 2


s_0 = 0
Input = [0, 1, 2, 1]
Output_1A = []
st_1A = s_0
for item_1A in Input:
    st_1A = f_1A(st_1A, item_1A)
    Output_1A.append(g_1A(st_1A))

print("Exercise 1A output: ", Output_1A)


# Problem 1B
def f_1B(s, x_i):
    return s[0] + x_i, s[1] + 1


def g_1B(s):
    return s[0] / s[1]


s_0 = (0, 0)
st_1B = s_0
Output_1B = []
for item_1B in Input:
    st_1B = f_1B(st_1B, item_1B)
    Output_1B.append(g_1B(st_1B))

print("Exercise 1B Output", Output_1B)
