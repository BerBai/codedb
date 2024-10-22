/*
 * @hw id=2023B lang=java
 *
 * 数字游戏
 */

// @hw code=start
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        int[] nums = new int[n];
        for(int i=0;i<n;i++) {
            nums[i] = in.nextInt();
        }
        List<Integer> list = new ArrayList<>();
        int sum = 0;
        int flag = 0;
        for(int num : nums) {
            sum += num;
            if(list.contains(sum%m)) {
                flag = 1;
                break;
            }
            list.add(sum%m);
        }
        System.out.println(flag);
    }
}
// @hw code=end