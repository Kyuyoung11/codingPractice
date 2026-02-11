from collections import deque

def get_tree_type(rootNode, childNodeCnt):
    #홀짝 -> 1
    #역홀짝 -> 2
    #해당 x -> -1
    if(rootNode%2 == childNodeCnt%2):
        return 1

    return 2


def make_tree(nodes, edges):
    treeDict = {node: [] for node in nodes}

    for edge in edges:
        treeDict[edge[0]].append(edge[1])
        treeDict[edge[1]].append(edge[0])

    return treeDict


def make_tree_type(treeDict):
    treeTypeDict = {}

    for key, val in treeDict.items():
        treeTypeDict[key] = get_tree_type(key, len(val)-1)  #루트노드가 아닌 경우, childNodeCnt -1 해야함

    return treeTypeDict



def solution(nodes, edges):
    answer = [0,0]

    treeDict = make_tree(nodes, edges)
    treeTypeDict = make_tree_type(treeDict)
    visited = {node: False for node in nodes}

    for n in nodes:
        if not visited[n]:
            #트리 만들기
            tree_nodes = []
            queue = deque([n])
            visited[n] = True

            while queue:
                curNode = queue.popleft()
                tree_nodes.append(curNode)
                for childNode in treeDict[curNode]:
                    if not visited[childNode]:
                        visited[childNode] = True
                        queue.append(childNode)

            #루트노드 설정 후 확인
            for rootNode in tree_nodes:
                result = True
                rootNodeType = get_tree_type(rootNode, len(treeDict[rootNode]))
                for childNode in tree_nodes:
                    if(rootNode == childNode): continue
                    if(rootNodeType != treeTypeDict[childNode]):
                        result=False
                        break

                if(result):
                    if(rootNodeType==1):
                        answer[0]+=1
                    elif(rootNodeType==2):
                        answer[1]+=1




    return answer