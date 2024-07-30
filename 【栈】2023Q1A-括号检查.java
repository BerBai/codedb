/*
 * @hw id=2023Q1A lang=java
 *
 * 括号检查
 */

// @hw code=start
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.nextLine();
        boolean isErr = false;
        int depth = 0;
        int maxDepth = 0;

        if(s.length()%2 == 1) {
            isErr = true;
        } else {
            List<Character> stack = new ArrayList<>();
            for(char c : s.toCharArray()) {
                if(c == '(' || c == '{' || c == '[') {
                    stack.add(c);
                    depth++;
                    maxDepth = Math.max(depth, maxDepth);
                } else {
                    if(stack.isEmpty()) {
                        isErr = true;
                        break;
                    } else {
                        char cl = stack.remove(stack.size()-1);
                        depth--;
                        if(c == ')') {
                            isErr = cl!='('?true:false;
                        } else if(c == '}') {
                            isErr = cl!='{'?true:false;
                        } else if(c == ']') {
                            isErr = cl!='['?true:false;
                        }
                        if(isErr) {
                            break;
                        }
                    }
                }
            }
            if(!stack.isEmpty()) {
                isErr = true;
            }
        }
        System.out.println(isErr?0:maxDepth);
    }
}
// @hw code=end