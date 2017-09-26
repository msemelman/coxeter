from . import qt
from . import np

# Here some symmetry operators groups are defined
# They have been given the name of space groups,
# however they represent only the rotational analogs
# of these groups. This means that any operation involving
# an inversion or reflection was not included. Half the elements
# are built from the rotation operators, the other half are these
# same operators after a quaternion rotation by [-1,0,0,0]

# The elements are listed as (n-fold, axis) tuples, with
# angle = 2pi/n

# http://it.iucr.org/Ab/ch7o1v0001/sgtable7o1o225/
mbarThreem = [
            (1, [1,1,1]), #1
            (2, [0,0,1]),
            (2, [0,1,0]),
            (2, [1,0,0]),
            (3, [1,1,1]), #5
            (3, [-1,1,-1]),
            (3, [1,-1,-1]),
            (3, [-1,-1,1]),
            (-3, [1,1,1]), #9
            (-3, [1,-1,-1]),
            (-3, [-1,-1,1]),
            (-3, [-1,1,-1]),
            (2, [1,1,0]), #13
            (2, [1,-1,0]),
            (-4, [0,0,1]),
            (4, [0,0,1]),
            (-4, [1,0,0]), #17
            (2, [0,1,1]),
            (2, [0,1,-1]),
            (4, [1,0,0]),
            (4, [0,1,0]), #21
            (2, [1,0,1]),
            (-4, [0,1,0]),
            (2, [-1,0,1]),
            ]

# http://it.iucr.org/Ab/ch7o1v0001/sgtable7o1o209/
FourThreeTwo = mbarThreem[0:24]

# http://onlinelibrary.wiley.com/iucr/itc/Ab/ch7o1v0001/sgtable7o1o123/
Four_mmm = [
           (1, [1,0,0]),
           (2, [0,0,1]),
           (4, [0,0,1]),
           (-4, [0,0,1]),
           (2, [0,1,0]),
           (2, [1,0,0]),
           (2, [1,1,0]),
           (2, [1,-1,0])
           ]

# http://onlinelibrary.wiley.com/iucr/itc/Ab/ch7o1v0001/sgtable7o1o089/
FourTwoTwo = [
             (1, [1,0,0]),
             (2, [0,0,1]),
             (4, [0,0,1]),
             (-4, [0,0,1]),
             (2, [0,1,0]),
             (2, [1,0,0]),
             (2, [1,1,0]),
             (2, [1,-1,0])
             ]

# http://onlinelibrary.wiley.com/iucr/itc/Ab/ch7o1v0001/sgtable7o1o111/
barFourTwom = [
              (1, [1,0,0]),
              (2, [0,0,1]),
              (2, [0,1,0]),
              (2, [1,0,0])
              ]

# http://onlinelibrary.wiley.com/iucr/itc/Ab/ch7o1v0001/sgtable7o1o160/
Threem = [
         (1, [1,0,0]),
         (3, [0,0,1]),
         (-3, [0,0,1])
         ]

# http://onlinelibrary.wiley.com/iucr/itc/Ab/ch7o1v0001/sgtable7o1o025/
mmTwo = [
        (1, [1,0,0]),
        (2, [0,0,1])
        ]

# http://onlinelibrary.wiley.com/iucr/itc/Ab/ch7o1v0001/sgtable7o1o187/
# This group does not follow the definition exactly, the axis of
# the two fold axes have been modified
barSixmTwo = [
             (1, [1,0,0]),
             (3, [0,0,1]),
             (-3, [0,0,1]),
             (2, [1,0,0]),
             (2, [np.cos(np.pi/3),np.sin(np.pi/3),0]),
             (2, [-np.cos(np.pi/3),np.sin(np.pi/3),0])
             ]

# http://www-history.mcs.st-and.ac.uk/~john/geometry/Lectures/L10.html
# Generated by hand
# Some variables to clean up the icosohedral group
icodi = np.pi - np.arctan(2) # the dihedral angle
picodi = -np.pi/2 + np.arctan(2) # pi/2 - the dihedral angle
face1 = [np.cos(picodi),0,-np.sin(picodi)] # a face vector that will be used a lot
lat_edge = qt.qrotate(qt.build_quat(angle=icodi/2, axis=[0,1,0]),[0,0,1]) # the vector to the crown edges
crown_edge = qt.qrotate(qt.build_quat(angle=2*2*np.pi/5, axis=face1),lat_edge) # the vector to the mid-latitude edges
crown_vert = [-0.850651, 0. ,1.11352 ] # A vertex in the top pentagon
equi_vert = qt.qrotate(qt.build_quat(angle=1*2*np.pi/5, axis=face1), crown_vert)

Icosohedral = [
              (1, [1,0,0]),
              (5, [0,0,1]), # first face pair
              (5/2, [0,0,1]),
              (5/3, [0,0,1]),
              (5/4, [0,0,1]),
              (5, face1), # second face pair
              (5/2, face1),
              (5/3, face1),
              (5/4, face1),
              (5, qt.qrotate(qt.build_quat(angle=2*np.pi/5,axis=[0,0,1]), face1)), # third face pair
              (5/2, qt.qrotate(qt.build_quat(angle=2*np.pi/5,axis=[0,0,1]), face1)),
              (5/3, qt.qrotate(qt.build_quat(angle=2*np.pi/5,axis=[0,0,1]), face1)),
              (5/4, qt.qrotate(qt.build_quat(angle=2*np.pi/5,axis=[0,0,1]), face1)),
              (5, qt.qrotate(qt.build_quat(angle=2*2*np.pi/5,axis=[0,0,1]), face1)), # Fourth face pair
              (5/2, qt.qrotate(qt.build_quat(angle=2*2*np.pi/5,axis=[0,0,1]), face1)),
              (5/3, qt.qrotate(qt.build_quat(angle=2*2*np.pi/5,axis=[0,0,1]), face1)),
              (5/4, qt.qrotate(qt.build_quat(angle=2*2*np.pi/5,axis=[0,0,1]), face1)),
              (5, qt.qrotate(qt.build_quat(angle=3*2*np.pi/5,axis=[0,0,1]), face1)), # Fifth face pair
              (5/2, qt.qrotate(qt.build_quat(angle=3*2*np.pi/5,axis=[0,0,1]), face1)),
              (5/3, qt.qrotate(qt.build_quat(angle=3*2*np.pi/5,axis=[0,0,1]), face1)),
              (5/4, qt.qrotate(qt.build_quat(angle=3*2*np.pi/5,axis=[0,0,1]), face1)),
              (5, qt.qrotate(qt.build_quat(angle=4*2*np.pi/5,axis=[0,0,1]), face1)), # Sixth face pair
              (5/2, qt.qrotate(qt.build_quat(angle=4*2*np.pi/5,axis=[0,0,1]), face1)),
              (5/3, qt.qrotate(qt.build_quat(angle=4*2*np.pi/5,axis=[0,0,1]), face1)),
              (5/4, qt.qrotate(qt.build_quat(angle=4*2*np.pi/5,axis=[0,0,1]), face1)),
              (2, [0,1,0]), # equitorial band of edges
              (2, qt.qrotate(qt.build_quat(angle=1*2*np.pi/10,axis=[0,0,1]), [0,1,0])),
              (2, qt.qrotate(qt.build_quat(angle=2*2*np.pi/10,axis=[0,0,1]), [0,1,0])),
              (2, qt.qrotate(qt.build_quat(angle=3*2*np.pi/10,axis=[0,0,1]), [0,1,0])),
              (2, qt.qrotate(qt.build_quat(angle=4*2*np.pi/10,axis=[0,0,1]), [0,1,0])),
              (2, crown_edge), # the crown edges
              (2, qt.qrotate(qt.build_quat(angle=1*2*np.pi/5,axis=[0,0,1]), crown_edge)),
              (2, qt.qrotate(qt.build_quat(angle=2*2*np.pi/5,axis=[0,0,1]), crown_edge)),
              (2, qt.qrotate(qt.build_quat(angle=3*2*np.pi/5,axis=[0,0,1]), crown_edge)),
              (2, qt.qrotate(qt.build_quat(angle=4*2*np.pi/5,axis=[0,0,1]), crown_edge)),
              (2, lat_edge), # mid latitude edges
              (2, qt.qrotate(qt.build_quat(angle=1*2*np.pi/5,axis=[0,0,1]), lat_edge)),
              (2, qt.qrotate(qt.build_quat(angle=2*2*np.pi/5,axis=[0,0,1]), lat_edge)),
              (2, qt.qrotate(qt.build_quat(angle=3*2*np.pi/5,axis=[0,0,1]), lat_edge)),
              (2, qt.qrotate(qt.build_quat(angle=4*2*np.pi/5,axis=[0,0,1]), lat_edge)),
              (3, crown_vert), # The vertices in the top pentagon
              (-3, crown_vert),
              (3, qt.qrotate(qt.build_quat(angle=1*2*np.pi/5,axis=[0,0,1]), crown_vert)),
              (-3, qt.qrotate(qt.build_quat(angle=1*2*np.pi/5,axis=[0,0,1]), crown_vert)),
              (3, qt.qrotate(qt.build_quat(angle=2*2*np.pi/5,axis=[0,0,1]), crown_vert)),
              (-3, qt.qrotate(qt.build_quat(angle=2*2*np.pi/5,axis=[0,0,1]), crown_vert)),
              (3, qt.qrotate(qt.build_quat(angle=3*2*np.pi/5,axis=[0,0,1]), crown_vert)),
              (-3, qt.qrotate(qt.build_quat(angle=3*2*np.pi/5,axis=[0,0,1]), crown_vert)),
              (3, qt.qrotate(qt.build_quat(angle=4*2*np.pi/5,axis=[0,0,1]), crown_vert)),
              (-3, qt.qrotate(qt.build_quat(angle=4*2*np.pi/5,axis=[0,0,1]), crown_vert)),
              (3, equi_vert), # the equitorial vertices
              (-3, equi_vert),
              (3, qt.qrotate(qt.build_quat(angle=1*2*np.pi/5,axis=[0,0,1]),equi_vert)),
              (-3, qt.qrotate(qt.build_quat(angle=1*2*np.pi/5,axis=[0,0,1]),equi_vert)),
              (3, qt.qrotate(qt.build_quat(angle=2*2*np.pi/5,axis=[0,0,1]),equi_vert)),
              (-3, qt.qrotate(qt.build_quat(angle=2*2*np.pi/5,axis=[0,0,1]),equi_vert)),
              (3, qt.qrotate(qt.build_quat(angle=3*2*np.pi/5,axis=[0,0,1]),equi_vert)),
              (-3, qt.qrotate(qt.build_quat(angle=3*2*np.pi/5,axis=[0,0,1]),equi_vert)),
              (3, qt.qrotate(qt.build_quat(angle=4*2*np.pi/5,axis=[0,0,1]),equi_vert)),
              (-3, qt.qrotate(qt.build_quat(angle=4*2*np.pi/5,axis=[0,0,1]),equi_vert))
]

symgroups = {"m-3m":mbarThreem, "432":FourThreeTwo, "4_mmm":Four_mmm, "422":FourTwoTwo, "-42m":barFourTwom, "3m":Threem, "mm2":mmTwo,
        "-6m2":barSixmTwo, "icoso":Icosohedral}

# A function that generates the invariant quaternions from the above group definitions
def gen_sym_quats(group):
    operations = symgroups[group]
    quats = []
    for operation in operations:
        qtemp = qt.build_quat(axis=operation[1], angle=2*np.pi/operation[0])
        quats.append(qtemp.tolist())
        quats.append(qt.qproduct([-1,0,0,0], qtemp).tolist())

    return quats

# This is a json loadable string that has the quaternions that bring the shape definitions of Damsceno into alignment with the
# above symmetry definitions

DAMASCENO_FIX='{"J18": [1, 0, 0, 0], "A08": [1, 0, 0, 0], "O15": [0.7045564242640256, 0.4557687746359653, 0.060002041867676825, 0.540624476015312], "J45": [0.9569403357322088, 0.0, 0.0, 0.29028467725446233], "A12": [1, 0, 0, 0], "A01": [0.9238795325112867, -0.0, -0.0, 0.3826834323650897], "J61": [5.720154115573641e-17, 0.3568228725033438, 2.1849099433689207e-17, 0.9341720599859871], "J90": [0.19591344291270588, 0.6039888920172233, -0.18730394955680352, 0.7494882065024902], "J27": [1, 0, 0, 0], "C04": [0.9238795325112867, -0.0, -0.0, 0.3826834323650897], "C01": [0.9238795325112867, -0.0, -0.0, 0.3826834323650897], "J60": [0.1467739392257901, -0.3946011110748078, -0.7955911548080715, -0.4356398607724401], "J37": [0.9807852804032304, 0.0, 0.0, 0.19509032201612825], "P05": [1, 0, 0, 0], "P04": [1, 0, 0, 0]}'

# This is a json loadable string that has shapes in the proper orientations as well as their invariant quaternions

SYMSHAPES = '[{"Name": "Rhombic Dodecahedron", "ShortName": "C01", "vertices": [[-1.1547011310369448, 2.7755575615628914e-17, 0.0], [-0.5773505655184724, -0.5773499999999998, -0.5773505655184725], [-0.5773505655184724, 0.57735, -0.5773505655184723], [2.7755575615628914e-17, 2.7755575615628914e-16, -1.1547011310369448], [-0.5773505655184724, -0.5773500000000001, 0.5773505655184724], [-0.5773505655184724, 0.5773499999999998, 0.5773505655184725], [0.0, -1.1547, -1.6653345369377348e-16], [0.0, 1.1547, 1.6653345369377348e-16], [0.5773505655184724, -0.5773499999999998, -0.5773505655184725], [0.5773505655184724, 0.5773500000000001, -0.5773505655184724], [-2.7755575615628914e-17, -2.7755575615628914e-16, 1.1547011310369448], [0.5773505655184724, -0.57735, 0.5773505655184723], [0.5773505655184724, 0.5773499999999998, 0.5773505655184725], [1.1547011310369448, -2.7755575615628914e-17, 0.0]], "invariantQ": [[-1.0, 7.07050159149938e-17, 7.07050159149938e-17, 7.07050159149938e-17], [1.0, -7.07050159149938e-17, -7.07050159149938e-17, -7.07050159149938e-17], [6.123233995736766e-17, 0.0, 0.0, 1.0], [-6.123233995736766e-17, 0.0, 0.0, -1.0], [6.123233995736766e-17, 0.0, 1.0, 0.0], [-6.123233995736766e-17, 0.0, -1.0, 0.0], [6.123233995736766e-17, 1.0, 0.0, 0.0], [-6.123233995736766e-17, -1.0, 0.0, 0.0], [0.5000000000000001, 0.5, 0.5, 0.5], [-0.5000000000000001, -0.5, -0.5, -0.5], [0.5000000000000001, -0.5, 0.5, -0.5], [-0.5000000000000001, 0.5, -0.5, 0.5], [0.5000000000000001, 0.5, -0.5, -0.5], [-0.5000000000000001, -0.5, 0.5, 0.5], [0.5000000000000001, -0.5, -0.5, 0.5], [-0.5000000000000001, 0.5, 0.5, -0.5], [0.5000000000000001, -0.5, -0.5, -0.5], [-0.5000000000000001, 0.5, 0.5, 0.5], [0.5000000000000001, -0.5, 0.5, 0.5], [-0.5000000000000001, 0.5, -0.5, -0.5], [0.5000000000000001, 0.5, 0.5, -0.5], [-0.5000000000000001, -0.5, -0.5, 0.5], [0.5000000000000001, 0.5, -0.5, 0.5], [-0.5000000000000001, -0.5, 0.5, -0.5], [6.123233995736766e-17, 0.7071067811865475, 0.7071067811865475, 0.0], [-6.123233995736766e-17, -0.7071067811865475, -0.7071067811865475, 0.0], [6.123233995736766e-17, 0.7071067811865475, -0.7071067811865475, 0.0], [-6.123233995736766e-17, -0.7071067811865475, 0.7071067811865475, 0.0], [0.7071067811865476, -0.0, -0.0, -0.7071067811865475], [-0.7071067811865476, 0.0, 0.0, 0.7071067811865475], [0.7071067811865476, 0.0, 0.0, 0.7071067811865475], [-0.7071067811865476, 0.0, 0.0, -0.7071067811865475], [0.7071067811865476, -0.7071067811865475, -0.0, -0.0], [-0.7071067811865476, 0.7071067811865475, 0.0, 0.0], [6.123233995736766e-17, 0.0, 0.7071067811865475, 0.7071067811865475], [-6.123233995736766e-17, 0.0, -0.7071067811865475, -0.7071067811865475], [6.123233995736766e-17, 0.0, 0.7071067811865475, -0.7071067811865475], [-6.123233995736766e-17, 0.0, -0.7071067811865475, 0.7071067811865475], [0.7071067811865476, 0.7071067811865475, 0.0, 0.0], [-0.7071067811865476, -0.7071067811865475, 0.0, 0.0], [0.7071067811865476, 0.0, 0.7071067811865475, 0.0], [-0.7071067811865476, 0.0, -0.7071067811865475, 0.0], [6.123233995736766e-17, 0.7071067811865475, 0.0, 0.7071067811865475], [-6.123233995736766e-17, -0.7071067811865475, 0.0, -0.7071067811865475], [0.7071067811865476, -0.0, -0.7071067811865475, -0.0], [-0.7071067811865476, 0.0, 0.7071067811865475, 0.0], [6.123233995736766e-17, -0.7071067811865475, 0.0, 0.7071067811865475], [-6.123233995736766e-17, 0.7071067811865475, 0.0, -0.7071067811865475]], "symGroup": "m-3m"}, {"Name": "Rhombicuboctahedron", "ShortName": "A08", "vertices": [[-0.5, -0.5, -1.20711], [-0.5, -0.5, 1.20711], [-0.5, 0.5, -1.20711], [-0.5, 0.5, 1.20711], [-0.5, -1.20711, -0.5], [-0.5, -1.20711, 0.5], [-0.5, 1.20711, -0.5], [-0.5, 1.20711, 0.5], [0.5, -0.5, -1.20711], [0.5, -0.5, 1.20711], [0.5, 0.5, -1.20711], [0.5, 0.5, 1.20711], [0.5, -1.20711, -0.5], [0.5, -1.20711, 0.5], [0.5, 1.20711, -0.5], [0.5, 1.20711, 0.5], [-1.20711, -0.5, -0.5], [-1.20711, -0.5, 0.5], [-1.20711, 0.5, -0.5], [-1.20711, 0.5, 0.5], [1.20711, -0.5, -0.5], [1.20711, -0.5, 0.5], [1.20711, 0.5, -0.5], [1.20711, 0.5, 0.5]], "invariantQ": [[-1.0, 7.07050159149938e-17, 7.07050159149938e-17, 7.07050159149938e-17], [1.0, -7.07050159149938e-17, -7.07050159149938e-17, -7.07050159149938e-17], [6.123233995736766e-17, 0.0, 0.0, 1.0], [-6.123233995736766e-17, 0.0, 0.0, -1.0], [6.123233995736766e-17, 0.0, 1.0, 0.0], [-6.123233995736766e-17, 0.0, -1.0, 0.0], [6.123233995736766e-17, 1.0, 0.0, 0.0], [-6.123233995736766e-17, -1.0, 0.0, 0.0], [0.5000000000000001, 0.5, 0.5, 0.5], [-0.5000000000000001, -0.5, -0.5, -0.5], [0.5000000000000001, -0.5, 0.5, -0.5], [-0.5000000000000001, 0.5, -0.5, 0.5], [0.5000000000000001, 0.5, -0.5, -0.5], [-0.5000000000000001, -0.5, 0.5, 0.5], [0.5000000000000001, -0.5, -0.5, 0.5], [-0.5000000000000001, 0.5, 0.5, -0.5], [0.5000000000000001, -0.5, -0.5, -0.5], [-0.5000000000000001, 0.5, 0.5, 0.5], [0.5000000000000001, -0.5, 0.5, 0.5], [-0.5000000000000001, 0.5, -0.5, -0.5], [0.5000000000000001, 0.5, 0.5, -0.5], [-0.5000000000000001, -0.5, -0.5, 0.5], [0.5000000000000001, 0.5, -0.5, 0.5], [-0.5000000000000001, -0.5, 0.5, -0.5], [6.123233995736766e-17, 0.7071067811865475, 0.7071067811865475, 0.0], [-6.123233995736766e-17, -0.7071067811865475, -0.7071067811865475, 0.0], [6.123233995736766e-17, 0.7071067811865475, -0.7071067811865475, 0.0], [-6.123233995736766e-17, -0.7071067811865475, 0.7071067811865475, 0.0], [0.7071067811865476, -0.0, -0.0, -0.7071067811865475], [-0.7071067811865476, 0.0, 0.0, 0.7071067811865475], [0.7071067811865476, 0.0, 0.0, 0.7071067811865475], [-0.7071067811865476, 0.0, 0.0, -0.7071067811865475], [0.7071067811865476, -0.7071067811865475, -0.0, -0.0], [-0.7071067811865476, 0.7071067811865475, 0.0, 0.0], [6.123233995736766e-17, 0.0, 0.7071067811865475, 0.7071067811865475], [-6.123233995736766e-17, 0.0, -0.7071067811865475, -0.7071067811865475], [6.123233995736766e-17, 0.0, 0.7071067811865475, -0.7071067811865475], [-6.123233995736766e-17, 0.0, -0.7071067811865475, 0.7071067811865475], [0.7071067811865476, 0.7071067811865475, 0.0, 0.0], [-0.7071067811865476, -0.7071067811865475, 0.0, 0.0], [0.7071067811865476, 0.0, 0.7071067811865475, 0.0], [-0.7071067811865476, 0.0, -0.7071067811865475, 0.0], [6.123233995736766e-17, 0.7071067811865475, 0.0, 0.7071067811865475], [-6.123233995736766e-17, -0.7071067811865475, 0.0, -0.7071067811865475], [0.7071067811865476, -0.0, -0.7071067811865475, -0.0], [-0.7071067811865476, 0.0, 0.7071067811865475, 0.0], [6.123233995736766e-17, -0.7071067811865475, 0.0, 0.7071067811865475], [-6.123233995736766e-17, 0.7071067811865475, 0.0, -0.7071067811865475]], "symGroup": "m-3m"}, {"Name": "Cuboctahedron", "ShortName": "A01", "vertices": [[-0.7071067811865475, 1.1102230246251565e-16, -0.7071067811865475], [-0.7071067811865476, -0.7071069999999999, -1.1102230246251565e-16], [-0.7071067811865475, 0.707107, 1.1102230246251565e-16], [-1.434097586361965e-17, -0.7071069999999998, -0.7071067811865476], [0.0, 0.707107, -0.7071067811865474], [-0.7071067811865475, -1.1102230246251565e-16, 0.7071067811865475], [0.7071067811865475, 1.1102230246251565e-16, -0.7071067811865475], [0.0, -0.707107, 0.7071067811865474], [1.434097586361965e-17, 0.7071069999999998, 0.7071067811865476], [0.7071067811865475, -0.707107, -1.1102230246251565e-16], [0.7071067811865476, 0.7071069999999999, 1.1102230246251565e-16], [0.7071067811865475, -1.1102230246251565e-16, 0.7071067811865475]], "invariantQ": [[-1.0, 7.07050159149938e-17, 7.07050159149938e-17, 7.07050159149938e-17], [1.0, -7.07050159149938e-17, -7.07050159149938e-17, -7.07050159149938e-17], [6.123233995736766e-17, 0.0, 0.0, 1.0], [-6.123233995736766e-17, 0.0, 0.0, -1.0], [6.123233995736766e-17, 0.0, 1.0, 0.0], [-6.123233995736766e-17, 0.0, -1.0, 0.0], [6.123233995736766e-17, 1.0, 0.0, 0.0], [-6.123233995736766e-17, -1.0, 0.0, 0.0], [0.5000000000000001, 0.5, 0.5, 0.5], [-0.5000000000000001, -0.5, -0.5, -0.5], [0.5000000000000001, -0.5, 0.5, -0.5], [-0.5000000000000001, 0.5, -0.5, 0.5], [0.5000000000000001, 0.5, -0.5, -0.5], [-0.5000000000000001, -0.5, 0.5, 0.5], [0.5000000000000001, -0.5, -0.5, 0.5], [-0.5000000000000001, 0.5, 0.5, -0.5], [0.5000000000000001, -0.5, -0.5, -0.5], [-0.5000000000000001, 0.5, 0.5, 0.5], [0.5000000000000001, -0.5, 0.5, 0.5], [-0.5000000000000001, 0.5, -0.5, -0.5], [0.5000000000000001, 0.5, 0.5, -0.5], [-0.5000000000000001, -0.5, -0.5, 0.5], [0.5000000000000001, 0.5, -0.5, 0.5], [-0.5000000000000001, -0.5, 0.5, -0.5], [6.123233995736766e-17, 0.7071067811865475, 0.7071067811865475, 0.0], [-6.123233995736766e-17, -0.7071067811865475, -0.7071067811865475, 0.0], [6.123233995736766e-17, 0.7071067811865475, -0.7071067811865475, 0.0], [-6.123233995736766e-17, -0.7071067811865475, 0.7071067811865475, 0.0], [0.7071067811865476, -0.0, -0.0, -0.7071067811865475], [-0.7071067811865476, 0.0, 0.0, 0.7071067811865475], [0.7071067811865476, 0.0, 0.0, 0.7071067811865475], [-0.7071067811865476, 0.0, 0.0, -0.7071067811865475], [0.7071067811865476, -0.7071067811865475, -0.0, -0.0], [-0.7071067811865476, 0.7071067811865475, 0.0, 0.0], [6.123233995736766e-17, 0.0, 0.7071067811865475, 0.7071067811865475], [-6.123233995736766e-17, 0.0, -0.7071067811865475, -0.7071067811865475], [6.123233995736766e-17, 0.0, 0.7071067811865475, -0.7071067811865475], [-6.123233995736766e-17, 0.0, -0.7071067811865475, 0.7071067811865475], [0.7071067811865476, 0.7071067811865475, 0.0, 0.0], [-0.7071067811865476, -0.7071067811865475, 0.0, 0.0], [0.7071067811865476, 0.0, 0.7071067811865475, 0.0], [-0.7071067811865476, 0.0, -0.7071067811865475, 0.0], [6.123233995736766e-17, 0.7071067811865475, 0.0, 0.7071067811865475], [-6.123233995736766e-17, -0.7071067811865475, 0.0, -0.7071067811865475], [0.7071067811865476, -0.0, -0.7071067811865475, -0.0], [-0.7071067811865476, 0.0, 0.7071067811865475, 0.0], [6.123233995736766e-17, -0.7071067811865475, 0.0, 0.7071067811865475], [-6.123233995736766e-17, 0.7071067811865475, 0.0, -0.7071067811865475]], "symGroup": "m-3m"}, {"Name": "Snub Cuboctahedron", "ShortName": "A12", "vertices": [[-1.14261, -0.337754, -0.621226], [-1.14261, 0.337754, 0.621226], [-1.14261, -0.621226, 0.337754], [-1.14261, 0.621226, -0.337754], [1.14261, -0.337754, 0.621226], [1.14261, 0.337754, -0.621226], [1.14261, -0.621226, -0.337754], [1.14261, 0.621226, 0.337754], [-0.337754, -1.14261, 0.621226], [-0.337754, 1.14261, -0.621226], [-0.337754, -0.621226, -1.14261], [-0.337754, 0.621226, 1.14261], [0.337754, -1.14261, -0.621226], [0.337754, 1.14261, 0.621226], [0.337754, -0.621226, 1.14261], [0.337754, 0.621226, -1.14261], [-0.621226, -1.14261, -0.337754], [-0.621226, 1.14261, 0.337754], [-0.621226, -0.337754, 1.14261], [-0.621226, 0.337754, -1.14261], [0.621226, -1.14261, 0.337754], [0.621226, 1.14261, -0.337754], [0.621226, -0.337754, -1.14261], [0.621226, 0.337754, 1.14261]], "invariantQ": [[-1.0, 7.07050159149938e-17, 7.07050159149938e-17, 7.07050159149938e-17], [1.0, -7.07050159149938e-17, -7.07050159149938e-17, -7.07050159149938e-17], [6.123233995736766e-17, 0.0, 0.0, 1.0], [-6.123233995736766e-17, 0.0, 0.0, -1.0], [6.123233995736766e-17, 0.0, 1.0, 0.0], [-6.123233995736766e-17, 0.0, -1.0, 0.0], [6.123233995736766e-17, 1.0, 0.0, 0.0], [-6.123233995736766e-17, -1.0, 0.0, 0.0], [0.5000000000000001, 0.5, 0.5, 0.5], [-0.5000000000000001, -0.5, -0.5, -0.5], [0.5000000000000001, -0.5, 0.5, -0.5], [-0.5000000000000001, 0.5, -0.5, 0.5], [0.5000000000000001, 0.5, -0.5, -0.5], [-0.5000000000000001, -0.5, 0.5, 0.5], [0.5000000000000001, -0.5, -0.5, 0.5], [-0.5000000000000001, 0.5, 0.5, -0.5], [0.5000000000000001, -0.5, -0.5, -0.5], [-0.5000000000000001, 0.5, 0.5, 0.5], [0.5000000000000001, -0.5, 0.5, 0.5], [-0.5000000000000001, 0.5, -0.5, -0.5], [0.5000000000000001, 0.5, 0.5, -0.5], [-0.5000000000000001, -0.5, -0.5, 0.5], [0.5000000000000001, 0.5, -0.5, 0.5], [-0.5000000000000001, -0.5, 0.5, -0.5], [6.123233995736766e-17, 0.7071067811865475, 0.7071067811865475, 0.0], [-6.123233995736766e-17, -0.7071067811865475, -0.7071067811865475, 0.0], [6.123233995736766e-17, 0.7071067811865475, -0.7071067811865475, 0.0], [-6.123233995736766e-17, -0.7071067811865475, 0.7071067811865475, 0.0], [0.7071067811865476, -0.0, -0.0, -0.7071067811865475], [-0.7071067811865476, 0.0, 0.0, 0.7071067811865475], [0.7071067811865476, 0.0, 0.0, 0.7071067811865475], [-0.7071067811865476, 0.0, 0.0, -0.7071067811865475], [0.7071067811865476, -0.7071067811865475, -0.0, -0.0], [-0.7071067811865476, 0.7071067811865475, 0.0, 0.0], [6.123233995736766e-17, 0.0, 0.7071067811865475, 0.7071067811865475], [-6.123233995736766e-17, 0.0, -0.7071067811865475, -0.7071067811865475], [6.123233995736766e-17, 0.0, 0.7071067811865475, -0.7071067811865475], [-6.123233995736766e-17, 0.0, -0.7071067811865475, 0.7071067811865475], [0.7071067811865476, 0.7071067811865475, 0.0, 0.0], [-0.7071067811865476, -0.7071067811865475, 0.0, 0.0], [0.7071067811865476, 0.0, 0.7071067811865475, 0.0], [-0.7071067811865476, 0.0, -0.7071067811865475, 0.0], [6.123233995736766e-17, 0.7071067811865475, 0.0, 0.7071067811865475], [-6.123233995736766e-17, -0.7071067811865475, 0.0, -0.7071067811865475], [0.7071067811865476, -0.0, -0.7071067811865475, -0.0], [-0.7071067811865476, 0.0, 0.7071067811865475, 0.0], [6.123233995736766e-17, -0.7071067811865475, 0.0, 0.7071067811865475], [-6.123233995736766e-17, 0.7071067811865475, 0.0, -0.7071067811865475]], "symGroup": "432"}, {"Name": "Tetrakis Hexahedron", "ShortName": "C04", "vertices": [[-0.6666666372637077, -0.6666669999999999, -0.6666666372637078], [-0.6666666372637077, 0.6666670000000001, -0.6666666372637076], [-1.000000309448952, 8.326672684688674e-17, 0.0], [-2.7755575615628914e-17, 2.220446049250313e-16, -1.0000003094489522], [-0.6666666372637076, -0.666667, 0.6666666372637075], [-0.6666666372637076, 0.6666669999999999, 0.6666666372637078], [0.0, -1.0, -2.220446049250313e-16], [0.0, 1.0, 2.220446049250313e-16], [0.6666666372637076, -0.6666669999999999, -0.6666666372637078], [0.6666666372637076, 0.666667, -0.6666666372637075], [2.7755575615628914e-17, -2.220446049250313e-16, 1.0000003094489522], [1.000000309448952, -8.326672684688674e-17, 0.0], [0.6666666372637077, -0.6666670000000001, 0.6666666372637076], [0.6666666372637077, 0.6666669999999999, 0.6666666372637078]], "invariantQ": [[-1.0, 7.07050159149938e-17, 7.07050159149938e-17, 7.07050159149938e-17], [1.0, -7.07050159149938e-17, -7.07050159149938e-17, -7.07050159149938e-17], [6.123233995736766e-17, 0.0, 0.0, 1.0], [-6.123233995736766e-17, 0.0, 0.0, -1.0], [6.123233995736766e-17, 0.0, 1.0, 0.0], [-6.123233995736766e-17, 0.0, -1.0, 0.0], [6.123233995736766e-17, 1.0, 0.0, 0.0], [-6.123233995736766e-17, -1.0, 0.0, 0.0], [0.5000000000000001, 0.5, 0.5, 0.5], [-0.5000000000000001, -0.5, -0.5, -0.5], [0.5000000000000001, -0.5, 0.5, -0.5], [-0.5000000000000001, 0.5, -0.5, 0.5], [0.5000000000000001, 0.5, -0.5, -0.5], [-0.5000000000000001, -0.5, 0.5, 0.5], [0.5000000000000001, -0.5, -0.5, 0.5], [-0.5000000000000001, 0.5, 0.5, -0.5], [0.5000000000000001, -0.5, -0.5, -0.5], [-0.5000000000000001, 0.5, 0.5, 0.5], [0.5000000000000001, -0.5, 0.5, 0.5], [-0.5000000000000001, 0.5, -0.5, -0.5], [0.5000000000000001, 0.5, 0.5, -0.5], [-0.5000000000000001, -0.5, -0.5, 0.5], [0.5000000000000001, 0.5, -0.5, 0.5], [-0.5000000000000001, -0.5, 0.5, -0.5], [6.123233995736766e-17, 0.7071067811865475, 0.7071067811865475, 0.0], [-6.123233995736766e-17, -0.7071067811865475, -0.7071067811865475, 0.0], [6.123233995736766e-17, 0.7071067811865475, -0.7071067811865475, 0.0], [-6.123233995736766e-17, -0.7071067811865475, 0.7071067811865475, 0.0], [0.7071067811865476, -0.0, -0.0, -0.7071067811865475], [-0.7071067811865476, 0.0, 0.0, 0.7071067811865475], [0.7071067811865476, 0.0, 0.0, 0.7071067811865475], [-0.7071067811865476, 0.0, 0.0, -0.7071067811865475], [0.7071067811865476, -0.7071067811865475, -0.0, -0.0], [-0.7071067811865476, 0.7071067811865475, 0.0, 0.0], [6.123233995736766e-17, 0.0, 0.7071067811865475, 0.7071067811865475], [-6.123233995736766e-17, 0.0, -0.7071067811865475, -0.7071067811865475], [6.123233995736766e-17, 0.0, 0.7071067811865475, -0.7071067811865475], [-6.123233995736766e-17, 0.0, -0.7071067811865475, 0.7071067811865475], [0.7071067811865476, 0.7071067811865475, 0.0, 0.0], [-0.7071067811865476, -0.7071067811865475, 0.0, 0.0], [0.7071067811865476, 0.0, 0.7071067811865475, 0.0], [-0.7071067811865476, 0.0, -0.7071067811865475, 0.0], [6.123233995736766e-17, 0.7071067811865475, 0.0, 0.7071067811865475], [-6.123233995736766e-17, -0.7071067811865475, 0.0, -0.7071067811865475], [0.7071067811865476, -0.0, -0.7071067811865475, -0.0], [-0.7071067811865476, 0.0, 0.7071067811865475, 0.0], [6.123233995736766e-17, -0.7071067811865475, 0.0, 0.7071067811865475], [-6.123233995736766e-17, 0.7071067811865475, 0.0, -0.7071067811865475]], "symGroup": "m-3m"}, {"Name": "Elongated Square Gyrobicupola", "ShortName": "J37", "vertices": [[-0.6532814824381883, 0.27059805007309845, -1.2071099999999997], [0.27059805007309845, 0.6532814824381883, -1.2071099999999997], [-0.6532816845954584, -0.2705981338093816, 1.2071099999999997], [0.6532816845954584, 0.2705981338093816, 1.2071099999999997], [-0.27059805007309845, -0.6532814824381883, -1.2071099999999997], [0.6532814824381883, -0.27059805007309845, -1.2071099999999997], [-0.2705981338093816, 0.6532816845954584, 1.2071099999999997], [0.2705981338093816, -0.6532816845954584, 1.2071099999999997], [1.3065659386722441, 1.2317865800692829e-06, -0.5], [1.3065659386722441, 1.2317865800692829e-06, 0.5], [0.9238825063071543, 0.9238807642978668, -0.5], [0.9238825063071543, 0.9238807642978668, 0.5], [-1.2317865800692829e-06, 1.3065659386722441, -0.5], [-1.2317865800692829e-06, 1.3065659386722441, 0.5], [-0.9238807642978668, 0.9238825063071543, -0.5], [-0.9238807642978668, 0.9238825063071543, 0.5], [-1.3065659386722441, -1.2317865800692829e-06, -0.5], [-1.3065659386722441, -1.2317865800692829e-06, 0.5], [-0.9238825063071543, -0.9238807642978668, -0.5], [-0.9238825063071543, -0.9238807642978668, 0.5], [1.2317865800692829e-06, -1.3065659386722441, -0.5], [1.2317865800692829e-06, -1.3065659386722441, 0.5], [0.9238807642978668, -0.9238825063071543, -0.5], [0.9238807642978668, -0.9238825063071543, 0.5]], "invariantQ": [[-1.0, 1.2246467991473532e-16, 0.0, 0.0], [1.0, -1.2246467991473532e-16, 0.0, 0.0], [6.123233995736766e-17, 0.0, 0.0, 1.0], [-6.123233995736766e-17, 0.0, 0.0, -1.0], [0.7071067811865476, 0.0, 0.0, 0.7071067811865475], [-0.7071067811865476, 0.0, 0.0, -0.7071067811865475], [0.7071067811865476, -0.0, -0.0, -0.7071067811865475], [-0.7071067811865476, 0.0, 0.0, 0.7071067811865475], [6.123233995736766e-17, 0.0, 1.0, 0.0], [-6.123233995736766e-17, 0.0, -1.0, 0.0], [6.123233995736766e-17, 1.0, 0.0, 0.0], [-6.123233995736766e-17, -1.0, 0.0, 0.0], [6.123233995736766e-17, 0.7071067811865475, 0.7071067811865475, 0.0], [-6.123233995736766e-17, -0.7071067811865475, -0.7071067811865475, 0.0], [6.123233995736766e-17, 0.7071067811865475, -0.7071067811865475, 0.0], [-6.123233995736766e-17, -0.7071067811865475, 0.7071067811865475, 0.0]], "symGroup": "4_mmm"}, {"Name": "Gyroelongated Square Bicupola", "ShortName": "J45", "vertices": [[-0.39284760075979186, -0.5879379831464158, -1.13725], [0.39284760075979186, 0.5879379831464158, -1.13725], [-0.7258858436540914, -1.0863649366500132, 0.4301479999999999], [0.7258858436540914, 1.0863649366500132, 0.4301479999999999], [-0.5879379831464158, 0.39284760075979186, -1.13725], [0.5879379831464158, -0.39284760075979186, -1.13725], [-0.39284710587998073, 0.5879374915471228, 1.13725], [0.39284710587998073, -0.5879374915471228, 1.13725], [1.2814604002163266, -0.2548995778290194, -0.4301479999999999], [-1.0863649366500132, 0.7258858436540914, 0.4301479999999999], [1.0863649366500132, -0.7258858436540914, 0.4301479999999999], [-1.2814583722962256, -0.2548979185319254, 0.4301479999999999], [-0.2548979185319254, 1.2814583722962256, 0.4301479999999999], [0.2548979185319254, -1.2814583722962256, 0.4301479999999999], [1.2814583722962256, 0.2548979185319254, 0.4301479999999999], [-1.0863691901315646, -0.7258901671967242, -0.4301479999999999], [1.0863691901315646, 0.7258901671967242, -0.4301479999999999], [-0.2548995778290194, -1.2814604002163266, -0.4301479999999999], [0.2548995778290194, 1.2814604002163266, -0.4301479999999999], [0.7258901671967242, -1.0863691901315646, -0.4301479999999999], [-0.7258901671967242, 1.0863691901315646, -0.4301479999999999], [-1.2814604002163266, 0.2548995778290194, -0.4301479999999999], [-0.5879374915471228, -0.39284710587998073, 1.13725], [0.5879374915471228, 0.39284710587998073, 1.13725]], "invariantQ": [[-1.0, 1.2246467991473532e-16, 0.0, 0.0], [1.0, -1.2246467991473532e-16, 0.0, 0.0], [6.123233995736766e-17, 0.0, 0.0, 1.0], [-6.123233995736766e-17, 0.0, 0.0, -1.0], [0.7071067811865476, 0.0, 0.0, 0.7071067811865475], [-0.7071067811865476, 0.0, 0.0, -0.7071067811865475], [0.7071067811865476, -0.0, -0.0, -0.7071067811865475], [-0.7071067811865476, 0.0, 0.0, 0.7071067811865475], [6.123233995736766e-17, 0.0, 1.0, 0.0], [-6.123233995736766e-17, 0.0, -1.0, 0.0], [6.123233995736766e-17, 1.0, 0.0, 0.0], [-6.123233995736766e-17, -1.0, 0.0, 0.0], [6.123233995736766e-17, 0.7071067811865475, 0.7071067811865475, 0.0], [-6.123233995736766e-17, -0.7071067811865475, -0.7071067811865475, 0.0], [6.123233995736766e-17, 0.7071067811865475, -0.7071067811865475, 0.0], [-6.123233995736766e-17, -0.7071067811865475, 0.7071067811865475, 0.0]], "symGroup": "422"}, {"Name": "Triangular Orthobicupola", "ShortName": "J27", "vertices": [[0.0, -1.0, 0.0], [0.0, 1.0, 0.0], [-0.288675, -0.5, -0.816497], [-0.288675, -0.5, 0.816497], [-0.288675, 0.5, -0.816497], [-0.288675, 0.5, 0.816497], [0.57735, 0.0, -0.816497], [0.57735, 0.0, 0.816497], [-0.866025, -0.5, 0.0], [-0.866025, 0.5, 0.0], [0.866025, -0.5, 0.0], [0.866025, 0.5, 0.0]], "invariantQ": [[-1.0, 1.2246467991473532e-16, 0.0, 0.0], [1.0, -1.2246467991473532e-16, 0.0, 0.0], [0.5000000000000001, 0.0, 0.0, 0.8660254037844386], [-0.5000000000000001, 0.0, 0.0, -0.8660254037844386], [0.5000000000000001, -0.0, -0.0, -0.8660254037844386], [-0.5000000000000001, 0.0, 0.0, 0.8660254037844386], [6.123233995736766e-17, 1.0, 0.0, 0.0], [-6.123233995736766e-17, -1.0, 0.0, 0.0], [6.123233995736766e-17, 0.5000000000000001, 0.8660254037844386, 0.0], [-6.123233995736766e-17, -0.5000000000000001, -0.8660254037844386, 0.0], [6.123233995736766e-17, -0.5000000000000001, 0.8660254037844386, 0.0], [-6.123233995736766e-17, 0.5000000000000001, -0.8660254037844386, 0.0]], "symGroup": "-6m2"}, {"Name": "Disphenocingulum", "ShortName": "J90", "vertices": [[0.35355601067474907, 0.3535516520557829, -1.104432684890909], [0.7965444780135226, 0.7965417080286229, -0.3249983748890818], [-0.18888844101392216, 0.8959966828939351, -0.46294680405955757], [-0.35355134445029374, -0.35355166835769564, -1.1044398333351966], [0.8959974782871691, -0.1888909639845683, -0.4629443493338358], [-0.8959956111502988, 0.1888914945377682, -0.4629502689498131], [0.18888787050894587, 0.8959953189264307, 0.462947544045344], [-0.796544205629287, 0.7965441058194818, 0.325001085416781], [0.18888920475525983, -0.8959957190578602, -0.4629473194673348], [0.8959945563859366, 0.18888938635067853, 0.4629486551073039], [-0.7965441383314684, -0.7965421279138671, -0.3250052836393526], [0.7965421061481694, -0.7965443197479932, 0.3250017962980476], [-0.8959971279738894, -0.18889007893733817, 0.4629451258318339], [-0.35355308668715957, 0.35355417273804174, 1.1044361680318455], [-0.18889083571971202, -0.8959954651213813, 0.46294528478183583], [0.3535530866871597, -0.353554172738042, 1.104439257793885]], "invariantQ": [[-1.0, 1.2246467991473532e-16, 0.0, 0.0], [1.0, -1.2246467991473532e-16, 0.0, 0.0], [6.123233995736766e-17, 0.0, 0.0, 1.0], [-6.123233995736766e-17, 0.0, 0.0, -1.0], [6.123233995736766e-17, 0.0, 1.0, 0.0], [-6.123233995736766e-17, 0.0, -1.0, 0.0], [6.123233995736766e-17, 1.0, 0.0, 0.0], [-6.123233995736766e-17, -1.0, 0.0, 0.0]], "symGroup": "-42m"}, {"Name": "Triaugmented Dodecahedron", "ShortName": "J61", "vertices": [[0.9341748529796053, 1.144034243545423e-16, 1.004325725425985], [-0.9341753141647604, -1.1440348083343469e-16, -1.0845462197472033], [0.17841151082603823, 1.30902, 0.42697546964196753], [0.17841151082603857, -1.30902, 0.42697546964196753], [-1.044439695772282, 0.8090169999999998, -0.5071974430578344], [-1.044439695772282, -0.8090170000000002, -0.5071974430578344], [-0.46708742648980284, 0.809017, 1.0043292180190952], [-0.4670874264898026, -0.809017, 1.0043292180190952], [1.222848228767508, 0.5000000000000002, -0.5072002805981312], [1.222848228767508, -0.4999999999999999, -0.5072002805981312], [-1.222848689952663, 0.4999999999999999, 0.42697978627691274], [-1.222848689952663, -0.5000000000000002, 0.42697978627691274], [-5.213895438560545e-06, -6.385180359922157e-22, -1.441371193294186], [1.0444392345871267, 0.8090170000000002, 0.42697694873661596], [1.0444392345871267, -0.8090169999999998, 0.42697694873661596], [4.75271028338442e-06, 5.820391435821441e-22, 1.3611506989729676], [0.46708696530464744, 0.809017, -1.0845497123403136], [0.46708696530464766, -0.809017, -1.0845497123403136], [1.6101493334317312, 1.971864227336414e-16, 0.26740091799819954], [-0.17841197201119366, 1.30902, -0.5071959639631859], [-0.17841197201119333, -1.30902, -0.5071959639631859], [-0.8050723668895453, -1.3944299999999998, 0.2674020140376014], [-0.8050723668895458, 1.3944299999999998, 0.2674020140376014]], "invariantQ": [[-1.0, 1.2246467991473532e-16, 0.0, 0.0], [1.0, -1.2246467991473532e-16, 0.0, 0.0], [0.5000000000000001, 0.0, 0.0, 0.8660254037844386], [-0.5000000000000001, 0.0, 0.0, -0.8660254037844386], [0.5000000000000001, -0.0, -0.0, -0.8660254037844386], [-0.5000000000000001, 0.0, 0.0, 0.8660254037844386]], "symGroup": "3m"}, {"Name": "Metabiaugmented Dodecahedron", "ShortName": "J60", "vertices": [[0.809020263100338, 0.809014770920135, -0.7306723621609981], [-0.809020381049436, -0.8090148846798465, 0.8873643672980063], [-0.500001872529516, -1.1375971167848498e-07, -1.2306732345547478], [0.8090211392595555, 0.8090154795571065, 0.887365000694301], [-1.3090206159641702, -0.499997989532927, 0.0783484999109888], [-0.5000017545804181, -5.551115123125783e-17, 1.387365122244093], [-0.8090169682739694, 0.8090217652662582, -0.7306707358516563], [1.893109782657998e-06, 1.3090197547991853, 0.5783458864814476], [0.8090156739702739, -0.8090220595484701, -0.7306709298512174], [1.3090168243686908, -0.5000063098590772, 0.07834582896417461], [-1.3090169423177889, 0.5000061960993655, 0.07834617617283365], [-0.8090157919193716, 0.8090219457887583, 0.8873629349882258], [-6.505952075075427e-06, -1.309018595078542, 0.5783487083557945], [0.50000163663132, -1.1375971159521825e-07, -1.2306731171070844], [1.3090204980150724, 0.4999978757732155, 0.0783435052260198], [6.3880029770313485e-06, 1.3090184813188306, -0.42165670321878623], [-2.011058880757588e-06, -1.3090198685588967, -0.42165388134443926], [0.8090168503248716, -0.8090218790259699, 0.8873627409886647], [1.3944297656490652, -2.4180643696247728e-06, -0.7834603558552322], [-0.8090212572086535, -0.8090155933168179, -0.7306729955572926], [0.5000017545804181, 5.551115123125783e-17, 1.3873652396917564], [-1.3944285825945202, 3.5500535754962037e-06, -0.7834596906309649]], "invariantQ": [[-1.0, 1.2246467991473532e-16, 0.0, 0.0], [1.0, -1.2246467991473532e-16, 0.0, 0.0], [6.123233995736766e-17, 0.0, 0.0, 1.0], [-6.123233995736766e-17, 0.0, 0.0, -1.0]], "symGroup": "mm2"}, {"Name": "Squashed Dodecahedron", "ShortName": "O15", "vertices": [[-0.7071091731492744, 1.2247443003541598, -0.999998227589546], [-1.414214263818451, -3.3306690738754696e-16, -0.4999965362176715], [-4.082480096722562e-06, -1.0072534643921875e-16, -1.4999999189614197], [0.707105090667494, 1.2247443003541598, -0.5000023097140125], [-0.7071037298447225, 1.2247443003541598, 1.0000008399028295], [-1.4142156246412232, -3.3306690738754696e-16, 0.5000058842909731], [0.7071098535690792, 1.224747835888066, 0.5000001107779655], [-0.7071091731492739, -1.2247443003541603, -0.9999982275895456], [1.4142101813366716, 3.3306690738754696e-16, -1.0000040010858866], [4.082476730845547e-06, 1.3692414647307853e-16, 1.4999986822771434], [0.7071050906674945, -1.2247443003541596, -0.5000023097140124], [-0.7071037298447219, -1.22474430035416, 1.0000008399028297], [1.4142156246412232, 3.3306690738754696e-16, 0.9999950664064888], [0.7071098535690793, -1.2247478358880657, 0.5000001107779657]], "invariantQ": [[-1.0, 1.2246467991473532e-16, 0.0, 0.0], [1.0, -1.2246467991473532e-16, 0.0, 0.0], [0.5000000000000001, 0.0, 0.0, 0.8660254037844386], [-0.5000000000000001, 0.0, 0.0, -0.8660254037844386], [0.5000000000000001, -0.0, -0.0, -0.8660254037844386], [-0.5000000000000001, 0.0, 0.0, 0.8660254037844386], [6.123233995736766e-17, 1.0, 0.0, 0.0], [-6.123233995736766e-17, -1.0, 0.0, 0.0], [6.123233995736766e-17, 0.5000000000000001, 0.8660254037844386, 0.0], [-6.123233995736766e-17, -0.5000000000000001, -0.8660254037844386, 0.0], [6.123233995736766e-17, -0.5000000000000001, 0.8660254037844386, 0.0], [-6.123233995736766e-17, 0.5000000000000001, -0.8660254037844386, 0.0]], "symGroup": "-6m2"}, {"Name": "Elongated Triangular Cupola", "ShortName": "J18", "vertices": [[0.0, -1.0, -0.7632994], [0.0, -1.0, 0.2367006], [0.0, 1.0, -0.7632994], [0.0, 1.0, 0.2367006], [-0.288675, -0.5, 1.0531976], [-0.288675, 0.5, 1.0531976], [0.57735, 0.0, 1.0531976], [-0.866025, -0.5, -0.7632994], [-0.866025, -0.5, 0.2367006], [-0.866025, 0.5, -0.7632994], [-0.866025, 0.5, 0.2367006], [0.866025, -0.5, -0.7632994], [0.866025, -0.5, 0.2367006], [0.866025, 0.5, -0.7632994], [0.866025, 0.5, 0.2367006]], "invariantQ": [[-1.0, 1.2246467991473532e-16, 0.0, 0.0], [1.0, -1.2246467991473532e-16, 0.0, 0.0], [0.5000000000000001, 0.0, 0.0, 0.8660254037844386], [-0.5000000000000001, 0.0, 0.0, -0.8660254037844386], [0.5000000000000001, -0.0, -0.0, -0.8660254037844386], [-0.5000000000000001, 0.0, 0.0, 0.8660254037844386]], "symGroup": "3m"}]'
