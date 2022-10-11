import os
import compas
from compas.datastructures import Mesh

SESSION = os.path.join(os.path.dirname(__file__), "session.json")

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

# =============================================================================
# Export
# =============================================================================

session["quads"] = quads

compas.json_dump(session, SESSION)
