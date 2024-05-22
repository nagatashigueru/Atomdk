#script principal

import sys
import toolsdk.load
import toolsdk.defect
from toolsdk.structure import BaseCenteredCubic, FaceCenteredCubic, SimpleCubic

Parameters = toolsdk.load.LoadConfig('config.rc')
Arguments = sys.argv
if len(Arguments) == 2:
    Values = toolsdk.load.LoadInput(Arguments[1], Parameters)
else:
    print('Debe indicar un archivo de input con las opciones correspondientes')

if Values['LatticeType'] == 'BCC':
    structure = BaseCenteredCubic(symbol=Values['Symbol'],
                              latticeconstant=float(Values['LatticeConst']),
                              size=(int(Values['SizeX'][0]),int(Values['SizeY'][0]),int(Values['SizeZ'][0])))
elif Values['LatticeType'] == 'FCC':
    structure = FaceCenteredCubic(symbol=Values['Symbol'],
                              latticeconstant=float(Values['LatticeConst']),
                              size=(int(Values['SizeX'][0]),int(Values['SizeY'][0]),int(Values['SizeZ'][0])))
elif Values['LatticeType'] == 'SC':
    structure = SimpleCubic(symbol=Values['Symbol'],
                              latticeconstant=float(Values['LatticeConst']),
                              size=(int(Values['SizeX'][0]),int(Values['SizeY'][0]),int(Values['SizeZ'][0])))


Positions = structure.getpositions()
Min, Max = structure.MinMax(Positions)
FaceX, FaceY, FaceZ = structure.Face(Positions,Min,Max)
Inside = structure.Inside(Positions, FaceX, FaceY, FaceZ)
EdgesYMin, EdgesYmax, EdgesZMax, EdgesZMin = structure.Edges(FaceX,FaceY,FaceZ)

structure.Write('Fe.xyz')

borrar = toolsdk.defect.SurfacePoint(FaceX, FaceY, FaceZ)
borrar2 = toolsdk.defect.InsidePoint(Inside)
borrar3 = toolsdk.defect.EdgePoint(EdgesYMin, EdgesYmax, EdgesZMax, EdgesZMin)

print('los minimos: {mi}'.format(mi = Min))
print('los maximos: {ma}'.format(ma = Max))
print('la cara x min: {facexmi}'.format(facexmi = FaceX[0]))
print('la arista y min x min: {edgeymixmi}'.format(edgeymixmi = EdgesYMin[0]))
print('atomo borrado {atom}'.format(atom = borrar3))