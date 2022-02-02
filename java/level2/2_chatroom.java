//¿ÀÇÂÃ¤ÆÃ¹æ
//https://programmers.co.kr/learn/courses/30/lessons/42888?language=java
import java.util.*;
class Solution {
    public String[] solution(String[] record) {
        
        Map<String, String> id_hash = new HashMap();
        ArrayList<ArrayList<String>> msg = new ArrayList<>();
        for (int i=0; i<record.length; i++) {
            ArrayList<String> temp = new ArrayList<>();
            String[] str_list = record[i].split(" ");
            // for (String str : str_list) {
            //     System.out.print(str);
            // }
            // System.out.println();
            if (str_list[0].equals("Enter")) {
                id_hash.put(str_list[1], str_list[2]);
                temp.add(str_list[0]);
                temp.add(str_list[1]);
                msg.add(temp);
            }
            else if(str_list[0].equals("Change")) {
                id_hash.put(str_list[1], str_list[2]);
            }
            else {
                temp.add(str_list[0]);
                temp.add(str_list[1]);
                msg.add(temp);
            }
        }
        // for (Map.Entry<String, String> entry : id_hash.entrySet()) {
        //     System.out.println(entry.getKey() + " : " + entry.getValue());
        // }
        
        String[] answer = new String[msg.size()];
        for (int i =0; i<msg.size(); i++) {
            if (msg.get(i).get(0).equals("Enter")) {
                answer[i] = id_hash.get(msg.get(i).get(1))+"´ÔÀÌ µé¾î¿Ô½À´Ï´Ù.";
            }
            else {
                answer[i] = id_hash.get(msg.get(i).get(1))+"´ÔÀÌ ³ª°¬½À´Ï´Ù.";
            }
        }
        return answer;
        
    }
}