/*
 * @hw id=2023B lang=java
 *
 * 找出符合要求的字符串子串
 */

// @hw code=start
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s1 = in.nextLine();
        String s2 = in.nextLine();
        Set<Character> set1 = new HashSet<>();
        for (char c : s1.toCharArray()) {
            set1.add(c);
        }
        Set<Character> set2 = new HashSet<>();
        for (char c : s2.toCharArray()) {
            set2.add(c);
        }
        StringBuilder sb = new StringBuilder();
        for (char c : set1) {
            if (set2.contains(c)) {
                sb.append(c);
            }
        }
        char[] ans = sb.toString().toCharArray();
        Arrays.sort(ans);
        System.out.println(new String(ans));
    }
}
// @hw code=end