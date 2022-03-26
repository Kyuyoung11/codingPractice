//가장 먼 노드
//https://programmers.co.kr/learn/courses/30/lessons/49189

import java.util.*;
class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0;
        boolean[] visit = new boolean[n];
        for (int i=0; i<edge.length; i++) {
            Arrays.sort(edge[i]);
        }
        visit[0] = true;
        Queue<Integer> q = new LinkedList<>();
        q.offer(1);
        int node;
        int size = 0;
        while (q.size()>0) {
            //System.out.println();
            size = q.size();
            for (int i=0; i<size; i++) {
                node = q.poll();
                //System.out.println(node + " " +size);
                for (int j=0; j<edge.length; j++) {
                    if (edge[j][0] == node && visit[edge[j][1]-1] == false) {
                        q.offer(edge[j][1]);
                        visit[edge[j][1]-1] = true;
                    }
                    else if (edge[j][1] == node && visit[edge[j][0]-1] == false) {
                        q.offer(edge[j][0]);
                        visit[edge[j][0]-1] = true;
                    }
                }
            }
            
        }
        return size;
    }
}