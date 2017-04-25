import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

rc("text", usetex = True)

class sistema:
    
    def __init__(self, planetas):
        self.planetas = planetas
        
    def fuerza(self, planeta):
        fuerza = np.array([0.0,0.0])
        for j in range(0,len(self.planetas)):
            if(j != planeta):
                fuerza += -self.planetas[j].masa*self.planetas[planeta].masa*(self.planetas[planeta].posicion - self.planetas[j].posicion)/(np.linalg.norm(self.planetas[j].posicion - self.planetas[planeta].posicion)**3)
        return fuerza

    def posiciones(self):
	return np.array([p.posicion for p in self.planetas])
                
    def actualizar(self, dt):
        for i in range(0,len(self.planetas)):
            self.planetas[i].velocidad += self.fuerza(i)*dt/(self.planetas[i].masa*2)
            self.planetas[i].posicion += self.planetas[i].velocidad*dt
            self.planetas[i].velocidad += self.fuerza(i)*dt/(self.planetas[i].masa*2)
    
class planetas:
    
    def __init__(self, masa, posicion, velocidad):
        self.masa = masa
        self.posicion = posicion
        self.velocidad = velocidad

masa_central = 1047.0
radio = 100.0
centro_masa = radio*1.0/(1.0+1047.0)
velocidad_centro_masa = np.sqrt(masa_central/radio)*1.0/(1.0+1047.0)
central = planetas(1047.0, np.array([0.0-centro_masa, 0.0]), np.array([0.0, -velocidad_centro_masa]))
masivo = planetas(1.0, np.array([radio-centro_masa, 0.0]), np.array([0.0, np.sqrt(central.masa/radio)+velocidad_centro_masa]))
troyano = planetas(0.005, np.array([(radio-centro_masa)*np.cos(np.pi/3), (radio-centro_masa)*np.sin(np.pi/3)]), np.array([-(np.sqrt(central.masa/radio)+velocidad_centro_masa)*np.sin(np.pi/3.0), (np.sqrt(central.masa/radio)+velocidad_centro_masa)*np.cos(np.pi/3.0)]))
sistema = sistema([central, masivo, troyano])

n_times = 4000
dt = 0.1

fig, ax = plt.subplots(3, figsize = (10,10))
orbitas = np.zeros((n_times + 1, 3, 2))
orbitas[0] = sistema.posiciones()
for i in range(1, n_times + 1):
    sistema.actualizar(dt)
    orbitas[i] = sistema.posiciones()
for j in range(0,len(sistema.planetas)):
    ax[j].plot(orbitas[:,j,0], orbitas[:,j,1], "k")
ax[0].set_title(r"Estrella central")
ax[1].set_title(r"Planeta masivo")
ax[2].set_title(r"Troyano")
ax[0].set_xlabel(r"$x$")
ax[1].set_xlabel(r"$x$")
ax[2].set_xlabel(r"$x$")
ax[0].set_ylabel(r"$y$")
ax[1].set_ylabel(r"$y$")
ax[2].set_ylabel(r"$y$")
fig.subplots_adjust(hspace=0.5)
fig.savefig("OrbitsPLOT.pdf")

fig,ax = plt.subplots(figsize = (10,10))
radio = 100.0
central = planetas(1047.0, np.array([0.0-centro_masa, 0.0]), np.array([0.0, -velocidad_centro_masa]))
masivo = planetas(1.0, np.array([radio-centro_masa, 0.0]), np.array([0.0, np.sqrt(central.masa/radio)+velocidad_centro_masa]))
troyano = planetas(0.005, np.array([(radio-centro_masa)*np.cos(np.pi/3.0), (radio-centro_masa)*np.sin(np.pi/3.0)]), np.array([-(np.sqrt(central.masa/radio)+velocidad_centro_masa)*np.sin(np.pi/3.0), (np.sqrt(central.masa/radio)+velocidad_centro_masa)*np.cos(np.pi/3.0)]))
orbitas = np.zeros((n_times + 1, 3, 2))
orbitas[0] = sistema.posiciones()
for i in range(1, n_times + 1):
    sistema.actualizar(dt)
    orbitas[i] = sistema.posiciones()	
ax.plot(orbitas[:,2,0]-orbitas[:,1,0], orbitas[:,2,1]-orbitas[:,1,1], "k")
radio = 100.0
central = planetas(1047.0, np.array([0.0-centro_masa, 0.0]), np.array([0.0, -velocidad_centro_masa]))
masivo = planetas(1.0, np.array([radio-centro_masa, 0.0]), np.array([0.0, np.sqrt(central.masa/radio)+velocidad_centro_masa]))
epsilon = 100
troyano = planetas(0.005, np.array([(radio-centro_masa)*np.cos(np.pi/3.0)+epsilon, (radio-centro_masa)*np.sin(np.pi/3.0)+epsilon]), np.array([-(np.sqrt(central.masa/radio)+velocidad_centro_masa)*np.sin(np.pi/3.0)-epsilon, (np.sqrt(central.masa/radio)+velocidad_centro_masa)*np.cos(np.pi/3.0)+epsilon]))
orbitas = np.zeros((n_times + 1, 3, 2))
orbitas[0] = sistema.posiciones()
for i in range(1, n_times + 1):
    sistema.actualizar(dt)
    orbitas[i] = sistema.posiciones()	
ax.plot(orbitas[:,2,0]-orbitas[:,1,0], orbitas[:,2,1]-orbitas[:,1,1], "b")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.set_title(r"Orbita Troyano (azul est\'a perturbada)")
fig.savefig("Troyano.pdf")

fig, ax = plt.subplots(4, figsize = (10,10))
m = np.array([10.0, 20.0, 30.0, 40.0])
for i in range(0, 4):
    radio = 100.0
    central = planetas(1047.0, np.array([0.0-centro_masa, 0.0]), np.array([0.0, -velocidad_centro_masa]))
    masivo = planetas(m[i], np.array([radio-centro_masa, 0.0]), np.array([0.0, np.sqrt(central.masa/radio)+velocidad_centro_masa]))
    troyano = planetas(0.005, np.array([(radio-centro_masa)*np.cos(np.pi/3.0), (radio-centro_masa)*np.sin(np.pi/3.0)]), np.array([-(np.sqrt(central.masa/radio)+velocidad_centro_masa)*np.sin(np.pi/3.0), (np.sqrt(central.masa/radio)+velocidad_centro_masa)*np.cos(np.pi/3.0)]))
    orbitas = np.zeros((n_times + 1, 3, 2))
    orbitas[0] = sistema.posiciones()
    for j in range(1, n_times + 1):
        sistema.actualizar(dt)
        orbitas[j] = sistema.posiciones()	
    ax[i].plot(orbitas[:,2,0], orbitas[:,2,1], "k")
    ax[i].set_title(r"$m_2 = %f$" % m[i])
    ax[i].set_xlabel(r"$x$")
    ax[i].set_ylabel(r"$y$")
fig.subplots_adjust(hspace=0.5)
fig.savefig("MassPLOT.pdf")
