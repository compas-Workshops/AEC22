import compas_rhino
from compas.geometry import Point
from compas.geometry import NurbsCurve
from compas.artists import Artist

compas_rhino.clear()

points = [
    Point(0, 0, 0),
    Point(3, 3, 0),
    Point(6, -6, 0),
    Point(9, 0, 0),
]

curve = NurbsCurve.from_points(points)
artist = Artist(curve, layer="Wall::Curve")
artist.draw()
