import os
import compas
from compas.datastructures import Mesh
from compas.artists import Artist
from compas.colors import Color

FILE = os.path.join(os.path.dirname(__file__), 'session.json')


session = compas.json_load(FILE)

dual = session['dual']
frames = dual.subdivide(scheme='frames', offset=0.1)

session['frames'] = frames


compas.json_dump(session, FILE)


Artist.clear()

artist = Artist(frames)

artist.draw_faces(join_faces=True, color=Color.from_hex('#0092d2').rgb255)

Artist.redraw()
