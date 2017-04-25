import numpy as np
import matplotlib.pyplot as plt

textraw = open("RotationCurve_F571-8.txt", "r").readlines()

Vel = []
VGas = []
VDisk = []
VBul = []
PRad = []

for lineraw in textraw:
	line = lineraw.rstrip("\n").split()
	PRad.append(line[2])
	Vel.append(line[6])
	VGas.append(line[3])
	VDisk.append(line[4])
	VBul.append(line[5])

VGas = np.array(VGas, dtype = float)
VDisk = np.array(VDisk, dtype = float)
VBul = np.array(VBul, dtype = float)
VelExpected = VGas + VDisk + VBul

plt.rc("text", usetex = True)
plt.title(r"Materia oscura y su efecto en la rotaci\'on de galaxias")
plt.scatter(PRad, Vel, c = "k", label = "Velocidades observadas")
plt.scatter(PRad, VelExpected, c = "g", label = "Velocidades esperadas")
plt.xlabel(r"Radio ($kpc$)")
plt.ylabel(r"Velocidad ($\frac{km}{s}$)")
plt.legend()
plt.savefig("RotationCurvePlot.pdf", format = "pdf")
