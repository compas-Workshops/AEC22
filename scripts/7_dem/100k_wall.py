import os
import compas
from compas_assembly.viewer import DEMViewer

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

# =============================================================================
# Export
# =============================================================================

wall["assembly"] = assembly

compas.json_dump(wall, FILE)

# =============================================================================
# Viz
# =============================================================================

viewer = DEMViewer()
viewer.view.camera.position = [-4, -6, 2]
viewer.view.camera.target = [3, 0, 1]

viewer.add_assembly(assembly)

viewer.run()
