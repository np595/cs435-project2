from q5_b_weightedgraphclass import WeightedGraph
from q5_c_randomweightedgraph import createRandomCompleteWeightedGraph
from q56_ebc_treadmillmazesolver import TreadmillMazeSolver
# for timing
from timeit import timeit

if __name__ == '__main__':
  # this will take FOREVER
  n = 10000
  maze = createRandomCompleteWeightedGraph(n)
  start = maze.nodes()[0]
  end = maze.nodes()[n-1]
  solver = TreadmillMazeSolver(maze)
  print(maze, end='\n\n')
  dijkstra_runtime = timeit(lambda: solver.dijkstras(start))
  print("Dijkstra's from {}: runtime {}".format(start, dijkstra_runtime))
  astar_runtime = timeit(lambda: solver.astar(start, end))
  print("A* from {} to {}: runtime {}".format(start, end, solver.astar(start, end)))