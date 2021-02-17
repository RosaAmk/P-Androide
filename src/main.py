# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 20:51:21 2021

@author: roza
"""
from agent import Agent
from graph_alea import Graph

from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

nb_agent = 200
nb_it =  500
class Env():
    def __init__(self):
        self.R1 = 200000
        self.R2 = 200000
        

def gen_from_density(n,d): 
    g1 = Graph(n,d)
    g = []
    for i in range(n):
        g.append(Agent())
    g1.gen_graph()
    for e in g1.edges_final:
        g[e[0]].add_neighbour(g[e[1]])
        g[e[1]].add_neighbour(g[e[0]])
    return g

def gen_star(n):
    g = []
    center = Agent()
    g.append(center)
    for i in range(n-1):
        new = Agent()
        new.add_neighbour(center)
        center.add_neighbour(new)
        g.append(new)
    return g

def gen_complet(n):
    g = []
    for i in range(n):
        g.append(Agent())
    for i in range(n):
        g[i].add_neighbours(g[0:i])
        g[i].add_neighbours(g[i+1:n])
    return g
    
def gen_ring(n):
    g = []
    prec = 0
    for i in range(n):
        current = Agent()
        g.append(current)
        if prec != 0:
            prec.add_neighbour(current)
            current.add_neighbour(prec)
        prec = current
    g[0].add_neighbour(g[n-1])
    g[n-1].add_neighbour(g[0])
    return g
def gen_chaine(n):
    g = []
    prec = 0
    for i in range(n):
        current = Agent()
        g.append(current)
        if prec != 0:
            prec.add_neighbour(current)
            current.add_neighbour(prec)
        prec = current
    return g
        
if __name__ == '__main__':
 
    print("~~~~~~~~random~~~~~~~~")
    sp = 2*[0]
    for j in range(10):
        c = Counter()
        env = Env()
        graph = gen_from_density(nb_agent,  10/nb_agent)
        i = 0
        boole = False
        for i in range(nb_it):
            i += 1
            for a in graph:
                a.move()
                a.compute_fitness(env, i)
                a.broadcast()
            for a in graph:
                a.apply_variation_fitness_prop()
        h = 3*[0]
        for a in graph:
            h[a.get_group()] += 1
            c[round(a.g_skill,1)] += 1
        if h[0]> 0.6*nb_agent or h[1]> 0.6*nb_agent:
            sp[0] += 1
        else:
            sp[1] += 1

        labels, values = zip(*sorted(c.items()))
        indexes = np.arange(len(labels))

        plt.bar(indexes, values)
        plt.xticks(indexes , labels)
        plt.show()
    print(sp)
   
            