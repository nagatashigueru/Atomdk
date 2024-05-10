
# --- #
# Nombre      : structure.py
# Descripción : Modulo que implementa el metodo para leer los archivos de
#               estructura cristalina.
# --- #

import numpy as np

def ReadXYZ(FileXYZ):

    # --- #
    # Descripción:
    #       Función que lee las coordenadas de los atomos en formato XYZ.
    # Parametros recibidos:
    #       + FileXYZ: Archivo que contiene la estructura cristalina en
    #                  formato XYZ
    # Valor devuelto:
    #       Devuelve array de Numpy <AtomsCoord> conteniendo las coordenadas
    #       de los atomos.
    # --- #

    Data = open(FileXYZ, 'r')

    DataLines = Data.read().splitlines()

    NumberOfAtoms = int(DataLines[0])

    AtomsCoord = np.zeros(shape=(NumberOfAtoms,3))

    for i in range(NumberOfAtoms):
        spl = DataLines[i+2].split()
        AtomsCoord[i] = spl[1:]

    Data.close()
    return AtomsCoord