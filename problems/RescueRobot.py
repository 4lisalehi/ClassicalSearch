from .Problem import Problem
from .State import State
from .Action import Action
from math import sqrt
import numpy as np


class RescueRobot(Problem):

    def read_input(self):

        pos = input().split()
        self.goal_state.name = pos[0] + ',' + pos[1]
        self.goal_state.matrix = [int(pos[0]), int(pos[1])]
        self.walls = np.full((int(pos[0])+1, int(pos[1])+1, 4), False)
        self.number_of_walls = int(input())
        self.n = int(pos[0])
        self.m = int(pos[1])

        for i in range(self.number_of_walls):
            walls = input().split()
            walls = [int(x) for x in walls]
            if walls[0] < walls[2]:
                self.walls[walls[0], walls[1], 1] = True
                self.walls[walls[2], walls[3], 3] = True
            elif walls[0] > walls[2]:
                self.walls[walls[0], walls[1], 3] = True
                self.walls[walls[2], walls[3], 1] = True
            elif walls[1] < walls[3]:
                self.walls[walls[0], walls[1], 2] = True
                self.walls[walls[2], walls[3], 0] = True
            elif walls[1] > walls[3]:
                self.walls[walls[0], walls[1], 0] = True
                self.walls[walls[2], walls[3], 2] = True
        for i in range(1, self.n+1):
            self.walls[i, 1, 0] = True
            self.walls[i, self.m, 2] = True

        for i in range(1, self.m+1):
            self.walls[1, i, 3] = True
            self.walls[self.n, i, 1] = True

    def __init__(self):
        super().__init__()
        self.walls = None
        self.init_state = State(name='1,1', matrix=[1, 1])
        self.goal_state = State()
        self.n = 0
        self.m = 0
        self.number_of_walls = 0
        self.states = set()
        self.states.add(self.init_state)
        self.states.add(self.goal_state)
        print('Problem inputs:')
        self.read_input()

    def initial_state(self):
        return self.init_state

    def actions(self, state):
        actions = list()

        if not self.walls[state.matrix[0], state.matrix[1], 0]:
            actions.append(Action(name='top', cost=1))
        if not self.walls[state.matrix[0], state.matrix[1], 1]:
            actions.append(Action('right', 1))
        if not self.walls[state.matrix[0], state.matrix[1], 2]:
            actions.append(Action(name='bottom', cost=1))
        if not self.walls[state.matrix[0], state.matrix[1], 3]:
            actions.append(Action(name='left', cost=1))
        return actions

    def result(self, state, action):
        if action.name == 'top':
            temp_name = str(state.matrix[0]) + ',' + str(state.matrix[1]-1)
            for _state in self.states:
                if _state.name == temp_name:
                    return _state
            else:
                next_state = State(name=temp_name, matrix=[state.matrix[0], state.matrix[1]-1])
                self.states.add(next_state)
                return next_state
        elif action.name == 'right':
            temp_name = str(state.matrix[0]+1) + ',' + str(state.matrix[1])
            for _state in self.states:
                if _state.name == temp_name:
                    return _state
            else:
                next_state = State(name=temp_name, matrix=[state.matrix[0]+1, state.matrix[1]])
                self.states.add(next_state)
                return next_state
        elif action.name == 'bottom':
            temp_name = str(state.matrix[0]) + ',' + str(state.matrix[1]+1)
            for _state in self.states:
                if _state.name == temp_name:
                    return _state
            else:
                next_state = State(name=temp_name, matrix=[state.matrix[0], state.matrix[1]+1])
                self.states.add(next_state)
                return next_state
        elif action.name == 'left':
            temp_name = str(state.matrix[0]-1) + ',' + str(state.matrix[1])
            for _state in self.states:
                if _state.name == temp_name:
                    return _state
            else:
                next_state = State(name=temp_name, matrix=[state.matrix[0]-1, state.matrix[1]])
                self.states.add(next_state)
                return next_state

    def goal_test(self, state):
        return (state.matrix[1] == self.goal_state.matrix[1]) and (state.matrix[0] == self.goal_state.matrix[0])

    def step_cost(self, state, action):
        return 1.0

    def path_cost(self, actions):
        cost = 0.0
        for action in actions:
            cost += action.cost
        return cost

    def heuristic(self, state):
        dist_x = state.matrix[0]-self.goal_state.matrix[0]
        dist_y = state.matrix[1]-self.goal_state.matrix[1]
        h = int(sqrt(dist_x**2 + dist_y**2))
        return h
