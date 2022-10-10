import compas
from compas.datastructures import Mesh
from compas.geometry import Line
from compas.geometry import Cylinder
from compas.colors import Color
from compas_view2.app import App
from compas_view2.objects import Collection

pink = Color.pink()
blue = Color.blue()
green = Color.green()

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))

start = mesh.edge_sample(size=1)[0]
forwardedges = mesh.halfedge_loop(start)
backwardedges = mesh.halfedge_loop((start[1], start[0]))

pipes = []
props = []

for edge in forwardedges:
    line = Line(mesh.vertex_coordinates(edge[0]), mesh.vertex_coordinates(edge[1]))
    pipe = Cylinder([(line.midpoint, line.direction), 0.1], line.length)
    color = pink if edge == start else blue
    pipes.append(pipe)
    props.append({'facecolor': color.lightened(50), 'linecolor': color})

for edge in backwardedges[1:]:
    line = Line(mesh.vertex_coordinates(edge[0]), mesh.vertex_coordinates(edge[1]))
    pipe = Cylinder([(line.midpoint, line.direction), 0.1], line.length)
    pipes.append(pipe)
    props.append({'facecolor': green.lightened(50), 'linecolor': green})

face_color = {}

for edge in forwardedges[1::2]:
    for u, v in mesh.halfedge_strip(edge):
        face = mesh.halfedge_face(u, v)
        face_color[face] = blue.lightened(50)

    for u, v in mesh.halfedge_strip((edge[1], edge[0])):
        face = mesh.halfedge_face(u, v)
        face_color[face] = blue.lightened(75)

for edge in backwardedges[1::2]:
    for u, v in mesh.halfedge_strip(edge):
        face = mesh.halfedge_face(u, v)
        face_color[face] = green.lightened(50)

    for u, v in mesh.halfedge_strip((edge[1], edge[0])):
        face = mesh.halfedge_face(u, v)
        face_color[face] = green.lightened(75)

viewer = App()
viewer.add(mesh, facecolor=face_color)
viewer.add(Collection(pipes, props))
viewer.view.camera.zoom_extents()
viewer.run()
