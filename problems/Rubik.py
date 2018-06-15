from .State import State
from .Action import Action
from .Problem import Problem


class Rubik(Problem):

    def __init__(self):
        super().__init__()
        self.init_state = State()
        self.states = set()
        print('Problem inputs:')
        self.read_input()

    def read_input(self):
        line = input().split()
        self.init_state.name = ''.join(line)

    def initial_state(self):
        return self.init_state

    def actions(self, state):
        actions = list()
        actions.append(Action('T', 1))
        actions.append(Action('TC', 1))
        actions.append(Action('F', 1))
        actions.append(Action('FC', 1))
        actions.append(Action('R', 1))
        actions.append(Action('RC', 1))
        return actions

    def result(self, state, action):
        nx_list = list(state.name)
        if action.name == 'T':
            nx_list[0] = state.name[2]
            nx_list[1] = state.name[0]
            nx_list[2] = state.name[3]
            nx_list[3] = state.name[1]

            nx_list[4] = state.name[20]
            nx_list[5] = state.name[21]

            nx_list[20] = state.name[15]
            nx_list[21] = state.name[14]

            nx_list[14] = state.name[17]
            nx_list[15] = state.name[16]

            nx_list[16] = state.name[4]
            nx_list[17] = state.name[5]

        elif action.name == 'TC':

            nx_list = list(state.name)

            nx_list[0] = state.name[1]
            nx_list[1] = state.name[3]
            nx_list[2] = state.name[0]
            nx_list[3] = state.name[2]

            nx_list[4] = state.name[16]
            nx_list[5] = state.name[17]

            nx_list[20] = state.name[4]
            nx_list[21] = state.name[5]

            nx_list[14] = state.name[21]
            nx_list[15] = state.name[20]

            nx_list[16] = state.name[15]
            nx_list[17] = state.name[14]

        elif action.name == 'F':

            nx_list = list(state.name)

            nx_list[4] = state.name[6]
            nx_list[5] = state.name[4]
            nx_list[6] = state.name[7]
            nx_list[7] = state.name[5]

            nx_list[2] = state.name[19]
            nx_list[3] = state.name[17]

            nx_list[20] = state.name[2]
            nx_list[22] = state.name[3]

            nx_list[9] = state.name[20]
            nx_list[8] = state.name[22]

            nx_list[17] = state.name[8]
            nx_list[19] = state.name[9]

        elif action.name == 'FC':

            nx_list = list(state.name)

            nx_list[4] = state.name[5]
            nx_list[5] = state.name[7]
            nx_list[6] = state.name[4]
            nx_list[7] = state.name[6]

            nx_list[2] = state.name[20]
            nx_list[3] = state.name[22]

            nx_list[20] = state.name[9]
            nx_list[22] = state.name[8]

            nx_list[9] = state.name[19]
            nx_list[8] = state.name[17]

            nx_list[17] = state.name[3]
            nx_list[19] = state.name[2]

        elif action.name == 'R':

            nx_list = list(state.name)

            nx_list[20] = state.name[22]
            nx_list[21] = state.name[20]
            nx_list[22] = state.name[23]
            nx_list[23] = state.name[21]

            nx_list[1] = state.name[5]
            nx_list[3] = state.name[7]

            nx_list[13] = state.name[1]
            nx_list[15] = state.name[3]

            nx_list[5] = state.name[9]
            nx_list[7] = state.name[11]

            nx_list[9] = state.name[13]
            nx_list[11] = state.name[15]

        elif action.name == 'RC':

            nx_list = list(state.name)

            nx_list[20] = state.name[21]
            nx_list[21] = state.name[23]
            nx_list[22] = state.name[20]
            nx_list[23] = state.name[22]

            nx_list[1] = state.name[13]
            nx_list[3] = state.name[15]

            nx_list[15] = state.name[11]
            nx_list[13] = state.name[9]

            nx_list[9] = state.name[5]
            nx_list[11] = state.name[7]

            nx_list[5] = state.name[1]
            nx_list[7] = state.name[3]

        nx_name = ''.join(nx_list)

        for the_state in self.states:
            if the_state.name == nx_name:
                return the_state

        next_state = State(name=nx_name)
        self.states.add(next_state)
        return next_state

    def goal_test(self, state):
        if state is not None:
            temp = state.name
            if self.equal(temp[0:4]) and self.equal(temp[4:8]) and self.equal(temp[8:12]) and self.equal(temp[12:16]) and self.equal(temp[16:20]) and self.equal(temp[20:24]):
                return True
            return False
        return False

    def step_cost(self, state, action):
        return 1

    def path_cost(self, actions):
        cost = 0.0
        for action in actions:
            cost += action.cost
        return cost

    def equal(self, input_str):
        return input_str == input_str[0] * len(input_str)
