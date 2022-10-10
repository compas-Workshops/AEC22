from compas.geometry import Box
from compas.geometry import Frame

box1 = Box(frame=Frame.worldXY(), xsize=1, ysize=1, zsize=1)
box2 = Box.from_width_height_depth(1, 1, 1)

print(box1)
print(box2)
