//¿ß¿Â
//https://programmers.co.kr/learn/courses/30/lessons/42578?language=java
import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        Arrays.sort(clothes, new Comparator<String[]>() {
           public int compare(String[] o1, String[] o2) {
               return o2[1].compareTo(o1[1]);
           } 
        });
        // for (String[] i : clothes) {
        //     for (String j: i) {
        //         System.out.print(j);
        //     }
        //     System.out.println();
        // }
        ArrayList<Integer> array = new ArrayList<>();
        String now = clothes[0][1];
        int cnt = 0;
        for (int i=0; i<clothes.length; i++) {
            if (clothes[i][1].equals(now)) {
                cnt++;
            }
            else {
                array.add(cnt);
                now = clothes[i][1];
                cnt = 1;
            }
            
        }
        array.add(cnt);
        for (int i : array) {
            //System.out.print(i + " ");
            answer *= (i+1);
        }
        //System.out.println();
        
        return --answer;
    }
}