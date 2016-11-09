from __future__ import division
from numpy import sqrt
import numpy
from euclid.FreudShape import ConvexPolyhedron

# Example:
# from euclid.FreudShape.RhombicDodecahedron import shape
points = [ 
          (-sqrt(2/3), -sqrt(2/3), 0),
          (-sqrt(2/3), 0, -(1/sqrt(3))),
          (-sqrt(2/3), 0, 1/sqrt(3)),
          (-sqrt(2/3), sqrt(2/3), 0),
          (0, -sqrt(2/3), -(1/sqrt(3))),
          (0, -sqrt(2/3), 1/sqrt(3)),
          (0, 0, -2/sqrt(3)),
          (0, 0, 2/sqrt(3)),
          (0, sqrt(2/3), -(1/sqrt(3))),
          (0, sqrt(2/3), 1/sqrt(3)),
          (sqrt(2/3), -sqrt(2/3), 0),
          (sqrt(2/3), 0, -(1/sqrt(3))),
          (sqrt(2/3), 0, 1/sqrt(3)),
          (sqrt(2/3), sqrt(2/3), 0),
         ]

shape = ConvexPolyhedron(numpy.array(points))