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

def EdgePoint():
    pass
    return