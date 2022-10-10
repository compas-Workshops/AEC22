import os
import compas

filepath = os.path.join(os.path.dirname(__file__), "box.json")
box = compas.json_load(filepath)

print(box)
