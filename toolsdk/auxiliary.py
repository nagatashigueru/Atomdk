# --- #
# modulo de funciones auxiliares
# --- #

def UniqueValues(Coords,Axe):
    
    Coords = Coords
    Axe = Axe

    UValues = []

    if Axe == 'x':
        for i in range(len(Coords)):
            val = Coords[i][0]
            if val not in UValues:
                UValues.append(val)
    elif Axe == 'y':
        for i in range(len(Coords)):
            val = Coords[i][1]
            if val not in UValues:
                UValues.append(val)
    elif Axe == 'z':
        for i in range(len(Coords)):
            val = Coords
            if val not in UValues:
                UValues.append(val)
    
    return UValues

def SortedValues(Coords,Axe,AxeDiff,AxeVal):

    Coords = Coords
    AxeDiff = AxeDiff
    AxeVal = AxeVal
    Axe = Axe

    SValues = []

    if AxeDiff == {'x'}:
        if Axe == 'y':
            for i in range(len(Coords)):
                if Coords[i][1] == AxeVal:
                    SValues.append(Coords[i][0])
        elif Axe == 'z':
            for i in range(len(Coords)):
                if Coords[i][2] == AxeVal:
                    SValues.append(Coords[i][0])
    elif AxeDiff == {'y'}:
        if Axe == 'x':
            for i in range(len(Coords)):
                if Coords[i][0] == AxeVal:
                    SValues.append(Coords[i][1])
        elif Axe == 'z':
            for i in range(len(Coords)):
                if Coords[i][2] == AxeVal:
                    SValues.append(Coords[i][1])
    elif AxeDiff == {'z'}:
        if Axe == 'y':
            for i in range(len(Coords)):
                if Coords[i][1] == AxeVal:
                    SValues.append(Coords[i][2])
        elif Axe == 'x':
            for i in range(len(Coords)):
                if Coords[i][0] == AxeVal:
                    SValues.append(Coords[i][2])

    SortedValues = sorted(SValues)

    return SortedValues