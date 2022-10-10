import os
import compas
from compas.datastructures import Mesh

FILE = os.path.join(os.path.dirname(__file__), 'session.json')


session = compas.json_load(FILE)

mesh: Mesh = session['mesh']
dual = session['dual']
frames = session['frames']
model = session['model']

# mesh.data

print(mesh.guid)
print(mesh.name)
print(mesh.dtype)

print(mesh.default_vertex_attributes)
print(mesh.default_edge_attributes)
print(mesh.default_face_attributes)
