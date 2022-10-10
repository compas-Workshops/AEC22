import os
import compas
from compas.datastructures import Mesh
from compas.datastructures import mesh_thicken
from compas.artists import Artist
from compas.colors import Color

FILE = os.path.join(os.path.dirname(__file__), 'session.json')


session = compas.json_load(FILE)

frames = session['frames']

model = mesh_thicken(frames, thickness=0.05)

session['model'] = model


compas.json_dump(session, FILE)


Artist.clear()

artist = Artist(model)

artist.draw_faces(join_faces=True, color=Color.from_hex('#0092d2').rgb255)

Artist.redraw()
