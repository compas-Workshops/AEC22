import os
import compas
from compas.artists import Artist

SESSION = os.path.join(os.path.dirname(__file__), "../3_data/session.json")
session = compas.json_load(SESSION)

mesh = session["mesh"]
quads = session["quads"]
remeshed = session["remeshed"]
dual = session["dual"]
frames = session["frames"]
thickened = session["thickened"]
# fem = session["fem"]

Artist.clear()

artist = Artist(mesh, layer="AEC22::Mesh")
artist.draw(disjoint=True)

artist = Artist(quads, layer="AEC22::Quads")
artist.draw(disjoint=True)

artist = Artist(remeshed, layer="AEC22::Remeshed")
artist.draw(disjoint=True)

artist = Artist(dual, layer="AEC22::Dual")
artist.draw(disjoint=True)

artist = Artist(frames, layer="AEC22::Frames")
artist.draw(disjoint=True)

artist = Artist(thickened, layer="AEC22::Thickened")
artist.draw(disjoint=True)

# artist = Artist(fem, layer="AEC22::FEM")
# artist.draw(disjoint=True)
