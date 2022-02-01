//½ÇÆÐÀ²
//https://programmers.co.kr/learn/courses/30/lessons/42889?language=java
import java.util.*;
class Solution {
    public static ArrayList<Integer> solution(int N, int[] stages) {
        ArrayList<Integer> answer = new ArrayList<>();
        Map <Integer, Double> map = new HashMap();
        int[] fail_cnt = new int[N];
        for (int i =0; i<N; i++) {
            map.put(i+1, 0.0);
        }
        for (int i: stages) {
            for (int j=0; j<i; j++) {
                if (j>=N) {continue;}
                map.put(j+1,map.get(j+1)+1);
            }
            if (i<=N) {
                fail_cnt[i-1]++;
            }
        }
        
        
        for (int i : map.keySet()) {
            if (map.get(i)!=0) {
                map.put(i,(double)fail_cnt[i-1]/map.get(i));
            }
        }
        List<Map.Entry<Integer, Double>> entries = new ArrayList<>(map.entrySet());
        Collections.sort(entries, new Comparator<Map.Entry<Integer, Double>>(){
            public int compare(Map.Entry<Integer, Double> o1, Map.Entry<Integer, Double> o2) {
                return o2.getValue().compareTo(o1.getValue());
            }
        });
        for (Map.Entry<Integer, Double> entry : entries) {
            answer.add(entry.getKey());
        }
        return answer;
    }
}