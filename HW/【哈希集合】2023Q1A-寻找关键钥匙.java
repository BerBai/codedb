/*
 * @hw id=2023Q1A lang=java
 *
 * 寻找关键钥匙
 */

// @hw code=start
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String k = in.nextLine();
        String[] boxes = in.nextLine().split(" ");
        Set<Character> set_k = new HashSet<>();
        for (char c : k.toCharArray()) {
            set_k.add(c);
        }
        int ans = -1;
        for (int i = 0; i < boxes.length; i++) {
            Set<Character> set_s = new HashSet<>();
            for (char c : boxes[i].toCharArray()) {
                if (Character.isLetter(c)) {
                    set_s.add(Character.toLowerCase(c));
                }
            }
            if (set_k.equals(set_s)) {
                ans = i + 1;
                break;
            }
        }
        System.out.println(ans);
    }
}
// @hw code=end