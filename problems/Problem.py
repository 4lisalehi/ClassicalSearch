

class Problem:

    def __init__(self):
        self._init_state = None

    def read_input(self):
        pass

    def initial_state(self):
        return self._init_state

    def actions(self, state):
        return []

    def result(self, state, action):
        return None

    def goal_test(self, state):
        return True

    def step_cost(self, state, action):
        return 0

    def path_cost(self, actions):
        return 0

    def heuristic(self, state):
        return 0

    def goal_state(self):
        return None
