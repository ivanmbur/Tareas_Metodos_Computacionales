import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

plt.rc("text", usetex = True)

textraw = open("TempHeight.txt", "r").readlines()

z = []
T = []


for lineraw in textraw:
	line = lineraw.strip("\n").split()
	z.append(line[0])
	T.append(line[1])

z = np.array(z, dtype = float) / 1000
T = np.array(T)

plt.figure()
plt.title(r"Temperatura media en funci\'on de la altura en Bogot\'a")
plt.scatter(z, T, c = "r", alpha = 0.7, label = "Datos observados")
plt.xlabel(r"Altura ($km$)")
plt.ylabel(r"Temperatura ($^{\circ}C$)")
plt.legend()
plt.savefig("TemperaturePlot.pdf", format = "pdf")

z_spline = np.linspace(2.5, 25, 150 + 1)
T_spline = interpolate.splev(z_spline, interpolate.splrep(z, T))
DT_spline = (T_spline[2:] - T_spline[:-2])/0.3

z_convection = []
T_convection = []
for n in range(0, len(DT_spline)):
	if(abs(DT_spline[n]) > 9.8):
		z_convection.append(z_spline[n + 1])
		T_convection.append(T_spline[n + 1])
plt.figure()
plt.title(r"Alturas a las cuales ocurre el fen\'omeno de convecci\'on y sus temperaturas en Bogot\'a")
plt.scatter(z_convection, T_convection, c = "r", alpha = 0.7, label = r"Puntos donde hay convecci\'on")
plt.xlabel(r"Altura ($km$)")
plt.ylabel(r"Temperatura ($^{\circ}C$)")
plt.legend()
plt.savefig("ConvectionPLOT.pdf", format = "pdf")

DT_adiabatic = -9.8 * np.ones(len(DT_spline))
plt.figure()
plt.title(r"Gradiente vertical de temperaturas de Bogot\'a y adiab\'atico contra altura")
plt.scatter(z_spline[1:-1], DT_spline, c = "r", alpha = 0.7, label = r"Bogot\'a")
plt.plot(z_spline[1:-1], DT_adiabatic, ls = "--", label = r"Adiab\'atico")
plt.xlabel(r"Altura ($km$)")
plt.ylabel(r"Gradiente vertical de temperatura ($\frac{^{\circ}C}{km}$)")
plt.legend()
plt.savefig("GradientsPlot.pdf", format = "pdf")
