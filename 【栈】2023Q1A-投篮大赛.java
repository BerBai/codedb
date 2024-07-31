/*
 * @hw id=2023Q1A lang=java
 *
 * 投篮大赛
 */

// @hw code=start
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String[] ops = in.nextLine().split(" ");
        ArrayList<Integer> stack = new ArrayList<>();
        boolean isErr = false;

        for(String s : ops) {
            if(!s.equals("D") && !s.equals("+") && !s.equals("C")) {
                stack.add(Integer.parseInt(s));
            } else if(s.equals("D") && stack.size() >= 1) {
                stack.add(stack.get(stack.size()-1)*2);
            } else if(s.equals("+") && stack.size() >= 2) {
                stack.add(stack.get(stack.size()-1) + stack.get(stack.size()-2));
            } else if(s.equals("C") && stack.size() >= 1) {
                stack.remove(stack.size()-1);
            } else {
                isErr = true;
                break;
            }
        }

        int sum = 0;
        if(!isErr) {
            int len = stack.size();
            for(int i=0;i<len;i++) {
                sum += stack.get(i);
            }
        }
        System.out.println(isErr?-1:sum);
        in.close();
    }
}
// @hw code=end