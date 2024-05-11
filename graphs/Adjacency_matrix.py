# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 09:48:24 2022

@author: raman
"""

class graph:
    def __init__(self,no_vertices):
        self.adj_matrix = [[-1]*no_vertices for x in range(no_vertices)]
        self.no_vertices = no_vertices # capacity of vertices
        self.vertices = {} # a set to maintain unique vertices only
        self.vertices_list = [0]*no_vertices
        
    def set_vertex(self,vtx, id):
        #vetrex ->(0to 6), and id is vertex id
        if 0<= vtx <= self.no_vertices:
            self.vertices[id] = vtx
            self.vertices_list[vtx] = id
            
    