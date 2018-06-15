from problems.Node import Node
from .consts import FAILURE, SUCCESS


class DFS:

    def __init__(self, problem, graph_mode):
        self.problem = problem
        self.graph_mode = graph_mode
        self.frontier = list()
        self.explored = set()
        self.path = list()
        self.root = Node(state=self.problem.initial_state())
        self.goal = Node(state=self.problem.goal_state)
        self.max_memory = 0
        self.visited_count = 0
        self.expanded_count = 0
        self.path_cost = 0

    def solve(self):
        self.frontier.append(self.root)
        self.visited_count += 1
        while True:
            if not self.frontier:
                return FAILURE
            current_node = self.frontier[-1]
            self.frontier.pop()
            self.expanded_count += 1
            if self.graph_mode:
                self.explored.add(current_node.state)
            for action in self.problem.actions(current_node.state):
                self.visited_count += 1
                temp_result = self.problem.result(current_node.state, action)
                next_node = Node(state=temp_result, g=current_node.g+action.cost)
                next_node.parent_node = current_node
                if not self.graph_mode or (self.graph_mode and next_node.state not in self.explored and not self.lookup_list(self.frontier, next_node.state)):
                    self.visited_count += 1
                    if self.problem.goal_test(next_node.state):
                        self.goal = next_node
                        target = self.goal
                        while target.parent_node is not None:
                            self.path_cost += 1
                            self.path.append(target)
                            target = target.parent_node
                        self.path.append(self.root)
                        self.path.reverse()
                        return SUCCESS
                    self.frontier.append(next_node)
                self.max_memory = max(self.max_memory, len(self.frontier) + len(self.explored))

    def get_search_info(self):
        return {
            'visited_count': self.visited_count,
            'expanded_count': self.expanded_count,
            'path_cost': self.path_cost,
            'max_memory': self.max_memory,
            'path': self.path
        }

    def lookup_list(self, the_list, the_state):
        for item in the_list:
            if item.state == the_state:
                return True
        return False
