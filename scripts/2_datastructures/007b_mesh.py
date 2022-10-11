from math import radians
import compas
from compas.datastructures import Mesh
from compas.geometry import Line
from compas.colors import Color
from compas_view2.app import App
from compas_view2.objects import Collection

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))

start = mesh.edge_sample(size=1)[0]
loop = mesh.edge_loop(start)

lines = []
props = []
for edge in loop:
    a = mesh.vertex_coordinates(edge[0])
    b = mesh.vertex_coordinates(edge[1])
    line = Line(a, b)
    lines.append(line)
    color = Color.pink() if edge == start else Color.blue()
    props.append({"linecolor": color})

# =============================================================================
# Viz
# =============================================================================

viewer = App()
viewer.view.show_grid = False
viewer.view.camera.position = [30, 28, 10]
viewer.view.camera.target = [30, 28, 0]
viewer.view.camera.rotation = [radians(75), 0, -radians(90)]

viewer.add(mesh)
viewer.add(Collection(lines, props), linewidth=10)

viewer.run()
