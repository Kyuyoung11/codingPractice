//가장 큰 수
//https://programmers.co.kr/learn/courses/30/lessons/42746?language=java
import java.util.*;
class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        ArrayList<String> arr = new ArrayList<>();
        for (int i : numbers) {
            arr.add(i+"");
        }
        Collections.sort(arr, new Comparator<String>() {
            public int compare(String o1, String o2) {
                return (o2+o2+o2+o2).substring(0,4).compareTo((o1+o1+o1+o1).substring(0,4));
            }
        });
        if(arr.get(0).equals("0")) return "0";
        for (String i : arr) {
            answer += i;
        }
        
        
        return answer;
    }
}