import os
import compas
from compas.datastructures import mesh_thicken

SESSION = os.path.join(os.path.dirname(__file__), "session.json")

session = compas.json_load(SESSION)

mesh = session["frames"]
thickened = mesh_thicken(mesh, thickness=0.05)

session["thickened"] = thickened
compas.json_dump(session, SESSION)
