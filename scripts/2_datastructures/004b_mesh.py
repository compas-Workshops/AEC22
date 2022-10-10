from math import radians
import compas
from compas.datastructures import Mesh
from compas.geometry import Point
from compas.colors import Color
from compas_view2.app import App

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))

vertex = mesh.vertex_sample(size=1)[0]
nbrs = mesh.vertex_neighbors(vertex)

# =============================================================================
# Viz
# =============================================================================

viewer = App()
viewer.view.camera.position = [30, 28, 10]
viewer.view.camera.target = [30, 28, 0]
viewer.view.camera.rotation = [radians(75), 0, -radians(90)]

viewer.add(mesh)

point = Point(*mesh.vertex_coordinates(vertex))
viewer.add(point, pointcolor=Color.blue())

for nbr in nbrs:
    point = Point(*mesh.vertex_coordinates(nbr))
    viewer.add(point, pointcolor=Color.pink())

viewer.run()
