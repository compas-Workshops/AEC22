from compas.geometry import Point
from compas.geometry import Box
from compas.geometry import Sphere
from compas.geometry import is_coplanar
from compas.datastructures import Mesh
from compas.datastructures import mesh_merge_faces
from compas.utilities import geometric_key

from compas_view2.app import App

from compas_cgal.booleans import boolean_union
from compas_cgal.meshing import remesh

# ==============================================================================
# Make a box
# ==============================================================================

box = Box.from_width_height_depth(2, 2, 2)
box = Mesh.from_shape(box)
box.quads_to_triangles()

A = box.to_vertices_and_faces()

# ==============================================================================
# Make a sphere
# ==============================================================================

sphere = Sphere(Point(1, 1, 1), 1)
sphere = Mesh.from_shape(sphere, u=32, v=32)
sphere.quads_to_triangles()

B = sphere.to_vertices_and_faces()

# ==============================================================================
# Remesh the sphere
# ==============================================================================

B = remesh(B, 0.3, 50)

# ==============================================================================
# Compute the boolean mesh
# ==============================================================================

V, F = boolean_union(A, B)

mesh = Mesh.from_vertices_and_faces(V, F)

# ==============================================================================
# Merge coplanar faces
# ==============================================================================

while True:
    has_merged = False
    for edge in mesh.edges():
        a, b = mesh.edge_faces(*edge)
        if a is not None and b is not None:
            points = mesh.face_coordinates(a)
            points += mesh.face_coordinates(b)
            if is_coplanar(points, tol=1e-16):
                face = mesh_merge_faces(mesh, [a, b])
                has_merged = True
                break

    if not has_merged:
        break

# ==============================================================================
# Visualize
# ==============================================================================

viewer = App()

viewer.add(mesh, show_faces=True, linewidth=2)

viewer.run()
