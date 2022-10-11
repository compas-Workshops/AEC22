import os
import compas
from compas.geometry import Frame
from compas.geometry import Transformation
from compas.datastructures import Mesh

mesh = Mesh.from_obj(compas.get("tubemesh.obj"))
mesh.update_default_face_attributes(box=None)

filepath = os.path.join(os.path.dirname(__file__), "box.json")
box = compas.json_load(filepath)

for face in mesh.face_sample(size=17):
    plane = mesh.face_plane(face)
    frame = Frame.from_plane(plane)
    transform = Transformation.from_frame_to_frame(box.frame, frame)

    mesh.face_attribute(face, "box", box.transformed(transform))

filepath = os.path.join(os.path.dirname(__file__), "mesh.json")
compas.json_dump(mesh, filepath)
