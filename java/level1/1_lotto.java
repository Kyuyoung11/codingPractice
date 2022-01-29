class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = {0,0};
        int zero_cnt = 0;
        int cnt = 0;
        for (int i = 0; i<lottos.length; i++) {
            //System.out.println(i);
            if (lottos[i] == 0) {
                zero_cnt++;
            }
            else {
                for (int j = 0; j<win_nums.length; j++){
                    if (lottos[i] == win_nums[j]) {
                        cnt++;
                        break;
                    }
                }
            }
        }
        //System.out.println(cnt);
        if (cnt == 0) {
            answer[1] = 6;
        }
        else 
            answer[1] = 7-cnt;
        if (cnt+zero_cnt == 0) {
            answer[0] = 6;
        }
        else 
            answer[0] = 7-cnt-zero_cnt;
        return answer;
    }
}