//K¹øÂ°¼ö
//https://programmers.co.kr/learn/courses/30/lessons/42748?language=java
import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for (int i =0; i<commands.length; i++) {
            int[] temp = new int[commands[i][1]-commands[i][0]+1];
            for (int j=commands[i][0]; j<=commands[i][1]; j++) {
                temp[j-commands[i][0]] = array[j-1];
                //System.out.println(array[j]);
            }
            Arrays.sort(temp);
            // for (int a : temp) {
            //     System.out.println(a);
            // }
            //System.out.println(temp[commands[i][2]-1]);
            answer[i] = temp[commands[i][2]-1];
        }
        return answer;
    }
}