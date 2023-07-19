# Basic searching algorithms

# Class for each node in the grid
class Node:
    def __init__(self, row, col, is_obs, h):
        self.row = row        # coordinate
        self.col = col        # coordinate
        self.is_obs = is_obs  # obstacle?
        self.g = None         # cost to come (previous g + moving cost)
        self.h = h            # heuristic
        self.cost = None      # total cost (depend on the algorithm)
        self.parent = None    # previous node

def dijkstra(grid, start, goal):
    '''Return a path found by Dijkstra alogirhm 
       and the number of steps it takes to find it.

    arguments:
    grid - A nested list with datatype int. 0 represents free space while 1 is obstacle.
           e.g. a 3x3 2D map: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    start - The start node in the map. e.g. [0, 0]
    goal -  The goal node in the map. e.g. [2, 2]

    return:
    path -  A nested list that represents coordinates of each step (including start and goal node), 
            with data type int. e.g. [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2]]
    steps - Number of steps it takes to find the final solution, 
            i.e. the number of nodes visited before finding a path (including start and goal node)

    >>> from main import load_map
    >>> grid, start, goal = load_map('test_map.csv')
    >>> dij_path, dij_steps = dijkstra(grid, start, goal)
    It takes 10 steps to find a path using Dijkstra
    >>> dij_path
    [[0, 0], [1, 0], [2, 0], [3, 0], [3, 1]]
    '''
    ### YOUR CODE HERE ###
    path = []
    found = False
    dist = []
    nodes = []
    vis = []
    unit = 1  # Cost of going to adjacent block
    data = []

    ####################################################################
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            if grid[i][j] == 0:
                new = [i, j]
                nodes.append(new)

    vis.append(start)
    data.append(start)

    for i in nodes:
        new = [i, float('inf')]
        dist.append(new)

    for n in dist:
        if n[0] == start:
            n[1] = 0

    dist.sort(key=lambda x: x[1])
    i = dist[0][0][0]
    j = dist[0][0][1]
    dist.pop(0)

    if i >= 0 and j + 1 >= 0:
        for n in dist:
            if n[0] == [i, j + 1]:
                n[1] = unit
                data.append([[i, j], [i, j + 1]])

    if i + 1 >= 0 and j >= 0:
        for n in dist:
            if n[0] == [i + 1, j]:
                n[1] = unit
                data.append([[i, j], [i + 1, j]])

    if i >= 0 and j - 1 >= 0:
        for n in dist:
            if n[0] == [i, j - 1]:
                n[1] = unit
                data.append([[i, j], [i, j - 1]])

    if i - 1 >= 0 and j >= 0:
        for n in dist:
            if n[0] == [i - 1, j]:
                n[1] = unit
                data.append([[i, j], [i - 1, j]])

    while vis.count(goal) == 0:
        dist.sort(key=lambda x: x[1])

        i = dist[0][0][0]
        j = dist[0][0][1]

        if grid[i][j] == 0:
            if [i, j] not in vis:
                vis.append(dist[0][0])
                m = dist[0][1]
                dist.pop(0)

                if 0 <= i <= 9 and 0 <= j + 1 <= 9:
                    if [i, j + 1] not in vis:
                        for n in dist:
                            if n[0] == [i, j + 1] and n[1] > m + unit:
                                n[1] = m + unit
                                data.append([[i, j], [i, j + 1]])

                if 0 <= i + 1 <= 9 and 0 <= j <= 9:
                    if [i + 1, j] not in vis:
                        for n in dist:
                            if n[0] == [i + 1, j] and n[1] > m + unit:
                                n[1] = m + unit
                                data.append([[i, j], [i + 1, j]])

                if 0 <= i <= 9 and 0 <= j - 1 <= 9:
                    if [i, j - 1] not in vis:
                        for n in dist:
                            if n[0] == [i, j - 1] and n[1] > m + unit:
                                n[1] = m + unit
                                data.append([[i, j], [i, j - 1]])

                if 0 <= i - 1 <= 9 and 0 <= j <= 9:
                    if [i - 1, j] not in vis:
                        for n in dist:
                            if n[0] == [i - 1, j] and n[1] > m + unit:
                                n[1] = m + unit
                                data.append([[i, j], [i - 1, j]])
            else:
                dist.pop(0)
        else:
            # print("obstacle")
            dist.pop(0)

        if vis.count(goal) == 1:
            dist.clear()
            found = True
            # print("Goal reached by visiting", vis)
            # dist.sort(key=lambda x: x[1])
            break

    data.pop(0)
    # print(data)
    path.append(goal)
    vargoal = goal
    while vargoal != start:
        for var in data:
            if var[1] == vargoal:
                vargoal = var[0]
                path.insert(0, vargoal)

    steps = len(vis)
#######################################################################################

    if found:
        print(f"It takes {steps} steps to find a path using Dijkstra")
    else:
        print("No path found")
    return path, steps


def astar(grid, start, goal):
    '''Return a path found by A* alogirhm 
       and the number of steps it takes to find it.

    arguments:
    grid - A nested list with datatype int. 0 represents free space while 1 is obstacle.
           e.g. a 3x3 2D map: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    start - The start node in the map. e.g. [0, 0]
    goal -  The goal node in the map. e.g. [2, 2]

    return:
    path -  A nested list that represents coordinates of each step (including start and goal node), 
            with data type int. e.g. [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2]]
    steps - Number of steps it takes to find the final solution, 
            i.e. the number of nodes visited before finding a path (including start and goal node)

    >>> from main import load_map
    >>> grid, start, goal = load_map('test_map.csv')
    >>> astar_path, astar_steps = astar(grid, start, goal)
    It takes 7 steps to find a path using A*
    >>> astar_path
    [[0, 0], [1, 0], [2, 0], [3, 0], [3, 1]]
    '''
    ### YOUR CODE HERE ###
    path = []
    found = False
    dist = []
    nodes = []
    vis = []
    unit = 1  # Cost of going to adjacent block
    data = []

    def man_dist(a, b):
        return sum(abs(e1 - e2) for e1, e2 in zip(a, b))

    ####################################################################
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            if grid[i][j] == 0:
                new = [i, j]
                nodes.append(new)

    vis.append(start)
    data.append(start)

    for i in nodes:
        new = [i, float('inf'), float('inf')]
        dist.append(new)

    for n in dist:
        if n[0] == start:
            n[1] = 0

    dist.sort(key=lambda x: x[1])
    i = dist[0][0][0]
    j = dist[0][0][1]
    dist.pop(0)

    if i >= 0 and j + 1 >= 0:
        for n in dist:
            if n[0] == [i, j + 1]:
                n[1] = unit + man_dist([i, j + 1], goal)
                n[2] = man_dist([i, j + 1], goal)
                data.append([[i, j], [i, j + 1]])

    if i + 1 >= 0 and j >= 0:
        for n in dist:
            if n[0] == [i + 1, j]:
                n[1] = unit + man_dist([i + 1, j], goal)
                n[2] = man_dist([i + 1, j], goal)
                data.append([[i, j], [i + 1, j]])

    if i >= 0 and j - 1 >= 0:
        for n in dist:
            if n[0] == [i, j - 1]:
                n[1] = unit + man_dist([i, j - 1], goal)
                n[2] = man_dist([i, j - 1], goal)
                data.append([[i, j], [i, j - 1]])

    if i - 1 >= 0 and j >= 0:
        for n in dist:
            if n[0] == [i - 1, j]:
                n[1] = unit + man_dist([i - 1, j], goal)
                n[2] = man_dist([i - 1, j], goal)
                data.append([[i, j], [i - 1, j]])

    while vis.count(goal) == 0:
        dist.sort(key=lambda x: x[1])
        dist.sort(key=lambda x: x[2])

        i = dist[0][0][0]
        j = dist[0][0][1]

        if grid[i][j] == 0:
            if [i, j] not in vis:
                vis.append(dist[0][0])

                m = dist[0][1]
                dist.pop(0)

                if 0 <= i <= 9 and 0 <= j + 1 <= 9:
                    if [i, j + 1] not in vis:
                        for n in dist:
                            if n[0] == [i, j + 1] and n[1] > m + unit + man_dist([i, j + 1], goal):
                                n[1] = m + unit + man_dist([i, j + 1], goal)
                                n[2] = man_dist([i, j + 1], goal)
                                data.append([[i, j], [i, j + 1]])

                if 0 <= i + 1 <= 9 and 0 <= j <= 9:
                    if [i + 1, j] not in vis:
                        for n in dist:
                            if n[0] == [i + 1, j] and n[1] > m + unit + man_dist([i + 1, j], goal):
                                n[1] = m + unit + man_dist([i + 1, j], goal)
                                n[2] = man_dist([i + 1, j], goal)
                                data.append([[i, j], [i + 1, j]])

                if 0 <= i <= 9 and 0 <= j - 1 <= 9:
                    if [i, j - 1] not in vis:
                        for n in dist:
                            if n[0] == [i, j - 1] and n[1] > m + unit + man_dist([i, j - 1], goal):
                                n[1] = m + unit + man_dist([i, j - 1], goal)
                                n[2] = man_dist([i, j - 1], goal)
                                data.append([[i, j], [i, j - 1]])

                if 0 <= i - 1 <= 9 and 0 <= j <= 9:
                    if [i - 1, j] not in vis:
                        for n in dist:
                            if n[0] == [i - 1, j] and n[1] > m + unit + man_dist([i - 1, j], goal):
                                n[1] = m + unit + man_dist([i - 1, j], goal)
                                n[2] = man_dist([i - 1, j], goal)
                                data.append([[i, j], [i - 1, j]])
            else:
                dist.pop(0)
        else:
            # print("obstacle")
            dist.pop(0)

        if vis.count(goal) == 1:
            dist.clear()
            found = True
            # print("Goal reached by visiting", vis)
            #dist.sort(key=lambda x: x[1])
            break

    data.pop(0)
    # print(data)
    path.append(goal)
    vargoal = goal
    while vargoal != start:
        for var in data:
            if var[1] == vargoal:
                vargoal = var[0]
                path.insert(0, vargoal)

    steps = len(vis)

    ####################################################################
    if found:
        print(f"It takes {steps} steps to find a path using A*")
    else:
        print("No path found")
    return path, steps


# Doctest
if __name__ == "__main__":
    # load doc test
    from doctest import testmod, run_docstring_examples
    # Test all the functions
    testmod()
