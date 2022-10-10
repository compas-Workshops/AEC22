from compas.geometry import Box
from compas.colors import Color
from compas_view2.app import App

box1 = Box.from_width_height_depth(1, 1, 1)
box2 = Box.from_corner_corner_height([0, 0, 0], [1, 1, 0], 1)
box3 = Box.from_diagonal([[0, 0, 0], [-1, 1, 1]])

viewer = App()

viewer.add(box1, facecolor=Color.red().lightened(50), linecolor=Color.red())
viewer.add(box2, facecolor=Color.green().darkened(50), linecolor=Color.green())
viewer.add(box3, facecolor=Color.blue().lightened(50), linecolor=Color.blue())

viewer.run()
