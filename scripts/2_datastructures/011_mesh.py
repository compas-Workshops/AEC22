import compas
from compas.datastructures import Mesh
from compas.geometry import Line
from compas.geometry import Cylinder
from compas.colors import Color
from compas_view2.app import App
from compas_view2.objects import Collection

pink = Color.pink()
blue = Color.blue()

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))

start = mesh.edge_sample(size=1)[0]
loop = mesh.halfedge_loop(start)

pipes = []
props = []

for edge in loop:
    a = mesh.vertex_coordinates(edge[0])
    b = mesh.vertex_coordinates(edge[1])
    line = Line(a, b)
    pipe = Cylinder([(line.midpoint, line.direction), 0.05], line.length)
    pipes.append(pipe)
    color = pink if edge == start else blue
    props.append({"facecolor": color.lightened(50), "linecolor": color})

viewer = App()
viewer.add(mesh)
viewer.add(Collection(pipes, props))
viewer.view.camera.zoom_extents()
viewer.run()