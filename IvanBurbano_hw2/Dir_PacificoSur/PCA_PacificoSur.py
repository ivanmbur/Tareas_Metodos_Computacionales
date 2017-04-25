import numpy as np
import matplotlib.pyplot as plt
import datetime
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
from matplotlib import rc

rc("text", usetex = True)

#Ya que necesitamos comparar los datos en el mismo tiempo, solo se toman los datos de ambos archivos entre Enero de 1979 y Enero de 2017

data_raw1 = []
for line in open("heat_content_index.txt", "r").readlines():
	data_raw1.append(line.rstrip("\n").split())
del data_raw1[:2]

time = []
region1 = []
region2 = []
region3 = []
for line in data_raw1[:-1]:
	time.append(datetime.date(int(line[0]), int(line[1]), 1))
	region1.append(float(line[2]))
	region2.append(float(line[3]))
	region3.append(float(line[4]))
time = np.array(time, dtype = "datetime64")
region1 = np.array(region1)
region2 = np.array(region2)
region3 = np.array(region3)

data_raw2 = []
for line in open("SOI.txt", "r").readlines():
	data_raw2.append(line.rstrip("\n").split())
del data_raw2[0]

SOI = []
for line in data_raw2[103:]:
	for i in range(1, len(line)):
		SOI.append(float(line[i]))
SOI = np.array(SOI)

fig, (ax1, ax2) = plt.subplots(2, sharex = True)
ax1.plot(time, region1, "bo", ms = 2, label = r"130E - 80W")
ax1.plot(time, region2, "ro", ms = 2, label = r"160E - 80W")
ax1.plot(time, region3, "go", ms = 2, label = r"180W - 100W")
ax2.plot(time, SOI, "ko", ms = 2)
ax2.set_xlabel(r"Fecha (ordinal Gregoriano)")
ax1.set_ylabel(r"Anomal\'ia promedio ($^{\circ}C$)")
ax1.legend(bbox_to_anchor=(0.5, 1.2), loc=9, ncol = 3)
ax2.set_ylabel(r"Indice de oscilaci\'on del sur")
fig.savefig("Anomalies_SOI_Plot.pdf")

region1 = region1 - np.mean(region1)
region2 = region2 - np.mean(region2)
region3 = region3 - np.mean(region3)
SOI = SOI - np.mean(SOI)

cov = np.cov(np.matrix([region1, region2, region3, SOI]))
values, vectors = np.linalg.eig(cov)

#Tenemos que as varianzas ya estan en orden
#print values

print "Las componentes principales son", vectors[:,0], "y", vectors[:,1]

datos = np.matrix([region1, region2, region3, SOI])
for i in range(0, len(datos[:,0])):
	datos[i] = datos[i] - np.mean(datos[i])
datos_proyectados = np.dot(vectors.T, datos)
fig, ax = plt.subplots()
ax.plot(datos_proyectados[0,:], datos_proyectados[1,:], "ko")
ax.set_xlabel("Componente principal")
ax.set_ylabel("Segunda componente principal")
ax.set_title(r"An\'alisis de componentes principales")
fig(figsize = (10,5))


print cov, valores, vectores
