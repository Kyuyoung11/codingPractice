//괄호 회전하기
//https://programmers.co.kr/learn/courses/30/lessons/76502
import java.util.*;
class Solution {
    public int solution(String s) {
        int answer = 0;
        
        String[] left = {"(", "{", "["};
        ArrayList<String> left_arr = new ArrayList<>(Arrays.asList(left));
        ArrayList<String> arr = new ArrayList<>();
        
        for (int i=0; i<s.length()-1; i++) {
            
            boolean flag = true;
            for (int j =0; j<s.length(); j++) {
                if (left_arr.contains(s.substring(j,j+1))) {
                    //System.out.println(s.substring(j,j+1));
                    arr.add(s.substring(j,j+1));
                }
                else if (arr.size() > 0) {
                    if(s.substring(j,j+1).equals(")")) {
                        
                        if (arr.get(arr.size()-1).equals("(")) {
                            arr.remove(arr.size()-1);
                        }
                        else {
                            flag = false;
                            break;
                        }
                    }
                    else if(s.substring(j,j+1).equals("}")) {
                        if (arr.get(arr.size()-1).equals("{")) {
                            arr.remove(arr.size()-1);
                        }
                        else {
                            flag = false;
                            break;
                        }
                    }
                    else {
                        if (arr.get(arr.size()-1).equals("[")) {
                            arr.remove(arr.size()-1);
                        }
                        else {
                            flag = false;
                            break;
                        }
                    }
                            
                }
                else {
                    flag = false;
                    break;
                }
            }
            //System.out.println(flag);
            if (flag == true && arr.size() == 0) {
                answer++;
            }
            s = s.substring(1,s.length()) + s.substring(0,1);
            //System.out.println(s);
            arr.clear();
            
        }
        return answer;
    }
}