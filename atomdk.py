#script principal

import sys
import toolsdk.load
import toolsdk.defect
import toolsdk.Writers
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
VerticesZMax, VerticesZMin = structure.Vertices(EdgesYMin, EdgesYmax, EdgesZMax, EdgesZMin)

if Values['OriginStruct'] == 'YES':
    structure.Write(Values['OriginFile'])

if Values['DefectType'] == 'Point':
    if Values['DefectPlace'] == 'Surface':
        AtomChoice = toolsdk.defect.SurfacePoint(FaceX, FaceY, FaceZ)
    elif Values['DefectPlace'] == 'Inside':
        AtomChoice = toolsdk.defect.InsidePoint(Inside)
    elif Values['DefectPlace'] == 'Edge':
        AtomChoice = toolsdk.defect.EdgePoint(EdgesYMin, EdgesYmax, EdgesZMax, EdgesZMin)
    elif Values['DefectPlace'] == 'Vertex':
        AtomChoice = toolsdk.defect.VertexPoint(VerticesZMax, VerticesZMin)

    toolsdk.Writers.WritePoint(Values['OutputFile'], Positions, AtomChoice, structure.symbol)

elif Values['DefectType'] == 'Line':
    if Values['DefectPlace'] == 'Edge':
        AtomChoice = toolsdk.defect.EdgeLine(EdgesYMin, EdgesYmax, EdgesZMax, EdgesZMin, int(Values['DefectSize']), structure.latticeconstant)
    elif Values['DefectPlace'] == 'Surface':
        AtomChoice = toolsdk.defect.SurfaceLine(FaceX,FaceY,FaceZ,int(Values['DefectSize']))

    toolsdk.Writers.WriteLine(Values['OutputFile'], Positions, AtomChoice, structure.symbol)
