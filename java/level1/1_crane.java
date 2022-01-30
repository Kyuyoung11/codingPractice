//크레인 인형뽑기 게임
//https://programmers.co.kr/learn/courses/30/lessons/64061?language=java
import java.util.*;
class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        ArrayList<Integer> stack = new ArrayList<>();
        for (int i = 0; i<moves.length; i++) {
            int index = 0;
            if (board[board.length-1][moves[i]-1] == 0) {
                continue;
            }
            while(board[index][moves[i]-1] == 0) {
                index++;
            }
            if (stack.size() > 0){
                if (stack.get(stack.size()-1) == board[index][moves[i]-1]) {
                    stack.remove(stack.size()-1);
                    answer+=2;
                }
                else {
                    stack.add(board[index][moves[i]-1]);
                }
            }
            else {
                stack.add(board[index][moves[i]-1]);
            }
            board[index][moves[i]-1] = 0;
            // for (int a : stack) {
            //     System.out.print(a);
            // }
            // System.out.println();
            
            
        }
        
        return answer;
    }
}