GRAFICAS1 = histograma_x.pdf histrograma_y.pdf x_y.pdf 
GRAFICAS2 = histograma_R.pdf histograma_C.pdf R_verosimilitud.pdf C_verosimilitud.pdf mejor_fit.pdf 

resultados_hw5.pdf : resultados_hw5.tex 
	pdflatex $<

$(GRAFICAS1) : plots_canal_ionico.py x_y.txt
	python $<

x_y.txt : canal_ionico.x Canal_ionico.txt Canal_ionico1.txt
	./$<

canal_ionico.x : canal_ionico.c
	cc $< -lm -o $@

$(GRAFICAS2) : circuitoRC.py CircuitoRC.txt
	python $<
