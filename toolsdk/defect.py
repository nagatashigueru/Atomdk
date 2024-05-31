# --- #
# modulo de defectos
# --- #

import random
import toolsdk.atoms
import toolsdk.auxiliary
import math

def SurfacePoint(FaceX, FaceY, FaceZ):

    FaceX = FaceX
    FaceY = FaceY
    FaceZ = FaceZ

    FaceXMin = FaceX[0]
    FaceXMax = FaceX[1]
    FaceYMin = FaceY[0]
    FaceYMax = FaceY[1]
    FaceZMin = FaceZ[0]
    FaceZMax = FaceZ[1]

    FaceOptions = (FaceXMin,
               FaceXMax,
               FaceYMin,
               FaceYMax,
               FaceZMin,
               FaceZMax)
    
    FaceChoice = random.choice(FaceOptions)

    AtomChoice = random.choice(FaceChoice)

    return AtomChoice

def InsidePoint(Inside):
    
    Inside = Inside

    AtomChoice = random.choice(Inside)

    return AtomChoice

def EdgePoint(EdgesYMin, EdgesYmax, EdgesZMax, EdgesZMin):
    
    EdgesYMin = EdgesYMin
    EdgesYmax = EdgesYmax
    EdgesZMax = EdgesZMax
    EdgesZMin = EdgesZMin

    EdgeXminYmin = EdgesYMin[0]
    EdgeXmaxYmin = EdgesYMin[1]
    EdgeZminYmin = EdgesYMin[2]
    EdgeZmaxYmin = EdgesYMin[3]

    EdgeXminYmax = EdgesYmax[0]
    EdgeXmaxYmax = EdgesYmax[1]
    EdgeZminYmax = EdgesYmax[2]
    EdgeZmaxYmax = EdgesYmax[3]

    EdgeXminZmax = EdgesZMax[0]
    EdgeXmaxZmax = EdgesZMax[1]
    EdgeXminZmin = EdgesZMin[0]
    EdgeXmaxZmin = EdgesZMin[1]

    EdgeOptions = (EdgeXminYmin,
                   EdgeXmaxYmin,
                   EdgeZminYmin,
                   EdgeZmaxYmin,
                   EdgeXminYmax,
                   EdgeXmaxYmax,
                   EdgeZminYmax,
                   EdgeZmaxYmax,
                   EdgeXminZmax,
                   EdgeXmaxZmax,
                   EdgeXminZmin,
                   EdgeXmaxZmin)
    
    Flag = 0

    while Flag == 0:
        EdgeChoice = random.choice(EdgeOptions)
        if len(EdgeChoice) > 0:
            Flag = 1
            AtomChoice = random.choice(EdgeChoice)

    return AtomChoice

def VertexPoint(VerticesZMax, VerticesZMin):

    VerticesZMax = VerticesZMax
    VerticesZMin = VerticesZMin

    VXiYiZa = VerticesZMax[0]
    VXiYaZa = VerticesZMax[1]
    VXaYaZa = VerticesZMax[2]
    VXaYiZa = VerticesZMax[3]

    VXiYiZi = VerticesZMin[0]
    VXiYaZi = VerticesZMin[1]
    VXaYaZi = VerticesZMin[2]
    VXaYiZi = VerticesZMin[3]

    VertexOptions = (VXiYiZa,
                     VXiYaZa,
                     VXaYaZa,
                     VXaYiZa,
                     VXiYiZi,
                     VXiYaZi,
                     VXaYaZi,
                     VXaYiZi)
    
    Flag = 0

    while Flag == 0:
        VertexChoice = random.choice(VertexOptions)
        if type(VertexChoice) is tuple:
            Flag = 1
            AtomChoice = VertexChoice

    return AtomChoice

def EdgeLine(EdgesYMin, EdgesYmax, EdgesZMax, EdgesZMin, Size, latticeconstant):

    EdgesYMin = EdgesYMin
    EdgesYmax = EdgesYmax
    EdgesZMax = EdgesZMax
    EdgesZMin = EdgesZMin
    latticeconstant = latticeconstant
    Size = Size

    EdgeXminYmin = EdgesYMin[0]
    EdgeXmaxYmin = EdgesYMin[1]
    EdgeZminYmin = EdgesYMin[2]
    EdgeZmaxYmin = EdgesYMin[3]

    EdgeXminYmax = EdgesYmax[0]
    EdgeXmaxYmax = EdgesYmax[1]
    EdgeZminYmax = EdgesYmax[2]
    EdgeZmaxYmax = EdgesYmax[3]

    EdgeXminZmax = EdgesZMax[0]
    EdgeXmaxZmax = EdgesZMax[1]
    EdgeXminZmin = EdgesZMin[0]
    EdgeXmaxZmin = EdgesZMin[1]

    EdgeOptions = (EdgeXminYmin,
                   EdgeXmaxYmin,
                   EdgeZminYmin,
                   EdgeZmaxYmin,
                   EdgeXminYmax,
                   EdgeXmaxYmax,
                   EdgeZminYmax,
                   EdgeZmaxYmax,
                   EdgeXminZmax,
                   EdgeXmaxZmax,
                   EdgeXminZmin,
                   EdgeXmaxZmin)
    
    AtomChoice = []
    
    Flag = 0

    while Flag == 0:
        EdgeChoice = random.choice(EdgeOptions)
        if len(EdgeChoice) > 0:
            Flag = 1
            if Size <= len(EdgeChoice):
                xmi, ymi, zmi = toolsdk.atoms.minimum(EdgeChoice)
                xma, yma, zma = toolsdk.atoms.maximum(EdgeChoice)

                if (xma - xmi) != 0:
                    for i in range(Size):
                        AtomChoice.append((xmi + (i * latticeconstant), ymi, zmi))
                elif (yma - ymi) != 0:
                    for i in range(Size):
                        AtomChoice.append((xmi, ymi + (i * latticeconstant), zmi))
                else:
                    for i in range(Size):
                        AtomChoice.append((xmi, ymi, zmi + (i * latticeconstant)))
            else:
                print('El tamaño es superior a las dimensiones de la arista.')

    return AtomChoice

def SurfaceLine(FaceX, FaceY, FaceZ, Size):

    FaceX = FaceX
    FaceY = FaceY
    FaceZ = FaceZ
    Size = Size
    
    FaceXMin = FaceX[0]
    FaceXMax = FaceX[1]
    FaceYMin = FaceY[0]
    FaceYMax = FaceY[1]
    FaceZMin = FaceZ[0]
    FaceZMax = FaceZ[1]

    FaceOptions = (FaceXMin,
                   FaceXMax,
                   FaceYMin,
                   FaceYMax,
                   FaceZMin,
                   FaceZMax)
    
    FaceChoice = random.choice(FaceOptions)

    xmi, ymi, zmi = toolsdk.atoms.minimum(FaceChoice)
    xma, yma, zma = toolsdk.atoms.maximum(FaceChoice)

    AtomChoice = []

    if (xma - xmi) != 0:
        if (yma - ymi) != 0:
            AxeOptions = ('x','y')
            axe = random.choice(AxeOptions)
            axeDiff = set(AxeOptions) ^ set(tuple(axe))
            Uvalues = toolsdk.auxiliary.UniqueValues(FaceChoice,axe)
            AxeVal = random.choice(Uvalues)
            SValues = toolsdk.auxiliary.SortedValues(FaceChoice,axe,axeDiff,AxeVal)
            if len(SValues) >= Size:
                if axe == 'x':
                    for i in range(Size):
                        AtomChoice.append((AxeVal,SValues[i],zmi))
                elif axe == 'y':
                    for i in range(Size):
                        AtomChoice.append((SValues[i],AxeVal,zmi))
            else:
                print('el tamaño es mayor a la dimension de la celda')
        elif (zma - zmi) != 0:
            AxeOptions = ('x','z')
            axe = random.choice(AxeOptions)
            axeDiff = set(AxeOptions) ^ set(tuple(axe))
            Uvalues = toolsdk.auxiliary.UniqueValues(FaceChoice,axe)
            AxeVal = random.choice(Uvalues)
            SValues = toolsdk.auxiliary.SortedValues(FaceChoice,axe,axeDiff,AxeVal)
            if len(SValues) >= Size:
                if axe == 'x':
                    for i in range(Size):
                        AtomChoice.append((AxeVal,ymi,SValues[i]))
                elif axe == 'z':
                    for i in range(Size):
                        AtomChoice.append((SValues[i],ymi,AxeVal))
            else:
                print('el tamaño es mayor a la dimension de la celda')
    elif (yma - ymi) != 0:
        if (zma - zmi) != 0:
            AxeOptions = ('y','z')
            axe = random.choice(AxeOptions)
            axeDiff = set(AxeOptions) ^ set(tuple(axe))
            Uvalues = toolsdk.auxiliary.UniqueValues(FaceChoice,axe)
            AxeVal = random.choice(Uvalues)
            SValues = toolsdk.auxiliary.SortedValues(FaceChoice,axe,axeDiff,AxeVal)
            if len(SValues) >= Size:
                if axe == 'y':
                    for i in range(Size):
                        AtomChoice.append((xmi,AxeVal,SValues[i]))
                elif axe == 'z':
                    for i in range(Size):
                        AtomChoice.append((xmi,SValues[i],AxeVal))
            else:
                print('el tamaño es mayor a la dimension de la celda')

    return AtomChoice