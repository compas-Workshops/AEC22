import os
import compas
from compas.geometry import Point, Plane
from compas.geometry import Box
from compas.geometry import Translation
from compas.geometry import NurbsCurve
from compas.utilities import pairwise
from compas.colors import Color

from compas_occ.geometry import OCCSurface
from compas_occ.conversions import compas_plane_to_occ_plane
from compas_occ.conversions import compas_point_from_occ_point

from OCC.Core.Geom import Geom_Plane
from OCC.Core.GeomAPI import GeomAPI_IntCS

from compas_view2.app import App

FILE = os.path.join(os.path.dirname(__file__), 'wall.json')

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

params_0 = [curve.domain[0] + i * step for i in range(N + 1)]
frames_0 = [curve.frame_at(t) for t in params_0]

# =============================================================================
# 1st Course
# =============================================================================

opoints_0 = []
ipoints_0 = []

for frame in frames_0:
    plane = compas_plane_to_occ_plane(Plane(frame.point, frame.xaxis))
    plane = Geom_Plane(plane)
    surface = OCCSurface.from_occ(plane)

    intersection = GeomAPI_IntCS(outer.occ_curve, surface.occ_surface)
    pnt = intersection.Point(1)
    point = compas_point_from_occ_point(pnt)
    opoints_0.append(point)

    intersection = GeomAPI_IntCS(inner.occ_curve, surface.occ_surface)
    pnt = intersection.Point(1)
    point = compas_point_from_occ_point(pnt)
    ipoints_0.append(point)

course_0 = []

params_1 = []
frames_1 = []

for (a, b), (c, d), (u, v) in zip(pairwise(opoints_0), pairwise(ipoints_0), pairwise(params_0)):
    ab = b - a
    cd = d - c
    L = min(ab.length, cd.length)
    t = 0.5 * (u + v)
    frame = curve.frame_at(t)
    box = Box(frame, L, W, H)

    course_0.append(box)
    params_1.append(t)
    frames_1.append(frame)

# =============================================================================
# 2nd Course
# =============================================================================

opoints_1 = []
ipoints_1 = []

for frame in frames_1:
    plane = compas_plane_to_occ_plane(Plane(frame.point, frame.xaxis))
    plane = Geom_Plane(plane)
    surface = OCCSurface.from_occ(plane)

    intersection = GeomAPI_IntCS(outer.occ_curve, surface.occ_surface)
    pnt = intersection.Point(1)
    point = compas_point_from_occ_point(pnt)
    opoints_1.append(point)

    intersection = GeomAPI_IntCS(inner.occ_curve, surface.occ_surface)
    pnt = intersection.Point(1)
    point = compas_point_from_occ_point(pnt)
    ipoints_1.append(point)

opoints_1.insert(0, opoints_0[0])
opoints_1.append(opoints_0[-1])

ipoints_1.insert(0, ipoints_0[0])
ipoints_1.append(ipoints_0[-1])

params_1.insert(0, params_0[0])
params_1.append(params_0[-1])

course_1 = []

for (a, b), (c, d), (u, v) in zip(pairwise(opoints_1), pairwise(ipoints_1), pairwise(params_1)):
    ab = b - a
    cd = d - c
    L = min(ab.length, cd.length)
    t = 0.5 * (u + v)
    frame = curve.frame_at(t)
    box = Box(frame, L, W, H)

    course_1.append(box)

# =============================================================================
# Courses
# =============================================================================

courses = []
for i in range(10):
    boxes = course_1 if i % 2 else course_0
    courses.append([box.transformed(Translation.from_vector([0, 0, i * box.zsize])) for box in boxes])

# =============================================================================
# Export
# =============================================================================

wall = {'courses': courses}

compas.json_dump(wall, FILE)

# =============================================================================
# Viz
# =============================================================================

viewer = App()
viewer.view.camera.position = [-4, -6, 2]
viewer.view.camera.target = [3, 0, 1]

viewer.add(curve.to_polyline())

for course in courses:
    for box in course:
        viewer.add(box, facecolor=Color.grey().lightened(50), linecolor=Color.grey())

viewer.run()
