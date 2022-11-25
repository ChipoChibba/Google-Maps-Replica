# Author:Chipo
# Date:11/12/2022
# Purpose:Lab 4

from collections import deque
from vertex import Vertex


def BFS(start, goal):
    back_pointer = {}
    back_pointer[start] = None
    frontier = deque()
    frontier.append(start)

    while len(frontier) != 0:
        curr_v = frontier.popleft()
        if curr_v == goal:
            break

        else:
            for adj in curr_v.adjacency_list:
                if adj not in back_pointer:
                    frontier.append(adj)
                    back_pointer[adj] = curr_v

        if goal in back_pointer:
            break

    path = []
    v = goal

    while v is not None:
        path.append(v)
        v = back_pointer[v]

    return path
