import compas
from compas.datastructures import Mesh
from compas.colors import Color

from compas_view2.app import App

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))

edges = mesh.edge_sample()
strip = mesh.edge_strip(edges[0])
faces = [mesh.halfedge_face(u, v) for u, v in strip]

facecolor = {face: Color.from_hex("#0092d2").lightened(50) for face in mesh.faces()}
for face in faces:
    facecolor[face] = Color.pink().lightened(50)

viewer = App()
viewer.add(
    mesh,
    facecolor=facecolor,
    linecolor=Color.from_hex("#0092d2"),
)
viewer.view.camera.zoom_extents()
viewer.run()
