import matplotlib.pyplot as plt
import networkx as nx


def fordfulkerson(graph, source, sink):
    maxflow, path = 0, True
    while path:
        path, increased_flow = dfs(graph, source, sink)
        maxflow += increased_flow
        for v, u in zip(path, path[1:]):
            if graph.has_edge(v, u):
                graph[v][u]['flow'] += increased_flow
            else:
                graph[u][v]['flow'] -= increased_flow
        results(graph, path, maxflow, increased_flow)
        draw_graph()
	

def dfs(graph, source, sink):
    undirected = graph.to_undirected()
    explored = {source}
    stack = [(source, 0, dict(undirected[source]))]
    while stack:
        v, zminna, neighbours = stack[-1]
        if v == sink:
            break
        while neighbours:
            u, e = neighbours.popitem()
            if u not in explored:
                break
        else:
            stack.pop()
            continue
        in_direction = graph.has_edge(v, u)
        capacity = e['capacity']
        flow = e['flow']
        neighbours = dict(undirected[u])
        if in_direction and flow < capacity:
            stack.append((u, capacity - flow, neighbours))
            explored.add(u)
        elif not in_direction and flow:
            stack.append((u, flow, neighbours))
            explored.add(u)
    reserve = min((f for zminna, f, zminna in stack[1:]), default=0)
    path = [v for v, zminna,zminna in stack]
    
    return path, reserve

G = nx.DiGraph()
G.add_nodes_from('1234567890')
G.add_edges_from([
    ('1', '2', {'capacity': 22, 'flow': 0}),
    ('1', '3', {'capacity': 18, 'flow': 0}),
    ('1', '4', {'capacity': 25, 'flow': 0}),
    ('2', '3', {'capacity': 5, 'flow': 0}),
    ('2', '5', {'capacity': 12, 'flow': 0}),
    ('3', '6', {'capacity': 8, 'flow': 0}),
    ('4', '5', {'capacity': 6, 'flow': 0}),
    ('4', '8', {'capacity': 6, 'flow': 0}),
    ('4', '9', {'capacity': 10, 'flow': 0}),
    ('5', '7', {'capacity': 13, 'flow': 0}),
    ('6', '1', {'capacity': 6, 'flow': 0}),
    ('6', '9', {'capacity': 15, 'flow': 0}),
    ('7', '8', {'capacity': 9, 'flow': 0}),
    ('7', '6', {'capacity': 12, 'flow': 0}),
    ('8', '9', {'capacity': 11, 'flow': 0}),
    ('9', '6', {'capacity': 5, 'flow': 0}),
    ('4', '0', {'capacity': 20, 'flow': 0}),
    ('6', '0', {'capacity': 11, 'flow': 0}),
    ('7', '0', {'capacity': 8, 'flow': 0}),
    ('9', '0', {'capacity': 10, 'flow': 0}),
    ('2', '6', {'capacity': 15, 'flow': 0}),
])
layout = {
    '1': [0, 0], '2': [1, 3], '3': [1, -3], '4': [5, 0],
    '5': [5, 3], '6': [6, -3], '7': [8, 3], '8': [10, 3],
    '9': [10, 0], '0': [10, -3]
}
def draw_graph():
    plt.figure(figsize=(12, 4))
    plt.axis('off')

    nx.draw_networkx_nodes(G, layout, node_color='firebrick', node_size=400)
    nx.draw_networkx_edges(G, layout, edge_color='gray')
    nx.draw_networkx_labels(G, layout, font_color='black')

    for u, v, e in G.edges(data=True):
        label = '{}/{}'.format(e['flow'], e['capacity'])
        color = 'black' if e['flow'] < e['capacity'] else 'red'
        x = layout[u][0] * .6 + layout[v][0] * .4
        y = layout[u][1] * .6 + layout[v][1] * .4
        t = plt.text(x, y, label, size=16, color=color, 
                    horizontalalignment='center', verticalalignment='center')
        
    plt.show()

def results(graph, path, current_flow, increased_flow):
	print('flow increased by: ', increased_flow, 'at path: ', path,'; current maximal flow: ', current_flow)

fordfulkerson(G, '1', '0')