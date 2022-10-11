import os
import compas
from compas.datastructures import mesh_thicken

from compas_occ.brep import BRep

from compas_view2.app import App

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
# Visualize the mesh and its block with the COMPAS viewer. 
# The collection allows displaying a list of objects as a group.
# ==============================================================================

viewer = App(viewmode='ghosted', show_grid=False, enable_propertyform=True)

viewer.add(shell_brep)

viewer.show()