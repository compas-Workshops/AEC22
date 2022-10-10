import os
import compas

SESSION = os.path.join(os.path.dirname(__file__), "session.json")

session = compas.json_load(SESSION)

mesh = session["dual"]
frames = mesh.subdivide(scheme="frames", offset=0.1)

session["frames"] = frames
compas.json_dump(session, SESSION)
