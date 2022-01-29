//완주하지 못한 선수
//https://programmers.co.kr/learn/courses/30/lessons/42576?language=java
import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        boolean flag = false;
        Arrays.sort(participant);
        Arrays.sort(completion);
        for (int i = 0; i<completion.length; i++) {
            if(!completion[i].equals(participant[i])) {
                answer = participant[i];
                flag = true;
                break;
            }
        }
        if (flag == false) {
            answer = participant[participant.length-1];
        }
        return answer;
    }
}