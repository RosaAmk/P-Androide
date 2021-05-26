# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 20:51:21 2021

@author: roza
"""
from agent import Agent
from gen_graph import Graph
import random
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import graphviz as pgv
import plot
from read_data import graph_sim
nb_agent = 100
nb_it = 20000
density=2/nb_agent
class Env():
    def __init__(self):
        self.R1 = 0
        self.R2 = 0  

def gen_from_density(n,d,method): 
    g1 = Graph(n,d)
    g = []
    for i in range(n):
        g.append(Agent(method))
    g1.gen_graph()
    graph = pgv.Digraph()
    for i in range(n):
        graph.node(str(g[i].g_skill))
    for e in g1.edges_final:
        graph.edge(str(g[e[0]].g_skill), str(g[e[1]].g_skill)) 
    return g, g1.edges_final


def gen_star(n, nb_branche, method):
    g = []

    for i in range(n):
        g.append(Agent(method))

    l = nb_branche*[-1]
    e = []
    d = 0
    for i in range(1,n):
        if l[d] == -1:
            e.append((0,i))
        else:
            e.append((l[d],i))
        l[d] = i
        d = (d+1)%nb_branche

    return g,e
def _2_complet(n, method):
    g = []

    for i in range(n):
        g.append(Agent(method))

    e = [(i,j) for i in range(n//2-1) for j in range(i+1,n//2)]+[(i,j) for i in range(n//2,n-1) for j in range(i+1,n)] + [(n//2-1,n//2)]
    #plot.draw_graph(g,e,"test.gv")
    return g,e

def gen_complet(n, method):
    g = []
    for i in range(n):
        g.append(Agent(method))
    e = [(i,j) for i in range(n) for j in range(i+1,n)]
    return g,e
    
def gen_ring(n, method):
    g = []
    for i in range(n):
        g.append(Agent(method))

    e = [(i,(i+1)%n) for i in range(n)]
    
    return g,e
def gen_chaine(n,method):
    g = []
    for i in range(n):
        g.append(Agent(method))

    e = [(i,i+1) for i in range(n-1)]
    
    return g,e

def get_graph(graph, n, method):
    if graph == 'ring':
        return gen_ring(n, method)
    elif graph == 'chaine':
        return gen_chaine(n, method)
    elif graph == 'star3':
        return gen_star(n, 3, method)
    elif graph == 'star10':
        return gen_star(n, 10, method)
    elif graph == 'complet':
        return gen_complet(n, method)
    
def _eval(nb_it = 20000, nb_agent = 100, method = 'elitist', graph = 'ring', den= 0.1):
            i = 0
            gskills = dict()
            for e in np.linspace(-1,1,21):
                gskills[round(e,1)] = i
                i += 1
            gskills_mat =np.zeros((21,nb_it//100))
            if graph == 'alea':
                graph,edges = gen_from_density(nb_agent ,den,method)
            else:
                graph,edges = get_graph(graph, nb_agent,method)
            chrono_mat = np.zeros((nb_agent,nb_it))
            c = Counter()
            for e in np.linspace(-1,1,21):
                c[round(e,1)] = 0
            env = Env()
            l = list(range(nb_agent))
            Liste_edges = list(range(len(edges)))
            dead_red = nb_it*[0]
            active_red = nb_it*[0]
            dead_blue = nb_it*[0]
            active_blue = nb_it*[0]
            none = nb_it*[0]
            for i in range(nb_it):     
                #print(i)
                for j in range(4):
                    env.R1 = nb_agent/2
                    env.R2 = nb_agent/2

                    
                    random.shuffle(l)
                    
                    for ag in l:
                            graph[ag].move()
                            graph[ag].compute_fitness(env)
                    random.shuffle(Liste_edges)
                    for ind_edg in Liste_edges:
                            e = edges[ind_edg]
                            first = random.choice([0,1])
                            graph[e[first]].broadcast(graph[e[1-first]])
                            graph[e[1-first]].broadcast(graph[e[first]])
                n = 0

                for a in graph:
                    a.select_genome()
                    a.genomeList = []
                    if a.g_skill != None:
                        chrono_mat[n, i] = round(a.g_skill,1)
                    if a.g_skill == None or a.g_skill == 0:
                        none[i] += 1
                    elif a.g_skill < 0:
                        if a.is_stopped():
                            dead_red[i] += 1
                        else:
                            active_red[i] += 1
                    elif a.g_skill > 0:
                        if a.is_stopped():
                            dead_blue[i] += 1
                        else:
                            active_blue[i] += 1
                    n += 1            
            cpt = 0   
            for a in graph:                
                if not a.is_stopped() :
                        cpt  += 1
                if a.g_skill != None :
                    c[round(a.g_skill,1)] += 1
                        
            labels,values = zip(*sorted(c.items()))
            #plot.draw_barplot(list(range(nb_it)), active_red,active_blue, none, dead_red, dead_blue,'graphe aleatoire densite == '+str(den)+' - sigma 0,1 '+ method)
            plot.chrono_plot( chrono_mat , method+' '+str(nb_agent))
            plot.histogramme_plot(labels,values,'graphe aleatoire densite == '+str(den)+' - sigma 0,1'+ method+' '+str(nb_agent))
            return cpt
        
        
 
if __name__ == '__main__':
    res = dict()
    methods = [ 'fitness prop','random', 'elitist', 'rank prop']
    for method in methods:
        c2 = Counter()
        c3 = []
        for run in range(1):
            c3.append(_eval(nb_it=20000,nb_agent=100,method=method,graph='ring'))
        res[method] = c3
    data=[]
    labels=[]
    
    
    with open("results.txt", "a") as fichier:
        fichier.write(str(nb_agent))
        for k in res.keys():
            data.append(res[k])
            
            labels.append(k)
            fichier.write(str(res[k]))
    
    plot.violin_plots(data, labels,'Agents active - sigma 0,1  - anneau de '+ str (nb_agent )+ ' agents' , 'Methode de selection', "Agents actives")


    


