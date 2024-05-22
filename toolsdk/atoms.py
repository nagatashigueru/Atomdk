# --- #
# script de metodos para atomos
# --- #

def minimum(Positions):
    Positions = Positions

    xmi = Positions[0][0]
    ymi = Positions[0][1]
    zmi = Positions[0][2]

    for i in range(len(Positions)):
        if Positions[i][0] < xmi:
            xmi = Positions[i][0]
        if Positions[i][1] < ymi:
            ymi = Positions[i][1]
        if Positions[i][2] < zmi:
            zmi = Positions[i][2]

    return (xmi, ymi, zmi)

def maximum(Positions):
    Positions = Positions

    xma = Positions[len(Positions) - 1][0]
    yma = Positions[len(Positions) - 1][1]
    zma = Positions[len(Positions) - 1][2]

    for i in range(len(Positions)):
        if Positions[i][0] > xma:
            xma = Positions[i][0]
        if Positions[i][1] > yma:
            yma = Positions[i][1]
        if Positions[i][2] > zma:
            zma = Positions[i][2]

    return (xma, yma, zma)

def Face(Positions, Min, Max):

    Positions = Positions
    Min = Min
    Max = Max

    XMin = []
    YMin = []
    ZMin = []

    XMax = []
    YMax = []
    ZMax = []

    Inside = []

    for i in range(len(Positions)):
            if Positions[i][0] == Min[0]:
                XMin.append(Positions[i])
            if Positions[i][0] == Max[0]:
                XMax.append(Positions[i])
            if Positions[i][1] == Min[1]:
                YMin.append(Positions[i])
            if Positions[i][1] == Max[1]:
                YMax.append(Positions[i])
            if Positions[i][2] == Min[2]:
                ZMin.append(Positions[i])
            if Positions[i][2] == Max[2]:
                ZMax.append(Positions[i])

    return XMin, XMax, YMin, YMax, ZMin, ZMax

def Inside(Positions, FaceX, FaceY, FaceZ):

    Positions = Positions
    FaceX = FaceX
    FaceY = FaceY
    FaceZ = FaceZ

    FaceXMin = FaceX[0]
    FaceXMax = FaceX[1]
    FaceYMin = FaceY[0]
    FaceYMax = FaceY[1]
    FaceZMin = FaceZ[0]
    FaceZMax = FaceZ[1]

    AtomsFace = [*FaceXMin,
                 *FaceXMax,
                 *FaceYMin,
                 *FaceYMax,
                 *FaceZMin,
                 *FaceZMax]
    
    Inside = []

    for i in range(len(Positions)):
        if Positions[i] not in AtomsFace:
            Inside.append(Positions[i])

    return Inside

def Edges(FaceX, FaceY, FaceZ):

    FaceX = FaceX
    FaceY = FaceY
    FaceZ = FaceZ

    FaceXMin = FaceX[0]
    FaceXMax = FaceX[1]
    FaceYMin = FaceY[0]
    FaceYMax = FaceY[1]
    FaceZMin = FaceZ[0]
    FaceZMax = FaceZ[1]

    EdgeXminYmin = []
    EdgeXmaxYmin = []
    EdgeZminYmin = []
    EdgeZmaxYmin = []

    EdgeXminYmax = []
    EdgeXmaxYmax = []
    EdgeZminYmax = []
    EdgeZmaxYmax = []

    EdgeXminZmax = []
    EdgeXmaxZmax = []
    EdgeXminZmin = []
    EdgeXmaxZmin = []

    for i in range(len(FaceYMin)):
        if FaceYMin[i] in FaceXMin:
            EdgeXminYmin.append(FaceYMin[i])
        if FaceYMin[i] in FaceXMax:
            EdgeXmaxYmin.append(FaceYMin[i])
        if FaceYMin[i] in FaceZMin:
            EdgeZminYmin.append(FaceYMin[i])
        if FaceYMin[i] in FaceZMax:
            EdgeZmaxYmin.append(FaceYMin[i])

    for j in range(len(FaceYMax)):
        if FaceYMax[i] in FaceXMin:
            EdgeXminYmax.append(FaceYMax[i])
        if FaceYMax[i] in FaceXMax:
            EdgeXmaxYmax.append(FaceYMax[i])
        if FaceYMax[i] in FaceZMin:
            EdgeZminYmax.append(FaceYMax[i])
        if FaceYMax[i] in FaceZMax:
            EdgeZmaxYmax.append(FaceYMax[i])

    for k in range(len(FaceZMax)):
        if FaceZMax[i] in FaceXMin:
            EdgeXminZmax.append(FaceZMax[i])
        if FaceZMax[i] in FaceXMax:
            EdgeXmaxZmax.append(FaceZMax[i])

    for l in range(len(FaceZMin)):
        if FaceZMin[i] in FaceXMin:
            EdgeXminZmin.append(FaceZMin[i])
        if FaceZMin[i] in FaceXMax:
            EdgeXmaxZmin.append(FaceZMin[i])

    return EdgeXminYmin, EdgeXmaxYmin, EdgeZminYmin, EdgeZmaxYmin, EdgeXminYmax, EdgeXmaxYmax, EdgeZminYmax, EdgeZmaxYmax, EdgeXminZmax, EdgeXmaxZmax, EdgeXminZmin, EdgeXmaxZmin

def Vertices(EdgesYMin, EdgesYmax, EdgesZMax, EdgesZMin):

    EdgesYMin = EdgesYMin
    EdgesYmax = EdgesYmax
    EdgesZMax = EdgesZMax
    EdgesZMin = EdgesZMin


    return