import os
import compas
from compas.artists import Artist
from compas.colors import Color

FILE = os.path.join(os.path.dirname(__file__), 'session.json')


session = compas.json_load(FILE)

mesh = session['mesh']
dual = session['dual']
frames = session['frames']
model = session['model']


Artist.clear()

artist = Artist(mesh, layer='TubeMesh::Mesh')
artist.draw(disjoint=True, color=Color.red())

artist = Artist(dual, layer='TubeMesh::Dual')
artist.draw(disjoint=True, color=Color.green())

artist = Artist(frames, layer='TubeMesh::Frames')
artist.draw(disjoint=True, color=Color.blue())

artist = Artist(model, layer='TubeMesh::Model')
artist.draw(disjoint=True, color=Color.grey())

Artist.redraw()
