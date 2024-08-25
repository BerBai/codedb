/*
 * @hw id=2023Q1A lang=java
 *
 * 删除最少字符
 */

// @hw code=start
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.nextLine();
        int[] cnt = new int[26];
        Arrays.fill(cnt, Integer.MAX_VALUE);
        for(char c : s.toCharArray()) {
            int i = c - 'a';
            if(cnt[i] == Integer.MAX_VALUE) {
                cnt[i] = 0;
            }
            cnt[i] += 1;
        }
        int mn = Arrays.stream(cnt).min().getAsInt();
        StringBuilder ans = new StringBuilder();
        for(char c : s.toCharArray()) {
            int i = c - 'a';
            if(cnt[i] > mn) {
                ans.append(c);
            }
        }
        System.out.println(ans.toString());
    }
}
// @hw code=end