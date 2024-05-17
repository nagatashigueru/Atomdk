
# --- #
# Nombre      : atomdk.py
# Descripción : Programa principal.
# --- #

import sys
import input
import atoms
import crystal

arguments = sys.argv
parameters = input.InputOptionsFile('options.config')
ParamValue = input.InputFileRead(arguments[1], parameters)

DefectType = {'Point': atoms.PointDefect}

Atoms = crystal.CubicGenerator(ParamValue['LatticeType'][0],
                               float(ParamValue['LatticeConst'][0]),
                               ParamValue['Symbol'][0],
                               int(ParamValue['SizeX'][0]),
                               int(ParamValue['SizeY'][0]),
                               int(ParamValue['SizeZ'][0]))

FaceXMin, FaceXMax, FaceYMin, FaceYMax, FaceZMin, FaceZMax, Inside = atoms.SurfaceInside(Atoms)

FacesList = FaceXMin + FaceXMax + FaceYMin + FaceYMax + FaceZMin + FaceZMax

DefectPlace = {'Surface': FacesList, 'Inside': Inside}

NewStructure = DefectType[ParamValue['DefectType'][0]](DefectPlace[ParamValue['DefectPlace'][0]])

print(NewStructure)
