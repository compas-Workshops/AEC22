import compas
import compas_rhino
from compas.datastructures import Mesh
from compas.artists import Artist

compas_rhino.clear()

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))

artist = Artist(mesh, layer="Tubemesh")
artist.draw_vertices()
artist.draw_edges()
artist.draw_faces(join_faces=True)
