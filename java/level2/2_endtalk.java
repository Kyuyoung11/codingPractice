//영어 끝말잇기
//https://programmers.co.kr/learn/courses/30/lessons/12981
import java.util.*;
class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        String l_word = words[0].substring(words[0].length()-1,words[0].length());
        String f_word = "";
        ArrayList<String> words_arr = new ArrayList<>();
        int cnt = 1;
        words_arr.add(words[0]);
        
        for (int i=1; i<words.length; i++) {
            f_word = words[i].substring(0,1);
            if (!f_word.equals(l_word) || words_arr.contains(words[i])) {
                answer[0] = (i % n) + 1;
                answer[1] = (cnt / n) + 1;
                break;
            }
            words_arr.add(words[i]);
            
            l_word = words[i].substring(words[i].length()-1, words[i].length());
            //System.out.println(words[i]+ " " + l_word + " " + words_arr.size());
            
            cnt++;
        }

        return answer;
    }
}