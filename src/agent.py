# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 10:06:00 2021

@author: roza
"""
import random
from math import exp
import numpy as np
class Agent():
        def __init__(self, method):
            super().__init__()
            self.g_skill = random.uniform(-1,1)
            self.fitness = 0
            self.genomeList = []
            self.energy = 4
            self.wait = 0
            self.max_energy =6
            self.sigma = 0.1
            self.listening = 0
            self.method = method

            
        def __str__(self):
            return " ".join((str(self.g_skill),str(self.fitness)))
        
        def add_neighbour(self,agent):
            self.neighbours.append(agent)
        
        def add_neighbours(self, agents):
            for a in agents:
                self.add_neighbour(a)
            
        def broadcast(self,a):
            if not self.is_stopped() :
                if a.wait == 0:
                        a.genomeList.append((self.g_skill,self.fitness))

        def apply_variation_random(self, pmut_uniform):
            
                liste = self.genomeList
                if liste:           
                    self.g_skill = np.random.choice([elem[0] for elem in liste] ) 
                    if pmut_uniform > 0:
                        rand = random.uniform(0, 1)
                        if rand < pmut_uniform:
                            self.g_skill = random.uniform(-1, 1)
                    else:
                        c = random.gauss(0, self.sigma)
                        self.g_skill += c
                        self.g_skill = min(1, self.g_skill)
                        self.g_skill = max(-1, self.g_skill)
                    
                else:
                    self.g_skill = None

        def apply_variation_fitness_prop(self, pmut_uniform):
                liste = self.genomeList
                if len(liste)>0:
                    x = [elem[1] for elem in liste]
                    if sum(x)== 0:
                        self.g_skill = np.random.choice([elem[0] for elem in liste] ) 

                    else:
                        self.g_skill = np.random.choice([elem[0] for elem in liste],p= np.array(x)/sum(x) )

                    if pmut_uniform > 0:
                        rand = random.uniform(0, 1)
                        if rand < pmut_uniform:
                            self.g_skill = random.uniform(-1, 1)
                    else:
                        c = random.gauss(0, self.sigma)
                        self.g_skill += c
                        self.g_skill = min(1, self.g_skill)
                        self.g_skill = max(-1, self.g_skill)
                else:
                    self.g_skill = None
                    

        def apply_variation_rank_prop(self, pmut_uniform):
                liste = self.genomeList
                if len(liste)>0:

                    x = list(range(1, len(liste)+1))
                    if sum(x)== 0:
                        self.g_skill = np.random.choice([elem[0] for elem in liste] ) 

                    else:
                        self.g_skill = np.random.choice([elem[0] for elem in sorted(liste, key=lambda tup: tup[1])],p= np.array(x)/sum(x) ) 

                    if pmut_uniform > 0:
                        rand = random.uniform(0, 1)
                        if rand < pmut_uniform:
                            self.g_skill = random.uniform(-1, 1)
                    else:
                        c = random.gauss(0, self.sigma)
                        self.g_skill += c
                        self.g_skill = min(1, self.g_skill)
                        self.g_skill = max(-1, self.g_skill)
                        
                else:
                    self.g_skill = None

        def apply_variation_Elitist(self, pmut_uniform):
                liste = self.genomeList
                if len(liste)>0:
                    
                    self.g_skill = max(liste, key = lambda i : i[1])[0]
                    if pmut_uniform > 0:
                        rand = random.uniform(0, 1)
                        if rand < pmut_uniform:
                            self.g_skill = random.uniform(-1, 1)
                    else:
                        c = random.gauss(0, self.sigma)
                        self.g_skill += c
                        self.g_skill = min(1, self.g_skill)
                        self.g_skill = max(-1, self.g_skill)
                    
                else:
                    self.g_skill = None
        def select_genome(self, pmut_uniform = 0):
            if self.method == "random":
                self.apply_variation_random(pmut_uniform)
            elif self.method == "elitist":
                self.apply_variation_Elitist(pmut_uniform)
            elif self.method == "fitness prop":
                self.apply_variation_fitness_prop(pmut_uniform)
            elif self.method == "rank prop":
                self.apply_variation_rank_prop(pmut_uniform)

        def f_syn(self, env):
            if self.g_skill > 0 and env.R1<= 0:
                r =  0
            elif self.g_skill < 0 and env.R2<= 0:
                r =  0
            elif self.g_skill > 0 :    
                env.R1 -= 1
                r = 1/(1 + exp(8*(-3*self.g_skill+1)))
            elif self.g_skill < 0 :
                env.R2 -= 1
                r =  1/(1 + exp(8*((3*self.g_skill)+1)))
            else:
                r = 0
                
            if r < 0.01: return 0
            if r > 0.99: return 1
            return r
        def compute_fitness(self, env):
            if not self.is_stopped():
                x=self.f_syn(env)
                self.energy = min(self.max_energy , self.energy+ x)                
                self.fitness = x

        def move(self):
            if self.is_stopped():
                if self.wait > 0  or self.listening >0 :
                    self.charge()
            else :
                self.energy = max(0 , self.energy-1)
                if self.energy == 0:
                    #self.genomeList = []
                    self.wait = random.randint(4, 15)

        
        def is_stopped(self):
            if self.wait > 0  or self.listening >0 or self.g_skill == None:
                return True
            else:
                return False
        
        
        def charge(self):
            if self.wait > 0:
                self.wait -= 1
                if self.wait == 0:                   
                    self.listening = 4
            else:
                self.listening -= 1
                if self.listening == 0:
                    self.energy = 4
                    self.select_genome()
    




        
                