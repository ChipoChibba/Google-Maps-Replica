# Author:Chipo
# Date:11/12/2022
# Purpose:Lab 4

from cs1lib import *
from load_graph import *
from vertex import Vertex
from breadth_for_search import BFS

W = 1012
H = 811
mpressed = False
start = None
goal = None
dictionary = load_graph("dartmouth_graph.txt")


def mymouse_press(mx, my):
    global start, mpressed
    mpressed = True

    for i in dictionary:
        if dictionary[i].in_region(mx, my):
            start = dictionary[i]


def mymouse(mx, my):
    global goal, mpressed

    if mpressed:
        for i in dictionary:
            if dictionary[i].in_region(mx, my):
                goal = dictionary[i]


def main_draw():
    global start, goal, mpressed

    img = load_image("dartmouth_map.png")
    draw_image(img, 0, 0)

    for i in dictionary:
        dictionary[i].all_edges(1, 0, 0)

    if mpressed and start is not None:
        if goal is not None:
            start.draw_vertex(0, 0, 1)
            goal.draw_vertex(0, 0, 1)

            path = BFS(start, goal)
            i = 0
            j = i + 1
            while j < len(path):
                path[i].draw_edge(path[j], 0, 0, 1)
                i = i + 1
                j = j + 1


start_graphics(main_draw, width=W, height=H, mouse_press=mymouse_press, mouse_move=mymouse)
