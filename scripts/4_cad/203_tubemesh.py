import os
import compas
from compas.datastructures import Mesh
from compas.artists import Artist

FILE = os.path.join(os.path.dirname(__file__), 'session.json')


session = compas.json_load(FILE)

mesh = session['mesh']
dual = mesh.dual()

session['dual'] = dual

compas.json_dump(session, FILE)


Artist.clear()

artist = Artist(dual)

artist.draw_faces()

Artist.redraw()
