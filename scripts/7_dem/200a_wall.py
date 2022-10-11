import compas_rhino
from compas_rhino.conversions import RhinoCurve
from compas.artists import Artist

# compas_rhino.clear()

guid = compas_rhino.select_curve()

curve = RhinoCurve.from_guid(guid).to_compas()

artist = Artist(curve, layer="Wall::Curve")
artist.draw()
