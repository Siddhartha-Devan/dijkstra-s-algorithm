# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 18:51:44 2022

@author: Siddhartha Devan V
"""

#import numpy as np
# no_of_nodes = int(input("enter the number of nodes\n"))
# initial_matrix = np.zeros((no_of_nodes,no_of_nodes), int)
# print(initial_matrix)

no_of_nodes = int(input("enter the number of nodes\n"))
def matrix_builder(no_of_nodes):
    initial_matrix = []
    for _ in range(0, no_of_nodes):
        initial_matrix.append([None]*no_of_nodes)
    print(initial_matrix)  #initializes a square matrix with all elements as zero
    # initial_matrix = np.zeros((no_of_nodes,no_of_nodes))
# gets input from the user...
# limiter is set because it is enough to fill either the upper or the lower triangle of the matrix since both of them ar the same
    # print(initial_matrix) 
 
    limiter = 1
    for i in range(len(initial_matrix)):
        for j in range(0,limiter):
            dist = int(input(f"Enter the distance between the nodes {i} and {j}\n"))
            if dist == 0:
                dist = None
            initial_matrix[i][j] = dist
            initial_matrix[j][i] = dist
        limiter += 1
    
    return initial_matrix
    
graph =  matrix_builder(no_of_nodes)
print("the graph is\n",graph)

target_node = int(input("Enter the target node:\n"))

def dijkstras(graph, target_node):               
    current_node = 0
    traversed_nodes = []
    all_nodes = []
    distance_travelled = 0
    possible_nodes = [None]*no_of_nodes
    all_nodes.append(possible_nodes)
    print("distance travelled = ", distance_travelled)
    print("cur node = ", current_node)
    print(possible_nodes)
    while current_node != target_node:
        for i in range(no_of_nodes):
            a = graph[current_node][i]
            if a != None:
                a = a+distance_travelled
                # if possible_nodes.index(a) not in traversed_nodes:
                if i not in traversed_nodes:
                    if possible_nodes[i] == None:
                        possible_nodes[i] = a 
                    elif a >= possible_nodes[i]:
                        print("a is greater")
                    elif a < possible_nodes[i]:
                        possible_nodes[i] = a 
                        
    
        all_nodes.append([[current_node],possible_nodes.copy()])
        traversed_nodes.append(current_node)
        possible_nodes[current_node] = None
        # for j in range(len(possible_nodes)):
        #     if j not in traversed_nodes:
        #         if possible_nodes[j] != np.NaN:
                    
        pos_nodes_without_none =[]
        for i in possible_nodes:
            if i != None:
                pos_nodes_without_none.append(i)
        current_node = possible_nodes.index(min(pos_nodes_without_none))
        distance_travelled = min(pos_nodes_without_none)
        print(possible_nodes)
        print("distance travelled = ", distance_travelled)
        print("cur node = ", current_node)
    
    print(distance_travelled)
    print("the all_nodes list is---")
    all_nodes.append([[current_node],possible_nodes.copy()])
    
    all_nodes = all_nodes[::-1]
    for i in all_nodes:
        print(i)
    
    try:
        pointer = all_nodes[0][0][0]
        i = 0
        path = []
        path.append(pointer)
        while i < len(all_nodes)-1:
            print(i)
            if all_nodes[i][1][pointer] == all_nodes[i+1][1][pointer]:
                print("yess", all_nodes[i][1][pointer], all_nodes[i+1][1][pointer])
                i += 1
                
            else:
                pointer = all_nodes[i][0][0]
                path.append(pointer)
                i += 1
                
            print(path)
    except TypeError:
        path.append(0)
        print(path[::-1])
            
print(dijkstras(graph, target_node))

















