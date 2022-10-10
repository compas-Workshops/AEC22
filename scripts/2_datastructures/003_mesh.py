import compas
from compas.datastructures import Mesh
from compas.colors import Color
from compas_view2.app import App

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))

face_color = {}
for face in mesh.face_sample(size=17):
    face_color[face] = Color.from_hex("#0092d2").lightened(50)

viewer = App()
viewer.add(
    mesh,
    facecolor=face_color,
)
viewer.view.camera.zoom_extents()
viewer.run()
