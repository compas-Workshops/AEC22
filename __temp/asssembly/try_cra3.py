from typing import List
import os

import compas
from compas.datastructures import Mesh
from compas.geometry import Box
from compas.geometry import Frame
from compas.geometry import Translation

from compas_assembly.datastructures import Assembly
from compas_assembly.datastructures import Block
from compas_assembly.viewer import DEMViewer

from compas_cra.datastructures import CRA_Assembly
from compas_cra.equilibrium import cra_solve

# =============================================================================
# Blocks
# =============================================================================

support = Box(Frame.worldXY(), 1, 1, 1)
free1 = support.transformed(Translation.from_vector([0, 0, 1]))

assembly = CRA_Assembly()
assembly.add_block(Block.from_shape(support), node=0)
assembly.add_block(Block.from_shape(free1), node=1)
assembly.set_boundary_conditions([0])

# =============================================================================
# Interfaces
# =============================================================================

polygon = [support.points[i] for i in support.top]
interface1 = Mesh.from_polygons([polygon])

assembly.add_interfaces_from_meshes([interface1], 0, 1)

# =============================================================================
# Equilibrium
# =============================================================================

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

viewer = DEMViewer()

viewer.add_assembly(assembly)

viewer.view.camera.zoom_extents()
viewer.run()
