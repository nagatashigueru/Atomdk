# --- #
# modulo de defectos
# --- #

import random

def SurfacePoint(FaceX, FaceY, FaceZ):

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