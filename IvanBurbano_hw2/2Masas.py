import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

rc("text", usetex = True)

#Debe de ser lo suficientemente sencillo escribir un programa que solucione el problema para un numero N de masas. En lo siguiente vamos a definir el sistema de ecuaciones que caracteriza el sistema. Los primeros N + 1 valores de x son los senos de los angulos, los siguientes N + 1 son los cosenos y los ultimos N + 1 son las tensiones. Notese que para obtener simetria en las ecuaciones se utiliza el negativo del ultimo angulo que se muestra en la figura en el enunciado de la tarea. Esto se revierte en la entrega de resultado. Es necesario definir un array L donde los primeros N + 1 valores sean los de las cuerdas y el ultimo valor sea el de la distancia horizontal del sistema y un array de pesos W.

N = 2
L = np.array([3, 4, 4, 8])
W = np.array([10, 20])

def f(x):
    resultado = []
    resultado.append(np.sum(L[:-1] * x[:(N + 1)]))
    resultado.append(np.sum(L[:-1] * x[(N + 1):(2*N)]) - L[N + 1])
    resultado = np.concatenate((np.array(resultado), ((x[(2 * (N + 1)):(-1)]*x[(N + 1):((2 * (N + 1)) - 1)]) - (x[((2 * (N + 1)) + 1):]*x[((N + 1) + 1):(2 * (N + 1))])), ((x[(2 * (N + 1)):(-1)]*x[:((N + 1) - 1)]) - (x[((2 * (N + 1)) + 1):]*x[1:(N + 1)]) - W), (x[:(N + 1)]**2 + x[(N + 1):(2 * (N + 1))]**2 - 1)))
    return resultado

guess = np.array([0.5, 0.3, -0.86, 0.9, 0.95, 0.5, 5, 5, 15])
paso = 1.0
iteracion = 0
actual = f(guess)
angulos = np.arcsin(guess[:(N + 1)])
angulos[len(angulos) - 1] = -angulos[len(angulos) - 1]
tensiones = guess[(2 * (N + 1)):]

while not((actual < 0.001).all()):
    iteracion += 1
    J = np.zeros((3 * (N + 1), 3 * (N + 1)))
    for n in range(0, 3 * (N + 1)):
        for m in range(0, 3 * (N + 1)):
            y = guess.copy()
            y[m] += paso
            J[n, m] = (f(y)[n] - f(guess)[n])/paso
    delta = np.linalg.solve(J, -f(guess))
    guess = guess + delta
    actual = f(guess)
    angulos = np.concatenate((angulos, np.arcsin(guess[:(N + 1)])))
    angulos[len(angulos) - 1] = -angulos[len(angulos) - 1]
    tensiones = np.concatenate((tensiones, guess[(2 * (N + 1)):]))
resultado = guess

c = ["bo", "ro", "go"]
X = np.arange(iteracion + 1)

plt.figure()
for n in range(0, N + 1):
    plt.plot(X, angulos[n::(N + 1)], c[n], label = r"$\theta_{%d}$" % (n + 1))
plt.xlabel(r"N\'umero de iteraci\'on")
plt.ylabel(r"Angulo (rad)")
plt.legend()
plt.savefig("AnglesPLOT.pdf")

plt.figure()
for n in range(0, N + 1):
    plt.plot(X, tensiones[n::(N + 1)], c[n], label = r"$T_{%d}$" % (n + 1))
plt.xlabel(r"N\'umero de iteraci\'on")
plt.ylabel(r"Tension (unidades en las que est\'a el peso)")
plt.legend()
plt.savefig("TensionsPLOT.pdf")

angulos = np.arcsin(resultado[:(N + 1)])
angulos[N] = -angulos[N]
tensiones = resultado[(2 * (N + 1)):]

print "Los angulos hallados fueron", angulos, "y la tensiones fueron", tensiones


