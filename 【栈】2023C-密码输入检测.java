/*
 * @hw id=2023C lang=java
 *
 * 密码输入检测
 */

// @hw code=start
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.nextLine();
        List<Character> stack = new ArrayList<>();
        for (char c : s.toCharArray()) {
            if(c == '<' && stack.size() >= 1) {
                stack.remove(stack.size() - 1);
            } else if(c != '<') {
                stack.add(c);
            }
        }
        
        int flag = 0;
        for(char c : stack) {
            if(Character.isUpperCase(c)) {
                flag |= 0b0001;
            } else if (Character.isLowerCase(c)) {
                flag |= 0b0010;
            } else if (Character.isDigit(c)) {
                flag |= 0b0100;
            } else if (!Character.isLetterOrDigit(c) && !Character.isWhitespace(c)) {
                flag |= 0b1000;
            }
        }
        StringBuilder sb = new StringBuilder();

        for(int i=0;i<stack.size();i++) {
            sb.append(stack.get(i));
        }

        if(flag==0b1111 && stack.size() >= 8) {
            System.out.println(sb.toString() + ",true");
        } else {
            System.out.println(sb.toString() + ",false");
        }
    }
}
// @hw code=end