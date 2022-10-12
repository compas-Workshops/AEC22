from compas.geometry import Point
from compas.geometry import NurbsCurve
from compas_view2.app import App

# =============================================================================
# Curve
# =============================================================================

points = [
    Point(0, 0, 0),
    Point(2, 2, 0),
    Point(4, -4, 0),
    Point(6, 0, 0),
]

curve = NurbsCurve.from_points(points)

# =============================================================================
# Params
# =============================================================================

N = 11
W = 0.4
H = 0.2

# =============================================================================
# Offsets
# =============================================================================

outer = curve.copy()
outer.offset(0.5 * W, [0, 0, -1])

inner = curve.copy()
inner.offset(0.5 * W, [0, 0, +1])

# =============================================================================
# Frames
# =============================================================================

span = curve.domain[1] - curve.domain[0]
step = span / N

params = [curve.domain[0] + i * step for i in range(N + 1)]
frames = [curve.frame_at(t) for t in params]

# =============================================================================
# Viz
# =============================================================================

viewer = App()

viewer.add(curve.to_polyline())
viewer.add(outer.to_polyline(), linecolor=(1, 0, 0))
viewer.add(inner.to_polyline(), linecolor=(0, 0, 1))

for frame in frames:
    viewer.add(frame, linewidth=3, size=0.3)

viewer.run()
