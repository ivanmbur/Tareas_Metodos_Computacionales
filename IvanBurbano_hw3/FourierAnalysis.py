import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wv
from matplotlib import rc
import scipy.fftpack as fft

rc("text", usetex = True)

violin_rate, violin = wv.read("violin.wav")
trumpet_rate, trumpet = wv.read("trumpet.wav")

violin_fft = fft.fft(violin)
trumpet_fft = fft.fft(trumpet)
violin_freq = fft.fftfreq(len(violin),1.0/violin_rate)
trumpet_freq = fft.fftfreq(len(trumpet),1.0/trumpet_rate)
fig, ax = plt.subplots(2, figsize = (10,10))
ax[0].plot(violin_freq, np.real(violin_fft), c="k", label = r"Viol\'in")
ax[1].plot(trumpet_freq, np.real(trumpet_fft), c = "k", label = r"Trompeta")
ax[0].set_xlim(0,25000)
ax[1].set_xlim(0,25000), 
ax[1].set_xlabel(r"Frecuencia (Hz)")
ax[0].set_ylabel(r"FFT")
ax[1].set_ylabel(r"FFT")
ax[0].set_title(r"Transformada de Fourier")
ax[0].legend()
ax[1].legend()
fig.savefig("ViolinTrompeta.pdf")

def filtro_fundamental(x, freq):
    y = x.copy()
    pos_fundamental = np.where(y==np.max(y))
    y[pos_fundamental]=0
    y[np.where(freq == np.abs(freq[pos_fundamental]))]=0
    return y
    
def filtro_pasa_bajos(x, freq):
    y = x.copy()
    y[np.where(np.abs(freq) > 2000)]=0
    return y
    
def filtro_pasa_altos(x, freq):
    y = x.copy()
    y[np.where(np.abs(freq) < 2000)]=0
    return y
    
epsilon = 50

def filtro_pasa_bandas(x, freq):
    y = x.copy()
    pos_fundamental = np.where(y==np.max(y))
    y[np.where(np.abs(freq) > np.abs(freq[pos_fundamental]) + epsilon)]=0
    y[np.where(np.abs(freq) < np.abs(freq[pos_fundamental]) - epsilon)]=0
    return y

fig, ax = plt.subplots(5, figsize = (10,10))
ax[0].plot(violin_freq, np.real(violin_fft), c="k", label = r"Viol\'in")
ax[1].plot(violin_freq, np.real(filtro_fundamental(violin_fft,violin_freq)), c="k", label = r"Viol\'in sin frecuencia fundamental")
ax[2].plot(violin_freq, np.real(filtro_pasa_bajos(violin_fft,violin_freq)), c="k", label = r"Viol\'in sin frecuencias altas")
ax[3].plot(violin_freq, np.real(filtro_pasa_altos(violin_fft,violin_freq)), c="k", label = r"Viol\'in sin frecuencias bajas")
ax[4].plot(violin_freq, np.real(filtro_pasa_bandas(violin_fft,violin_freq)), c="k", label = r"Viol\'in sin frecuencias extremales")
ax[4].set_xlabel(r"Frecuencia (Hz)")
ax[0].set_ylabel(r"FFT")
ax[1].set_ylabel(r"FFT")
ax[2].set_ylabel(r"FFT")
ax[3].set_ylabel(r"FFT")
ax[4].set_ylabel(r"FFT")
ax[0].set_title(r"Filtros")
ax[0].set_xlim(0,25000)
ax[1].set_xlim(0,25000)
ax[2].set_xlim(0,25000)
ax[1].legend()
ax[2].legend()
ax[3].legend()
ax[4].legend()
ax[3].set_xlim(0,25000)
ax[4].set_xlim(0,25000)
ax[0].legend()
fig.savefig("ViolinFiltros.pdf")
    
wv.write("violin_pico.wav", violin_rate, np.real(fft.ifft(filtro_fundamental(violin_fft,violin_freq))).astype("int16"))
wv.write("violin_pasabajos.wav", violin_rate, np.real(fft.ifft(filtro_pasa_bajos(violin_fft,violin_freq))).astype("int16"))
wv.write("violin_pasaaltos.wav", violin_rate, np.real(fft.ifft(filtro_pasa_altos(violin_fft,violin_freq))).astype("int16"))
wv.write("violin_pasabanda.wav", violin_rate, np.real(fft.ifft(filtro_pasa_bandas(violin_fft,violin_freq))).astype("int16"))

