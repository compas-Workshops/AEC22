import compas
from compas.geometry import Line
from compas.geometry import Cylinder
from compas.datastructures import Mesh
from compas.colors import Color

from compas_view2.app import App
from compas_view2.objects import Collection

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))

facecolor = {face: Color.from_hex("#0092d2").lightened(50) for face in mesh.faces()}

edges = mesh.edge_sample()
loop = mesh.edge_loop(edges[0])

for u, v in loop[::2]:
    left = [mesh.halfedge_face(u, v) for u, v in mesh.halfedge_strip((u, v))]
    right = [mesh.halfedge_face(u, v) for u, v in mesh.halfedge_strip((v, u))]
    for face in left:
        facecolor[face] = Color.pink().lightened(75)
    for face in right:
        facecolor[face] = Color.pink().lightened(25)

viewer = App()
viewer.add(
    mesh,
    facecolor=facecolor,
    linecolor=Color.from_hex("#0092d2"),
)
viewer.view.camera.zoom_extents()
viewer.run()
