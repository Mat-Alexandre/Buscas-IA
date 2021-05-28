import time
from graph.graph import Graph
from graph.bidirectional_search import bidirectional_search

def main():
	graph = Graph()
	graph.add_edge('a', {'b', 'd'})
	graph.add_edge('b', {'a', 'c', 'd', 'e'})
	graph.add_edge('c', {'b','e'})
	graph.add_edge('d', {'a', 'b', 'e', 'f'})
	graph.add_edge('e', {'b', 'c', 'd', 'f', 'g'})
	graph.add_edge('f', {'d', 'e', 'g'})
	graph.add_edge('g', {'e', 'f'})
	graph.add_edge('h', {'i'})
	graph.add_edge('i', {'h'})

	print(bidirectional_search(graph, 'a', 'g'))

if __name__ == '__main__':
	main()