import os
import compas
from compas.colors import Color
from compas.geometry import Point
from compas_assembly.datastructures import Assembly
from compas_assembly.datastructures import Block

from compas_view2.app import App

FILE = os.path.join(os.path.dirname(__file__), 'wall.json')

# =============================================================================
# Import
# =============================================================================

wall = compas.json_load(FILE)

# =============================================================================
# Assembly
# =============================================================================

assembly = Assembly()

for course in wall['courses']:
    for box in course:
        block = Block.from_shape(box)
        assembly.add_block(block)

# =============================================================================
# Export
# =============================================================================

wall['assembly'] = assembly

compas.json_dump(wall, FILE)

# =============================================================================
# Viz
# =============================================================================

viewer = App()
viewer.view.camera.position = [-4, -6, 2]
viewer.view.camera.target = [3, 0, 1]

for node in assembly.graph.nodes():
    block = assembly.graph.node_attribute(node, 'block')
    point = Point(*block.centroid())

    viewer.add(point)
    viewer.add(block, facecolor=Color.grey().lightened(50), linecolor=Color.grey(), opacity=0.5)

viewer.run()
