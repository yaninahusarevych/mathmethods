import matplotlib.pyplot as plt
import networkx as nx


def fordfulkerson(graph, source, sink):
	nodes = list(graph.nodes)
	edges = dict(graph.edges)
	dictofnodes = {i : 'unmarked' for i in nodes}
	path, capacities = [], []
	maxflow, flow = 0, 0
	source_node = source
	zminna = 1
	while dictofnodes[sink] != 'visited':
		dictofnodes[source_node] = 'visited'
		path.append(source_node)
		neighbours = list(graph.successors(source_node))
		max_capacity = 0
		for i in range(len(neighbours)):
			dictofnodes[neighbours[i]] = 'marked and unvisited'
			if dict(graph.get_edge_data(source_node, neighbours[i]))['capacity'] > max_capacity:
				max_capacity = dict(graph.get_edge_data(source_node, neighbours[i]))['capacity']
				path.append(neighbours[i])
		if max_capacity <= 0:
			print("Stop, maximal flow is reached")
			dictofnodes[sink] = 'visited'
			break
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
			path.clear()
			source_node = source
			zminna = 1
			dictofnodes = {i : 'unmarked' for i in nodes}
	

G = nx.DiGraph()
G.add_nodes_from('ABCDEFGH')
G.add_edges_from([
    ('A', 'B', {'capacity': 4, 'flow': 0}),
    ('A', 'C', {'capacity': 5, 'flow': 0}),
    ('A', 'D', {'capacity': 7, 'flow': 0}),
    ('B', 'E', {'capacity': 7, 'flow': 0}),
    ('C', 'E', {'capacity': 6, 'flow': 0}),
    ('C', 'F', {'capacity': 4, 'flow': 0}),
    ('C', 'G', {'capacity': 1, 'flow': 0}),
    ('D', 'F', {'capacity': 8, 'flow': 0}),
    ('D', 'G', {'capacity': 1, 'flow': 0}),
    ('E', 'H', {'capacity': 7, 'flow': 0}),
    ('F', 'H', {'capacity': 6, 'flow': 0}),
    ('G', 'H', {'capacity': 4, 'flow': 0}),
])
layout = {
    'A': [0, 1], 'B': [1, 2], 'C': [1, 1], 'D': [1, 0],
    'E': [2, 2], 'F': [2, 1], 'G': [2, 0], 'H': [3, 1],
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

fordfulkerson(G, 'A', 'H')