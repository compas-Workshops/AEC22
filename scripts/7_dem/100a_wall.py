from typing import List

from compas.geometry import Point, Plane, Frame, Line
from compas.geometry import NurbsCurve
from compas.geometry import Box
from compas.geometry import Transformation
from compas.geometry import Translation
from compas.geometry import Polygon

from compas.colors import Color
from compas.utilities import pairwise

from compas_assembly.datastructures import Assembly
from compas_assembly.datastructures import Block
from compas_assembly.datastructures import Interface
from compas_assembly.algorithms import assembly_interfaces

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

span = curve.domain[1] - curve.domain[0]

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
# Even
# =============================================================================

step = span / N
params = [curve.domain[0] + i * step for i in range(N + 1)]
frames = [curve.frame_at(t) for t in params]

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

even = []

for (a, b), (c, d) in zip(pairwise(outerpoints), pairwise(innerpoints)):
    ab = b - a
    cd = d - c
    L = min(ab.length, cd.length)
    box = Box(Frame.worldXY(), L, W, H)
    even.append(box)

oddparams = []
oddframes = []

for box, (u, v) in zip(even, pairwise(params)):
    t = 0.5 * (u + v)
    frame = curve.frame_at(t)
    transform = Transformation.from_frame_to_frame(box.frame, frame)
    box.transform(transform)

    oddparams.append(t)
    oddframes.append(frame)

# =============================================================================
# Odd
# =============================================================================

outerpoints = []
innerpoints = []

for frame in oddframes:
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

odd = []

for (a, b), (c, d) in zip(pairwise(outerpoints), pairwise(innerpoints)):
    ab = b - a
    cd = d - c
    L = min(ab.length, cd.length)
    box = Box(Frame.worldXY(), L, W, H)
    odd.append(box)

for box, (u, v) in zip(odd, pairwise(oddparams)):
    t = 0.5 * (u + v)
    transform = Transformation.from_frame_to_frame(box.frame, curve.frame_at(t))
    box.transform(transform)

# =============================================================================
# Courses
# =============================================================================

courses = []

for i in range(6):
    course = []
    if i % 2:
        boxes = odd
    else:
        boxes = even
    translation = Translation.from_vector([0, 0, i * box.zsize])
    for box in boxes:
        course.append(box.transformed(translation))
    courses.append(course)

# =============================================================================
# Assembly
# =============================================================================

assembly = Assembly()

for course in courses:
    for box in course:
        block = Block.from_shape(box)
        assembly.add_block(block)

assembly_interfaces(assembly, tmax=1e-6, amin=1e-2)

# =============================================================================
# Viz
# =============================================================================

viewer = App()

viewer.add(curve.to_polyline(), linewidth=3)
viewer.add(outer.to_polyline(), linecolor=(1, 0, 0))
viewer.add(inner.to_polyline(), linecolor=(0, 0, 1))

for frame in frames:
    viewer.add(frame, linewidth=5, size=0.1)

viewer.add(Collection(outerpoints))
viewer.add(Collection(innerpoints))

# for box in even:
#     viewer.add(box, facecolor=Color.blue().lightened(75), linecolor=Color.blue())

# for box in odd:
#     box.transform(Translation.from_vector([0, 0, box.zsize]))
#     viewer.add(box, facecolor=Color.red().lightened(75), linecolor=Color.red())

# for course in courses:
#     for box in course:
#         viewer.add(box, facecolor=Color.grey().lightened(75), linecolor=Color.grey())

for node in assembly.graph.nodes():
    block = assembly.graph.node_attribute(node, "block")

    if assembly.graph.node_attribute(node, "is_support"):
        color = Color.red()
    else:
        color = Color.grey()

    viewer.add(block, facecolor=color.lightened(50), linecolor=color, linewidth=2, opacity=0.5, show_faces=False)

    viewer.add(Point(*block.centroid()))

for edge in assembly.graph.edges():
    interfaces: List[Interface] = assembly.graph.edge_attribute(edge, "interfaces")
    for interface in interfaces:
        polygon = Polygon(interface.points)
        viewer.add(polygon)

    a = assembly.graph.node_attribute(edge[0], "block").centroid()
    b = assembly.graph.node_attribute(edge[1], "block").centroid()

    line = Line(a, b)

    viewer.add(line, linewidth=3)

viewer.run()
