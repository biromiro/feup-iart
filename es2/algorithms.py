from queue import PriorityQueue


def getPath(node):

    path = [node]
    currentNode = node

    while (True):
        currentNode = currentNode.previousNode
        if (not currentNode): break
        path.append(currentNode)

    path.reverse()

    return path


def bfs(initial, condition):

    nodesToVisit = [initial]
    visited = []

    while (nodesToVisit):
        currentNode = nodesToVisit.pop(0)

        if (currentNode in visited): continue

        visited.append(currentNode)

        if (condition(currentNode)):
            return f'BFS Result: \n{getPath(currentNode)}\nVisited {len(visited) + 1} nodes:\n{visited}\n'

        edgeNodes = currentNode.edgeNodes()
        nodesToVisit += edgeNodes

    return None


def dfs(node, condition, visited=[]):

    if (not node or node in visited): return None
    if (condition(node)):
        return f'DFS Result: \n{getPath(node)}\nVisited {len(visited) + 1} nodes:\n{visited + [node]}\n'

    for edgeNode in node.edgeNodes():
        if (edgeNode in visited): continue
        val = dfs(edgeNode, condition, visited + [node])
        if (val): return val

    return None


def dls(node, condition, maxDepth, visited=[], depth=0):

    if (node in visited): return (None, False)
    if (condition(node)):
        return (
            f'DLS Result (max depth of {maxDepth}): \n{getPath(node)}\nVisited {len(visited) + 1} nodes:\n{visited + [node]}\n',
            False)
    if (maxDepth == depth): return (None, visited != [])

    for edgeNode in node.edgeNodes():
        if (edgeNode in visited): continue
        finalNode, _ = dls(edgeNode, condition, maxDepth, visited + [node],
                           depth + 1)
        if (finalNode): return (finalNode, False)

    return (None, visited == [])


def it_deep(initial, condition):

    path = None
    curDepth = 1

    while (True):

        path, remaining = dls(initial, condition, curDepth)
        if (path): return path
        if (not remaining): return None

        curDepth += 1


def ucost(initial, condition):

    nodesToVisit = PriorityQueue()
    nodesToVisit.put((initial.distance, initial))
    visited = []

    while (not nodesToVisit.empty()):
        heuristicVal, currentNode = nodesToVisit.get()

        if (currentNode in visited): continue

        visited.append(currentNode)

        if (condition(currentNode)):
            return f'UCost Result: Visited Nodes: {len(visited) + 1} \n'

        edgeNodes = currentNode.edgeNodes(currentNode.distance + 1)

        for node in edgeNodes:
            nodesToVisit.put((node.distance, node))

    return None


def greedy(initial, condition, heuristic):

    nodesToVisit = PriorityQueue()
    nodesToVisit.put((heuristic(initial), initial))

    visited = []

    while (not nodesToVisit.empty()):
        heuristicVal, currentNode = nodesToVisit.get()

        if (currentNode in visited): continue

        visited.append(currentNode)

        if (condition(currentNode)):
            return f'Greedy Result: Visited Nodes: {len(visited) + 1} \n'

        edgeNodes = currentNode.edgeNodes()

        for node in edgeNodes:
            nodesToVisit.put((heuristic(node), node))

    return None


def astar(initial, condition, heuristic):

    nodesToVisit = PriorityQueue()
    nodesToVisit.put((heuristic(initial), initial))
    visited = []

    while (not nodesToVisit.empty()):
        heuristicVal, currentNode = nodesToVisit.get()

        if (currentNode in visited): continue

        visited.append(currentNode)

        if (condition(currentNode)):
            return f'AStar Result: Visited Nodes: {len(visited) + 1} \n'

        edgeNodes = currentNode.edgeNodes(currentNode.distance + 1)

        for node in edgeNodes:
            heuristicNode = node.distance + heuristic(node)
            nodesToVisit.put((heuristicNode, node))

    return None
