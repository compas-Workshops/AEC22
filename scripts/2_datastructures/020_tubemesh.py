import compas
from compas.datastructures import Mesh
from compas_view2.app import App

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))
mesh.quads_to_triangles()

viewer = App()
viewer.add(mesh)
viewer.view.camera.zoom_extents()
viewer.run()
