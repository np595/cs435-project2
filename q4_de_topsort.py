from q4_b_directedgraphclass import DAG
from q4_c_randomDAGIter import createRandomDAGIter
from queue import Queue

class TopSort:
  def __init__(self, graph):
    self.graph = graph

  def Kahns(self):
    in_degree = {node:len(self.graph.adjacent(node)) for node in self.graph.nodes()}
    # queue all vertices with indegree 0
    in_deg_0 = [node for node in in_degree.keys() if in_degree[node] == 0]
    node_q = Queue()
    for node in in_deg_0:
      node_q.put(node)
    # now go through queue and queue adjacent when their indegree is 0
    count = 0
    ordered = []
    while not node_q.empty():
      cursor = node_q.get()
      ordered.append(cursor)
      for adj in self.graph.adjacent(cursor):
        in_degree[adj] -= 1
        if in_degree[adj] == 0:
          node_q.put(adj)
      count += 1
    # return ordered output of nodes in graph
    return ordered
    
  def mDFS(self):
    out = []
    visited = {n:False for n in self.graph.nodes()}
    stack = []
    def helper(node, visited, stack):
      visited[node] = True
      for adj in self.graph.adjacent(node):
        if not visited[adj]:
          helper(adj, visited, stack)
      # the 'modified' part
      stack.insert(0, node)
    # 'modified' part: do for all vertices
    for node in self.graph.nodes():
      if not visited[node]:
        helper(node, visited, stack)
    return stack

if __name__ == '__main__':
  n = 10
  graph = createRandomDAGIter(n)
  print(graph, end="\n\n")
  sorter = TopSort(graph)
  print("Topological sort by Kahn's: {}".format(sorter.Kahns()))
  print("Topological sort by mDFS's: {}".format(sorter.mDFS()))