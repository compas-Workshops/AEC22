import os
import compas
from compas.datastructures import Mesh
from compas.datastructures import mesh_thicken
from compas.geometry import add_vectors
from compas.geometry import scale_vector
from compas.geometry import offset_polygon
from compas.geometry import intersection_line_plane

from compas_occ.brep import BRep
from OCC.Core.TopoDS import TopoDS_Compound
from OCC.Core.BRep import BRep_Builder

from compas_view2.app import App
from compas_view2.objects import Collection

# ==============================================================================
# Set the path to the input file.
# The input file was generated with `Export` which serialises the cablemesh
# data structure to a JSON file. It must be stored in the data folder.
# ==============================================================================

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'CableMesh.json')

# ==============================================================================
# Load the cablemesh.
# ==============================================================================

cablemesh = compas.json_load(FILE)

for vertex in cablemesh.vertices():
    cablemesh.unset_vertex_attribute(vertex, 'constraint')

# ==============================================================================
# Set the value of the thickness of the foam blocks in [m].
# Set the value of the offset distance for the edges of the faces to create space
# for the ribs.
# ==============================================================================

THICKNESS = 0.10
THICKNESS_BOX = 0.07
OFFSET = 0.03

# ==============================================================================
# Create a thickened shell mesh without cavities yet.
# ==============================================================================

shell_mesh = mesh_thicken(cablemesh, thickness=THICKNESS, both=False)

# ==============================================================================
# Convert to a BRep.
# ==============================================================================

shell_brep = BRep.from_mesh(shell_mesh)
shell_brep.sew()
shell_brep.fix()
shell_brep.make_solid()

# ==============================================================================
# Generate the formwork blocks.
# ==============================================================================

compound = TopoDS_Compound()
builder = BRep_Builder()
builder.MakeCompound(compound)
for fkey in cablemesh.faces():

    # get the point coordinates for all vertices of current face.
    vertices = cablemesh.face_vertices(fkey)
    points = cablemesh.vertices_attributes('xyz', keys=vertices)

    # offset edges of the bottom face polygon to create space for the ribs.
    bottom = offset_polygon(points, OFFSET) 

    # define the 2 planes perpendicular to the face normal 
    # placed at a distances along the face normal from the face centroid.
    origin = cablemesh.face_centroid(fkey)
    normal = cablemesh.face_normal(fkey, unitized=True)
    plane = add_vectors(origin, scale_vector(normal, THICKNESS_BOX)), normal
    
    # the vertices of the top face are the intersection points of the face normal
    # placed at each (offset) bottom vertex and the previously constructed plane.
    top = []
    for a in bottom:
        b = add_vectors(a, normal)
        line = a, b
        intersection = intersection_line_plane(line, plane)
        top.append(intersection)

    # offset top polygon to create tapering of blocks
    top[:] = offset_polygon(top, OFFSET)

    # The vertices of the block mesh are simply the vertices of the bottom and top
    # faces. The faces themselves are defined such that once the block is formed
    # all face normals point towards the exterior of the block.
    vertices = bottom + top
    faces = [[0, 3, 2, 1], [4, 5, 6, 7], [3, 0, 4, 7], [2, 3, 7, 6], [1, 2, 6, 5], [0, 1, 5, 4]]

    # Generate the mesh represeting the block.
    block = Mesh.from_vertices_and_faces(vertices, faces)

    # Convert to solid BRep and add to compound.
    brep = BRep.from_mesh(block)
    brep.sew()
    brep.fix()
    brep.make_solid()
    builder.Add(compound, brep.occ_shape)

# Create one BRep form compund of all blocks. 
blocks_brep = BRep.from_shape(compound)

# ==============================================================================
# Visualize the mesh and its block with the COMPAS viewer. 
# The collection allows displaying a list of objects as a group.
# ==============================================================================

viewer = App(viewmode='ghosted', show_grid=False, enable_propertyform=True)

viewer.add(cablemesh)
viewer.add(blocks_brep)

viewer.show()