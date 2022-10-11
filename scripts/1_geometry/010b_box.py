from compas.geometry import Point, Box, NurbsCurve
from compas_view2.app import App

points = [
    Point(0, 0, 0),
    Point(3, 3, 0),
    Point(6, -6, 3),
    Point(9, 0, 0),
]
curve = NurbsCurve.from_points(points)

frame = curve.frame_at(curve.domain[0])
box = Box(frame, 0.8, 0.5, 0.3)

n = 100
span = curve.domain[1] - curve.domain[0]
step = span / n
params = [curve.domain[0] + i * step for i in range(n + 1)]

frames = [curve.frame_at(t) for t in params]

# =============================================================================
# Viz
# =============================================================================

viewer = App(width=1600, height=900)
viewer.view.camera.position = [0, 8, 2]
viewer.view.camera.target = [4, 0, 0]

viewer.add(curve.to_polyline(), linewidth=2)
viewer.add(box)

for frame in frames:
    viewer.add(frame, linewidth=5, size=0.5)

viewer.run()
