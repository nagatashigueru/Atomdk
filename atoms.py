
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
    if type(AtomsList) is tuple:
        Atoms = random.choice(AtomsList)
        SizeList = len(Atoms)
        IndexSelect = random.randrange(0,SizeList+1,1)
        Atoms.pop(IndexSelect)
    else:
        Atoms = AtomsList
        SizeList = len(Atoms)
        IndexSelect = random.randrange(0,SizeList+1,1)
        Atoms.pop(IndexSelect)
            
    return Atoms

def LinearDefect(AtomsList,Size,Direction,Place):
    if Place == 'Surface':
        Atoms = random.choice(AtomsList)
        xmax, ymax, zmax = Atoms.max(axis=0)
        xmin, ymin, zmin = Atoms.min(axis=0)
        if xmax != xmin:
            if ymax != ymin:
                SizeX = len(Atoms[])
        else:
            pass
    elif Place == 'Inside':
        pass
    else:
        print('Parametro equivocado')
    return