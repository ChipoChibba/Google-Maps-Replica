# Author:Chipo
# Date:11/12/2022
# Purpose:Lab 4

from vertex import Vertex


def load_graph(filename):
    fp = open(filename, "r")
    dictionary = {}

    for line in fp:  # making objects that are referred to by the vertex names in dictionary
        information = line.split(";")
        name = information[0]
        coordinates = information[2].strip().split(",")

        v = Vertex(name, int(coordinates[0]), int(coordinates[1]))

        dictionary[name] = v

    fp.close()

    fp = open(filename, "r")

    for line in fp:  # appending adjacent members to list of created objects
        information = line.split(";")
        name = information[0]
        adjacent_member = information[1].strip().split(",")

        adjacent = []
        for a in adjacent_member:
            if a:
                a = a.strip()  # cleaning white spaces around a
                a = dictionary[a]
                adjacent.append(a)

        dictionary[name].adjacency_list = adjacent

    fp.close()

    return dictionary
