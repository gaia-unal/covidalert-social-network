# -*- coding: utf-8 -*-
"""Modelado red social personal

#bookstores social network
import networkx as nx
import matplotlib.pyplot as plt
import json

ListUSR.columns = ['source','target','weight','color']
ListUSR['color']=ListUSR['color'].replace({0:"blue",1:"red"})

L = ListUSR.copy()
L.drop_duplicates(subset =["target"], keep = 'last', inplace = True)
L.drop_duplicates()

G = nx.from_pandas_edgelist(ListUSR,edge_attr = ['weight','color'])
nx.draw_networkx(G,node_color = L['color'],with_labels=False)

