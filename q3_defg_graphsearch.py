from q3_a_graphclass import Graph
from q3_b_randomunweighted import createRandomUnweightedGraphIter
from q3_c_linkedlist import createLinkedList
from queue import Queue
#For a bit of house cleaning, you could protentially just separate DFS from BFT into two separate projects. 
#That way you can get results for one or the other without shifting around values
class GraphSearch:
  def __init__(self, graph):
    self.graph = graph
  
  def DFSRec(self, start, end):
    out = []
    visited = {n:False for n in self.graph.nodes()}
    def helper(node, visited):
      visited[node] = True
      # dont add if already found
      if end not in out:
        out.append(node)
      for adj in self.graph.adjacent(node):
        if not visited[adj]:
          helper(adj, visited)
    helper(start, visited)
    return out
    
  def DFSIter(self, start, end):
    visited = {n:False for n in self.graph.nodes()}
    stack = [start]
    out = []
    while len(stack) > 0:
      node = stack.pop()
      if node is end:
        out.append(node)
        break
      if not visited[node]:
        out.append(node)
        visited[node] = True
        for adj in self.graph.adjacent(node):
          stack.append(adj)
    return out

  def BFTRec(self):
    out = []
    visited = {n:False for n in self.graph.nodes()}
    node_q = Queue()
    node_q.put(self.graph.nodes()[0])
    def helper(node_q):
      if node_q.empty():
        return
      node = node_q.get()
      if node not in out:
        out.append(node)
      for adj in self.graph.adjacent(node):
        if not visited[adj]:
          visited[adj] = True
          node_q.put(adj)
      helper(node_q)
    helper(node_q)
    return out
 #You could also just set visited as a value within node as a true or false statement that would be set to false naturally on creation
  def BFTIter(self):
    out = []
    node_q = Queue()
    visited = {n:False for n in self.graph.nodes()}
    for node in self.graph.nodes():
      if not visited[node]:
        visited[node] = True
        node_q.put(node)
        while not node_q.empty():
          cursor = node_q.get()
          out.append(cursor)
          for adj in self.graph.adjacent(cursor):
            if not visited[adj]:
              visited[adj] = True
              node_q.put(adj)
    return out
#I like how you made a normal node array for the nodes to use throughout the project to keep things organized instead of alternate methods
# for testing
if __name__ == '__main__':
  search = GraphSearch(createRandomUnweightedGraphIter(10))
  print(search.graph, end = '\n\n')
  nodes = search.graph.nodes()
  start = nodes[0]
  end = nodes[9]
  print("DFS recursive search from {} to {}: {}".format(start, end, search.DFSRec(start, end)))
  print("DFS iterative search from {} to {}: {}".format(start, end, search.DFSIter(start, end)))
  print("BFT recursive traversal: {}".format(search.BFTRec()))
  print("BFT iterative traversal: {}".format(search.BFTIter()))
