The format is based on `Keep a Changelog <http://keepachangelog.com/en/1.0.0/>`__.
This project adheres to `Semantic Versioning <http://semver.org/spec/v2.0.0.html>`__.

v0.3.0 - 2020-06-18
-------------------

Added
~~~~~

-  Calculation of circumsphere from center for convex polyhedra.
-  Simple name-based shape getter for damasceno SHAPES dictionary.
-  Polygons moment of inertia calculation.
-  Interoperability with the GSD shape specification.
-  Shape families and stored data for well-known families.
-  All shapes can be centered anywhere in 3D Euclidean space.
-  Extensive style checking using black, isort, and various other flake8
   plugins.
-  Make Circle area settable.
-  3D shapes can be oriented by their principal axes.
-  Make Sphere volume settable.

Changed
~~~~~~~

-  Inertia tensors for polyhedra and moments of inertia for polygons are
   calculated in global coordinates rather than the body frame.
-  Modified testing of convex hulls to generate points on ellipsoids to
   avoid degenerate simplices.
-  All insphere, circumsphere, and bounding sphere calculations now
   return the appropriate classes instead of tuples.

v0.2.0 - 2020-04-09
-------------------

Added
~~~~~

-  Continuous integrated testing on CircleCI.
-  New Polygon class with property-based API.
-  New ConvexSpheropolygon class with property-based API.
-  New Polyhedron class with property-based API and robust facet sorting
   and merging.
-  New ConvexPolyhedron class with property-based API.
-  New ConvexSpheropolyhedron class with property-based API.
-  Ability to plot Polyhedra and Polygons.
-  Can now check whether points lie inside a ConvexPolyhedron or
   ConvexSpheropolyhedron.
-  Added documentation.
-  New Ellipsoid class with property-based API.
-  New Sphere class with property-based API.
-  New Ellipse class with property-based API.
-  New Circle class with property-based API.
-  Added insphere from center calculation for convex polyhedra.
-  New ConvexPolygon class.
-  Documentation is hosted on ReadTheDocs.

Changed
~~~~~~~

-  Moved core shape classes from euclid.FreudShape into top-level
   package namespace.
-  Moved common shape definitions into common_shapes subpackage.
-  Shapes from Damasceno science 2012 paper are now stored in a JSON
   file that is loaded in the damasceno module.

Fixed
~~~~~

-  Formatting now properly follows PEP8.

Removed
~~~~~~~

-  Various unused or redundant functions in the utils module.
-  The quaternion_tools module (uses rowan for quaternion math instead).
-  The shapelib module.
-  Old polygon.py and polyhedron.py modules, which contained old
   implementations of various poly\* and spheropoly\* classes.

v0.1.0
------

-  Initial version of code base.
