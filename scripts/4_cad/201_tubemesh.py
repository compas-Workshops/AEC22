import compas
from compas.datastructures import Mesh
from compas.artists import Artist
from compas.colors import Color
from compas.rpc import Proxy

meshing = Proxy('compas_cgal.meshing')


mesh = Mesh.from_obj(compas.get('tubemesh.obj'))
mesh.quads_to_triangles()

L = sum([mesh.edge_length(*edge) for edge in mesh.edges()])
L = 0.5 * L / mesh.number_of_edges()

V, F = meshing.remesh(mesh.to_vertices_and_faces(), target_edge_length=L)

mesh = Mesh.from_vertices_and_faces(V, F)


Artist.clear()

artist = Artist(mesh)

artist.draw_faces()

Artist.redraw()
