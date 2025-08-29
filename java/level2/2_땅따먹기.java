// dfs -> 시간초과

class Solution {
    static int max = 0;

    int solution(int[][] land) {


        for (int i =0; i< 4; i++) {
            _dfs(land,0,i, 0);
        }


        int answer = 0;
        return max;

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