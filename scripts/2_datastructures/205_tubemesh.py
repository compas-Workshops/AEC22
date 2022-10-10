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

dual: Mesh = mesh.dual()
frames = dual.subdivide(scheme="frames", offset=0.2)
thick = mesh_thicken(frames, thickness=0.2)

model = MeshModel.from_mesh(thick)
model.options.mesh.meshsize_max = 0.1
model.generate_mesh()
mesh = model.mesh_to_compas()

viewer = App()
viewer.add(mesh)
viewer.view.camera.zoom_extents()
viewer.run()
