import os
import compas
from compas.datastructures import Mesh

SESSION = os.path.join(os.path.dirname(__file__), "session.json")

session = compas.json_load(SESSION)

mesh = session["mesh"].copy()
mesh.quads_to_triangles()

session["quads"] = mesh

compas.json_dump(session, SESSION)
