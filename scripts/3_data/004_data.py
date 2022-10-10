import os
import compas
from compas.datastructures import Mesh

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))

filepath = os.path.join(os.path.dirname(__file__), "mesh.json")
compas.json_dump(mesh, filepath)
