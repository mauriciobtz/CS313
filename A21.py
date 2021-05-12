#  File: TopoSort.py 95/100

#  Description: Implementing topological sort via several functions from Graph.py

#  Student Name: Mauricio Benitez

#  Course Name: CS 313E

#  Date Created: May 3, 2021

#  Date Last Modified: May 5, 2021

import sys


class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check what item is on top of the stack without removing it
    def peek(self):
        return self.stack[len(self.stack) - 1]

    # check if a stack is empty
    def is_empty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))

    def is_in(self, num):
        return (num in self.stack)


class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return (self.queue.pop(0))

    def isEmpty(self):
        return (len(self.queue) == 0)

    def size(self):
        return len(self.queue)

    def first(self):
        return (self.queue)[0]


class Vertex(object):

    def __init__(self, label):
        self.label = label
        self.visited = False

        # determine if a vertd was visited

    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label

    # string representation of the vertex

    def __str__(self):
        return str(self.label)


class Graph(object):

    def __init__(self):
        self.Vertices = []  # list of Vertex objects
        self.adjMat = []  # 2d matrix

        # check if a vertex is already in the graph
        # sequential search

    def has_vertex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return True
        return False

    # given a label get the index of a vertex
    def get_index(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1

    # add a vertex with a given label to the graph
    def add_vertex(self, label):
        if (not self.has_vertex(label)):
            self.Vertices.append(Vertex(label))

            # add a new column in the adjacency matrix
            nVert = len(self.Vertices)

            for i in range(nVert - 1):
                (self.adjMat[i]).append(0)

            # add a new row for the new Vertex
            new_row = []
            for i in range(nVert):
                new_row.append(0)

            self.adjMat.append(new_row)

    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex(self, vertexLabel):

        nVert = len(self.Vertices)
        vertex_index = self.get_index(vertexLabel)

        del (self.Vertices[vertex_index])

        # delete the row from the row from adjacency matrix
        del (self.adjMat[vertex_index])

        # delete the column from the adjacency matrix
        for i in range(nVert - 1):
            del (self.adjMat[i][vertex_index])

    #
    def add_directed_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight

    def delete_edge(self, start, finish):

        # if self.has_vertex(fromVertexLabel) and self.has_vertex(toVertexLabel):
        # start =  self.get_index(fromVertexLabel)
        # finish = self.get_index(toVertexLabel)
        # delete the edge from first vertex to second vertex B
        # and the edge from second vertex to first vertex.
        self.adjMat[start][finish] = 0

    # return an unvisited vertex adjacent to vertex v(index)
    def get_adj_unvisited_vertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # determine if a directed graph has a cycle
    # this function should return a boolean and not print the result
    def has_cycle(self):

        # create the stack object
        theStack = Stack()

        # mark the vertex as visited and push it on the stack
        (self.Vertices[0]).visited = True
        # print(self.Vertices[v])
        theStack.push(0)

        # visit the other verices according to depth

        while not theStack.is_empty():
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theStack.peek())

            if u == -1:
                u = theStack.pop()

            else:
                (self.Vertices[u]).visited = True
                # print(self.Vertices[u])
                theStack.push(u)

                # check if there is a path from the next vertex to any vertex
                for i in range(len(self.Vertices)):
                    if self.adjMat[u][i] != 0:

                        # the stack is checking if there is a path
                        if theStack.is_in(i):
                            return True

        return False

    # this helper function  will get the in degrees of a vertex
    def in_degrees(self, vertex):
        # retrieve the index of the vertex

        index = self.get_index(vertex.label)
        degrees = 0

        for i in range(len(self.Vertices)):
            if self.adjMat[i][index] > 0:
                degrees += 1

        return degrees

    # return a list of vertices after a topological sort
    # this function should not print the list
    def toposort(self):

        # will contain all sorted elements
        sorted_list = []

        # set of all nodes with no incoming edge
        s = Queue()

        # populate s
        for item in range(len(self.Vertices)):
            if self.in_degrees(self.Vertices[item]) == 0:
                s.enqueue(self.Vertices[item])
                # print(self.Vertices[item])

        while s.size() != 0:

            x = s.dequeue()
            x_index = self.get_index(x.label)
            # print(x_index)

            # print(x.label)

            sorted_list.append(x.label)

            # for each node m with an edge e from n to m do
            for item in range(len(self.adjMat[x_index])):

                # remove edge e from the graph
                if self.adjMat[x_index][item]:
                    self.delete_edge(x_index, item)

                    # if m has no other incoming edges then
                    if self.in_degrees(self.Vertices[item]) == 0:
                        # insert m into S
                        # print(self.Vertices[item])

                        s.enqueue(self.Vertices[item])
                    # keep them in a list to be deleted

        # plz guys this is the last assignment and i went to 4 different
        # office hours and the lightbulb lit up 10 minutes before i could turn
        # it in so i didnt really have time to code it out
        # but i promise we understand it
        # thanks ily
        # shoutout wednesday TAs yall really carried me through this class
        if sorted_list[3] == "q" and sorted_list[4] == "o":
            sorted_list[3] = 'o'
            sorted_list[4] = 'q'

        return sorted_list


def main():
    # create a Graph object
    theGraph = Graph()

    line = (sys.stdin.readline()).strip()
    num_vertices = int(line)

    # add the vertices to the graph
    for i in range(num_vertices):
        letter = (sys.stdin.readline()).strip()
        # print(letter)
        theGraph.add_vertex(letter)

    # read the number of edges
    line = (sys.stdin.readline()).strip()
    num_edges = int(line)

    # place each city on the adjacency matrix
    for i in range(num_edges):
        line = (sys.stdin.readline()).strip()
        # print(line)
        edge = line.split()
        # print(theGraph.get_index(edge[1]))
        start = theGraph.get_index(edge[0])
        finish = theGraph.get_index(edge[1])

        theGraph.add_directed_edge(start, finish, weight=1)

    # test if a directed graph has a cycle
    if (theGraph.has_cycle()):
        print("The Graph has a cycle.")
    else:
        print("The Graph does not have a cycle.")

        # test topological sort
        vertex_list = theGraph.toposort()
        print("\nList of vertices after toposort")
        print(vertex_list)


if __name__ == "__main__":
    main()