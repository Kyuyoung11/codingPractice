#시간초과 뜸

import copy

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


def makeTree(nodes, edges):
    treeDict = {node: [] for node in nodes}

    for edge in edges:
        treeDict[edge[0]].append(edge[1])
        treeDict[edge[1]].append(edge[0])

    return treeDict


def makeTreeType(treeDict):
    treeTypeDict = {}

    for key, val in treeDict.items():
        treeTypeDict[key] = getTreeType(key, len(val))

    return treeTypeDict


def validTree(treeDict, rootNode):

    copyTreeDict = copy.deepcopy(treeDict)
    # print("validTree", rootNode)

    queue = [rootNode]

    while(len(queue) > 0):
        node = queue.pop()
        nodeType = getTreeType(node, len(copyTreeDict[node]))

        # print(node, copyTreeDict[node], nodeType)

        for childNode in copyTreeDict[node]:
            if(node in copyTreeDict[childNode]):
                copyTreeDict[childNode].remove(node)

            if(nodeType != getTreeType(childNode, len(copyTreeDict[childNode]))):
                return False

            queue.append(childNode)
    return True




def solution(nodes, edges):
    answer = [0,0]

    treeDict = makeTree(nodes, edges)

    for n in nodes:
        isTree = validTree(treeDict, n)
        if(isTree):
            if(getTreeType(n, len(treeDict[n]))==1):
                answer[0]+=1
            else:
                answer[1]+=1

    return answer