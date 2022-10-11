import os
import compas
from compas.datastructures import Mesh
from compas_view2.app import App

filepath = os.path.join(os.path.dirname(__file__), "mesh.json")
mesh: Mesh = compas.json_load(filepath)

viewer = App()
viewer.add(mesh)
for face in mesh.faces():
    box = mesh.face_attribute(face, 'box')
    if box:
        viewer.add(box)

viewer.view.camera.zoom_extents()
viewer.run()