# Author:Chipo
# Date:11/12/2022
# Purpose:Lab 4 checkpoint

from cs1lib import *

R = 5
line_wid = 5
boundary=7

class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.adjacency_list = []

    def __str__(self):
        return self.name + "; " + "Location: " + str(self.x) + ", " + str(self.y) + "; " + "Adjacent vertices: " \
               + ", ".join(str(member.name) for member in self.adjacency_list)

    def draw_vertex(self, r, g, b):
        set_fill_color(r, g, b)
        set_stroke_color(r, g, b)

        # labelling vertex on map
        draw_circle(self.x, self.y, R)

    def draw_edge(self, other_vertex, r, g, b):
        set_stroke_width(line_wid)

        # drawing edge
        other_vertex.draw_vertex(r, g, b)
        draw_line(self.x, self.y, other_vertex.x, other_vertex.y)

    def all_edges(self, r, g, b):
        i = 0

        while i < len(self.adjacency_list):
            self.draw_edge(self.adjacency_list[i], r, g, b)
            i = i + 1

    def in_region(self, x, y):
        if x in range(self.x - boundary, self.x + boundary):
            if y in range(self.y - boundary, self.y + boundary):
                return True
