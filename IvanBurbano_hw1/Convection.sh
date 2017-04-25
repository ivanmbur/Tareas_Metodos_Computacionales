#!/bin/sh

mkdir Convection
mv PLOTS_Convection.py Convection
mv DatosRadioSonda.dat Convection
cd Convection
awk '{print $2, $3}' DatosRadioSonda.dat | sed '1,7d' | sed '$d' > TempHeight.txt
python PLOTS_Convection.py
mv PLOTS_Convection.py ..
