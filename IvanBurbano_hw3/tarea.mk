resultados.pdf : resultados.tex Troyano.pdf OrbitsPLOT.pdf MassPLOT.pdf
	pdflatex $<

Troyano.pdf : Troyanos.py
	python $^

OrbitsPLOT.pdf : Troyanos.py
	python $^

MassPLOT.pdf : Troyanos.py
	python $^ 
