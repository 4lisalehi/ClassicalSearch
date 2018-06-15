from .consts import CUTOFF, FAILURE, SUCCESS
from problems.Node import Node


class DepthLimitedDFS:

    def __init__(self, problem, graph_mode):
        self.problem = problem
        self.graph_mode = graph_mode
        self.root = Node(state=self.problem.initial_state())
        self.frontier = list()
        self.explored = set()
        self.path = list()
        self.goal = Node(state=self.problem.goal_state)
        self.visited_count = 0
        self.expanded_count = 0
        self.max_memory = 0
        self.path_cost = 0

    def solve(self, limit):
        self.visited_count += 1
        final_result = self.recursive_dls(self.root, limit)
        if final_result != FAILURE and final_result != CUTOFF:
            target = final_result
            while target.parent_node is not None:
                self.path_cost += 1
                self.path.append(target)
                target = target.parent_node
            self.path.append(self.root)
            self.path.reverse()
            return SUCCESS
        return FAILURE

    def recursive_dls(self, node, limit):
        if self.problem.goal_test(node.state):
            return node
        elif limit == 0:
            return CUTOFF
        else:
            cutoff_occurred = False
            self.expanded_count += 1
            for action in self.problem.actions(node.state):
                next_node = Node(state=self.problem.result(node.state, action), g=node.g+action.cost)
                next_node.parent_node = node
                result = self.recursive_dls(next_node, limit-1)
                if result == CUTOFF:
                    cutoff_occurred = True
                elif result != FAILURE:
                    return result
            if cutoff_occurred:
                return CUTOFF
            else:
                return FAILURE

    def get_search_info(self):
        return {
            'path': self.path,
            'max_memory': self.max_memory,
            'visited_count': self.visited_count,
            'expanded_count': self.expanded_count,
            'path_cost': self.path_cost
        }
