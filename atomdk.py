import sys
import input

parameters = input.InputOptionsFile('options.config')

arguments = sys.argv

ParamValue = input.InputFileRead(arguments[1], parameters)

print(ParamValue)

