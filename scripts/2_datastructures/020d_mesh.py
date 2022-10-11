from math import radians
import compas
from compas.datastructures import Mesh
from compas_cgal.meshing import remesh
from compas_view2.app import App

# load a tubemesh

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))

# convert all quads to triangles

mesh.quads_to_triangles()

# compute the average edge length
# and divide by two

L = sum(mesh.edge_length(*edge) for edge in mesh.edges())
L = L / mesh.number_of_edges()
L = 0.5 * L

# remesh the triangle mesh
# until the average target edge length is reached

V, F = remesh(mesh.to_vertices_and_faces(), target_edge_length=L)

mesh = Mesh.from_vertices_and_faces(V, F)

# construct the dual of the remeshed mesh

dual = mesh.dual()

# subdivide the faces of the dual mesh into "frames"

frames = dual.subdivide(scheme="frames", offset=0.1)

# =============================================================================
# Viz
# =============================================================================

viewer = App()
viewer.view.camera.position = [30, 28, 10]
viewer.view.camera.target = [30, 28, 0]
viewer.view.camera.rotation = [radians(75), 0, -radians(90)]

viewer.add(frames)

viewer.run()
