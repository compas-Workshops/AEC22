from compas.geometry import Box
from compas.geometry import Sphere
from compas.colors import Color
from compas_occ.brep import BRep
from compas_view2.app import App

box = Box.from_corner_corner_height([0, 0, 0], [1, 1, 0], 1.0)
box = BRep.from_box(box)

sphere = Sphere([1, 1, 1], 0.5)
sphere = BRep.from_sphere(sphere)

shape = box - sphere

viewer = App()
# viewer.add(
#     box,
#     facecolor=Color.red().lightened(50),
#     linecolor=Color.red(),
# )
# viewer.add(
#     sphere,
#     facecolor=Color.blue().lightened(50),
#     linecolor=Color.blue(),
# )
viewer.add(
    shape,
    facecolor=Color.green().darkened(50),
    linecolor=Color.green(),
)
viewer.view.camera.zoom_extents()
viewer.run()
