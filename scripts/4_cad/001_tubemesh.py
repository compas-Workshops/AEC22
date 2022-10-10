import compas
from compas.datastructures import Mesh
from compas.artists import Artist

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))

artist = Artist(mesh)
artist.draw_faces()
artist.draw_vertices()
