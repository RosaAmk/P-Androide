# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:26:55 2021

@author: roza
"""

import random
class Graph():
    def __init__(self,n, d):
        self.n = n
        self.d = d
        self.connected = n*[0]
        self.cpt = n*[0]    
        self.edges_final = []
    def join( self, a ,b ):
        if not self.connected[a] and not self.connected[b]:
            self.connected[a] = max(self.connected) + 1 
            self.connected[b] = max(self.connected) 
        if self.connected[a] != self.connected[b]:
            if self.connected[a] and not self.connected[b]:
                self.connected[b] = self.connected[a]
            if not self.connected[a]:
                self.connected[a] = self.connected[b]
            else:
                for i in range(len(self.connected)):
                    x = self.connected[b]
                    if self.connected[i] == x:
                        self.connected[i] = self.connected[a]
            self.cpt[a] += 1
            self.cpt[b] += 1
                             
    def gen_graph(self):
        edges = [(i,j) for i in range(self.n) for j in range(i+1,self.n)]
        
        while len(self.edges_final)/((self.n)*(self.n-1)) < self.d/2 :
            e = random.choice(edges)
            self.edges_final.append(e)
            edges.remove(e)
            self.join(e[0], e[1])
        while(len(set(self.connected)) > 1):
            Missing = self.get_connecting()
            Removable = self.get_Removable()
            e = random.choice(Missing)
            self.edges_final.append(e)
            self.join(e[0], e[1])
            self.remove(random.choice(Removable))

        
    def get_connecting(self):
        comp = set(self.connected)
        Missing = []
        l = []
        for elem in comp:
            s = [i for i in range(self.n) if self.connected[i]== elem]
            l.append(s)
        if len(l) > 1:
            for i in range(len(l)):
                for j in range(i+1,len(l)):
                    Missing.extend([(a,b) for a in l[i] for b in l[j]])            
        return Missing
        
    def get_Removable(self):
        edges = []
        for e in self.edges_final:
            if self.cpt[e[0]]>1 or self.cpt[e[1]]>1:
                edges.append(e)
        #print(edges)
        return edges
    
    def remove(self, e):
        self.cpt[e[0]] -=   1   
        self.cpt[e[1]] -=   1 
        self.edges_final.remove(e)
        m = self.connected[e[0]]
        l = [i for i in range(self.n) if self.connected[i]== m]
        liste = [0 if v==m else v for v in self.connected]
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                if (l[i],l[j]) in self.edges_final:
                    self.join(l[i],l[j])
if __name__ == '__main__':
    g = Graph(20,0.1)
    g.gen_graph()
    
