/*
 * @hw id=2023Q1A lang=java
 *
 * 集五福
 */

// @hw code=start
import java.util.*;

public class Main { 
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String[] team = in.nextLine().split(",");
        int[] cnt = new int[5];
        for(String p : team) {
            for(int i = 0; i < p.length(); i++) {
                cnt[i] += p.charAt(i) - '0';
            }
        }
        System.out.println(Arrays.stream(cnt).min().getAsInt());
    }
}
// @hw code=end