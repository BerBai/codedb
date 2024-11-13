/*
 * @hw id=2023B lang=java
 *
 * 分割数组的最大差值
 */

// @hw code=start
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] nums = new int[n];
        int rsum = 0, lsum = 0, ans = 0;
        for(int i=0;i<n;i++) {
            nums[i] = in.nextInt();
            rsum += nums[i];
        }
        for(int i=0;i<n;i++) {
            lsum += nums[i];
            rsum -= nums[i];
            ans = Math.max(ans, Math.abs(lsum - rsum));
        }
        System.out.println(ans);
    }
}
// @hw code=end