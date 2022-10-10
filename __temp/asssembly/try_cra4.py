import os
import compas

from compas_assembly.datastructures import Assembly
from compas_assembly.viewer import DEMViewer

from compas_cra.geometry import Arch
from compas_cra.algorithms import assembly_interfaces_numpy
from compas_cra.equilibrium import cra_solve

# =============================================================================
# Blocks
# =============================================================================

height = 5
span = 10
thickness = 0.5
depth = 0.5
num_blocks = 20

assembly = Arch(
    height=height,
    span=span,
    thickness=thickness,
    depth=depth,
    num_blocks=num_blocks,
    extra_support=False,
).assembly()

# =============================================================================
# Interfaces
# =============================================================================

assembly_interfaces_numpy(assembly, nmax=10, amin=1e-2, tmax=1e-2)

# =============================================================================
# Equilibrium
# =============================================================================

cra_solve(assembly, mu=0.7, verbose=True, timer=True)

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
