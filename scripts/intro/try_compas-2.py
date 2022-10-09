from compas.geometry import Box
from compas.geometry import Frame

from compas_view2.app import App

frame = Frame([1, 1, 0], [1, 0, 0], [0, 0, 1])
box = Box(frame=frame, xsize=0.8, ysize=0.5, zsize=0.3)

viewer = App()
viewer.add(frame)
viewer.add(box, show_faces=True)
viewer.view.camera.zoom_extents()
viewer.run()
