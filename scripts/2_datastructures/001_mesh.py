from compas.datastructures import Mesh
from compas.colors import Color
from compas_view2.app import App

mesh = Mesh.from_meshgrid(10, 10)

viewer = App()
viewer.add(mesh)
viewer.run()
