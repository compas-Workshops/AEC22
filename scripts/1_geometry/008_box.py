from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Transformation
from compas_view2.app import App

box1 = Box.from_width_height_depth(width=0.8, height=0.3, depth=0.5)

frame = Frame([1, 1, 0], [1, 0, 0], [0, 0, 1])
transformation = Transformation.from_frame(frame)

box2: Box = box1.transformed(transformation)

viewer = App()
viewer.add(box1)
viewer.add(box1.frame, linewidth=3, size=0.5)
viewer.add(box2)
viewer.add(box2.frame, linewidth=3, size=0.5)
viewer.view.camera.zoom_extents()
viewer.run()
