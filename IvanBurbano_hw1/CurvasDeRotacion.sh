#!/bin/sh

mkdir RotationCurves
mv PLOTS_RotationCurves.py RotationCurves/
cd RotationCurves/
wget http://iopscience.iop.org/1538-3881/122/5/2396/fulltext/datafile3.txt
awk '{if($1 ==  "F571-8") print $0}' datafile3.txt > RotationCurve_F571-8.txt
python PLOTS_RotationCurves.py
rm datafile3.txt
mv PLOTS_RotationCurves.py ..
