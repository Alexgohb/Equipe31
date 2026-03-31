import numpy as np
import matplotlib.pyplot as plt
from tridiagonal import tridiagonal
from problimite import problimite


#Question 2 a)

#fonction solution exacte:
def solution_exacte(x):
    T = 350
    Ta = 20
    k = 1.2
    beta1 = (-(T - Ta) * np.exp(-12*k))/(1 - np.exp(-12*k))
    beta2 = (T - Ta)/(1 - np.exp(-12*k))
    return Ta + beta1*np.exp(k*x) + beta2*np.exp(-k*x)

#Avec h = 1:
Nh1 = 5
k = 1.2
Ta = 20
a = 0
b = 6
T = 350
alpha = 350
beta = 20

Q1 = k**2*np.ones(Nh1)
R1 = -k**2*Ta*np.ones(Nh1)
axe1_x = np.linspace(0,6,7)
axe1_y = problimite(Nh1, Q1, R1, a, b, alpha, beta)

#Avec h = 2:
Nh2 = 2
Q2 = k**2*np.ones(Nh2)
R2 = -k**2*Ta*np.ones(Nh2)
axe2_x = np.array([0, 2, 4, 6])
axe2_y = problimite(Nh2, Q2, R2, a, b, alpha, beta)

Axex_exacte = np.linspace(0,6,100)
Axey_exacte = solution_exacte(Axex_exacte)

#Representaiton graphique des courbes:

plt.plot(Axex_exacte, Axey_exacte, label='Solution exacte', color='red')
plt.plot(axe1_x, axe1_y, 'o-', label='h=1', color='green')
plt.plot(axe2_x, axe2_y, 'o-', label='h=2', color='blue')
plt.title('Figure 1: Comparaison des fonctions avec h=1, h=2 et la fonction exacte')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.grid(True)
plt.show()

#Question 2 b)

#On peut faire une fonction pour faciliter le calcul du max de difference entre approx et exacte:

def calcul_max(N):
    x = np.linspace(0, 6, N+2)
    y_exact = np.zeros(N+2)
    for i, j in enumerate(x):
        y_exact[i] = solution_exacte(j)
    y_approx = problimite(N, k**2*np.ones(N), -k**2*Ta*np.ones(N), a, b, alpha, beta)
    difference = []
    for i in range(N+2):
        difference.append(abs(y_exact[i] - y_approx[i]))
    return max(difference)

#Pour h = L/3, N = 2  
print(calcul_max(2))
#Pour h = L/6, N = 5
print(calcul_max(5))
#Pour h = L/100, N = 99
print(calcul_max(99))
#Pour h = L/1000, N = 999
print(calcul_max(999))
#Pour h = L/10000, N = 9999
print(calcul_max(9999))

#On fait le graphique avec echelle log:

Erreur = np.array([calcul_max(2),calcul_max(5),calcul_max(99),calcul_max(999),calcul_max(9999)])
h = np.array([2, 1, 6/100, 6/1000, 6/10000])

plt.loglog(h, Erreur, 'o-', color='red')
plt.xlabel('h')
plt.ylabel('E(h)')
plt.title('Figure 2: Erreur en fonction de h')
plt.grid()
plt.show()