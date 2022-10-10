from typing import List
import os
import compas
from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Translation
from compas.geometry import Line
from compas.geometry import Polygon
from compas.geometry import Point
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

session = {"assembly": assembly.copy(cls=Assembly)}
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
        polygon = Polygon(interface.points)
        viewer.add(polygon)

contactforces = []
friction = []

for edge in assembly.graph.edges():
    interfaces: List[Interface] = assembly.graph.edge_attribute(edge, "interfaces")
    for interface in interfaces:
        forces = interface.forces
        if forces is None:
            continue

        frame: Frame = interface.frame
        w, u, v = frame.zaxis, frame.xaxis, frame.yaxis
        for i, point in enumerate(interface.points):
            point = Point(*point)

            force = forces[i]["c_np"] - forces[i]["c_nn"]
            p1 = point + w * force * 0.5
            p2 = point - w * force * 0.5
            contactforces.append(Line(p1, p2))

            ft_uv = (u * forces[i]["c_u"] + v * forces[i]["c_v"]) * 0.5
            p1 = point + ft_uv
            p2 = point - ft_uv
            friction.append(Line(p1, p2))

viewer.add(Collection(contactforces), linewidth=3, linecolor=Color.blue())
viewer.add(Collection(friction), linewidth=3, linecolor=Color.cyan())

viewer.run()
