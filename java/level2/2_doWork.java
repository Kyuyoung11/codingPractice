import java.util.*;

class Solution {
    
    public String[] solution(String[][] plans) {
        String[] answer = {};
        
        //1. �ð� �� plan ����
        LinkedList<String[]> planList = _sortPlan(plans);
        
        // for (String[] str : planList) {
        //     for (String s : str) {
        //         System.out.print(s+ " ");
        //     }
        //     System.out.println();
        // }
        
        //2. study ���
        ArrayList<String> workStack = new ArrayList<>();
        workStack.add(_study(plans, 0));
        
        
        return answer;
    }
    
    private LinkedList<String[]> _sortPlan(String[][] plans) {
        LinkedList<String[]> planList = new LinkedList<>();
        for (String[] str : plans) {
            planList.add(str);
        }
        
        Collections.sort(planList, new Comparator<String[]>() {
           @Override
            public int compare(String[] o1, String[] o2) {
                if (o1[1].compareTo(o2[1])>=0) return +1;
                else return -1;
            }
        });
        
        return planList;
    }
    
    
    private String _study(String[][] plans, int index) {
        if (plans.size() == 1) {
            return plans[0][0];
        };
        
        // index+1
        // music 13:00 > computer 12:30 => music 12:30 30 ����
        // music 12:30 30
        // computer 12:30 100
        // science 12:40 50
        
        // index+1
        // computer 14:10 > science 12:40 => computer 12:40 90 ����
        // music 12:30 30
        // computer 12:40 90
        // science 12:40 50 
        // history 14:00 30
        
        // index+1
        // science 13:30 < history 14:00 => return science and remove?
        // music 12:30 30
        // computer 12:40 90 -> computer 13:30 40
        // history 14:00 30
        
        // index-1
        // computer 14:10 > history 14:00 => computer 14:00 10 ����
        // music 12:30 30
        // computer 14:00 10
        // history 14:00 30
        
        if (_calcTime(plans[index]).compareTo(plans[index+1][1]) > 0) {
            //�ð� update
            _study(plans, index+1);
        } else { 
            _study(plans, index-1);
        }
        
        System.out.println(plans[index][0]);
        return plans[index][0];
    }
    
    
    private String _calcTime(String beforeTime, String playTime) {
        
    }
}
