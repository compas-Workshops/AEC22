import compas
from compas.geometry import Point
from compas.geometry import Vector
from compas.geometry import Line
from compas.datastructures import Mesh
from compas.colors import Color

from compas_view2.app import App
from compas_view2.objects import Collection

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))

lines = []
for vertex in mesh.vertices():
    point = Point(*mesh.vertex_coordinates(vertex))
    vector = Vector(*mesh.vertex_normal(vertex))
    lines.append(Line(point, point + vector))

viewer = App()
viewer.add(
    mesh,
    facecolor=Color.from_hex("#0092d2").lightened(50),
    linecolor=Color.from_hex("#0092d2"),
)
viewer.add(Collection(lines), linewidth=5, linecolor=Color.pink())
viewer.view.camera.zoom_extents()
viewer.run()
