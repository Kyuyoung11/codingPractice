//두 개 뽑아서 더하기
//https://programmers.co.kr/learn/courses/30/lessons/68644?language=java
import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        
        ArrayList<Integer> array = new ArrayList<>();
        for (int i = 0; i<numbers.length-1; i++) {
            int num = 0;
            for (int j = i+1; j<numbers.length; j++) {
                num = numbers[i] + numbers[j];
                //System.out.println(num);
            
                if (!array.contains(num)) {
                    array.add(num);
                }
            }
            
        }
        
        Collections.sort(array);
        
        int[] answer = new int[array.size()];
        for (int i = 0; i<array.size(); i++) {
            answer[i] = array.get(i);
        }
        
        
        return answer;
    }
}