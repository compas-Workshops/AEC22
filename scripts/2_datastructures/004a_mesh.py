from math import radians
import compas
from compas.datastructures import Mesh
from compas.colors import Color
from compas_view2.app import App

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))

vertex = mesh.vertex_sample(size=1)[0]
nbrs = mesh.vertex_neighbors(vertex)

point_color = {vertex: Color.blue()}
point_color.update({nbr: Color.pink() for nbr in nbrs})

# =============================================================================
# Viz
# =============================================================================

viewer = App()
viewer.view.camera.position = [30, 28, 10]
viewer.view.camera.target = [30, 28, 0]
viewer.view.camera.rotation = [radians(75), 0, -radians(90)]

viewer.add(mesh, vertices=[vertex] + nbrs, show_points=True, pointcolor=point_color)

viewer.run()
