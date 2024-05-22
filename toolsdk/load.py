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
