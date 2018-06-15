from .State import State
from .Problem import Problem
from .Action import Action
from math import sqrt


class EightPuzzle(Problem):

    def __init__(self):
        self.states = set()
        self.init_state = State()
        self.goal_state = State(matrix=[[0, 1, 2], [3, 4, 5], [6, 7, 8]], name='0,0')
        self.empty_pos = list()
        print('Problem inputs:')
        self.read_input()

    def read_input(self):
        row1 = input().split()
        row2 = input().split()
        row3 = input().split()

        row1 = [int(x) for x in row1]
        row2 = [int(x) for x in row2]
        row3 = [int(x) for x in row3]

        self.init_state.matrix = [row1, row2, row3]

        check = False
        for i, v in enumerate(self.init_state.matrix):
            for j, value in enumerate(v):
                if value == 0:
                    self.init_state.name = str(i) + ',' + str(j)
                    check = True
                    break
            if check:
                break

    def initial_state(self):
        return self.init_state

    def actions(self, state):
        actions = list()
        if state.name == '0,0':
            actions.append(Action('right', 1))
            actions.append(Action('down', 1))
        elif state.name == '0,1':
            actions.append(Action('right', 1))
            actions.append(Action('down', 1))
            actions.append(Action('left', 1))
        elif state.name == '0,2':
            actions.append(Action('down', 1))
            actions.append(Action('left', 1))
        elif state.name == '1,0':
            actions.append(Action('top', 1))
            actions.append(Action('right', 1))
            actions.append(Action('down', 1))
        elif state.name == '1,1':
            actions.append(Action('top', 1))
            actions.append(Action('right', 1))
            actions.append(Action('down', 1))
            actions.append(Action('left', 1))
        elif state.name == '1,2':
            actions.append(Action('top', 1))
            actions.append(Action('down', 1))
            actions.append(Action('left', 1))
        elif state.name == '2,0':
            actions.append(Action('top', 1))
            actions.append(Action('right', 1))
        elif state.name == '2,1':
            actions.append(Action('top', 1))
            actions.append(Action('right', 1))
            actions.append(Action('left', 1))
        elif state.name == '2,2':
            actions.append(Action('top', 1))
            actions.append(Action('left', 1))
        return actions

    def result(self, state, action):
        temp_matrix = [[-1, -1, -1],
                       [-1, -1, -1],
                       [-1, -1, -1]]
        temp_name = "" + state.name
        temp_array = temp_name.split(',')
        temp_array = [int(x) for x in temp_array]
        for i, row in enumerate(state.matrix):
            for j, value in enumerate(row):
                temp_matrix[i][j] = value

        if action.name == 'top':
            temp = temp_matrix[temp_array[0]-1][temp_array[1]]
            temp_matrix[temp_array[0]-1][temp_array[1]] = 0
            temp_matrix[temp_array[0]][temp_array[1]] = temp
            temp_array[0] -= 1

        elif action.name == 'right':
            temp = temp_matrix[temp_array[0]][temp_array[1]+1]
            temp_matrix[temp_array[0]][temp_array[1]+1] = 0
            temp_matrix[temp_array[0]][temp_array[1]] = temp
            temp_array[1] += 1

        elif action.name == 'down':
            temp = temp_matrix[temp_array[0]+1][temp_array[1]]
            temp_matrix[temp_array[0]+1][temp_array[1]] = 0
            temp_matrix[temp_array[0]][temp_array[1]] = temp
            temp_array[0] += 1

        elif action.name == 'left':
            temp = temp_matrix[temp_array[0]][temp_array[1]-1]
            temp_matrix[temp_array[0]][temp_array[1]-1] = 0
            temp_matrix[temp_array[0]][temp_array[1]] = temp
            temp_array[1] -= 1

        for the_state in self.states:
            if the_state.matrix == temp_matrix:
                return the_state
        temp_array = [str(x) for x in temp_array]
        next_state = State(matrix=temp_matrix, name=','.join(temp_array))
        self.states.add(next_state)
        return next_state

    def step_cost(self, state, action):
        return 1

    def path_cost(self, actions):
        cost = 0.0
        for action in actions:
            cost += action.cost
        return cost

    def goal_test(self, state):
        return state.matrix == self.goal_state.matrix

    def heuristic(self, state):
        h = 0
        for i, row in enumerate(state.matrix):
            for j, value in enumerate(row):
                e_i = int(value / 3)
                e_j = int(value % 3)
                h += int(sqrt((e_i-i)**2 + (e_j-j)**2))
        return h
