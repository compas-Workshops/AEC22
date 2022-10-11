import compas
from compas.geometry import Box
from compas.geometry import Frame

box = Box(Frame.worldXY(), 1, 1, 1)

print(box.guid)
print(box.data)

print(compas.json_dumps(box))
