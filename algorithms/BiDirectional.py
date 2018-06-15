from problems.Node import Node
from algorithms.consts import FAILURE, SUCCESS


class BiDirectional:

    def __init__(self, problem, graph_mode):
        self.problem = problem
        self.graph_mode = graph_mode
        self.root = Node(state=self.problem.initial_state())
        self.goal = Node(state=self.problem.goal_state)
        self.frontier1 = list()
        self.frontier2 = list()
        self.explored1 = set()
        self.explored2 = set()
        self.path = list()
        self.max_memory = 0
        self.expanded_count = 0
        self.visited_count = 0
        self.path_cost = 0

    def solve(self):
        self.frontier1.insert(0, self.root)
        self.frontier2.insert(0, self.goal)

        while self.frontier1 and self.frontier2:

            current_node = self.frontier1[-1]
            self.frontier1.pop()
            self.expanded_count += 1

            if self.graph_mode:
                self.explored1.add(current_node)

            for action in self.problem.actions(current_node.state):
                self.visited_count += 1
                next_node = Node(state=self.problem.result(current_node.state, action))
                next_node.parent_node = current_node

                if next_node.state not in self.explored1:
                    self.frontier1.insert(0, next_node)

                if self.lookup_frontier(2, next_node):
                    return SUCCESS

            self.max_memory = max(self.max_memory,
                                  len(self.frontier1) + len(self.frontier2) + len(self.explored1) + len(self.explored2))

            current_node = self.frontier2[-1]
            self.frontier2.pop()
            self.expanded_count += 1

            if self.graph_mode:
                self.explored2.add(current_node.state)

            for action in self.problem.actions(current_node.state):

                next_node = Node(state=self.problem.result(current_node.state, action))
                next_node.parent_node = current_node

                if next_node.state not in self.explored2:
                    self.frontier2.insert(0, next_node)

                if self.lookup_frontier(1, next_node):
                    return SUCCESS

            self.max_memory = max(self.max_memory,
                                  len(self.frontier1) + len(self.frontier2) + len(self.explored1) + len(
                                      self.explored2))
        return FAILURE

    def lookup_frontier(self, num, node):
        if num == 1:
            for item in self.frontier1:
                if item.state == node.state:
                    list1 = list()
                    list2 = list()

                    target = node
                    while target != self.goal:
                        self.path_cost += 1
                        list2.append(target)
                        target = target.parent_node
                    list2.append(self.goal)
                    target = item
                    while target.parent_node != self.root:
                        self.path_cost += 1
                        target = target.parent_node
                        list1.append(target)
                    self.path_cost += 1
                    list1.append(self.root)
                    list1.reverse()
                    self.path = list1 + list2
                    return True
            return False
        elif num == 2:
            for item in self.frontier2:
                if item.state == node.state:
                    list1 = list()
                    list2 = list()
                    target = node
                    while target != self.root:
                        list1.append(target)
                        target = target.parent_node
                    list1.append(self.root)
                    list1.reverse()

                    target = item

                    while target.parent_node != self.goal:
                        target = target.parent_node
                        list2.append(target)
                    list2.append(self.goal)

                    self.path = list1 + list2
                    return True
            return False

    def get_search_info(self):
        return {
            'path': self.path,
            'visited_count': self.visited_count,
            'expanded_count': self.expanded_count,
            'path_cost': self.path_cost,
            'max_memory': self.max_memory
        }
