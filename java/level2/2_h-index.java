//H-Index
//https://programmers.co.kr/learn/courses/30/lessons/42747
import java.util.*;
class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        Arrays.sort(citations);
        int[] cnt = new int[citations[citations.length-1]+1];
        for (int i : citations) {
            for (int j=0; j<=i; j++) {
                cnt[j]++;
            }
        }
        
        for (int i =cnt.length-1; i>0; i--) {
            if (i <= cnt[i] && i>=cnt[i+1]){
                answer = i;
                break;
            }
        }
        
        return answer;
    }
}