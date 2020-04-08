from pprint import pformat

class Node:
  def __init__(self, str):
    self.val = str
  def __repr__(self):
    return self.val
class DAG:
  def __init__(self):
    self.node_adj_dict = {}
  def addNode(self, val):
    new_node = Node(val)
    self.node_adj_dict[new_node] = set()
  def addDirectedEdge(self, first, second):
    self.node_adj_dict[first].add(second)
  def removeDiirectedEdge(self, first, second):
    self.node_adj_dict[first].remove(second)
  def getAllNodes(self):
    return self.node_adj_dict.keys()
  def adjacent(self, node):
    return self.node_adj_dict[node]
  def __str__(self):
    return pformat(self.node_adj_dict)
  def nodes(self):
    return list(self.node_adj_dict.keys())

# for testing
if __name__ == '__main__':
  pass