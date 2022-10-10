import os
import compas

filepath = os.path.join(os.path.dirname(__file__), "mesh.json")

mesh = compas.json_load(filepath)

print(mesh)
