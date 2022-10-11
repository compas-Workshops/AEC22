import os
import compas
from compas.artists import Artist

SESSION = os.path.join(os.path.dirname(__file__), "../3_data/session.json")
session = compas.json_load(SESSION)

mesh = session["remeshed"]

artist = Artist(mesh, layer="AEC22::Remeshed")
artist.clear_layer()
artist.draw(disjoint=True)
