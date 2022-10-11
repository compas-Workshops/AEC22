import os
import compas
from compas.artists import Artist

SESSION = os.path.join(os.path.dirname(__file__), "../3_data/session.json")
session = compas.json_load(SESSION)

mesh = session["thickened"]

artist = Artist(mesh, layer="AEC22::Thickened")
artist.clear_layer()
artist.draw(disjoint=True)
