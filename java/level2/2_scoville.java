//´õ ¸Ê°Ô
//https://programmers.co.kr/learn/courses/30/lessons/42626?language=java
import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i: scoville) {
            pq.offer(i);
        }
        int mix, temp;
        while (pq.size() > 1) {
            
            temp = pq.poll();
            //System.out.println(pq.size() + " " + temp);
            if (temp >= K) {
                return answer;
            }
            mix = temp + (pq.poll()) * 2;
            answer++;
            pq.add(mix);
        }
        if(pq.poll() >= K) {
            return answer;    
        }
        return -1;
    }
}