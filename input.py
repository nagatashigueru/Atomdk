# --- #
# Nombre      : input.py
# Descripción : Modulo que implementa el metodo para leer las opciones desde un archivo de
#               entrada (input).
# Fecha       : Mayo -2014
# Autor       : Shigueru Nagata
# --- #

def InputOptionsFile(OptionsFile):
    # --- #
    # >>> Descripción <<<
    # Función que genera un diccionario con las opciones o comandos que
    # reconoce el programa como palabras clave (keyWords).
    # >>> Parámetros Entrada <<<
    # Options: Lista de keywords
    # --- #

    # Leer File de opciones

    OptionFile = open(OptionsFile, 'r')

    OptionsList = OptionFile.read().splitlines()

    # Lista de Valores por defecto

    DefaultValues = ['Default' for _ in range(len(OptionsList))]

    # Diccionario de opciones

    OptionsDict = dict(zip(OptionsList, DefaultValues))

    OptionFile.close()

    return OptionsDict



def InputFileRead(InputFile, Params):
    FileInput = open(InputFile, 'r')
    lines = FileInput.read().splitlines()

    for line in lines:
        spl = line.split()
        if spl[0] in Params.keys():
            Params[spl[0]] = spl[1]
        else:
            print('El parametro %s no esta definido' % (spl[0]))

    FileInput.close()
    return Params