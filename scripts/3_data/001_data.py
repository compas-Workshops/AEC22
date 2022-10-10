import compas
from compas.geometry import Box
from compas.geometry import Frame

box1 = Box(Frame.worldXY(), 1, 1, 1)
box2: Box = compas.json_loads(compas.json_dumps(box1))

print(box1.guid)
print(box2.guid)
