from compas.geometry import Box
from compas.datastructures import Mesh
from compas.colors import Color

from compas_view2.app import App

box = Box.from_corner_corner_height([0, 0, 0], [1, 1, 0], 1.0)
mesh = Mesh.from_shape(box)

viewer = App()
viewer.add(
    mesh,
    facecolor=Color.from_hex("#0092d2").lightened(50),
    linecolor=Color.from_hex("#0092d2"),
)
viewer.view.camera.zoom_extents()
viewer.run()
