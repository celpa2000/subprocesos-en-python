# -*- coding: utf-8 -*-


import subprocess
import sys
try:
    proceso = sys.argv[1]
except IndexError:
    sys.exit()

"""CON EL MODULO SUBPROCESS Y EL PROGRAMA PROCESSINFO PASADO
    COMO ARGUMENTO CAPTURAMOS LA SALIDA POR PANTALLA CON EL SIGUIENTE PARAMETRO 'capture_ouput'
    LUEGO LE PASAMOS COMO TRECER PARAMETRO LA CODIFICACION 'cp850'
"""
r = subprocess.run("processinfo",capture_output=True, encoding="cp850")


lineas = r.stdout.split("\n")


lineas = lineas[4:-2]

for linea in lineas:
    linea = linea.split("|")
    usuario = linea[3]
    pid = linea[1]
    proces = linea[2]
    proces = proces.strip()

    if proceso == proces:
         print("PID:",pid,"Usuario:",usuario[-6:])
