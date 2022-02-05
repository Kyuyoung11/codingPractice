//네트워크
//https://programmers.co.kr/learn/courses/30/lessons/43162
import java.util.*;
class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        ArrayList<ArrayList<Integer>> nw = new ArrayList<>();
       
        
        for (int i=0; i<computers.length; i++) {
            for (int j=0; j<computers[i].length; j++) {
                ArrayList<Integer> temp = new ArrayList<>();
                boolean flag = false;
                if (computers[i][j] == 1) {
                    if (nw.size() == 0) {
                        temp.add(i);
                        temp.add(j);
                        nw.add(temp);
                        
                    } else {
                        for (int a=0; a<nw.size(); a++) {
                            if (nw.get(a).contains(i)) {
                                if (flag == false) {
                                    temp = (ArrayList<Integer>)nw.get(a).clone();
                                    temp.add(j);
                                    nw.set(a, temp);
                                    flag = true;
                                } else {
                                    nw.remove(a);
                                }
                            }else if (nw.get(a).contains(j)) {
                                if (flag == false){
                                    temp = (ArrayList<Integer>)nw.get(a).clone();
                                    temp = nw.get(a);
                                    temp.add(i);
                                    nw.set(a, temp);
                                    flag = true;
                                } else {
                                    nw.remove(a);
                                }
                            }
                        }
                        if (flag == false) {
                            temp.add(i);
                            temp.add(j);
                            nw.add(temp);
                        }
                    }
                }
                // System.out.println(nw.size());
                // for (int x=0; x<nw.size(); x++) {
                //     for (int y=0; y<nw.get(x).size(); y++){
                //         System.out.print(nw.get(x).get(y) + " ");
                //     }
                //     System.out.println();
                // }
                
            }
        }
        
        return nw.size();
    }
}