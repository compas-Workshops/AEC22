from math import radians
import compas
from compas.datastructures import Mesh
from compas.geometry import Line
from compas.colors import Color
from compas_view2.app import App
from compas_view2.objects import Collection

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))

edge = mesh.edge_sample(size=1)[0]
loop = mesh.edge_loop(edge)

lines = []
for edge in loop:
    a = mesh.vertex_coordinates(edge[0])
    b = mesh.vertex_coordinates(edge[1])
    line = Line(a, b)
    lines.append(line)

# =============================================================================
# Viz
# =============================================================================

viewer = App()
viewer.view.show_grid = False
viewer.view.camera.position = [30, 28, 10]
viewer.view.camera.target = [30, 28, 0]
viewer.view.camera.rotation = [radians(75), 0, -radians(90)]

viewer.add(mesh)
viewer.add(Collection(lines), linewidth=10, linecolor=Color.blue())

viewer.run()
