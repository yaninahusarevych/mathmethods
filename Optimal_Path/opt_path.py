import matplotlib.pyplot as plt
import networkx as nx
import numpy as np 

G = nx.DiGraph()
layout = { }
inf = 1000000
delta_v = np.array([
	[8, 10, 9, 15, 11, 11, 0],
	[12, 8, 10, 8, 8, 6, inf],
	[8, 9, 11, 9, 8, 5, inf],
	[14, 8, 0, 9, 12, 9, inf],
	[12, 8, 4, 12, 10, 15, inf]
	])
delta_h = np.array([
	[inf, inf, inf, inf, inf, inf, 0],
	[6, 12, 9, 12, 6, 7, 10],
	[24, 10, 14, 11, 7, 8, 4],
	[17, 17, 11, 9, 10, 5, 8],
	[18, 8, 6, 7, 12, 8, 8]
	])
delta_h_v = np.array([
	[inf, inf, inf, inf, inf, inf, 0],
	[15, 19, 13, 11, 13, 14, inf],
	[15, 13, 15, 13, 12, 12, inf],
	[20, 12, 9, 12, 9, 11, inf],
	[10, 10, 10, 14, 6, 10, inf]
	])
mitka = np.array([
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0]
	])

i = 5
while i != -6:
	if i >= 0:
		m = 0 
		n = i
	else:
		m = -i
		n = 0
	zminna1 = delta_v.diagonal(i)
	zminna2 = delta_h.diagonal(i)
	zminna3 = delta_h_v.diagonal(i)
	for x in range(0, len(zminna1), 1):			
		if m == 0:
			mitka[m][n] = zminna1[x] + mitka[m][n+1]
			G.add_edge(mitka[m][n], mitka[m][n+1])
		elif n == 6:
			mitka[m][n] = zminna2[x] + mitka[m-1][n]
			G.add_edge(mitka[m][n], mitka[m-1][n])
		else:
			list_zminna = np.array([zminna1[x] + mitka[m][n+1], zminna2[x] + mitka[m-1][n], zminna3[x] + mitka[m-1][n+1]])
			mitka[m][n] = min(list_zminna)
			l = list_zminna.tolist()
			ind = l.index(min(l))
			if ind == 0:
				G.add_edge(mitka[m][n], mitka[m][n+1])
			elif ind == 1:
				G.add_edge(mitka[m][n], mitka[m-1][n])
			elif ind == 2:
				G.add_edge(mitka[m][n], mitka[m-1][n+1])
		layout[mitka[m][n]] = [n, m]
		m+=1
		n+=1
	i-=1
layout[0] = [6, 0]
print("Minimal resources in path from S0 to Sn = " + str(mitka[4][0]))
plt.figure(figsize=(12, 12))
nx.draw(G, layout, edges=G.edges(), edge_color='green', node_color='firebrick')
nx.draw_networkx_labels(G, layout, font_color='black')
plt.show()