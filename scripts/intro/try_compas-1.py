from compas.geometry import Box
from compas.geometry import Polygon

box = Box.from_width_height_depth(1, 1, 1)

for name in dir(box):
    if not name.startswith('_'):
        print(name)

print(box.area)
print(box.volume)
print(box.dimensions)
print(box.edges)
print(box.faces)
print(box.points)

polygons = []
for face in box.faces:
    polygon = Polygon([box.points[index] for index in face])
    polygons.append(polygon)

for polygon in polygons:
    print(polygon.area)
