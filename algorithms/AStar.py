from .consts import FAILURE, SUCCESS
from heapq import heappush, heappop
from problems.Node import Node


class AStar:

    def __init__(self, problem, graph_mode):
        self.problem = problem
        self.graph_mode = graph_mode
        self.root = Node(state=self.problem.initial_state())
        self.goal = Node(state=self.problem.goal_state)
        self.path = list()
        self.frontier = list()
        self.explored = set()
        self.max_memory = -1
        self.visited_count = 0
        self.expanded_count = 0
        self.path_cost = 0
        heappush(self.frontier, self.root)
        self.temp = None

    def solve(self):
        self.visited_count += 1
        while True:
            if not self.frontier:
                return FAILURE
            current_node = self.frontier[0]
            heappop(self.frontier)
            if self.problem.goal_test(current_node.state):
                self.goal = current_node
                target = self.goal
                while target.parent_node is not None:
                    self.path_cost += 1
                    self.path.append(target)
                    target = target.parent_node
                self.path.append(self.root)
                self.path.reverse()
                return SUCCESS
            if self.graph_mode:
                self.explored.add(current_node.state)
            self.expanded_count += 1
            for action in self.problem.actions(current_node.state):
                next_state = self.problem.result(current_node.state, action)
                next_h = self.problem.heuristic(next_state)
                next_node = Node(state=next_state,
                                 g=current_node.g+action.cost,
                                 h=next_h)
                next_node.parent_node = current_node

                self.temp = self.pq_get(self.frontier, next_node.state)
                self.max_memory = max(self.max_memory, len(self.frontier) + len(self.explored))
                if (not self.graph_mode and self.temp is None) or (self.graph_mode and self.temp is None and next_node.state not in self.explored):
                    self.visited_count += 1
                    heappush(self.frontier, next_node)
                elif self.temp is not None and self.temp.gh > next_node.gh:
                    self.temp = next_node

    def pq_get(self, tuple_list, state):
        for item in tuple_list:
            if item.state == state:
                return item
        return None

    def get_search_info(self):
        return {
            'path': self.path,
            'max_memory': self.max_memory,
            'expanded_count': self.expanded_count,
            'visited_count': self.visited_count,
            'path_cost': self.path_cost
        }
