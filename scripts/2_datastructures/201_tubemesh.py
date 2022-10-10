import compas
from compas.datastructures import Mesh
from compas_cgal.meshing import remesh
from compas_view2.app import App

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))
mesh.quads_to_triangles()

L = sum([mesh.edge_length(*edge) for edge in mesh.edges()])
L = 0.5 * L / mesh.number_of_edges()

V, F = remesh(
    mesh.to_vertices_and_faces(),
    target_edge_length=L,
    number_of_iterations=30,
)

mesh = Mesh.from_vertices_and_faces(V, F)

viewer = App()
viewer.add(mesh)
viewer.view.camera.zoom_extents()
viewer.run()
