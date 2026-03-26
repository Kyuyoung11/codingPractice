#https://school.programmers.co.kr/learn/courses/30/lessons/468373
from itertools import product
from collections import deque

def make_tree(edges):
    tree_dict = {}
    for edge in edges:
        if(edge[0] not in tree_dict):
            tree_dict[edge[0]] = []
        if(edge[1] not in tree_dict):
            tree_dict[edge[1]] = []
        tree_dict[edge[0]].append([edge[1],edge[2]])
        tree_dict[edge[1]].append([edge[0],edge[2]])

    # print(tree_dict)
    return tree_dict

def make_com(k):

    coms = list(product([1,2,3], repeat = k))
    # print(coms)

    return coms

def infect(tree, current_type, infected):
    queue = deque()
    visited = [False for _ in range(len(tree)+1)]


    for infect_node in infected:
        queue.append(infect_node) #감염되어있는 노드는 queue에 미리 삽입
        visited[infect_node] = True

    while queue:
        current_node = queue.popleft()

        for node in tree[current_node]:

            if not visited[node[0]] and node[1] == current_type:
                queue.append(node[0])
                infected.append(node[0])
                visited[node[0]] = True

    return infected

def solution(n, infection, edges, k):
    answer = 0

    # 노드별로 이어진 노드, type 저장
    tree = make_tree(edges)

    # 중복조합
    coms = make_com(k)

    max_infection =  0

    for combi in coms:

        infected = [infection]
        past_type = 0

        for t in combi:
            if(past_type == t): continue
            infected = infect(tree, t, infected)
            # print(combi, infected)

        if(max_infection < len(infected)):
            max_infection = len(infected)


    return max_infection