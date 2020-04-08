from q5_b_weightedgraphclass import WeightedGraph

def createLinkedList(n):
  graph = WeightedGraph()
  node_vals = [str(i) for i in range(n)]
  for val in node_vals:
    graph.addNode(val)
  nodes = sorted(graph.nodes(), key = lambda n: int(n.val))
  weight = 1
  for idx, first in enumerate(nodes[:-1]):
    second = nodes[idx + 1]
    graph.addWeightedEdge(first, second, weight)
  return graph  

if __name__ == '__main__':
  n = 10
  graph = createLinkedList(n)
  print(graph)