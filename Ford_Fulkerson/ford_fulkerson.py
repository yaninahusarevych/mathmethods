import matplotlib.pyplot as plt
import networkx as nx


def fordfulkerson(graph, source, sink):
	nodes = list(graph.nodes)
	edges = dict(graph.edges)
	dictofnodes = {i : 'unmarked' for i in nodes}
	path, capacities = [source], []
	maxflow, flow = 0, 0
	source_node = source
	zminna = 1
	while dictofnodes[sink] != 'visited':	
		dictofnodes[source_node] = 'visited'
		neighbours = list(graph.successors(source_node))
		max_capacity = 0
		for i in range(len(neighbours)):
			if dictofnodes[neighbours[i]] != 'visited':
				if dict(graph.get_edge_data(source_node, neighbours[i]))['capacity'] > max_capacity:
					max_capacity = dict(graph.get_edge_data(source_node, neighbours[i]))['capacity']
					path.append(neighbours[i])
					dictofnodes[neighbours[i]] = 'marked and unvisited'
		if max_capacity <= 0:
			dictofnodes[path[-1]] = 'visited' 
			del path[-1]
			if len(path) != 0:
				source_node = path[-1]
			else:
				print("Stop, maximal flow is reached")
				break
			continue
		else:
			capacities.append(max_capacity)
			del path[zminna:len(path)-1]
			source_node = path[-1]
			zminna = zminna + 1
		if source_node == sink:
			maxflow = maxflow + min(capacities)
			flow = min(capacities)
			for i in range(0, len(path) - 1, 1):
				edges[(path[i], path[i+1])]['capacity'] -= flow
				edges[(path[i], path[i+1])]['flow'] += flow
			results(graph, path, maxflow, flow)
			draw_graph()
			capacities.clear()
			path = [source]
			source_node = source
			zminna = 1
			dictofnodes = {i : 'unmarked' for i in nodes}
	

G = nx.DiGraph()
G.add_nodes_from('123456789')
G.add_edges_from([
    ('1', '2', {'capacity': 8, 'flow': 0}),
    ('1', '3', {'capacity': 5, 'flow': 0}),
    ('1', '4', {'capacity': 5, 'flow': 0}),
    ('2', '3', {'capacity': 2, 'flow': 0}),
    ('2', '5', {'capacity': 12, 'flow': 0}),
    ('3', '6', {'capacity': 8, 'flow': 0}),
    ('4', '5', {'capacity': 4, 'flow': 0}),
    ('4', '8', {'capacity': 6, 'flow': 0}),
    ('4', '9', {'capacity': 10, 'flow': 0}),
    ('5', '7', {'capacity': 3, 'flow': 0}),
    ('6', '1', {'capacity': 6, 'flow': 0}),
    ('6', '9', {'capacity': 15, 'flow': 0}),
    ('7', '8', {'capacity': 9, 'flow': 0}),
    ('7', '6', {'capacity': 12, 'flow': 0}),
    ('8', '9', {'capacity': 11, 'flow': 0}),
    ('9', '6', {'capacity': 5, 'flow': 0}),
])
layout = {
    '1': [0, 1], '2': [1, 2], '3': [1, 1], '4': [1, 0],
    '5': [2, 2], '6': [2, 1], '7': [2, 0], '8': [3, 1],
    '9': [3, 3]
}
def draw_graph():
    plt.figure(figsize=(12, 4))
    plt.axis('off')

    nx.draw_networkx_nodes(G, layout, node_color='green', node_size=600)
    nx.draw_networkx_edges(G, layout, edge_color='gray')
    nx.draw_networkx_labels(G, layout, font_color='black')

    for u, v, e in G.edges(data=True):
        label = '{}/{}'.format(e['flow'], e['capacity'])
        color = 'green' if e['flow'] < e['capacity'] else 'red'
        x = layout[u][0] * .6 + layout[v][0] * .4
        y = layout[u][1] * .6 + layout[v][1] * .4
        t = plt.text(x, y, label, size=16, color=color, 
                    horizontalalignment='center', verticalalignment='center')
        
    plt.show()

def results(graph, path, current_flow, increased_flow):
	print('flow increased by', increased_flow, 'at path', path,'; current flow', current_flow)

fordfulkerson(G, '2', '9')