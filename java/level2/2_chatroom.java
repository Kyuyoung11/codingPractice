//����ä�ù�
//https://programmers.co.kr/learn/courses/30/lessons/42888?language=java
import java.util.*;

class Solution {


    private String _doAction(String[] userRecord, Map<String,String> users) {

        switch(userRecord[0]) {
            case "Change":
                break;
            case "Enter":
                return users.get(userRecord[1]) + "님이 들어왔습니다.";
            case "Leave":
                return users.get(userRecord[1]) + "님이 나갔습니다.";
            default:
                break;
        }

        return "";
    }


    private Map<String, String> _createUsers(String[] record) {
        Map<String, String> users = new HashMap<String,String>();

        for(String r : record) {
            // 1. 들어온 정보 split
            String[] userRecord = r.split(" ");

            // 2. Change, Enter인 경우 id, name 저장
            switch(userRecord[0]) {
                case "Change":
                case "Enter":
                    users.put(userRecord[1], userRecord[2]);
                    break;
                case "Leave":
                    break;
                default:
                    break;
            }
        }

        // System.out.println(users);

        return users;

    }

    public String[] solution(String[] record) {


        // 1. 유저 정보 생성
        Map<String, String> users = _createUsers(record);

        // 2. 동작 실행
        ArrayList<String> answerList = new ArrayList<>();

        for (String r: record) {
            String[] userRecord = r.split(" ");
            String actionString = _doAction(userRecord, users);

            if(actionString.length() > 0) {
                answerList.add(_doAction(userRecord, users));
            }
        }

        // 3. Array 변환
        String[] answer = new String[answerList.size()];
        for(int i =0; i<answerList.size(); i++) {
            answer[i] = answerList.get(i);
        }

        return answer;
    }
}