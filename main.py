from problems.RescueRobot import RescueRobot
from problems.EightPuzzle import EightPuzzle
from problems.Rubik import Rubik
from algorithms.DFS import DFS
from algorithms.BFS import BFS
from algorithms.DepthLimitedDFS import DepthLimitedDFS
from algorithms.IterativeDeepening import IterativeDeepening
from algorithms.UniformCost import UniformCost
from algorithms.AStar import AStar
from algorithms.BiDirectional import BiDirectional
from algorithms.consts import FAILURE, SUCCESS


# Adding multiple accepted answers for each Problem/Algorithm, for user convenience
p1_choices = ['1', 'rescue', 'rescue robot', 'robot']
p2_choices = ['2', 'eight', 'puzzle', 'eight puzzle']
p3_choices = ['3', 'rubik', 'cube', 'rubik cube']

uc_choices = ['1', 'uniform cost', 'uniform', 'uc']
dfs_choices = ['2', 'dfs', 'graph dfs', 'graph_dfs']
bfs_choices = ['1', 'bfs', 'breadth first search']
bd_choices = ['3', 'bi-directional', 'bi directional', 'bi', 'bi-directional bfs']
astar_choices = ['4', 'astar', 'a-star', 'a star']
depth_limited_choices = ['2', 'depth limited', 'depth limited dfs', '']
iterative_deepening_choices = ['3', 'iterative', 'deepening', 'iterative deepening']


input_problem = input('Please pick one of the problems below: \n'
                      '1- Rescue Robot\n'
                      '2- Eight Puzzle\n'
                      '3- Rubik Cube\n')

if input_problem.lower() in p1_choices:

    print('Problem inputs: ')
    rescue_robot = RescueRobot()

    input_algorithm = input('Please pick one of the algorithms below: \n1- Uniform Cost\n2- Graph DFS\n3- Bi-Directional\n')

    if input_algorithm in uc_choices:
        uniform_cost = UniformCost(rescue_robot, True)
        uc_target_node = uniform_cost.solve()

        if uc_target_node == FAILURE:
            print('Failed to find a path')
        else:
            search_info = uniform_cost.get_search_info()
            print('Visited Count: {}'.format(search_info['visited_count']))
            print('Expanded Count: {}'.format(search_info['expanded_count']))
            print('Path Cost: {}'.format(search_info['path_cost']))
            print('Max Memory used: {}'.format(search_info['max_memory']))
            print('Path:')
            for _node in search_info['path']:
                print(_node.state.name, end=' -> ')
            print('')
            for _node in search_info['path']:
                if _node.state.matrix is not None:
                    for row in _node.state.matrix:
                        for val in row:
                            if val is not None:
                                print(val, end=' ')
                        print('')
                print('')

    elif input_algorithm in dfs_choices:
        graph_dfs = DFS(rescue_robot, True)
        dfs_target_node = graph_dfs.solve()

        if dfs_target_node == FAILURE:
            print('Failed to find a path')
        elif dfs_target_node == SUCCESS:
            search_info = graph_dfs.get_search_info()
            print('Visited Count: {}'.format(search_info['visited_count']))
            print('Expanded Count: {}'.format(search_info['expanded_count']))
            print('Path Cost: {}'.format(search_info['path_cost']))
            print('Max Memory used: {}'.format(search_info['max_memory']))
            print('Path:')
            for _node in search_info['path']:
                print(_node.state.name, end=' -> ')
            print('')
            for _node in search_info['path']:
                if _node.state.matrix is not None:
                    for row in _node.state.matrix:
                        for val in row:
                            if val is not None:
                                print(val, end=' ')
                        print('')
                print('')

    elif input_algorithm in bd_choices:
        bi_directional = BiDirectional(rescue_robot, True)
        bd_target_node = bi_directional.solve()

        if bd_target_node == FAILURE:
            print('Failed to find a path to goal state')
        elif bd_target_node == SUCCESS:
            search_info = bi_directional.get_search_info()
            print('Visited Count: {}'.format(search_info['visited_count']))
            print('Expanded Count: {}'.format(search_info['expanded_count']))
            print('Path Cost: {}'.format(search_info['path_cost']))
            print('Max Memory used: {}'.format(search_info['max_memory']))
            print('Path:')
            for _node in search_info['path']:
                print(_node.state.name, end=' -> ')
            print('')
            for _node in search_info['path']:
                if _node.state.matrix is not None:
                    for row in _node.state.matrix:
                        for val in row:
                            if val is not None:
                                print(val, end=' ')
                        print('')
                print('')

    elif input_algorithm in astar_choices:
        astar = AStar(rescue_robot, True)
        astar_target_node = astar.solve()
        if astar_target_node == FAILURE:
            print('Failed to find a path to goal state')
        elif astar_target_node == SUCCESS:
            search_info = astar.get_search_info()
            print('Visited Count: {}'.format(search_info['visited_count']))
            print('Expanded Count: {}'.format(search_info['expanded_count']))
            print('Path Cost: {}'.format(search_info['path_cost']))
            print('Max Memory used: {}'.format(search_info['max_memory']))
            print('Path:')
            for _node in search_info['path']:
                print(_node.state.name, end=' -> ')
            print('')
            for _node in search_info['path']:
                if _node.state.matrix is not None:
                    for row in _node.state.matrix:
                        for val in row:
                            if val is not None:
                                print(val, end=' ')
                        print('')
                print('')

elif input_problem.lower() in p2_choices:

    eight_puzzle = EightPuzzle()

    input_algorithm = input('Please pick one of the algorithms below: \n1- Uniform Cost\n2- Graph DFS\n3- Bi-Directional BFS\n4- AStar\n')

    if input_algorithm in uc_choices:
        uniform_cost = UniformCost(eight_puzzle, True)
        uc_target_node = uniform_cost.solve()

        if uc_target_node == FAILURE:
            print('Failed to find a path to goal state')
        elif uc_target_node == SUCCESS:
            search_info = uniform_cost.get_search_info()
            print('Visited Count: {}'.format(search_info['visited_count']))
            print('Expanded Count: {}'.format(search_info['expanded_count']))
            print('Path Cost: {}'.format(search_info['path_cost']))
            print('Max Memory used: {}'.format(search_info['max_memory']))
            print('Path:')
            for _node in search_info['path']:
                print(_node.state.name, end=' -> ')
            print('')
            for _node in search_info['path']:
                if _node.state.matrix is not None:
                    for row in _node.state.matrix:
                        for val in row:
                            if val is not None:
                                print(val, end=' ')
                        print('')
                print('')

    elif input_algorithm in dfs_choices:
        graph_dfs = DFS(eight_puzzle, True)

        dfs_target_node = graph_dfs.solve()

        if dfs_target_node == FAILURE:
            print('Failed to find a path to goal state')
        elif dfs_target_node == SUCCESS:
            search_info = graph_dfs.get_search_info()
            print('Visited Count: {}'.format(search_info['visited_count']))
            print('Expanded Count: {}'.format(search_info['expanded_count']))
            print('Path Cost: {}'.format(search_info['path_cost']))
            print('Max Memory used: {}'.format(search_info['max_memory']))
            print('Path:')
            for _node in search_info['path']:
                print(_node.state.name, end=' -> ')
            print('')
            for _node in search_info['path']:
                if _node.state.matrix is not None:
                    for row in _node.state.matrix:
                        for val in row:
                            if val is not None:
                                print(val, end=' ')
                        print('')
                print('')

    elif input_algorithm in bd_choices:
        bi_directional = BiDirectional(eight_puzzle, True)

        bd_target_node = bi_directional.solve()

        if bd_target_node == FAILURE:
            print('Failed to find a path to goal state')
        elif bd_target_node == SUCCESS:
            search_info = bi_directional.get_search_info()
            print('Visited Count: {}'.format(search_info['visited_count']))
            print('Expanded Count: {}'.format(search_info['expanded_count']))
            print('Path Cost: {}'.format(search_info['path_cost']))
            print('Max Memory used: {}'.format(search_info['max_memory']))
            print('Path:')
            for _node in search_info['path']:
                print(_node.state.name, end=' -> ')
            print('')
            for _node in search_info['path']:
                if _node.state.matrix is not None:
                    for row in _node.state.matrix:
                        for val in row:
                            if val is not None:
                                print(val, end=' ')
                        print('')
                print('')

    elif input_algorithm in astar_choices:
        a_star = AStar(eight_puzzle, True)
        astar_target_node = a_star.solve()

        if astar_target_node == FAILURE:
            print('Failed to find a path to goal state')
        elif astar_target_node == SUCCESS:
            search_info = a_star.get_search_info()
            print('Visited Count: {}'.format(search_info['visited_count']))
            print('Expanded Count: {}'.format(search_info['expanded_count']))
            print('Path Cost: {}'.format(search_info['path_cost']))
            print('Max Memory used: {}'.format(search_info['max_memory']))
            print('Path:')
            for _node in search_info['path']:
                print(_node.state.name, end=' -> ')
            print('')
            for _node in search_info['path']:
                if _node.state.matrix is not None:
                    for row in _node.state.matrix:
                        for val in row:
                            if val is not None:
                                print(val, end=' ')
                        print('')
                print('')

elif input_problem.lower() in p3_choices:
    rubik = Rubik()
    input_algorithm = input('Please pick one of the algorithms below: \n'
                            '1- BFS\n'
                            '2- Depth Limited DFS(14)\n'
                            '3- Iterative Deepening DFS\n')

    if input_algorithm in bfs_choices:
        bfs = BFS(rubik, True)
        bfs_target_node = bfs.solve()

        if bfs_target_node == FAILURE:
            print('Failed to find a path to goal state')
        elif bfs_target_node == SUCCESS:
            print('success')
            search_info = bfs.get_search_info()
            print('Visited Count: {}'.format(search_info['visited_count']))
            print('Expanded Count: {}'.format(search_info['expanded_count']))
            print('Path Cost: {}'.format(search_info['path_cost']))
            print('Max Memory used: {}'.format(search_info['max_memory']))
            print('Path:')
            for _node in search_info['path']:
                print(_node.state.name, end=' -> ')
            print('')
            for _node in search_info['path']:
                if _node.state.matrix is not None:
                    for row in _node.state.matrix:
                        for val in row:
                            if val is not None:
                                print(val, end=' ')
                        print('')
                print('')

    elif input_algorithm in depth_limited_choices:
        depth_limited = DepthLimitedDFS(rubik, True)
        limited_target_node = depth_limited.solve(14)
        if limited_target_node == FAILURE:
            print('Failed to find a path to goal state')
        elif limited_target_node == SUCCESS:
            search_info = depth_limited.get_search_info()
            print('Visited Count: {}'.format(search_info['visited_count']))
            print('Expanded Count: {}'.format(search_info['expanded_count']))
            print('Path Cost: {}'.format(search_info['path_cost']))
            print('Max Memory used: {}'.format(search_info['max_memory']))
            print('Path:')
            for _node in search_info['path']:
                print(_node.state.name, end=' -> ')

    elif input_algorithm in iterative_deepening_choices:
        iterative_deepening = IterativeDeepening(rubik, 14)

        iterative_target_node = iterative_deepening.solve()

        if iterative_target_node == FAILURE:
            print('Failed to find a path to goal state')
        else:
            search_info = iterative_deepening.get_search_info()
            print('Visited Count: {}'.format(search_info['visited_count']))
            print('Expanded Count: {}'.format(search_info['expanded_count']))
            print('Path Cost: {}'.format(search_info['path_cost']))
            print('Max Memory used: {}'.format(search_info['max_memory']))
            print('Path:')
            for _node in search_info['path']:
                print(_node.state.name, end=' -> ')
            print('')

            for _node in search_info['path']:
                if _node.state.matrix is not None:
                    for row in _node.state.matrix:
                        for val in row:
                            if val is not None:
                                print(val, end=' ')
                        print('')
                print('')
