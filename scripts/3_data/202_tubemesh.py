import os
import compas
from compas.datastructures import Mesh

SESSION = os.path.join(os.path.dirname(__file__), "session.json")

session = compas.json_load(SESSION)

mesh = session["remeshed"]
dual = mesh.dual()

session["dual"] = dual
compas.json_dump(session, SESSION)
