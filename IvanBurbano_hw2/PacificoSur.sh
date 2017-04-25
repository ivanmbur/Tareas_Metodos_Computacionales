#!/bin/bash

wget http://www.cpc.ncep.noaa.gov/products/analysis_monitoring/ocean/index/heat_content_index.txt
mkdir Dir_PacificoSur
mv heat_content_index.txt Dir_PacificoSur
mv SOI.txt Dir_PacificoSur
mv PCA_PacificoSur.py Dir_PacificoSur
cd Dir_PacificoSur
python PCA_PacificoSur.py
