import os
import compas
from compas.colors import Color
from compas.geometry import Point, Line, Polygon
from compas_assembly.algorithms import assembly_interfaces

from compas_view2.app import App

FILE = os.path.join(os.path.dirname(__file__), "wall.json")

# =============================================================================
# Import
# =============================================================================

wall = compas.json_load(FILE)

# =============================================================================
# Assembly
# =============================================================================

assembly = wall["assembly"]

# =============================================================================
# Interfaces
# =============================================================================

assembly_interfaces(assembly, tmax=1e-6, amin=1e-2)

# =============================================================================
# Export
# =============================================================================

wall["assembly"] = assembly

compas.json_dump(wall, FILE)

# =============================================================================
# Viz
# =============================================================================

viewer = App()
viewer.view.camera.position = [-4, -6, 2]
viewer.view.camera.target = [3, 0, 1]

for node in assembly.graph.nodes():
    block = assembly.graph.node_attribute(node, "block")
    point = Point(*block.centroid())

    viewer.add(point)
    viewer.add(block, facecolor=Color.grey().lightened(50), linecolor=Color.grey(), opacity=0.5)

for edge in assembly.graph.edges():
    interfaces = assembly.graph.edge_attribute(edge, "interfaces")
    for interface in interfaces:
        polygon = Polygon(interface.points)
        viewer.add(polygon)

    a = assembly.graph.node_attribute(edge[0], "block").centroid()
    b = assembly.graph.node_attribute(edge[1], "block").centroid()
    line = Line(a, b)
    viewer.add(line, linewidth=3)

viewer.run()
