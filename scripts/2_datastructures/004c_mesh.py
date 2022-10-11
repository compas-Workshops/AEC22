from math import radians
import compas
from compas.datastructures import Mesh
from compas.geometry import Sphere
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

sphere = Sphere(mesh.vertex_coordinates(vertex), 0.2)
viewer.add(sphere, facecolor=Color.blue().lightened(50), linecolor=Color.blue())

for nbr in nbrs:
    sphere = Sphere(mesh.vertex_coordinates(nbr), 0.2)
    viewer.add(sphere, facecolor=Color.pink().lightened(50), linecolor=Color.pink())

viewer.run()
