from compas.geometry import Frame, Box
from compas_view2.app import App

world = Frame.worldXY()
box = Box(world, 0.8, 0.5, 0.3)

frame = Frame([1, 1, 0], [1, 0, 0], [0, 0, 1])

# =============================================================================
# Viz
# =============================================================================

viewer = App()
viewer.view.camera.position = [2, -3, 1]
viewer.view.camera.target = [0, 1, 0]

viewer.add(box)
viewer.add(box.frame, linewidth=5, size=0.5)
viewer.add(frame, linewidth=5, size=0.5)

viewer.run()
