from q3_a_graphclass import Graph
from random import random

def createRandomUnweightedGraphIter(n):
  graph = Graph()
  node_vals = [str(num) for num in range(n)]
  # create nodes
  for val in node_vals:
    graph.addNode(val)
  # randomly create edges
  for node in graph.nodes():
    for second in [n for n in graph.nodes() if n is not node]:
      if random() > 0.8:
        graph.addUndirectedEdge(node, second)
  return graph

# for testing
if __name__ == '__main__':
  graph = createRandomUnweightedGraphIter(10)
  print(graph)