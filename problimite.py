import numpy as np
from tridiagonal import tridiagonal

def problimite(N, Q, R, a, b, alpha, beta):
    h = (b - a)/(N + 1)
    diagonale_inf = np.ones(N-1)
    diagonale_sup = np.ones(N-1)
    diagonale_principale = np.zeros(N)
    vec_b = np.zeros(N)
    vec_y = np.zeros(N+2)
    for i in range(N):
        diagonale_principale[i] = -Q[i]*h**2 - 2
    for i in range(N):
        if i == 0:
            vec_b[i] = R[i]*h**2 - alpha
        elif i == N-1:
            vec_b[i] = R[i]*h**2 - beta
        else:
            vec_b[i] = R[i]*h**2
    y = tridiagonal(N, diagonale_principale, diagonale_inf, diagonale_sup, vec_b)
    vec_y[0] = alpha
    vec_y[-1] = beta
    vec_y[1:N+1] = y
    return vec_y