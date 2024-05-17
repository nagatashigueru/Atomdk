from ase.lattice.cubic import FaceCenteredCubic, BodyCenteredCubic
import ase.io as aio

def CubicGenerator(StrucType,LatticeConst,Symbol,SizeX=1,SizeY=1,SizeZ=1):
    if StrucType == 'BCC':
        Coords = BodyCenteredCubic(directions=[[1,0,0],[0,1,0],[0,0,1]], size=(SizeX,SizeY,SizeZ),symbol=Symbol,pbc=(1,1,1),latticeconstant=LatticeConst)
    elif StrucType == 'FCC':
        Coords = FaceCenteredCubic(directions=[[1,0,0],[0,1,0],[0,0,1]], size=(SizeX,SizeY,SizeZ),symbol=Symbol,pbc=(1,1,1),latticeconstant=LatticeConst)
    else:
        print('Structure type not yet available')

    return Coords.get_positions()