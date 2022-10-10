import compas
from compas.datastructures import Mesh

mesh = Mesh.from_obj(compas.get("tubesmesh.obj"))

print(mesh.default_vertex_attributes)
print(mesh.default_edge_attributes)
print(mesh.default_face_attributes)
