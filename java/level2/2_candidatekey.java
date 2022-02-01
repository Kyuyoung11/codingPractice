//ÈÄº¸Å°
//https://programmers.co.kr/learn/courses/30/lessons/42890
import java.util.*;
class Solution {
    public int solution(String[][] relation) {
        int answer = 0;
        int max = (int)Math.pow(2,relation[0].length);
        int beat = 1;
        int length = relation[0].length;
        ArrayList<String> ban_arr = new ArrayList<>();
        while(beat < max) {
            ArrayList<Integer> index = new ArrayList<>();
            String str_beat = Integer.toBinaryString(beat);
            int[] list_beat = new int[length];
            boolean flag = false;
            boolean flag2 = false;
            for (int i=0; i< ban_arr.size(); i++) {
                flag = false;
                for (int j=0; j<ban_arr.get(i).length(); j++) {
                    if (ban_arr.get(i).substring(j,j+1).equals("1")) {
                        if (str_beat.substring(str_beat.length()-ban_arr.get(i).length()+j,
                                              str_beat.length()-ban_arr.get(i).length()+j+1)
                           .equals("1")) {
                            flag = true;
                        }
                        else {
                            flag = false;
                            break;
                        }
                    }
                }
                if (flag == true) {
                    flag2 = true;
                    break;
                }
            }
            if (flag2==true) {
                beat++;
                continue;
            }
            
            //System.out.println(str_beat);
            for (int i =0; i < str_beat.length(); i++) {
                if (str_beat.substring(i,i+1).equals("1")){
                    index.add(length-str_beat.length()+i);
                }
            }
            // for (int i : index) {
            //     System.out.print(i+" ");
            // }
            // System.out.println();
            ArrayList<ArrayList<String>> records = new ArrayList<>();
            boolean flag3 = false;
            for (int i=0; i<relation.length; i++) {
                ArrayList<String> record = new ArrayList<>();
                for (int j=0; j<index.size(); j++) {
                    record.add(relation[i][index.get(j)]);
                }
                if (!records.contains(record)) {
                    //System.out.println(record);
                    records.add(record);
                }
                else {
                    flag3 = true;
                    break;
                }
            }
            if (flag3 == false) {
                //System.out.println(str_beat);
                ban_arr.add(str_beat);
                answer+=1;
            }
            beat++;
        }
        return answer;
    }
}