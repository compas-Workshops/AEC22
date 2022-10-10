import compas
from compas.datastructures import Mesh
from compas.geometry import Point
from compas.colors import Color
from compas_view2.app import App

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))
vertex = mesh.vertex_sample(size=1)[0]
nbrs = mesh.vertex_neighbors(vertex)

viewer = App()

viewer.add(mesh)

viewer.add(Point(*mesh.vertex_coordinates(vertex)), pointsize=20)
for nbr in nbrs:
    viewer.add(
        Point(*mesh.vertex_coordinates(nbr)),
        pointcolor=Color.pink(),
        pointsize=20,
    )

viewer.view.camera.zoom_extents()
viewer.run()
