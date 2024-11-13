/*
 * @hw id=2023C lang=java
 *
 * 篮球游戏
 */

// @hw code=start
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String[] ss = in.nextLine().split(",");
        String[] sns = in.nextLine().split(",");
        
        Deque<String> q = new LinkedList<>();
        int i = 0;
        StringBuilder sb = new StringBuilder();
        for(String s : ss) {
            q.offer(s);
            while(!q.isEmpty()) {
                // 先判断左出的，肯定会满足最后一位只能左出条件
                if(q.peek().equals(sns[i])) {
                    sb.append("L");
                    i++;
                    q.poll();
                } else if(q.peekLast().equals(sns[i])) {
                    sb.append("R");
                    i++;
                    q.pollLast();
                } else {
                    break;
                }
            }
        }
        if(sb.length() == sns.length) {
            System.out.println(sb.toString());
        } else {
            System.out.println("NO");
        }
    }
}
// @hw code=end