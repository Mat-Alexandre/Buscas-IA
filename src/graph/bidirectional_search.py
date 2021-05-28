from graph.graph import Graph

def __in_queue(vertex, queue):
	if(queue.count(vertex) == 0):
		return False
	return True

def __bfs(graph: Graph, src_queue: list, src_visited: list, dst_queue: list, destiny):
	# Breadth First Search adapted for bidirectional search
	vertex = src_queue.pop(0)
	if(vertex == destiny or __in_queue(vertex, dst_queue)):
		return f'{src_visited[src_visited.count(vertex)]}'
	for v_neighbor in graph.graph[vertex[0]]:
		# For all vertex neighbors
		if(src_visited.count(v_neighbor) == 0):
			src_visited.append(v_neighbor)
			src_queue.append(v_neighbor)
	return None

def bidirectional_search(graph: Graph, source, destiny) -> str:
	if type(graph) is not Graph:
		raise TypeError('graph must be a Graph object.')
	
	src_queue = []
	dst_queue = []

	src_visited = []
	dst_visited = []
	
	src_queue.append(source)
	src_visited.append(source)
	
	dst_queue.append(destiny)
	dst_visited.append(destiny)
	
	result = None
	while(src_queue and dst_queue):
		# Loop while boths queue are not empty
		# If the poped vertex is the destiny vertex or if it's in the alternate
		# queue.
		if(src_queue):
			result = __bfs(graph, src_queue, src_visited, dst_queue, destiny)

		if(dst_queue):
			result = __bfs(graph, dst_queue, dst_visited, src_queue, source)
	return result