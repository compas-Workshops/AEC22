from math import radians
import compas
from compas.datastructures import Mesh
from compas.geometry import Line, Cylinder
from compas.colors import Color
from compas_view2.app import App
from compas_view2.objects import Collection

pink = Color.pink()
blue = Color.blue()
green = Color.green()

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))

start = mesh.edge_sample(size=1)[0]
forward = mesh.halfedge_loop(start)
backward = mesh.halfedge_loop((start[1], start[0]))

pipes = []
props = []

for edge in forward:
    a = mesh.vertex_coordinates(edge[0])
    b = mesh.vertex_coordinates(edge[1])
    line = Line(a, b)
    pipe = Cylinder([(line.midpoint, line.direction), 0.05], line.length)
    pipes.append(pipe)
    color = pink if edge == start else blue
    props.append({"facecolor": color.lightened(50), "linecolor": color})

for edge in backward[1:]:
    a = mesh.vertex_coordinates(edge[0])
    b = mesh.vertex_coordinates(edge[1])
    line = Line(a, b)
    pipe = Cylinder([(line.midpoint, line.direction), 0.05], line.length)
    pipes.append(pipe)
    props.append({"facecolor": green.lightened(50), "linecolor": green})

# =============================================================================
# Viz
# =============================================================================

viewer = App()
viewer.view.show_grid = False
viewer.view.camera.position = [30, 28, 10]
viewer.view.camera.target = [30, 28, 0]
viewer.view.camera.rotation = [radians(75), 0, -radians(90)]

viewer.add(mesh)
viewer.add(Collection(pipes, props))

viewer.run()
