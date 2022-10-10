from compas.geometry import Point
from compas.geometry import Box
from compas.geometry import NurbsCurve

from compas_view2.app import App

points = [
    Point(0, 0, 0),
    Point(3, 3, 0),
    Point(6, -6, 3),
    Point(9, 0, 0),
]
curve = NurbsCurve.from_points(points)
frame = curve.frame_at(0)
box = Box(frame=frame, xsize=0.8, ysize=0.5, zsize=0.3)

viewer = App()
viewer.add(curve.to_polyline())
viewer.add(box)
viewer.view.camera.zoom_extents()
viewer.run()
