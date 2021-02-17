# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 10:06:00 2021

@author: Roza
"""
import random
from math import exp
import numpy as np
class Agent():
        def __init__(self):
            super().__init__()
            self.g_skill = random.uniform(-1,1)
            self.neighbours = []
            self.fitness = 0
            self.genomeList = []
            self.energy = 4
            self.wait = 0
            
        def __str__(self):
            return " ".join((str(self.g_skill),str(self.fitness)))
        
        def add_neighbour(self,agent):
            self.neighbours.append(agent)
        
        def add_neighbours(self, agents):
            for a in agents:
                self.add_neighbour(a)
            
        def broadcast(self):
            if not self.is_stopped():
                for a in self.neighbours:
                    if not a.is_stopped():
                        a.genomeList.append(((self.g_skill , self.fitness)))

        def apply_variation_random(self):
            if not self.is_stopped():
                if not self.genomeList:
                    self.g_skill = 0
                else:
                    self.g_skill = random.choice(self.genomeList)[0]
                self.genomeList = []
        def apply_variation_fitness_prop(self):
            if not self.is_stopped():
                if not self.genomeList:
                    self.g_skill = 0
                else:
                    x = [elem[1] for elem in self.genomeList]
                    if sum(x)== 0:
                        self.g_skill = np.random.choice([elem[0] for elem in self.genomeList] )
                    else:
                        self.g_skill = np.random.choice([elem[0] for elem in self.genomeList],p= np.array(x)/sum(x) )
                self.genomeList = []
                
        def apply_variation_rank_prop(self):
            if not self.is_stopped():
                if not self.genomeList:
                    self.g_skill = 0
                else:
                    x = list(range(len(self.genomeList)))
                    if sum(x)== 0:
                        self.g_skill = np.random.choice([elem[0] for elem in self.genomeList] )
                    else:
                        self.g_skill = np.random.choice([elem[0] for elem in sorted(self.genomeList, key=lambda tup: tup[1])],p= np.array(x)/sum(x) )
               
                    self.genomeList = []
        def apply_variation_fitness(self):
            if not self.is_stopped():
                if not self.genomeList:
                    self.g_skill = 0
                else:
                    self.g_skill = max(self.genomeList, key = lambda i : i[1])[0]
                self.genomeList = []
        def get_neighbours(self):
            return self.neighbours
                
        def get_genome(self):
            return self.g_skill
        
        def get_fitness(self):
            return self.fitness
        def f_syn(self, env):
            if self.g_skill > 0 and env.R1<= 0:
                return 0
            if self.g_skill < 0 and env.R2<= 0:
                return 0
            if self.g_skill > 0 :    
                env.R1 -= 1
                return 1/(1 + exp(50*(-1*self.g_skill+0.5)))
            if self.g_skill < 0 :
                env.R2 -= 1
                return 1/(1 + exp(50*((self.g_skill)+0.5)))
            return 0

        def compute_fitness(self, env,it):     
            if not self.is_stopped():
                self.energy += self.f_syn(env)
                if it > 10:
                    self.fitness += self.f_syn(env)
            
        def get_group(self):

            if self.g_skill>=0 :
                return 0
            elif self.g_skill<0:
                return 1

            
        def move(self):
            if self.is_stopped():
                self.charge()
                return 0
            self.energy -= 0.5
            if not self.energy:
                self.genomeList = []
                self.wait = random.randint(4, 15)

        
        def is_stopped(self):
            return self.wait
        
        
        def charge(self):
            self.wait -= 1
            if self.wait == 0:
                self.energy = 4
                

if __name__ == '__main__':
    print("rger")