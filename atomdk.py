
# --- #
# Nombre      : atomdk.py
# Descripción : Programa principal.
# --- #

import sys
import IO
import atoms
import crystal
import ase.io

arguments = sys.argv
parameters = IO.InputOptionsFile('options.config')
ParamValue = IO.InputFileRead(arguments[1], parameters)

Structure = crystal.CubicGenerator(ParamValue['LatticeType'][0],
                               float(ParamValue['LatticeConst'][0]),
                               ParamValue['Symbol'][0],
                               int(ParamValue['SizeX'][0]),
                               int(ParamValue['SizeY'][0]),
                               int(ParamValue['SizeZ'][0]))

FaceXMin, FaceXMax, FaceYMin, FaceYMax, FaceZMin, FaceZMax, Inside = atoms.SurfaceInside(Structure)

Faces = (FaceXMin, FaceXMax, FaceYMin, FaceYMax, FaceZMin, FaceZMax)

DefectType = {'Point': atoms.PointDefect,
              'Linear': atoms.LinearDefect}

DefectPlace = {'Surface': Faces,
               'Inside': Inside}

if ParamValue['DefectType'][0] == 'Point':
    NewStructure = atoms.PointDefect(DefectPlace[ParamValue['DefectPlace'][0]])
elif ParamValue['DefectType'][0] == 'Linear':
    NewStructure = atoms.LinearDefect(DefectPlace[ParamValue['DefectPlace'][0]],
                                      3,
                                      'X',
                                      ParamValue['DefectPlace'][0])

IO.WriteXYZ('NuevaEstructura.xyz',NewStructure)