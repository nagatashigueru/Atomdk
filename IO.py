
# --- #
# Nombre      : input.py
# Descripción : Modulo que implementa el metodo para leer las opciones desde un archivo de
#               entrada (input)
# --- #

def InputOptionsFile(OptionsFile):

    # --- #
    # Descripción:
    #       Función que genera un diccionario con las opciones o comandos
    #       que reconoce el programa como keyWords.
    # Parametros recibidos:
    #       + OptionFile: Archivo que contiene las keywords que el programa
    #                     reconoce.
    # Valor devuelto:
    #       Devuelve un diccionario <OptionsDict> con las keywords como claves
    #       leidas desde <OptionsFile> y listas vacias como valores por defecto.
    # --- #

    OptionFile = open(OptionsFile, 'r')
    OptionsList = OptionFile.read().splitlines()

    DefaultValues = [[] for _ in range(len(OptionsList))]
    OptionsDict = dict(zip(OptionsList, DefaultValues))

    OptionFile.close()
    return OptionsDict



def InputFileRead(InputFile, Params):

    # --- #
    # Descripcion:
    #       Funcion que lee el archivo input y asigna los valores a la keyword
    #       correspondiente.
    # Parametros recibidos:
    #       + InputFile: Archivo de entrada con las keywords y sus valores
    #                    deseados.
    #       + Params   : Diccionario conteniendo las keywords como claves.
    # Valor devuelto:
    #       Devuelve un diccionario <Params> con las keywords como claves y los
    #       valores leidos desde el archivo <InputFile> como valores.
    # --- #

    FileInput = open(InputFile, 'r')
    lines = FileInput.read().splitlines()

    for line in lines:
        spl = line.split()
        for valor in spl:
            if valor in Params.keys():
                state = valor
            else:
                Params[state].append(valor)

    FileInput.close()
    return Params

def WriteXYZ(Name,Structure):
    output = open(Name,'w')
    output.write(str(len(Structure)))
    output.write('\n')
    for i in range(len(Structure)):
        output.write(str(Structure[i][0]))
        output.write(' ')
        output.write(str(Structure[i][1]))
        output.write(' ')
        output.write(str(Structure[i][2]))
        output.write(' ')
        output.write('\n')
    output.close()
    return