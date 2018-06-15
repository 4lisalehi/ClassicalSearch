from .consts import FAILURE, SUCCESS
from problems.Node import Node


class BFS:
    def __init__(self, problem, graph_mode):
        self.problem = problem
        self.graph_mode = graph_mode
        self.root = Node(self.problem.initial_state())
        self.goal = Node(self.problem.goal_state())
        self.frontier = list()
        self.explored = set()
        self.frontier.insert(0, self.root)
        self.path = list()
        self.max_memory = 0
        self.visited_count = 0
        self.expanded_count = 0
        self.path_cost = 0

    def solve(self):
        current_node = Node(self.problem.initial_state())
        self.visited_count += 1
        if self.problem.goal_test(current_node.state):
            self.path.append(current_node)
            return SUCCESS

        while True:
            if not self.frontier:
                return FAILURE
            current_node = self.frontier[-1]
            self.frontier.pop()
            self.explored.add(current_node.state)
            self.expanded_count += 1
            for action in self.problem.actions(current_node.state):
                next_node = Node(state=self.problem.result(current_node.state, action), g=current_node.g+action.cost)
                next_node.parent_node = current_node
                if not self.lookup_list(self.frontier, next_node.state) and next_node.state not in self.explored:
                    self.visited_count += 1
                    if self.problem.goal_test(next_node.state):
                        target = next_node
                        while target.parent_node is not None:
                            self.path_cost += 1
                            self.path.append(target)
                            target = target.parent_node
                        self.path.append(self.root)
                        self.path.reverse()
                        return SUCCESS
                    self.frontier.insert(0, next_node)
                self.max_memory = max(self.max_memory, len(self.explored) + len(self.frontier))

    def lookup_list(self, the_list, state):
        for element in the_list:
            if element.state == state:
                return True
        return False

    def get_search_info(self):
        return {
            'path': self.path,
            'visited_count': self.visited_count,
            'expanded_count': self.expanded_count,
            'max_memory': self.max_memory,
            'path_cost': self.path_cost
        }
