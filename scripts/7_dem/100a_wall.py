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
# Viz
# =============================================================================

viewer = App()

viewer.add(curve.to_polyline(), linewidth=3)

viewer.run()
