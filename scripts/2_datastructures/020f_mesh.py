from math import radians
import compas
from compas.datastructures import Mesh
from compas.datastructures import mesh_thicken
from compas_cgal.meshing import remesh
from compas_gmsh.models import MeshModel
from compas_view2.app import App

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))
mesh.quads_to_triangles()

L = sum(mesh.edge_length(*edge) for edge in mesh.edges())
L = L / mesh.number_of_edges()

V, F = remesh(mesh.to_vertices_and_faces(), target_edge_length=L)

mesh = Mesh.from_vertices_and_faces(V, F)
dual = mesh.dual()

frames = dual.subdivide(scheme="frames", offset=0.2)

thickened = mesh_thicken(frames, thickness=0.2)

model = MeshModel.from_mesh(thickened)
model.options.mesh.meshsize_max = 0.1
model.generate_mesh()
mesh = model.mesh_to_compas()

# =============================================================================
# Viz
# =============================================================================

viewer = App()
viewer.view.camera.position = [30, 28, 10]
viewer.view.camera.target = [30, 28, 0]
viewer.view.camera.rotation = [radians(75), 0, -radians(90)]

viewer.add(mesh)

viewer.run()
