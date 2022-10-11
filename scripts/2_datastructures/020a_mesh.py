from math import radians
import compas
from compas.datastructures import Mesh
from compas_view2.app import App

# load a tubemesh

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))

# convert all quads to triangles

mesh.quads_to_triangles()

# =============================================================================
# Viz
# =============================================================================

viewer = App()
viewer.view.camera.position = [30, 28, 10]
viewer.view.camera.target = [30, 28, 0]
viewer.view.camera.rotation = [radians(75), 0, -radians(90)]

viewer.add(mesh)

viewer.run()
