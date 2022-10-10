import compas
from compas.datastructures import Mesh
from compas.artists import Artist
from compas.colors import Color


mesh = Mesh.from_obj(compas.get('tubemesh.obj'))
mesh.quads_to_triangles()


Artist.clear()

artist = Artist(mesh)

artist.draw_faces()

Artist.redraw()
