
# --- #
# Nombre      : atoms.py
# Descripción : Modulo que implementa metodos para trabajar con los atomos.
# --- #

import random

def SurfaceInside(AtomsCoord):

    # --- #
    # Descripción:
    #       Funcion que implementa el metodo para identificar los atomos
    #       ubicados en las caras y fuera de ellas. Los clasifica en 6
    #       grupos diferentes, uno por cara. Y uno mas para los demas.
    # Parametros recibidos:
    #       + AtomsCoord: Array de numpy conteniendo las coordenadas de
    #                     todos los atomos.
    # Valor devuelto:
    #       Devuelve 7 listas correspondientes a las 6 caras y 1 para los
    #       demas. FaceXMin, FaceXMax, FaceYMin, FaceYMax, FaceZMin, FaceZMax,
    #       Inside
    # --- #

    xmax, ymax, zmax = AtomsCoord.max(axis=0)
    xmin, ymin, zmin = AtomsCoord.min(axis=0)

    Dims = AtomsCoord.shape

    FaceXMin = []
    FaceXMax = []
    FaceYMin = []
    FaceYMax = []
    FaceZMin = []
    FaceZMax = []
    Inside = []

    for i in range(Dims[0]):
        if xmin == AtomsCoord[i,0]:
            FaceXMin.append(AtomsCoord[i,:])
        elif xmax == AtomsCoord[i,0]:
            FaceXMax.append(AtomsCoord[i,:])
        elif ymin == AtomsCoord[i,1]:
            FaceYMin.append(AtomsCoord[i,:])
        elif ymax == AtomsCoord[i,1]:
            FaceYMax.append(AtomsCoord[i,:])
        elif zmin == AtomsCoord[i,2]:
            FaceZMin.append(AtomsCoord[i,:])
        elif zmax == AtomsCoord[i,2]:
            FaceZMax.append(AtomsCoord[i,:])
        else:
            Inside.append(AtomsCoord[i,:])

    return FaceXMin, FaceXMax, FaceYMin, FaceYMax, FaceZMin, FaceZMax, Inside

def PointDefect(AtomsList):
    SizeList = len(AtomsList)
    IndexSelect = random.randrange(0,SizeList+1,1)
    AtomsList.pop(IndexSelect)
    return AtomsList