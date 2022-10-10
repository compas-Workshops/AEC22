from compas.geometry import Box, Sphere
from compas.colors import Color
from compas_view2.app import App

box = Box.from_corner_corner_height([0, 0, 0], [1, 1, 0], 1.0)
sphere = Sphere([1, 1, 1], 0.5)

viewer = App()
viewer.view.camera.position = [4, -2.5, 2]
viewer.view.camera.target = [0, 1, 0]

viewer.add(box, facecolor=Color.red().lightened(50), linecolor=Color.red())
viewer.add(sphere, facecolor=Color.blue().lightened(50), linecolor=Color.blue())

viewer.run()
