import compas
from compas.datastructures import Mesh
from compas.artists import Artist
from compas.colors import Color


mesh = Mesh.from_obj(compas.get('tubemesh.obj'))


faces = mesh.face_sample(size=17)
face_color = {face: Color.pink() for face in faces}
face_text = {face: str(face) for face in faces}

vertices = mesh.vertex_sample(size=23)
vertex_color = {vertex: Color.pink() for vertex in vertices}
vertex_text = {vertex: str(vertex) for vertex in vertices}


Artist.clear()

artist = Artist(mesh)

artist.draw_faces(faces=faces, color=face_color)
artist.draw_vertices(vertices=vertices, color=vertex_color)
artist.draw_edges()

artist.draw_facelabels(text=face_text)
artist.draw_vertexlabels(text=vertex_text)

Artist.redraw()
