from typing import List
import os
import compas
from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Translation
from compas.colors import Color
from compas_assembly.datastructures import Assembly
from compas_assembly.datastructures import Block
from compas_assembly.datastructures import Interface
from compas_cra.datastructures import CRA_Assembly
from compas_cra.equilibrium import cra_solve
from compas_view2.app import App
from compas_view2.objects import Collection

support = Box(Frame.worldXY(), 1, 1, 1)
free1 = support.transformed(Translation.from_vector([0, 0, 1]))

assembly = CRA_Assembly()
assembly.add_block(Block.from_shape(support), node=0)
assembly.add_block(Block.from_shape(free1), node=1)
assembly.set_boundary_conditions([0])

polygon = [support.points[i] for i in support.top]
interface1 = Mesh.from_polygons([polygon])

assembly.add_interfaces_from_meshes([interface1], 0, 1)

cra_solve(assembly, verbose=True, timer=True, density=1)

# =============================================================================
# Export
# =============================================================================

assembly = assembly.copy(cls=Assembly)

session = {"assembly": assembly}
filepath = os.path.join(os.path.dirname(__file__), "session.json")

compas.json_dump(session, filepath)

# =============================================================================
# Viz
# =============================================================================

viewer = App()

for node in assembly.graph.nodes():
    block = assembly.graph.node_attribute(node, "block")

    if assembly.graph.node_attribute(node, "is_support"):
        color = Color.red()
    else:
        color = Color.grey()

    viewer.add(
        block,
        facecolor=color.lightened(50),
        linecolor=color,
        linewidth=2,
        opacity=0.5,
    )

for edge in assembly.graph.edges():
    interfaces: List[Interface] = assembly.graph.edge_attribute(edge, "interfaces")
    for interface in interfaces:
        viewer.add(interface.polygon)

contactforces = []
frictionforces = []

for edge in assembly.graph.edges():
    interfaces: List[Interface] = assembly.graph.edge_attribute(edge, "interfaces")
    for interface in interfaces:
        contactforces += interface.contactforces
        frictionforces += interface.frictionforces

viewer.add(Collection(contactforces), linewidth=3, linecolor=Color.blue())
viewer.add(Collection(frictionforces), linewidth=3, linecolor=Color.cyan())

viewer.run()
