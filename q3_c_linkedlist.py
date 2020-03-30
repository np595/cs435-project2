from q3_a_graphclass import Graph

def createLinkedList(n):
  graph = Graph()
  node_vals = [str(i) for i in range(n)]
  for val in node_vals:
    graph.addNode(val)
  nodes = sorted(graph.nodes(), key = lambda n: int(n.val))
  for idx, first in enumerate(nodes[:-1]):
    second = nodes[idx + 1]
    graph.addUndirectedEdge(first, second)
  return graph

# for testing
if __name__ == '__main__':
  graph = createLinkedList(20)
  print(graph)