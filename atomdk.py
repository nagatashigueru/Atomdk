
# --- #
# Nombre      : atomdk.py
# Descripción : Programa principal.
# --- #

import sys
import input
import structure

parameters = input.InputOptionsFile('options.config')

arguments = sys.argv

ParamValue = input.InputFileRead(arguments[1], parameters)

Atoms = structure.XYZ('StructureExamples/Fe.xyz')
