import os

import compas

from compas_assembly.datastructures import Assembly
from compas_assembly.viewer import DEMViewer

from compas_cra.datastructures import CRA_Assembly
from compas_cra.algorithms import assembly_interfaces_numpy
from compas_cra.equilibrium import cra_penalty_solve

GEOMETRY = os.path.join(os.path.dirname(__file__), "shelf.json")
SESSION = os.path.join(os.path.dirname(__file__), "session.json")

# =============================================================================
# Blocks
# =============================================================================

assembly: Assembly = compas.json_load(GEOMETRY)
assembly: CRA_Assembly = assembly.copy(cls=CRA_Assembly)
assembly.set_boundary_conditions([0])

# =============================================================================
# Interfaces
# =============================================================================

assembly_interfaces_numpy(assembly, amin=1e-6, tmax=1e-4)

# =============================================================================
# Equilibrium
# =============================================================================

mu = 0.9
dispbnd = 1e-1
overlap = 1e-3
d = 1

cra_penalty_solve(assembly, verbose=True, density=d, d_bnd=dispbnd, eps=overlap, mu=mu)

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
