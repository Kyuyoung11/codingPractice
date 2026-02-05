# (수정중)

def getTreeType(rootNode, childNodeCnt):
    #홀짝 -> 1
    #역홀짝 -> 2
    #해당 x -> -1
    if(rootNode%2 == 0): #짝
        if(childNodeCnt%2 ==0): #짝
            return 1
        else:
            return 2

    else: #홀
        if(childNodeCnt%2 ==0): #짝
            return 2
        else:
            return 1

def makeTree(rootNode, nodes, edges, visited, treeType):
    # print('makeTree', rootNode, visited, treeType)
    if(treeType == -1):
        return treeType

    visited[rootNode]=True

    childNodes = []
    for edge in edges:
        if(edge[0] == rootNode and visited[edge[1]] == False):
            childNodes.append(edge[1])
        elif(edge[1] == rootNode and visited[edge[0]] == False):
            childNodes.append(edge[0])


    newTreeType = getTreeType(rootNode, len(childNodes))
    # print(childNodes, newTreeType)
    if(treeType > 0 and treeType!=newTreeType):
        return -1

    for childNode in childNodes:
        return makeTree(childNode, nodes, edges, visited, newTreeType)

    if(len(childNodes) == 0):
        return newTreeType

    return -1


def solution(nodes, edges):
    answer = []


    treeCnt = 0
    reverseTreeCnt = 0
    for n in nodes:
        visited = {node: False for node in nodes}
        treeType = makeTree(n, nodes, edges, visited, 0)
        # print(treeType, 'treeType')
        if(treeType == 1):
            treeCnt+=1
        elif(treeType == 2):
            reverseTreeCnt +=1

    answer.append(treeCnt)
    answer.append(reverseTreeCnt)
    return answer