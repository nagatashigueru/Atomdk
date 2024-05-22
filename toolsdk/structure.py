# --- #
# Clase para la estructura
# --- #

import toolsdk.atoms

class CrystalStructure:
    
    def __init__(self, symbol, size, latticeconstant):
        self.positions = []
        self.symbol = symbol
        self.size = size
        self.latticeconstant = latticeconstant

    def Write(self, FileName):
        OutputFile = open(FileName, 'w')
        OutputFile.write(str(len(self.positions)) + '\n')
        OutputFile.write('\n')
        for i in range(len(self.positions)):
            OutputFile.write('{symbol} {x} {y} {z} \n'.format(symbol = self.symbol, x = self.positions[i][0], y = self.positions[i][1], z = self.positions[i][2]))

        OutputFile.close()
        return
    
    def MinMax(self, Positions):
        
        Positions = Positions
        
        Min = toolsdk.atoms.minimum(Positions)
        Max = toolsdk.atoms.maximum(Positions)

        return Min, Max
    
    def FaceInside(self, Positions, Min, Max):

        Positions = Positions
        Min = Min
        Max = Max

        FaceXMin, FaceXMax, FaceYMin, FaceYMax, FaceZMin, FaceZMax, Inside = toolsdk.atoms.FaceInside(Positions, Min, Max)

        return (FaceXMin, FaceXMax) , (FaceYMin, FaceYMax) , (FaceZMin, FaceZMax) , Inside
    
    def Edges(self, FaceX, FaceY, FaceZ):

        FaceX = FaceX
        FaceY = FaceY
        FaceZ = FaceZ

        EdgeXminYmin, EdgeXmaxYmin, EdgeZminYmin, EdgeZmaxYmin, EdgeXminYmax, EdgeXmaxYmax, EdgeZminYmax, EdgeZmaxYmax, EdgeXminZmax, EdgeXmaxZmax, EdgeXminZmin, EdgeXmaxZmin = toolsdk.atoms.Edges(FaceX, FaceY, FaceZ)

        return (EdgeXminYmin, EdgeXmaxYmin, EdgeZminYmin, EdgeZmaxYmin) , (EdgeXminYmax, EdgeXmaxYmax, EdgeZminYmax, EdgeZmaxYmax) , (EdgeXminZmax, EdgeXmaxZmax) , (EdgeXminZmin, EdgeXmaxZmin)
    
    def Vertices(self, EdgesYMin, EdgesYmax, EdgesZMax, EdgesZMin):
        
        EdgesYMin = EdgesYMin
        EdgesYmax = EdgesYmax
        EdgesZMax = EdgesZMax
        EdgesZMin = EdgesZMin

        return

class BaseCenteredCubic(CrystalStructure):

    def getpositions(self):
        x1 = 0.0
        y1 = 0.0
        z1 = 0.0

        x2 = self.latticeconstant / 2.0
        y2 = self.latticeconstant / 2.0
        z2 = self.latticeconstant / 2.0

        for i in range(self.size[0]):
            for j in range(self.size[1]):
                for k in range(self.size[2]):
                    self.positions.append((x1 + (i * self.latticeconstant), y1 + (j * self.latticeconstant), z1 + (k * self.latticeconstant)))
                    self.positions.append((x2 + (i * self.latticeconstant), y2 + (j * self.latticeconstant), z2 + (k * self.latticeconstant)))
        return self.positions


class FaceCenteredCubic(CrystalStructure):

    def getpositions(self):
        x1 = 0.0
        y1 = 0.0
        z1 = 0.0

        x2 = self.latticeconstant / 2.0
        y2 = self.latticeconstant / 2.0
        z2 = 0.0

        x3 = self.latticeconstant / 2.0
        y3 = 0.0
        z3 = self.latticeconstant / 2.0

        x4 = 0.0
        y4 = self.latticeconstant / 2.0
        z4 = self.latticeconstant / 2.0

        for i in range(self.size[0]):
            for j in range(self.size[1]):
                for k in range(self.size[2]):
                    self.positions.append((x1 + (i * self.latticeconstant), y1 + (j * self.latticeconstant), z1 + (k * self.latticeconstant)))
                    self.positions.append((x2 + (i * self.latticeconstant), y2 + (j * self.latticeconstant), z2 + (k * self.latticeconstant)))
                    self.positions.append((x3 + (i * self.latticeconstant), y3 + (j * self.latticeconstant), z3 + (k * self.latticeconstant)))
                    self.positions.append((x4 + (i * self.latticeconstant), y4 + (j * self.latticeconstant), z4 + (k * self.latticeconstant)))
        return self.positions



class SimpleCubic(CrystalStructure):

    def getpositions(self):
        x1 = 0.0
        y1 = 0.0
        z1 = 0.0

        for i in range(self.size[0]):
            for j in range(self.size[1]):
                for k in range(self.size[2]):
                    self.positions.append((x1 + (i * self.latticeconstant), y1 + (j * self.latticeconstant), z1 + (k * self.latticeconstant)))
        return self.positions