import os
import compas

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
# Visualize the mesh and its block with the COMPAS viewer. 
# The collection allows displaying a list of objects as a group.
# ==============================================================================

viewer = App(viewmode='ghosted', show_grid=False, enable_propertyform=True)

viewer.add(cablemesh)

viewer.show()