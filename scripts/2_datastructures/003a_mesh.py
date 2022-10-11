from math import radians
import compas
from compas.datastructures import Mesh
from compas.colors import Color
from compas_view2.app import App

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))

faces = mesh.face_sample(size=53)

face_color = {}
for face in faces:
    face_color[face] = Color.blue().lightened(50)

# =============================================================================
# Viz
# =============================================================================

viewer = App()
viewer.view.camera.position = [30, 28, 10]
viewer.view.camera.target = [30, 28, 0]
viewer.view.camera.rotation = [radians(75), 0, -radians(90)]

viewer.add(mesh, facecolor=face_color)

viewer.run()
