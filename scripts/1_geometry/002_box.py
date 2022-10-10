from compas.geometry import Box

box1 = Box.from_width_height_depth(1, 1, 1)
box2 = Box.from_corner_corner_height([0, 0, 0], [1, 1, 0], 1)
box3 = Box.from_diagonal([[0, 0, 0], [1, 1, 1]])

print(box1)
print(box2)
print(box3)
