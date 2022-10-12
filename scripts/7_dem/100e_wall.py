from compas.geometry import Point, Plane
from compas.geometry import Box
from compas.geometry import NurbsCurve
from compas.utilities import pairwise
from compas.colors import Color

from compas_occ.geometry import OCCSurface
from compas_occ.conversions import compas_plane_to_occ_plane
from compas_occ.conversions import compas_point_from_occ_point

from OCC.Core.Geom import Geom_Plane
from OCC.Core.GeomAPI import GeomAPI_IntCS

from compas_view2.app import App
from compas_view2.objects import Collection

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
# 1st Course
# =============================================================================

outerpoints = []
innerpoints = []

for frame in frames:
    plane = compas_plane_to_occ_plane(Plane(frame.point, frame.xaxis))
    plane = Geom_Plane(plane)
    surface = OCCSurface.from_occ(plane)

    intersection = GeomAPI_IntCS(outer.occ_curve, surface.occ_surface)
    pnt = intersection.Point(1)
    point = compas_point_from_occ_point(pnt)
    outerpoints.append(point)

    intersection = GeomAPI_IntCS(inner.occ_curve, surface.occ_surface)
    pnt = intersection.Point(1)
    point = compas_point_from_occ_point(pnt)
    innerpoints.append(point)

course_0 = []

for (a, b), (c, d), (u, v) in zip(pairwise(outerpoints), pairwise(innerpoints), pairwise(params)):
    ab = b - a
    cd = d - c
    L = min(ab.length, cd.length)
    t = 0.5 * (u + v)
    frame = curve.frame_at(t)
    box = Box(frame, L, W, H)
    course_0.append(box)

# =============================================================================
# Viz
# =============================================================================

viewer = App()
viewer.view.camera.position = [-4, -6, 2]
viewer.view.camera.target = [3, 0, 1]

viewer.add(curve.to_polyline())
viewer.add(outer.to_polyline(), linecolor=(1, 0, 0))
viewer.add(inner.to_polyline(), linecolor=(0, 0, 1))

# for frame in frames:
#     viewer.add(frame, linewidth=3, size=0.3)

viewer.add(Collection(outerpoints))
viewer.add(Collection(innerpoints))

for box in course_0:
    viewer.add(box, facecolor=Color.blue().lightened(75), linecolor=Color.blue())

viewer.run()
