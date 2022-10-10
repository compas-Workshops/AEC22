from compas.geometry import Box
from compas.geometry import Sphere
from compas.datastructures import Mesh
from compas.colors import Color
from compas_view2.app import App

box = Box.from_corner_corner_height([0, 0, 0], [1, 1, 0], 1.0)
sphere = Sphere([1, 1, 1], 0.5)

shape = box - sphere
mesh = Mesh.from_shape(shape)

viewer = App()
viewer.add(
    mesh,
    facecolor=Color.green().darkened(50),
    linecolor=Color.green(),
)
viewer.view.camera.zoom_extents()
viewer.run()
