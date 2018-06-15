from .DepthLimitedDFS import DepthLimitedDFS
from .consts import CUTOFF, FAILURE, SUCCESS
from problems.Node import Node


class IterativeDeepening:

    def __init__(self, problem, max_depth):
        self.max_depth = max_depth
        self.problem = problem
        self.root = Node(self.problem.initial_state(), 0)
        self.dfs_limited = DepthLimitedDFS(problem, True)
        self.target = None

    def solve(self):
        for depth in range(0, self.max_depth+1):
            result = self.dfs_limited.solve(depth)
            if result != CUTOFF and result != FAILURE:
                self.target = result
                return SUCCESS
        return FAILURE

    def get_search_info(self):
        return self.dfs_limited.get_search_info()
