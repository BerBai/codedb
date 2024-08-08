/*
 * @hw id=2023C lang=java
 *
 * 找最小数
 */

// @hw code=start
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.nextLine();
        int n = in.nextInt();
        List<Character> stack = new ArrayList<>();

        for(char c : s.toCharArray()) {
            while(!stack.isEmpty() && c < stack.get(stack.size()-1) && n > 0) {
                stack.remove(stack.size()-1);
                n--;
            }
            stack.add(c);
        }
        while(n > 0) {
            stack.remove(stack.size()-1);
            n--;
        }
        StringBuilder sb = new StringBuilder();
        for(Character c : stack) {
            sb.append(c);
        }
        System.out.println(sb.toString());
    }
}
// @hw code=end