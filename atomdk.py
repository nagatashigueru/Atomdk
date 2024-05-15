
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
DefectType = {'Point': atoms.PointDefect}


Atoms = ReadCoords[ParamValue['StructFormat'][0]](ParamValue['StructureFile'][0])

FaceXMin, FaceXMax, FaceYMin, FaceYMax, FaceZMin, FaceZMax, Inside = atoms.SurfaceInside(Atoms)

FacesList = FaceXMin + FaceXMax + FaceYMin + FaceYMax + FaceZMin + FaceZMax

DefectPlace = {'Surface': FacesList, 'Inside': Inside}

NewStructure = DefectType[ParamValue['DefectType'][0]](DefectPlace[ParamValue['DefectPlace'][0]])


