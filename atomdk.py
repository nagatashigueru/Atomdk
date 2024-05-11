
# --- #
# Nombre      : atomdk.py
# Descripción : Programa principal.
# --- #

import sys
import input
import structure
import atoms

arguments = sys.argv
parameters = input.InputOptionsFile('options.config')
ParamValue = input.InputFileRead(arguments[1], parameters)

ReadCoords = {'XYZ': structure.ReadXYZ}

Atoms = ReadCoords[ParamValue['StructFormat'][0]](ParamValue['StructureFile'][0])

x,y,z,xx,yy,zz,i = atoms.SurfaceInside(Atoms)

#print(Atoms)
print(y)
