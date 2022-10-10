import os
import compas
from compas.datastructures import Mesh

SESSION = os.path.join(os.path.dirname(__file__), "session.json")

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))

session = {"mesh": mesh}

compas.json_dump(session, SESSION)
