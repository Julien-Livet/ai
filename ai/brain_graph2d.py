from graph_tool.all import Graph, graph_draw
import math
from matplotlib.colors import to_rgb

class BrainGraph:
    def __init__(self):
        self.g = Graph(directed = True)
        self.v_color = self.g.new_vertex_property("vector<float>")
        self.v_label = self.g.new_vertex_property("string")
        self.v_label_color = self.g.new_vertex_property("vector<float>")
        self.e_color = self.g.new_edge_property("vector<float>")
        self.e_width = self.g.new_edge_property("float")
        self.e_label = self.g.new_edge_property("string")
        self.vertices = []
        self.pos_to_vtx = {}

    def add_node(self, label: str = '', color = (1,0,0)):
        v = self.g.add_vertex()
        self.vertices.append(v)
        self.v_color[v] = to_rgb(color)
        self.v_label[v] = label
        self.v_label_color[v] = tuple(1.0 - c for c in to_rgb(color))

        return v

    def add_nodes(self, pos, colors):
        for k, v in colors.items():
            self.pos_to_vtx[pos[k]] = self.add_node(k, v)

    def add_edge(self, source_pos, target_pos, label: str = '', color = (0,0,0), width: float = 1.0):
        source_vtx = self.pos_to_vtx[source_pos]
        target_vtx = self.pos_to_vtx[target_pos]

        e = self.g.add_edge(source_vtx, target_vtx)
        self.e_color[e] = to_rgb(color)
        self.e_width[e] = width
        self.e_label[e] = label
        
        return e

    def show(self):
        """
        from graph_tool.draw import sfdp_layout

        pos = sfdp_layout(self.g)
        """
        
        pos = self.g.new_vertex_property("vector<double>")

        R = 100.0

        for i, v in enumerate(self.vertices):
            angle = 2 * math.pi * i / len(self.vertices)
            x = R * math.cos(angle)
            y = R * math.sin(angle)
            pos[v] = [x, y]
        
        graph_draw(
            self.g,
            pos = pos,
            vertex_fill_color = self.v_color,
            vertex_text = self.v_label,
            vertex_text_color = self.v_label_color,
            edge_color = self.e_color,
            edge_pen_width = self.e_width,
            edge_text = self.e_label
        )
