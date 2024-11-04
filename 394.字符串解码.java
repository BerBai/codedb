/*
 * @lc app=leetcode.cn id=394 lang=java
 *
 * [394] 字符串解码
 */

// @lc code=start
class Solution {
    public String decodeString(String s) {
        LinkedList<String> stack = new LinkedList<>();
        StringBuilder numStr = new StringBuilder();

        for (char c : s.toCharArray()) {
            if (c <= '9' && c >= '0') {
                numStr = numStr.append(c);
            } else if (c == '[') {
                stack.add(numStr.toString());
                numStr.setLength(0);
                stack.add("[");

            } else if (c == ']') {
                StringBuilder tmp = new StringBuilder();
                while(stack.peekLast()!="[") {
                    tmp.insert(0, stack.removeLast());
                }

                stack.removeLast();
                int num = Integer.parseInt(stack.removeLast());
                while(num-- > 0) {
                    stack.add(tmp.toString());
                }
            } else {
                stack.add(String.valueOf(c));
            }
        }
        return String.join("", stack);
    }
}
// @lc code=end

