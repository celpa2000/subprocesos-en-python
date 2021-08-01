# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 16:09:34 2021

@author: celso
"""

import subprocess
import pprint
import sys
try:
    proce = sys.argv[1]
except IndexError:
    print("Indique el nombre de un proceso: ")

    sys.exit()

r = subprocess.run("C:/Users/celso/Desktop/processinfo-windows/processinfo.exe",capture_output=True, encoding="cp850")
lineas = r.stdout.split("\n")
#pprint.pprint(lineas[4:-2])

lineas = lineas[4:-2]

for linea in lineas:
    linea = linea.split("|")
    #print(linea)
    
    usuario = linea[3]
    
       
  
    pid = linea[1]
    procesoo = linea[2]
    procesoo = procesoo.strip()
    if proce == procesoo:
        
        print("PID:",pid,"Usuario:",usuario[0:6])