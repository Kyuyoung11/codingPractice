//이상한 문자 만들기
//https://programmers.co.kr/learn/courses/30/lessons/12930?language=java
class Solution {
    public String solution(String s) {
        String answer = "";
        int index = 0;
        for (int i=0; i<s.length();i++) {
           
            String current = s.substring(i,i+1);
            //System.out.println(current);
            if(current.equals(" ")) {
                answer+=" ";
                index = 0;
                continue;
            }
            else if ((index)%2==0) {
                answer += current.toUpperCase();
                
            }
            else {
                answer += current.toLowerCase();
            }
            index++;
        }
        return answer;
    }
}