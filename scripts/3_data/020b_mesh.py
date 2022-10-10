import os
import compas
from compas.datastructures import Mesh
from compas_cgal.meshing import remesh

SESSION = os.path.join(os.path.dirname(__file__), "session.json")

# =============================================================================
# Import
# =============================================================================

session = compas.json_load(SESSION)

mesh = session["quads"]

# =============================================================================
# Do
# =============================================================================

L = sum([mesh.edge_length(*edge) for edge in mesh.edges()])
L = 0.5 * L / mesh.number_of_edges()

V, F = remesh(mesh.to_vertices_and_faces(), target_edge_length=L)

remeshed = Mesh.from_vertices_and_faces(V, F)

# =============================================================================
# Export
# =============================================================================

session["remeshed"] = remeshed

compas.json_dump(session, SESSION)
