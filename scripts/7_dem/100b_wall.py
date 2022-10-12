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
# Viz
# =============================================================================

viewer = App()

viewer.add(curve.to_polyline(), linewidth=3)
viewer.add(outer.to_polyline(), linecolor=(1, 0, 0))
viewer.add(inner.to_polyline(), linecolor=(0, 0, 1))

viewer.run()
