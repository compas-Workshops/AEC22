import os
import compas
from compas_gmsh.models import MeshModel

SESSION = os.path.join(os.path.dirname(__file__), "session.json")

session = compas.json_load(SESSION)

mesh = session["thickened"]

model = MeshModel.from_mesh(mesh)
model.options.mesh.meshsize_max = 0.1
model.generate_mesh()
fem = model.mesh_to_compas()

session["fem"] = fem
compas.json_dump(session, SESSION)
