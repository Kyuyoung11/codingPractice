// dfs -> 시간초과
import java.util.*;
class Solution {
    static int max = 0;

    int solution(int[][] land) {


        /* dfs 풀이
        for (int i =0; i< 4; i++) {
            _dfs(land,0,i, 0);
        }


        int answer = 0;
        return max;
         */

        for (int i =1; i<land.length; i++) {
            land[i][0] = land[i][0] + Math.max(land[i-1][1], Math.max(land[i-1][2], land[i-1][3]));
            land[i][1] = land[i][1] + Math.max(land[i-1][0], Math.max(land[i-1][2], land[i-1][3]));
            land[i][2] = land[i][2] + Math.max(land[i-1][0], Math.max(land[i-1][1], land[i-1][3]));
            land[i][3] = land[i][3] + Math.max(land[i-1][0], Math.max(land[i-1][1], land[i-1][2]));
        }


        int answer = 0;
        for (int i=0; i<4; i++) {
            if(land[land.length-1][i] > answer) {
                answer = land[land.length-1][i];
            }
        }
        return answer;

    }

    private void _dfs(int[][] land, int c, int r, int sum) {
        if(land.length-1 < c) {
            if (max < sum) {
                max = sum;
                // System.out.println(sum);
            }
            return ;
        }
        // 방문 표시
        sum += land[c][r];

        // System.out.println(c + " " + r + " " + sum + " " + land[c][r]);

        for (int i = 0; i<land[c].length; i++) {
            if(i == r) {
                continue;
            }
            _dfs(land, c+1, i, sum);

        }
    }
}