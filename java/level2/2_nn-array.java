//n^2 배열 자르기
//https://programmers.co.kr/learn/courses/30/lessons/87390?language=java
import java.util.*;
class Solution {
    public static ArrayList<Integer> solution(int n, long left, long right) {
        ArrayList<Integer> arr = new ArrayList<>();
        int num = 0;
        int start = (int)(left%n);
        boolean flag = true;
        for (int i=(int)(left/n); i<n; i++){
            num = i+1;
            for (int j=start; j<n; j++) {
                
                if(num-1 <= j) {
                    arr.add(j+1);
                } else {
                    arr.add(num);
                }
                if (arr.size() >= (int)(right-left)+1) {
                    flag = false;
                    break;
                }
                
                
            }
            start = 0;
            if (flag == false) {
                break;
            }
            
        }
        return arr;
    }
}