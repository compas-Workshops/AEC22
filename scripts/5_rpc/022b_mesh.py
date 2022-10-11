import os
import compas
from compas.datastructures import Mesh
from compas.datastructures import mesh_thicken
from compas.artists import Artist
from compas.rpc import Proxy

SESSION = os.path.join(os.path.dirname(__file__), "../3_data/session.json")

meshing = Proxy("compas_cgal.meshing")

# =============================================================================
# Import
# =============================================================================

session = compas.json_load(SESSION)

mesh = session["mesh"]

# =============================================================================
# Do
# =============================================================================

quads = mesh.copy()
quads.quads_to_triangles()

L = sum(quads.edge_length(*edge) for edge in mesh.edges())
L = L / quads.number_of_edges()

V, F = meshing.remesh(quads.to_vertices_and_faces(), target_edge_length=L)

remeshed = Mesh.from_vertices_and_faces(V, F)

dual = remeshed.dual()
frames = dual.subdivide(scheme="frames", offset=0.1)
thickened = mesh_thicken(frames, thickness=0.05)

# =============================================================================
# Viz
# =============================================================================

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
