import compas
from compas.datastructures import Mesh
from compas.geometry import Point
from compas.geometry import Sphere
from compas_occ.brep import BRep
from compas.colors import Color
from compas_view2.app import App

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))
vertex = mesh.vertex_sample(size=1)[0]
nbrs = mesh.vertex_neighbors(vertex)

viewer = App()

viewer.add(mesh)

viewer.add(
    BRep.from_sphere(Sphere(Point(*mesh.vertex_coordinates(vertex)), 0.2)),
    facecolor=Color.from_hex("#0092d2").lightened(50),
    linecolor=Color.from_hex("#0092d2"),
)
for nbr in nbrs:
    viewer.add(
        BRep.from_sphere(Sphere(Point(*mesh.vertex_coordinates(nbr)), 0.2)),
        facecolor=Color.pink().lightened(50),
        linecolor=Color.pink(),
    )

viewer.view.camera.zoom_extents()
viewer.run()
