"""
import numpy
from matplotlib import pyplot
import gemmi
# https://gemmi.readthedocs.io/en/latest/grid.html
ccp4 = gemmi.read_ccp4_map('${1:/Users/blaine/4bqrPatterson.ccp4}')
ccp4.setup()
arr = numpy.array(ccp4.grid, copy=False)
x = numpy.linspace(0, ccp4.grid.unit_cell.a, num=arr.shape[0], endpoint=False)
y = numpy.linspace(0, ccp4.grid.unit_cell.b, num=arr.shape[1], endpoint=False)
X, Y = numpy.meshgrid(x, y, indexing='ij')
pyplot.rcParams["figure.figsize"] = (8.0, 8.0)
pyplot.contour(X, Y, arr[:,:,0],500, zorder=1,linestyles='solid')
pyplot.gca().set_aspect('equal', adjustable='box')
pyplot.show()

arr2 = numpy.array(ccp4.grid, copy=False)
x = numpy.linspace(0, ccp4.grid.unit_cell.a, num=arr2.shape[0], endpoint=False)
z = numpy.linspace(0, ccp4.grid.unit_cell.c, num=arr2.shape[1], endpoint=False)
X, Z = numpy.meshgrid(x, z, indexing='ij')
pyplot.rcParams["figure.figsize"] = (4.0, 20.5)
pyplot.contour(X, Z, arr[:,:,0],500, zorder=1, linestyles='solid')
pyplot.gca().set_aspect('equal', adjustable='box')
pyplot.savefig('patterson.png', dpi=600)
pyplot.show()
"""

import numpy
from matplotlib import pyplot
import gemmi
# https://gemmi.readthedocs.io/en/latest/grid.html
ccp4 = gemmi.read_ccp4_map('/Users/blaine/4bqrPatterson.ccp4')
ccp4.setup()
arr = numpy.array(ccp4.grid, copy=False)
x = numpy.linspace(0, ccp4.grid.unit_cell.a, num=arr.shape[0], endpoint=False)
y = numpy.linspace(0, ccp4.grid.unit_cell.b, num=arr.shape[1], endpoint=False)
X, Y = numpy.meshgrid(x, y, indexing='ij')
pyplot.rcParams["figure.figsize"] = (8.0, 8.0)
pyplot.contour(X, Y, arr[:,:,0],500, zorder=1,linestyles='solid')
pyplot.gca().set_aspect('equal', adjustable='box')
pyplot.show()

arr2 = numpy.array(ccp4.grid, copy=False)
x = numpy.linspace(0, ccp4.grid.unit_cell.a, num=arr2.shape[0], endpoint=False)
z = numpy.linspace(0, ccp4.grid.unit_cell.c, num=arr2.shape[1], endpoint=False)
X, Z = numpy.meshgrid(x, z, indexing='ij')
pyplot.rcParams["figure.figsize"] = (4.0, 20.5)
pyplot.contour(X, Z, arr[:,:,0],500, zorder=1, linestyles='solid')
pyplot.gca().set_aspect('equal', adjustable='box')
pyplot.savefig('patterson.png', dpi=600)
pyplot.show()

# Description:  Read in a mtz file with iotbx.file_reader.
# Source:  NA

