import os
import compas
from compas.geometry import Box
from compas.geometry import Frame

box = Box(Frame.worldXY(), 1, 1, 1)

filepath = os.path.join(os.path.dirname(__file__), "box.json")
compas.json_dump(box, filepath)
