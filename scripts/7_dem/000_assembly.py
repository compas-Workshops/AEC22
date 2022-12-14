import os
import compas
from compas.geometry import Polygon
from compas.geometry import Scale
from compas.geometry import Pointcloud
from compas_assembly.datastructures import Assembly
from compas_assembly.datastructures import Block
from compas_assembly.algorithms import assembly_interfaces
from compas_assembly.viewer import DEMViewer

HERE = os.path.dirname(__file__)
GEOMETRY = os.path.join(HERE, "crossvault.json")
SESSION = os.path.join(HERE, "session.json")

meshes = compas.json_load(GEOMETRY)

# =============================================================================
# Scale
# =============================================================================

for mesh in meshes:
    mesh.transform(Scale.from_factors([1e-2, 1e-2, 1e-2]))

# =============================================================================
# Assemble
# =============================================================================

assembly = Assembly()
for mesh in meshes:
    block = mesh.copy(cls=Block)
    assembly.add_block(block)

# =============================================================================
# Interfaces
# =============================================================================

# we should make tmax dependent from the block size, as a default...
assembly_interfaces(assembly, nmax=20, tmax=1e-3, amin=1e-2)

# =============================================================================
# Export
# =============================================================================

compas.json_dump(assembly, SESSION)

# =============================================================================
# Viz
# =============================================================================

viewer = DEMViewer()

viewer.add_assembly(assembly)

viewer.run()
