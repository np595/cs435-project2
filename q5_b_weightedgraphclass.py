from pprint import pformat

class Node:
  def __init__(self, str):
    self.val = str
  def __repr__(self):
    return self.val
  def __lt__(self, other):
    return self if self.val < other.val else other
# now use tuple of (dest, weight) to represent edges
class WeightedGraph:
  def __init__(self):
    self.node_adj_dict = {}
  def addNode(self, val):
    new_node = Node(val)
    self.node_adj_dict[new_node] = set()
  def addWeightedEdge(self, first, second, weight):
    self.node_adj_dict[first].add((second, weight))
  def removeWeightedEdge(self, first, second):
    self.node_adj_dict[first].remove((second, weight))
  def getAllNodes(self):
    return self.node_adj_dict.keys()
  def adjacent(self, node):
    return self.node_adj_dict[node]
  def __str__(self):
    return pformat(self.node_adj_dict)
  def nodes(self):
    return list(self.node_adj_dict.keys())
  # for weighted graphs: get weight of edge a->b
  def weight(self, a, b):
    edges = [node for node, adj in self.node_adj_dict]
    pass

# for testing
if __name__ == '__main__':
  pass