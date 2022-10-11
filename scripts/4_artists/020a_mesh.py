import os
import compas
import compas_rhino
from compas.artists import Artist

SESSION = os.path.join(os.path.dirname(__file__), "../3_data/session.json")
session = compas.json_load(SESSION)

mesh = session["quads"]

compas_rhino.clear()

artist = Artist(mesh, layer="AEC22::Quads")
artist.draw_faces(join_faces=True)
