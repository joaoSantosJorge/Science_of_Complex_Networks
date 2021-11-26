#!/usr/bin/env python
# coding: utf-8



#dendrogram in project graph
#A dendrogram is a tree and each level is a partition of the graph nodes. Level 0 is the first 
#partition, which contains the smallest communities, and the best is len(dendrogram) - 1. The 
#higher the level is, the bigger are the communities

import community as community_louvain
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import networkx as nx

#Graph from test file
f = open("amazon0601_JUN_1_2003.txt", "r")
G = nx.Graph()

f_r =('')

for i in range(4):
    f.readline()

for i in range(3387388):
    str_spl = f.readline()
    split = str_spl.split()
    G.add_edge(split[0], split[1])


with open('results.txt', 'w') as file:
    dendo = community_louvain.generate_dendrogram(G)
    for level in range(len(dendo) -1):
        file.write("partition at level")
        file.write(str(level))
        file.write(" is ")
        file.write(str(community_louvain.partition_at_level(dendo,level)))


# In[10]:


#modularity in project graph
# this has no meaning once it calculates the best partition...
# high modularity (=0.878) wich means that the network has highly connected clusters and the clusters are not highly connected!
#great meaning for our project!

import community as community_louvain
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import networkx as nx

#Graph from test file
f = open("amazon0601_JUN_1_2003.txt", "r")
G = nx.Graph()

for i in range(4):
    f.readline()

for i in range(3387388):
    str = f.readline()
    split = str.split()
    G.add_edge(split[0], split[1])
    
    
partition = community_louvain.best_partition(G)
community_louvain.modularity(partition, G)


# In[23]:


#https://www.geeksforgeeks.org/how-to-read-dictionary-from-file-in-python/
# importing the module
import ast
  
# reading the data from the file
with open('dendrogram_example.txt') as f:
    data = f.read()
  
print("Data type before reconstruction : ", type(data))
      
# reconstructing the data as a dictionary
d = ast.literal_eval(data)
  
print("Data type after reconstruction : ", type(d))
print(d)


# In[5]:


#encontrar max do dic [max is number of clusters]
#arr com max
#count number of nodes in each cluster. Look for properties that are similar in each cluster


# importing the module
import ast
  
# reading the data from the file
with open('partition_0.txt') as f:
    data = f.read()
      
# reconstructing the data as a dictionary
d = ast.literal_eval(data)
max = 0
for i in d.values():
    if max < i :
        max = i

      
        
print('max: ', max)


nodes_per_community = {}
i = 0
while i < len(d) :
    if str(i) in d.keys():
        if str(d[str(i)]) not in nodes_per_community.keys():
            nodes_per_community[str(d[str(i)])] = 1
        else :
            nodes_per_community[str(d[str(i)])] = nodes_per_community[str(d[str(i)])] +1
            
    i +=1

print(nodes_per_community)

#just checking if all nodes were processed!
soma = 0
for k in nodes_per_community:
    soma += nodes_per_community[k]

print('soma: ', soma)


#number of elements in dictionary
print('number of communities: ', len(nodes_per_community))


#ver maiores 20 comunidades e numero de produtos em cada!
from heapq import nlargest

res = nlargest(10000, nodes_per_community, key = nodes_per_community.get)

print('100 biggest communities: ', res)

for i in res :
    print(i, ' : ', nodes_per_community[i])


# In[3]:


#encontrar max do dic [max is number of clusters]
#arr com max
#count number of nodes in each cluster. Look for properties that are similar in each cluster


# importing the module
import ast
  
# reading the data from the file
with open('partition_0.txt') as f:
    data = f.read()
      
# reconstructing the data as a dictionary
d = ast.literal_eval(data)
max = 0
for i in d.values():
    if max < i :
        max = i

      
        
print('max: ', max)


nodes_per_community = {}
i = 0
while i < len(d) :
    if str(i) in d.keys():
        if str(d[str(i)]) not in nodes_per_community.keys():
            nodes_per_community[str(d[str(i)])] = 1
        else :
            nodes_per_community[str(d[str(i)])] = nodes_per_community[str(d[str(i)])] +1
            
    i +=1

print(nodes_per_community)

#just checking if all nodes were processed!
soma = 0
for k in nodes_per_community:
    soma += nodes_per_community[k]

print('soma: ', soma)


#number of elements in dictionary
print('number of communities: ', len(nodes_per_community))


#ver menores 100 comunidades e numero de produtos em cada!
from heapq import nsmallest

res = nsmallest(15000, nodes_per_community, key = nodes_per_community.get)

for i in res :
    print(i, ' : ', nodes_per_community[i])


# In[ ]:


#who bought 'x' also bought 'y'
#ver numero de edges por node. Ver se e' random graph ou scale free graph
#small world
#degree distribution (random or scale free)
#maximum degree

#já tenho as 3 partitions
# ver o que partition significa
#ver maiores comunidades e ver o que há em comum nelas
#calcular modularity!

# apagar comunidades com menos de 20 / 10 /5 e tentar fazer rede visualizavel

#partition 28407 (2 elm) : [395878, 399522]
#partition 21047 (2 elm) : [402702, 402703]
# ver se há um componente fortemente ligado ou nao
    #se houver entao todos os produtos estao ligados entre si


# In[2]:


#community 6952 (2 elm) : [105166, 185103] = [5,5]
#community 28407 (2 elm) : [395878, 399522] = [2,1]
#community 21047 (2 elm) : [402702, 402703] = [2,2]
#community 20387(5 elm) : [321943, 366092, 366093, 366094, 366095] = [10, 4, 5, 4, 4]
#community 28203 (9 elm):[68302, 68303, 68304, 68305, 73508, 130466, 130467, 179445, 258632]=[18, 14, 16, 15, 11, 10, 11, 10, 1]
#community 24498 (32 elm) : [63631, 51821, 68586, 54911, 54912, 54913, 54915, 63784, 63789, 63790, 74407, 68585, 74405, 115669,
#115674, 259854, 115668, 115670, 115671, 115673, 115676, 184568, 160547, 160548, 160549, 176786, 299555, 176784, 177568, 298363,
#239346, 344204] 
#= [17, 11, 27, 14, 15, 10, 2, 16, 12, 9, 14, 20, 5, 28, 13, 11, 22, 13, 10, 12, 10, 10, 10, 2, 10, 12, 2, 10, 10, 10, 11, 10]


# In[16]:


#degree variation - last part of the project

#partition 6952 (2 elm) : [105166, 185103]
#partition 28407 (2 elm) : [395878, 399522]
#partition 21047 (2 elm) : [402702, 402703]
#partition 20387(5 elm) : [321943, 366092, 366093, 366094, 366095]
#partition 28203 (9 elm) : [68302, 68303, 68304, 68305, 73508, 130466, 130467, 179445, 258632]
#partition 24498 (32 elm) : [63631, 51821, 68586, 54911, 54912, 54913, 54915, 63784, 63789, 63790, 74407, 68585, 74405, 115669,
#115674, 259854, 115668, 115670, 115671, 115673, 115676, 184568, 160547, 160548, 160549, 176786, 299555, 176784, 177568, 298363,
#239346, 344204]

import community as community_louvain
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import networkx as nx

#Graph from test file
f = open("amazon0601_JUN_1_2003.txt", "r")
G = nx.Graph()

f_r =('')

for i in range(4):
    f.readline()

for i in range(3387388):
    str_spl = f.readline()
    split = str_spl.split()
    G.add_edge(split[0], split[1])

l1 = [105166, 185103]
l2 = [395878, 399522]
l3 = [402702, 402703]
l4 = [321943, 366092, 366093, 366094, 366095]
l5 = [68302, 68303, 68304, 68305, 73508, 130466, 130467, 179445, 258632]
l6 = [63631, 51821, 68586, 54911, 54912, 54913, 54915, 63784, 63789, 63790, 74407, 68585, 74405, 115669, 115674, 259854, 115668, 115670, 115671, 115673, 115676, 184568, 160547, 160548, 160549, 176786, 299555, 176784, 177568, 298363, 239346, 344204]
    
#count variable -> calcular total de vendas
degree_per_node = {}
i = 0
#count = 0
while i < 403394 :
    if str(i) in G:
        degree_per_node[i] = G.degree(str(i))
        #count += degree_per_node[i]
    i+=1

for i in l6:
    print('node: ', i, ' degree: ', degree_per_node[i])


# In[82]:


#degree distribution (biggest degree)
import community as community_louvain
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import networkx as nx

#Graph from test file
f = open("amazon0601_JUN_1_2003.txt", "r")
G = nx.Graph()

f_r =('')

for i in range(4):
    f.readline()

for i in range(3387388):
    str_spl = f.readline()
    split = str_spl.split()
    G.add_edge(split[0], split[1])

    
#count variable -> calcular total de vendas
degree_per_node = {}
i = 0
#count = 0
while i < 403394 :
    if str(i) in G:
        degree_per_node[i] = G.degree(str(i))
        #count += degree_per_node[i]
    i+=1

#see node degree
from heapq import nlargest

res = nlargest(1000, degree_per_node, key = degree_per_node.get)

#print('100 biggest communities: ', res)

sum = 0
for i in res :
    sum += degree_per_node[i]
    print(i, ' : ', degree_per_node[i])

print('sum: ', sum)
#100 biggest communities:  [1041, 45, 50, 529, 783, 10030, 89, 1862, 12245, 52, 41, 600, 186, 533, 24596, 5, 1036, 31457, 11788, 1039, 36, 1846, 833, 383, 2492, 29695, 82, 9087, 48, 10419, 669, 1515, 724, 1037, 14864, 34, 9874, 4322, 535, 15484, 9484, 6740, 605, 155, 603, 90, 614, 1619, 64501, 105, 1325, 1513, 239, 44, 40523, 599, 1517, 246, 28347, 49, 107, 8922, 23693, 103, 5619, 53547, 1147, 51, 42859, 832, 27627, 1615, 1024, 1085, 6, 9954, 749, 7899, 23511, 2153, 4754, 834, 6833, 22120, 46, 5020, 185, 1013, 6393, 26518, 608, 10975, 524, 7257, 14574, 57408, 2384, 11786, 1025, 61209]
#1041  :  2752
#45  :  2487
#50  :  2281
#529  :  1512
#783  :  1174
#10030  :  857
#89  :  807
#1862  :  786
#12245  :  722
#52  :  709
#41  :  657
#600  :  623
#186  :  592
#533  :  581
#24596  :  573
#5  :  566
#1036  :  564
#31457  :  556
#11788  :  533
#1039  :  530
#36  :  498
#1846  :  494
#833  :  493
#383  :  492
#2492  :  485
#29695  :  483
#82  :  482
#9087  :  482
#48  :  476
#10419  :  460
#669  :  450
#1515  :  442
#724  :  433
#1037  :  426
#14864  :  415
#34  :  411
#9874  :  411
#4322  :  408
#535  :  404
#15484  :  393
#9484  :  388
#6740  :  384
#605  :  374
#155  :  373
#603  :  373
#90  :  370
#614  :  370
#1619  :  370
#64501  :  369
#105  :  366
#1325  :  366
#1513  :  366
#239  :  365
#44  :  361
#40523  :  360
#599  :  358
#1517  :  352
#246  :  350
#28347  :  349
#49  :  348
#107  :  347
#8922  :  347
#23693  :  347
#103  :  345
#5619  :  343
#53547  :  343
#1147  :  342
#51  :  341
#42859  :  333
#832  :  331
#27627  :  328
#1615  :  326
#1024  :  324
#1085  :  324
#6  :  323
#9954  :  323
#749  :  318
#7899  :  315
#23511  :  315
#2153  :  314
#4754  :  314
#834  :  310
#6833  :  309
#22120  :  308
#46  :  307
#5020  :  307
#185  :  304
#1013  :  304
#6393  :  302
#26518  :  297
#608  :  296
#10975  :  296
#524  :  294
#7257  :  292
#14574  :  292
#57408  :  291
#2384  :  290
#11786  :  289
#1025  :  287
#61209  :  287

#sum:  48817


# In[92]:


#degree distribution (smallest degree)
import community as community_louvain
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import networkx as nx

#Graph from test file
f = open("amazon0601_JUN_1_2003.txt", "r")
G = nx.Graph()

f_r =('')

for i in range(4):
    f.readline()

for i in range(3387388):
    str_spl = f.readline()
    split = str_spl.split()
    G.add_edge(split[0], split[1])

degree_per_node = {}
i = 0
while i < 2443408 :
    if str(i) in G:
        degree_per_node[i] = G.degree(str(i))
    i+=1

#see node degree
from heapq import nsmallest

res = nsmallest(12000, degree_per_node, key = degree_per_node.get)

print('100 smallest node degree ', res)

for i in res :
    print(i, ' : ', degree_per_node[i])
#100 smallest node degree  [807, 1908, 4341, 4854, 4881, 5900, 6764, 7180, 7428, 7431, 7588, 7590, 8165, 8301, 8369, 9082, 9317, 9419, 9533, 9677, 9678, 9687, 9731, 10889, 10890, 11007, 11117, 11427, 12498, 12817, 13063, 13174, 14425, 15055, 15533, 15611, 15990, 16490, 16909, 17216, 18629, 19215, 19679, 20075, 20201, 20580, 20637, 20751, 21312, 21799, 22076, 22191, 22203, 22317, 22832, 22974, 23033, 23239, 23581, 23806, 24104, 24108, 24423, 24507, 24632, 24839, 24921, 24990, 25042, 25739, 25828, 26197, 26268, 26500, 26879, 26908, 27312, 28027, 28311, 29088, 29240, 29473, 29914, 30200, 30554, 30814, 30894, 30993, 32047, 32166, 32764, 32862, 32895, 33002, 33170, 33642, 33744, 33745, 34032, 34070]
#807  :  1
#1908  :  1
#4341  :  1
#4854  :  1
#4881  :  1
#5900  :  1
#6764  :  1
#7180  :  1
#7428  :  1
#7431  :  1
#7588  :  1
#7590  :  1
#8165  :  1
#8301  :  1
#8369  :  1
#9082  :  1
#9317  :  1
#9419  :  1
#9533  :  1
#9677  :  1
#9678  :  1
#9687  :  1
#9731  :  1
#10889  :  1
#10890  :  1
#11007  :  1
#11117  :  1
#11427  :  1
#12498  :  1
#12817  :  1
#13063  :  1
#13174  :  1
#14425  :  1
#15055  :  1
#15533  :  1
#15611  :  1
#15990  :  1
#16490  :  1
#16909  :  1
#17216  :  1
#18629  :  1
#19215  :  1
#19679  :  1
#20075  :  1
#20201  :  1
#20580  :  1
#20637  :  1
#20751  :  1
#21312  :  1
#21799  :  1
#22076  :  1
#22191  :  1
#22203  :  1
#22317  :  1
#22832  :  1
#22974  :  1
#23033  :  1
#23239  :  1
#23581  :  1
#23806  :  1
#24104  :  1
#24108  :  1
#24423  :  1
#24507  :  1
#24632  :  1
#24839  :  1
#24921  :  1
#24990  :  1
#25042  :  1
#25739  :  1
#25828  :  1
#26197  :  1
#26268  :  1
#26500  :  1
#26879  :  1
#26908  :  1
#27312  :  1
#28027  :  1
#28311  :  1
#29088  :  1
#29240  :  1
#29473  :  1
#29914  :  1
#30200  :  1
#30554  :  1
#30814  :  1
#30894  :  1
#30993  :  1
#32047  :  1
#32166  :  1
#32764  :  1
#32862  :  1
#32895  :  1
#33002  :  1
#33170  :  1
#33642  :  1
#33744  :  1
#33745  :  1
#34032  :  1
#34070  :  1


# In[58]:


#degree distribution to find if graph is scale free or random
#falta fazer pôr o gráfico em powerlaw para ver se aparenta scale-free properties
#calcular Y!

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

#Graph from test file
f = open("amazon0601_JUN_1_2003.txt", "r")
G = nx.Graph()


for i in range(4):
    f.readline()

for i in range(3387388):
    str_spl = f.readline()
    split = str_spl.split()
    G.add_edge(int(split[0]), int(split[1]))

#diameter, average path length to find small world effect
#for C in (G.subgraph(c).copy() for c in nx.connected_components(G)):
#    print(nx.average_shortest_path_length(C))  
    
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
#dmax = max(degree_sequence)

fig = plt.figure("Degree of a random graph", figsize=(8, 8))
# Create a gridspec for adding subplots of different sizes
axgrid = fig.add_gridspec(5, 4)

#ax0 = fig.add_subplot(axgrid[0:3, :])
#Gcc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
#pos = nx.spring_layout(Gcc, seed=10396953)
#nx.draw_networkx_nodes(Gcc, pos, ax=ax0, node_size=20)
#nx.draw_networkx_edges(Gcc, pos, ax=ax0, alpha=0.4)
#ax0.set_title("Connected components of G")
#ax0.set_axis_off()

ax1 = fig.add_subplot(axgrid[3:, :2])
ax1.loglog(degree_sequence, "b-", marker="o")
ax1.set_title("Degree Rank Plot")
ax1.set_ylabel("Degree")
ax1.set_xlabel("Rank")

ax2 = fig.add_subplot(axgrid[3:, 2:])
ax2.plot(degree_sequence, "b-", marker="o")
ax2.set_title("Degree Rank Plot")
ax2.set_ylabel("Degree")
ax2.set_xlabel("Rank")

#ax2 = fig.add_subplot(axgrid[3:, 3:])
#ax2.bar(*np.unique(degree_sequence, return_counts=True))
#ax2.set_title("Degree histogram")
#ax2.set_xlabel("Degree")
#ax2.set_ylabel("# of Nodes")

#fig.tight_layout()
plt.show()


# In[ ]:


# 1 - Know how many connected components there are! Can I reach a product if I am in any place of the graph (no! limitations:
# people are not constrained in the graph, so maybe later they can once one person that likes football buys some classic music
# cds! What this shows is that it maybe is not that probably)
#connected components
#https://networkx.org/documentation/stable/reference/algorithms/component.html


# 2 - degree distribution with powerlaw graph and histogram
#there is a small number of products that most people buy! is it pareto distribution? 80-20? Or is it different?

# 3 - shortest path
# see the shortest path in large communities. What can this help us? Has one person access to every product of that community?
#https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html

#it might be usefull to jump to point 6...

# 4 - centrality - see wich products are better referenced! wich ones are they for each community?
#https://networkx.org/documentation/stable/reference/algorithms/centrality.html
#how close you are (closeness & harmonic centrality)
#the others are not that important... 

# 5 - small world - search in google how to do
#https://networkx.org/documentation/stable/reference/algorithms/smallworld.html

# 6 - go back to dendrogram and try and see the communities!




#coomunities
#https://networkx.org/documentation/stable/reference/algorithms/community.html
#maybe useful to check if set is a partition


#clustering
#https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.cluster.clustering.html
# compute the cluster for each node (probably takes a while...)
# not that usefull


# In[68]:


# 1 - Know how many connected components there are! Can I reach a product if I am in any place of the graph (no! limitations:
# people are not constrained in the graph, so maybe later they can once one person that likes football buys some classic music
# cds! What this shows is that it maybe is not that probably)
#connected components
#https://networkx.org/documentation/stable/reference/algorithms/component.html

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

#Graph from test file
f = open("amazon0601_JUN_1_2003.txt", "r")
G = nx.Graph()


for i in range(4):
    f.readline()

for i in range(3387388):
    str_spl = f.readline()
    split = str_spl.split()
    G.add_edge(int(split[0]), int(split[1]))
    
print(nx.number_connected_components(G))

print(list(nx.connected_components(G)))

#[len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]


#2 elements group{340003, 340004}
#music, Rock, 'Living Off the Radar'), (book, Literature and fiction, 'My Antonia') 

#2 elements group {360296, 360297}
#(video, Actors and Actresses, 'The Monkees - Our Favorite Episodes (in Metal Lunchbox)')
#(Book, no categories, 'Beatrix Potter Mom's Brag Book')

#3 elements group {376281, 376282, 394995}
#(Book, Cooking, Food and Wine, '100 Innovative Recipes--From Appetizers to Desserts')
#(Book, no categories, 'The Maltese Dog (Wishbone Mysteries Promotion , No 6)')
#(Music, Classical, 'Sofia Gubaidulina: Offertorium (Concerto for Violin & Orchestra, 1980) / 
    #Hommage à T.S. Eliot, for Octet & Soprano (1987) - Gidon Kremer / Charles Dutoit')

#3 elements group {383840, 383841, 383842}
#(Book, Religion and Spirituality, 'The Tabernacle of David')
#(Book, Religion and Spirituality, 'God's Life in Us')
#(Book, Religion and Spirituality | Philosophy, 'The Inner Reaches of Outer Space: Metaphor as Myth and as Religion')

#5 elements group {385301, 385302, 385303, 385304, 385305}
#(Book, Literature and Fiction | Romance, 'Real for Me')
#(Book, Literature and Fiction, 'Oh My Goth!')
#(Book, Crafts and Hobbies | Home and Garden, 'The Art of the Quilt')
#(Book, Business and Investment, 'The Engaged Customer: Using the New Rules of Internet Direct 
#    Marketing to Create Profitable Customer Relationships')
#(Book, Sports | Basketball, 'Three-Point Field Goal Offense for Mens and Womens Basketball 
#    (The Art and Science of Coaching Series)')

#15 elements group {384064, 384065, 384066, 384067, 384068, 384069, 384070, 384071, 384072, 384073, 389697, 394986,
#    394985, 386528, 384063}
#(Book, Children's book | Religion | Christianity, 'The Miracles of Jesus (Young Reader's Christian Library)')
#(Book, Home & Garden, 'Ruffing It: The Complete Guide to Camping With Dogs')
#(Music, Classical | Opera,'Japanese Melodies')
#(Book, History | Military, 'The American Civil War: The War in the East 1863-1865 (Essential Histories)')
#(Book, Literature and Fiction | Erotical | Adult Fiction'The Lov-Ed Solution')
#(Music, Dance and DJ, 'Mixed')
#(Music, Classical, 'Michael Tilson Thomas Performs and Conducts Gershwin')
#(Music, Classical | Opera and Vocal,'Fascinatin' Rampal (Jean-Pierre Rampal Plays Gershwin)')
#(Music, Latin Music, 'Rabanes')
#(Music, Featured Composers, 'Haydn: Flute Concerto; Oboe Concerto')
#(Book, Science | Mathematics, 'Foundations of Mathematical Logic')
#(Book, Home & Garden, 'R 2800: Pratt & Whitney's Dependable Masterpiece [R-241]')
#(Book, Social Sciences, 'Intercultural Competence: Interpersonal Communication Across Cultures (4th Edition)')
#(Book, Health, Mind and Body, '10,000 Ways to Say I Love You: The Biggest Collection of Romantic Ideas 
#    Ever Gathered in One Place')
#(Music,Hard Rock and Metal, 'Real Life')


# In[6]:


# 3 - shortest path
# see the shortest path in large communities. What can this help us? Has one person access to every product of that community?
#https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html

import networkx as nx
import random

#Graph from test file
f = open("amazon0601_JUN_1_2003.txt", "r")
G = nx.Graph()


for i in range(4):
    f.readline()

for i in range(3387388):
    str_spl = f.readline()
    split = str_spl.split()
    G.add_edge(int(split[0]), int(split[1]))

#remove edges out of main cluster
c1 = [384064, 384065, 384066, 384067, 384068, 384069, 384070, 384071, 384072, 384073, 389697, 394986,
394985, 386528, 384063]
c2 = [385301, 385302, 385303, 385304, 385305]
c3 = [383840, 383841, 383842]
c4 = [376281, 376282, 394995]
c5 = [360296, 360297]
c6 = [340003, 340004]

for i in c1:
    G.remove_node(i)
for i in c2:
    G.remove_node(i)
for i in c3:
    G.remove_node(i)
for i in c4:
    G.remove_node(i)
for i in c5:
    G.remove_node(i)
for i in c6:
    G.remove_node(i)


#average_path_length = 6.5 (10 elementos)
#average_path_length = 6.37 (100 elementos)
#average_path_length = 6.492 (1000 elementos)
#average_path_length = 6.4222 (10 000 elementos)
#average_path_length = 6.42314 (100 000 elementos) demorou mais de uma hora a correr
#pode ser interessante analisar nodes em cada extremo. tanto para grande numero de ligacoes e para poucas.
#como e' que este factor se comporta para diferentes situações?
arr = []

for i in range(100000):
        r1 = random.choice(list(G))
        r2 = random.choice(list(G)) 
        try:
            arr.append(nx.shortest_path_length(G, source=r1, target=r2, weight=None, method='dijkstra'))
        except NetworkXNoPath as no_path :
            print('source: ',r1,' destination: ', r2)
        #print('source: ',r1,' end: ', r2, ' shortest_path: ', arr[i])

print('average_path_length: ', sum(arr)/len(arr))


# In[49]:


# 3.1 - shortest path between selected edges
# see the shortest path in large communities. What can this help us? Has one person access to every product of that community?
#https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html

import networkx as nx
import random

#Graph from test file
f = open("amazon0601_JUN_1_2003.txt", "r")
G = nx.Graph()


for i in range(4):
    f.readline()

for i in range(3387388):
    str_spl = f.readline()
    split = str_spl.split()
    G.add_edge(int(split[0]), int(split[1]))

#Compare different categories
#different categories (book, 66244) and (Music, 327220) = 8
#different categories (book, 171441) and (Music, 327220) = 8
#different categories (Music, 160760) and (DVD, 253209) = 6
#different categories (DVD, 160729) and (Book, 96365) = 6
#different categories (Video, 272471) and (Book, 322875) = 6
#average = 6.8


#compare different subjects
#different subjects (Computer Science, 99093, Book) and (Cooking, Food & Wine, 206462, Book) = 8
#different subjects (Sports, 393195, Book) and (Computer Science, 206466, Book) = 7
#different subjects (Cooking, Food & Wine, 393327, Book) and (Health, Mind & Body, 149251, Book) =8
#different subjects (Health, Mind & Body, 149244, Book) and (Sports, 216862, Book) = 6
#different subjects (Biographies & Memoirs, 376670, Book) and (Religion & Spirituality, 1, Book) = 7
#average = 7.2




#different subjects (Opera, 100530, Music) and (Computer Science, 206466, Book)
#different subjects (Actors & Actresses, 450455, DVD) and (Religion & Spirituality, 413902, Book)
#different subjects (Health, Mind & Body, 149251, Book) and (Opera, 100530, Music)
#different subjects (History, 171440, Book) and (Actors & Actresses, 185089, DVD)
#different subjects (Sports, 216862, Book) and (History, 393188, Book)


#compare same subjects
#same subjects (Computer Science, 99093, Book) and (Computer Science, 206466, Book) = 6
#same subjects (Cooking, Food & Wine, 206462, Book) and (Cooking, Food & Wine, 393418, Book) = 7
#same subjects (Sports, 216862, Book) and (Sports, 393412, Book) = 6
#same subjects (Health, Mind & Body, 149251, Book) and (Health, Mind & Body, 149244, Book) = 1
#same subjects (Biographies & Memoirs, 393391, Book) and (Biographies & Memoirs, 334866, Book) = 7
#average = 5.4
#average = 6.5 (discarding value 1)





#same subjects (Religion & Spirituality, 1, Book) and (Religion & Spirituality, 413902, Book)
#same subjects (Opera, 544008, Book) and (Opera, 22624, Music)
#same subjects (Opera, 99326, Music) and (Opera, 100530, Music)
#same subjects (Actors & Actresses, 185089, DVD) and (Actors & Actresses, 450455, DVD)
#same subjects (History, 393188, Book) and (History, 171440, Book)

print(99093 in G)
print(206466 in G)
print(206462 in G)
print(393418 in G)
print(216862 in G)

print(393412 in G)
print(149251 in G)
print(149244 in G)
print(393391 in G)
print(334866 in G)

path_length = nx.shortest_path_length(G, source=int(99093), target=int(206466), weight=None, method='dijkstra')
print(path_length)
path_length_2 = nx.shortest_path_length(G, source=206462, target=393418, weight=None, method='dijkstra')
print(path_length_2)
path_length_3 = nx.shortest_path_length(G, source=216862, target=393412, weight=None, method='dijkstra')
print(path_length_3)
path_length_4 = nx.shortest_path_length(G, source=149251, target=149244, weight=None, method='dijkstra')
print(path_length_4)
path_length_5 = nx.shortest_path_length(G, source=393391, target=334866, weight=None, method='dijkstra')
print(path_length_5)


# In[ ]:





# In[99]:


# 3.2 - shortest path between selected edges
# see the shortest path in large communities. What can this help us? Has one person access to every product of that community?
#https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html

import networkx as nx
import random

#Graph from test file
f = open("amazon0601_JUN_1_2003.txt", "r")
G = nx.Graph()


for i in range(4):
    f.readline()

for i in range(3387388):
    str_spl = f.readline()
    split = str_spl.split()
    G.add_edge(int(split[0]), int(split[1]))








#high degree node (20 producs) node - number of edges
#1041  :  2752
#45  :  2487
#50  :  2281
#529  :  1512
#783  :  1174
#10030  :  857
#89  :  807
#1862  :  786
#12245  :  722
#52  :  709
#41  :  657
#600  :  623
#186  :  592
#533  :  581
#24596  :  573
#5  :  566
#1036  :  564
#31457  :  556
#11788  :  533
#1039  :  530

#small degree node (20 producs) node - number of edges
#807  :  1
#1908  :  1
#4341  :  1
#4854  :  1
#4881  :  1
#5900  :  1
#6764  :  1
#7180  :  1
#7428  :  1
#7431  :  1
#29240  :  1
#29473  :  1
#29914  :  1
#30200  :  1
#30554  :  1
#30814  :  1
#30894  :  1
#30993  :  1
#32047  :  1
#32166  :  1
#32764  :  1
#32862  :  1

#small and big degree (20 products)
#small
#29914  :  1
#30200  :  1
#30554  :  1
#30814  :  1
#30894  :  1
#30993  :  1
#32047  :  1
#32166  :  1
#32764  :  1
#32862  :  1

#big
#1041  :  2752
#45  :  2487
#50  :  2281
#529  :  1512
#783  :  1174
#10030  :  857
#89  :  807
#1862  :  786
#12245  :  722
#52  :  709


#path distance between 20 biggest degree nodes =
# 1,2,2,3,2,3,4,2,2,1
# average = 2.2

#path distance between 20 smallest degree nodes
# 7,7,9,8,5,9,9,8,7,9
# average = 7.8

#path distance between a node with high and small degree
# 5,5,5,5,6,4,5,6,6,6
# average = 5.3
path_length = nx.shortest_path_length(G, source=29914, target=1041, weight=None, method='dijkstra')
print(path_length)
path_length_2 = nx.shortest_path_length(G, source=30200, target=45, weight=None, method='dijkstra')
print(path_length_2)
path_length_3 = nx.shortest_path_length(G, source=30554, target=50, weight=None, method='dijkstra')
print(path_length_3)
path_length_4 = nx.shortest_path_length(G, source=30814, target=529, weight=None, method='dijkstra')
print(path_length_4)
path_length_5 = nx.shortest_path_length(G, source=30894, target=783, weight=None, method='dijkstra')
print(path_length_5)


path_length_6 = nx.shortest_path_length(G, source=30993, target=10030, weight=None, method='dijkstra')
print(path_length_6)
path_length_7 = nx.shortest_path_length(G, source=32047, target=89, weight=None, method='dijkstra')
print(path_length_7)
path_length_8 = nx.shortest_path_length(G, source=32166, target=1862, weight=None, method='dijkstra')
print(path_length_8)
path_length_9 = nx.shortest_path_length(G, source=32764, target=12245, weight=None, method='dijkstra')
print(path_length_9)
path_length_10 = nx.shortest_path_length(G, source=32862, target=52, weight=None, method='dijkstra')
print(path_length_10)


# In[61]:


# 4 - centrality - see wich products are better referenced! wich ones are they for each community?
#https://networkx.org/documentation/stable/reference/algorithms/centrality.html
#how close you are (closeness & harmonic centrality)
#the others are not that important... 

import networkx as nx

#Graph from test file
f = open("amazon0601_JUN_1_2003.txt", "r")
G = nx.Graph()


for i in range(4):
    f.readline()

for i in range(3387388):
    str_spl = f.readline()
    split = str_spl.split()
    G.add_edge(int(split[0]), int(split[1]))



#o interessante aqui é analisar a diferença entre um node ao calhas e um node muito conectado
#tambem pode ser interessante ver um node que tem pucas ligacoes
arr = []
for i in range(10):
    r = random.choice(list(G))
    arr.append(nx.closeness_centrality(G, r, distance=None, wf_improved=True))

print('num_nodes: ', len(arr), ' closeness_centrality: ', sum(arr)/len(arr))


# In[100]:


(5+5+5+5+6+4+5+6+6+6)/10


# In[1]:


#num produtos 403394 

#total de vendas 4886816
#20 % dos produtos = 80678 responsaveis por -> 2077215 compras (corresponde a 42 % das vendas)
# 1000 produtos mais vendidos (0.247 % produtos) -> 188502 compras (corresponde a 3.857% das vendas)


# In[1]:


#partition 0
#community 8774

#no subject 3
#discontinued product 4
#Religion & Spirituality 9 (Dolphin Talk: An Animal Communicator Shares Her Connection)
#Home & Garden
#History
#general music
#Cooking, Food & Wine 2
#Literature & Fiction 2
#Business & Investing
#Children's Books 8
#Travel
#contemporanic pop music
#Outdoors & Nature
#country music
#Art House & International DVD
#music general
#Health, Mind & Body 5
#Humor
#Computers & Internet 2
#medicine 3
#book on entertaining 2
#Philosophy 2
#Biographies & Memoirs 2 (The Case Against Hillary Clinton)
#Education
#sports 2
#Parenting & Families 2
#country music
#book on classical music
#Education
#Business & Investing
#Arts & Photography 2
#Mystery & Thrillers 2
#classical music
#Music Jazz
#music dance and DJ
#Documentary Video
#Social Sciences
#Women's Studies
#folk traditional music
#Mystery & Thrillers
#video on classic rock
#Entertainment


# In[ ]:




