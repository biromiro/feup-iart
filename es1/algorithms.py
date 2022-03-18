def getPath(node):
    
    path = [node]
    currentNode = node
    
    while(True):
        currentNode = currentNode.previousNode;
        if(not currentNode): break;
        path.append(currentNode);

    path.reverse();
    
    return path;    

def bfs(initial, condition):
        
    nodesToVisit = [initial]
    visited = []
    
    while (nodesToVisit):        
        currentNode = nodesToVisit.pop(0);
                
        if(currentNode in visited): continue;
        if(condition(currentNode)): return getPath(currentNode);
        
        edgeNodes = currentNode.edgeNodes();
        nodesToVisit += edgeNodes;
        
        visited.append(currentNode);
    
    return None;

def dfs(node, condition, visited = []):
    
    if(not node or node in visited): return None;
    if(condition(node)): return getPath(node);

    for edgeNode in node.edgeNodes():
        if(edgeNode in visited): continue;
        val = dfs(edgeNode, condition, visited + [node])
        if(val): return val;
    
    return None;


def dls(node, condition, maxDepth, visited = [], depth = 0):
    
    if(node in visited): return (None, False);
    if(condition(node)): return (getPath(node), False);
    if(maxDepth == depth): return (None, visited != []);
    
    for edgeNode in node.edgeNodes():
        if(edgeNode in visited): continue;
        finalNode, _ = dls(edgeNode, condition, maxDepth, visited + [node], depth + 1)
        if(finalNode): return (finalNode, False);
    
    return (None, visited == []);

def it_deep(initial, condition):
    
    path = None
    curDepth = 1
    
    while (True):
        
        path, remaining = dls(initial, condition, curDepth);
        if(path): return path;
        if(not remaining): return None;
        
        curDepth += 1;