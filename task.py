import numpy as np

def Norm(mat):
    return np.max(np.sum(mat, axis=1))

E = 0.01

A = np.matrix([[12, -3, -1, 3],
              [5, 20, 9, 1],
              [6, -3, -21, -7],
              [8, -7, 3, -27]], dtype="float32")

B = np.matrix([-31/12, 90/20, 119/-21, 71/-27], dtype="float32").transpose()

a = np.zeros_like(A)

for i in range(4):
    for j in range(4):
        a[i, j] = A[i, j]/A[i, i]
    a[i, i] = 0

def F_x_n(n, a, B):
    if n == 0:
        return B
    else:
        x_n = np.dot(a, F_x_n(n-1, a, B)) + B

    return x_n

def checker(a, n, x_n):
    E_n = abs(Norm(a)/(1 - Norm(a)) * Norm(x_n - F_x_n(n-1, a, B)))
    if E_n <= 0.01:
        print(n, '\n', F_x_n(n, a, B))
        return False
    else: 
        return True

n = 1
x_n = F_x_n(n, a, B)

while checker(a, n, x_n):
    n+=1
    x_n = F_x_n(n, a, B)