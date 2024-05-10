
# --- #
# Nombre      : atomdk.py
# Descripción : Programa principal.
# --- #

import sys
import input
import structure

arguments = sys.argv
parameters = input.InputOptionsFile('options.config')
ParamValue = input.InputFileRead(arguments[1], parameters)

ReadCoords = {'XYZ': structure.ReadXYZ}

Atoms = ReadCoords[ParamValue['StructFormat'][0]](ParamValue['StructureFile'][0])

print(Atoms)
