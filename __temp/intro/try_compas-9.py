import compas
from compas.datastructures import Mesh
from compas.colors import Color

from compas_view2.app import App

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))

viewer = App()
viewer.add(
    mesh,
    facecolor=Color.from_hex("#0092d2").lightened(50),
    linecolor=Color.from_hex("#0092d2"),
)
viewer.view.camera.zoom_extents()
viewer.run()
