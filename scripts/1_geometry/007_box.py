from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Transformation
from compas_view2.app import App

box = Box.from_width_height_depth(width=0.8, height=0.3, depth=0.5)

frame = Frame([1, 1, 0], [1, 0, 0], [0, 0, 1])
transformation = Transformation.from_frame(frame)

box.transform(transformation)

viewer = App()
viewer.add(box)
viewer.add(box.frame, linewidth=3, size=0.5)
viewer.view.camera.zoom_extents()
viewer.run()
