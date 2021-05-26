# -*- coding: utf-8 -*-
"""
Created on Fri May  7 14:49:21 2021
@author: roza
"""
import re
import csv
class graph_sim():
    def __init__(self):
        with open('../data/DATA_boids.csv', newline='',encoding = "ISO-8859-1")  as csvfile:
            self.data = list(csv.reader(csvfile ,delimiter ='\t'))
        print("finished reading")
            
    def get_edges(self,it):
        edges = []
    
        for elem in self.data[256*it:256*(it+1)]:
            elem = re.sub(r"\[|]","",elem[0])
            elem = re.sub(' ',"\t",elem)
            elem = re.split(",",elem, 2)
            #print(elem[0])
            if len(elem)>1:
                agent = int(elem[1])
            if len(elem)>2:
                neighbours = [int(x) for x in re.split(',',elem[2]) if x!= '']
                for n in neighbours:
                    if not (n,agent)  in edges:
                        edges.append((agent,n))
        return edges

