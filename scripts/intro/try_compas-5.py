from compas.geometry import Point
from compas.geometry import Box
from compas.geometry import NurbsCurve
from compas.geometry import Transformation

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

frames = [curve.frame_at(t / 100) for t in range(1, 101)]
transforms = [Transformation.from_frame_to_frame(frame, f) for f in frames]

viewer = App()

viewer.add(curve.to_polyline())

frameobj = viewer.add(frame)
boxobj = viewer.add(box)


@viewer.on(interval=100, frames=100)
def slide(f):
    matrix = transforms[f].matrix
    boxobj.matrix = matrix
    frameobj.matrix = matrix
    boxobj.update()
    frameobj.update()


viewer.view.camera.zoom_extents()
viewer.run()
