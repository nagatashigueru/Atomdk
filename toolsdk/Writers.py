# --- #
# modulo para escribir archivos
# --- #

# =================== #
# WRITERS HOMOGENEOS
# =================== #

def Write(FileName, Positions, Symbol):

    Positions = Positions
    Symbol = Symbol

    OutputFile = open(FileName, 'w')
    OutputFile.write(str(len(Positions)) + '\n')
    OutputFile.write('\n')
    for i in range(len(Positions)):
        OutputFile.write('{symbol} {x} {y} {z} \n'.format(symbol = Symbol, x = Positions[i][0], y = Positions[i][1], z = Positions[i][2]))

    OutputFile.close()
    
    return

def WritePoint(FileName, Positions, AtomChoice, Symbol):

    FileName = FileName
    Positions = Positions
    AtomChoice = AtomChoice
    Symbol = Symbol

    OutputFile = open(FileName, 'w')
    OutputFile.write(str(len(Positions) - 1) + '\n')
    OutputFile.write('\n')

    for i in range(len(Positions)):
        if Positions[i] == AtomChoice:
            continue
        else:
            OutputFile.write('{symbol} {x} {y} {z} \n'.format(symbol = Symbol, x = Positions[i][0], y = Positions[i][1], z = Positions[i][2]))

    OutputFile.close()

    return

def WriteLine(FileName, Positions, AtomChoice, Symbol):
    
    FileName = FileName
    Positions = Positions
    AtomChoice = AtomChoice
    Symbol = Symbol

    OutputFile = open(FileName, 'w')
    OutputFile.write(str(len(Positions) - len(AtomChoice)) + '\n')
    OutputFile.write('\n')

    for i in range(len(Positions)):
        if Positions[i] not in AtomChoice:
            OutputFile.write('{symbol} {x} {y} {z} \n'.format(symbol = Symbol, x = Positions[i][0], y = Positions[i][1], z = Positions[i][2]))

    OutputFile.close()
    
    return
