# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 21:04:12 2021

@author: gr_am
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcol
import pygraphviz as pgv1

def violin_plots(data , labels, title, title_x, title_y):
    fig,ax=plt.subplots(figsize=(5,5))

    ax.violinplot(data, showmeans=False, showmedians=True)
    ax.set_title(title)
    # adding horizontal grid lines
    ax.yaxis.grid(True)
    ax.set_xticks([y + 1 for y in range(len(data))])
    ax.set_xlabel(title_x)
    ax.set_ylabel(title_y)

    # add x-tick labels
    plt.setp(ax, xticks=[y + 1 for y in range(len(data))],
        xticklabels=labels)
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
    plt.show() 


def histogramme_plot(labels,values,title):
    indexes = np.arange(len(labels))
    plt.bar(indexes, values)
    plt.xticks(indexes , labels)
    plt.title(title)
    plt.show()

def heatmap_plot(labels_x, labels_y, data , title):

    fig, ax = plt.subplots()
    im = ax.imshow(data, cmap='gray_r')
    plt.gray()
    # We want to show all ticks...
    ax.set_xticks(np.arange(len(labels_x)))
    ax.set_yticks(np.arange(len(labels_y)))
    cbar = ax.figure.colorbar(im, ax=ax)

    ax.set_title(title)
    fig.tight_layout()
    plt.show()
    
def chrono_plot( data , title):
    fig, ax = plt.subplots()
    cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["r","w","b"])

    im = ax.imshow(data,  cmap=cm1 , interpolation='nearest', aspect='auto')
    cbar = ax.figure.colorbar(im, ax=ax)

    ax.set_title(title)
    fig.tight_layout()
    plt.show()
    
def draw_graph(g,e,title,edge = True):
    graph= pgv1.AGraph()
    
    for i in range(len(g)):
        if g[i].g_skill == None or g[i].is_stopped() or g[i].g_skill == 0 :
            fill_color = 'white'
        else:
            fill_color = 'red' if g[i].g_skill>0 else 'blue'
        graph.add_node(str(i),color=fill_color, style='filled')
        #graph.add(str(i), fillcolor=fill_color, style='filled')
    if edge:
        for a in e:
            graph.add_edge(str(a[0]), str(a[1])) 
  
   

    #graph.add_nodes_from()
    #graph.add_edges_from(e)
    graph.node_attr.update(color="red")
    #A_unflattened = g.unflatten('-f -l 3')
    graph.unflatten('-f -l 3').layout()
     #g.layout(prog="dot")
    graph.draw(title+".pdf")
def draw_barplot(gen, active_red, active_blue, none , dead_red, dead_blue, title):

 
 
    # Values of each group
    bars1 = np.add(active_red, dead_red).tolist()
    bars2 = np.add(bars1,none).tolist()
    bars3 = np.add(bars2, dead_blue).tolist()

 
    # Heights of bars1 + bars2
    bars = np.add(bars1, bars2).tolist()
    
    
    names = gen
     
    plt.bar(gen, active_red, color='red', width=1.0)
    plt.bar(gen, dead_red, bottom=active_red, color='green', width=1.0)

    plt.bar(gen, none, bottom=bars1, color='yellow',width=1.0)
     
    plt.bar(gen, dead_blue, bottom=bars2, color='lightgreen', width=1.0)
    
    plt.bar(gen, active_blue, bottom=bars3, color='blue', width=1.0)
     
    # Custom X axis
    plt.xlabel("iteration")
 
    # Show graphic
    plt.title(title)
    plt.show()

def chrono_star(chrono_mat_first,chrono_mat_second,chrono_mat_third, chrono_mat_four,chrono_mat_five,chrono_mat_six,chrono_mat_seven ,chrono_mat_eight , chrono_mat_nine,chrono_mat_ten,title):
    fig, axs = plt.subplots(10, 1, figsize=(60,60))
    #box = dict(facecolor='yellow', pad=5, alpha=0.2)
    # Fixing random state for reproducibility
    ax1 = axs[0]
    cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["r","w","b"])
    im = ax1.imshow(chrono_mat_first, cmap=cm1 , interpolation='nearest', aspect='auto')
    #cbar = ax1.figure.colorbar(im, ax=ax1)
    #ax1.set_title('1ère branche')
    #ax1.set_ylabel('misaligned 1', bbox=box)

    ax2 = axs[1]
    cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["r","w","b"])
    im = ax2.imshow(chrono_mat_second, cmap=cm1 , interpolation='nearest', aspect='auto')
    #cbar = ax2.figure.colorbar(im, ax=ax2)
    #ax2.set_title('2ème branche')
    #ax2.set_ylabel('misaligned 1', bbox=box)
    
    
    ax3 = axs[2]
    cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["r","w","b"])
    im = ax3.imshow(chrono_mat_third, cmap=cm1 , interpolation='nearest', aspect='auto')
    #cbar = ax3.figure.colorbar(im, ax=ax3)
    #ax3.set_title('3ème branche')
    #ax3.set_ylabel('misaligned 1', bbox=box)

    

    ax4 = axs[3]
    cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["r","w","b"])
    im = ax4.imshow(chrono_mat_four, cmap=cm1 , interpolation='nearest', aspect='auto')
    #cbar = ax4.figure.colorbar(im, ax=ax4)
    #ax4.set_title('4ème branche')
    #ax4.set_ylabel('nb_iteration', bbox=box)
    
    ax5 = axs[4]
    cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["r","w","b"])
    im = ax5.imshow(chrono_mat_five, cmap=cm1 , interpolation='nearest', aspect='auto')
   # cbar = ax5.figure.colorbar(im, ax=ax5)
    #ax5.set_title('5ème branche')
    #ax5.set_ylabel('nb_iteration', bbox=box)
    
    ax6 = axs[5]
    cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["r","w","b"])
    im = ax6.imshow(chrono_mat_six, cmap=cm1 , interpolation='nearest', aspect='auto')
    #cbar = ax6.figure.colorbar(im, ax=ax6)
    #ax6.set_title('6 ème branche')
    #ax6.set_ylabel('nb_iteration', bbox=box)

    ax7 = axs[6]
    cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["r","w","b"])
    im = ax7.imshow(chrono_mat_seven, cmap=cm1 , interpolation='nearest', aspect='auto')
    #cbar = ax7.figure.colorbar(im, ax=ax7)
    #ax7.set_title('7 ème branche')
    #ax7.set_ylabel('nb_iteration', bbox=box)    
    
    ax8 = axs[7]
    cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["r","w","b"])
    im = ax8.imshow(chrono_mat_eight, cmap=cm1 , interpolation='nearest', aspect='auto')
    #cbar = ax8.figure.colorbar(im, ax=ax8)
    #ax8.set_title('8 ème branche')
    #ax8.set_ylabel('nb_iteration', bbox=box)    
    
    ax9 = axs[8]
    cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["r","w","b"])
    im = ax9.imshow(chrono_mat_nine, cmap=cm1 , interpolation='nearest', aspect='auto')
    #cbar = ax9.figure.colorbar(im, ax=ax9)
    #ax9.set_title('9 ème branche')
    #ax9.set_ylabel('nb_iteration', bbox=box)  
    #ax9.figure.figsize=(60,40)
    
    ax10 = axs[9]
    cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["r","w","b"])
    im = ax10.imshow(chrono_mat_ten, cmap=cm1 , interpolation='nearest', aspect='auto')
    # cbar = ax10.figure.colorbar(im, ax=ax10)
    #ax10.set_title('10 ème branche')
    #ax10.set_ylabel('nb_iteration', bbox=box)  
    #ax10.figure.figsize=(60,40)
    fig.tight_layout()
    plt.show()
    
def chrono_star3(chrono_mat_first,chrono_mat_second,chrono_mat_third,title):
    fig, axs = plt.subplots(3, 1,figsize=(60,60))
    #box = dict(facecolor='yellow', pad=5, alpha=0.2)
    # Fixing random state for reproducibility
    ax1 = axs[0]
    cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["r","w","b"])
    im = ax1.imshow(chrono_mat_first, cmap=cm1 , interpolation='nearest', aspect='auto')
   # cbar = ax1.figure.colorbar(im, ax=ax1)
    #ax1.set_title('1ère branche')
    #ax1.set_ylabel('misaligned 1', bbox=box)
    #ax1.figure.figsize=(60,40)

    ax2 = axs[1]
    cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["r","w","b"])
    im = ax2.imshow(chrono_mat_second, cmap=cm1 , interpolation='nearest', aspect='auto')
    #cbar = ax2.figure.colorbar(im, ax=ax2)
    #ax2.set_title('2ème branche')
    #ax2.set_ylabel('misaligned 1', bbox=box)
    #ax2.figure.figsize=(60,40)
    
    ax3 = axs[2]
    cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["r","w","b"])
    im = ax3.imshow(chrono_mat_third, cmap=cm1 , interpolation='nearest', aspect='auto')
    #cbar = ax3.figure.colorbar(im, ax=ax3)
    #ax3.set_title('3ème branche')
    #ax3.set_ylabel('misaligned 1', bbox=box)
    #ax3.figure.figsize=(60,40)
    fig.tight_layout()
    plt.show()
    
    
"""
    cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["r","w","b"])
    im = ax.imshow(data, cmap=cm1 , interpolation='nearest', aspect='auto')
    cbar = ax.figure.colorbar(im, ax=ax)
    ax.set_title(title) """
   
   