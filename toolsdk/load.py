# --- #
# Nombre: load.py
# --- #

def LoadConfig(ConfigFile):
    
    ConfigFile   = open(ConfigFile, 'r')
    ConfigLines  = ConfigFile.read().splitlines()
    ConfigValues = [ 'DefaultValue' for _ in range(len(ConfigLines))]
    ConfigDict   = dict(zip(ConfigLines, ConfigValues))
    
    ConfigFile.close()
    return ConfigDict

def LoadInput(InputFile, Parameters):
    InputFile = open(InputFile, 'r')
    InputLines = InputFile.read().splitlines()

    for line in InputLines:
        InputElements = line.split()
        for Element in InputElements:
            if Element in Parameters.keys():
                State = Element
            else:
                Parameters[State] = Element

    InputFile.close()
    return Parameters

def LoadCoords(CoordsFile):
    
    CoordsFile = open(CoordsFile, 'r')
    CoordsLines = CoordsFile.read().splitlines()

    Species = []

    for line in CoordsLines:
        Elements = line.split()
        if Elements[0] not in Species:
            Species.append(Elements[0])

    SpecieCoord = [[] for _ in range(len(Species))]

    Coords = dict(zip(Species,SpecieCoord))

    for line in CoordsLines:
        Elements = line.split()
        Coords[Elements[0]].append((Elements[1],Elements[2],Elements[3]))

    CoordsFile.close()

    return Coords