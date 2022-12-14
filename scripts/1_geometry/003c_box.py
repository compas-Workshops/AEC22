from compas.geometry import Box
from compas.colors import Color
from compas_view2.app import App

box1 = Box.from_width_height_depth(1, 1, 1)
box2 = Box.from_corner_corner_height([0, 0, 0], [1, 1, 0], 1)

# =============================================================================
# Viz
# =============================================================================

viewer = App()
viewer.view.camera.position = [2, -3, 1]
viewer.view.camera.target = [0, 0, 0]

viewer.add(box1, facecolor=Color.red())
viewer.add(box2, facecolor=Color.blue())

viewer.run()
