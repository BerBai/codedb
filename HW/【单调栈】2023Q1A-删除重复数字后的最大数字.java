/*
 * @hw id=2023Q1A lang=java
 *
 * 删除重复数字后的最大数字
 */

// @hw code=start
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.nextLine();
        Map<Character, Integer> cnt = new HashMap<>();
        for(char c : s.toCharArray()) {
            cnt.put(c, cnt.getOrDefault(c, 0) + 1);
        }
        List<Character> stack = new ArrayList<>();
        Set<Character> used = new HashSet<>();
        for(char c : s.toCharArray()) {
            if(used.contains(c)) {
                // 如果这个数字已经被使用，那么就直接数量减1，避免入栈，减少计算次数
                cnt.put(c, cnt.get(c) - 1);
            } else {
                // 如果这个数字没有被使用，那么就入栈，入栈前需要检查是否需要移除若干栈顶元素
                while (!stack.isEmpty() && c > stack.get(stack.size() - 1) && cnt.get(stack.get(stack.size() - 1)) > 1) {
                    // 计数大于1，并且小于c，则移除（移除较小数）
                    cnt.put(stack.get(stack.size() - 1), cnt.get(stack.get(stack.size()-1))-1);
                    used.remove(stack.get(stack.size() - 1));
                    stack.remove(stack.size() - 1);
                }
                stack.add(c);
                used.add(c);
            }
        }
        
        // 得到的栈就是最终结果
        StringBuilder sb = new StringBuilder();
        for(Character c : stack) {
            sb.append(c);
        }
        System.out.println(sb.toString());
    }
}
// @hw code=end