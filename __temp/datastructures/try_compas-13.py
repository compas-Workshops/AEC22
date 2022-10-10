import compas
from compas.geometry import Point
from compas.geometry import Vector
from compas.geometry import Line
from compas.datastructures import Mesh
from compas.colors import Color
from compas.artists import Artist

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))
mesh.flip_cycles()

artist = Artist(mesh)
artist.draw_faces()
