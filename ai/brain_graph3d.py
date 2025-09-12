import numpy as np
import plotly.graph_objects as go

class BrainGraph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.arrows = []

    def add_nodes(self, pos, colors):
        self.nodes.append(go.Scatter3d(x = [pos[n][0] for n in pos],
                                       y = [pos[n][1] for n in pos],
                                       z = [pos[n][2] for n in pos],
                                       mode = "markers",
                                       marker = dict(size = 8, color = [colors[n] for n in pos]),
                                       text = list(pos.keys()),
                                       hoverinfo = "text"))

    def add_edge(self, pos1, pos2, text: str, color, width: float, with_arrow: bool = True):
        if (all(np.isclose(pos1, pos2))):
            return

        self.edges.append(go.Scatter3d(x = [pos1[0], pos2[0]],
                                       y = [pos1[1], pos2[1]],
                                       z = [pos1[2], pos2[2]],
                                       mode = "lines",
                                       text = text,
                                       line = dict(color = color, width = width)))

        if (with_arrow):
            self.arrows.append(go.Cone(x = [pos2[0]], y = [pos2[1]], z = [pos2[2]],
                                       u = [pos2[0] - pos1[0]], v = [pos2[1] - pos1[1]], w = [pos2[2] - pos1[2]],
                                       colorscale = [[0, color], [1, color]],
                                       sizemode = "absolute", sizeref = 0.1 * width, anchor = "tip"))

    def show(self):
        fig = go.Figure(data = self.nodes + self.edges + self.arrows)
        fig.update_layout(scene = dict(aspectmode = "cube"))
        fig.show()
