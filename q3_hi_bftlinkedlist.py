from q3_c_linkedlist import createLinkedList
from q3_defg_graphsearch import GraphSearch
from sys import setrecursionlimit

def BFTRecLinkedList(graph):
  search = GraphSearch(graph)
  return search.BFTRec()

def BFTIterLinkedList(graph):
  search = GraphSearch(graph)
  return search.BFTIter()

# for testing
if __name__ == '__main__':
  # recursive bft will quit unless recursion limit is set very high
  setrecursionlimit(15000)
  num_nodes = 10000
  num_print = 10
  print("Creating linked list size {}...".format(num_nodes))
  linked_list = createLinkedList(num_nodes)
  try:
    print("BFT (recursive) on linked list size {}: {}...".format(num_nodes, BFTRecLinkedList(linked_list)[:num_print]))
  except RecursionError as error:
    print("BFT (recursive) failed: {}".format(str(error)))
  print("BFT (iterative) on linked list size {}: {}...".format(num_nodes, BFTIterLinkedList(linked_list)[:num_print]))