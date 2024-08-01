/*
 * @hw id=2023C lang=java
 *
 * 找朋友
 */

// @hw code=start
import java.util.*;

public class Main{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] height = new int[n];
        for(int i=0;i<n;i++) {
            height[i] = in.nextInt();
        }
        List<Integer> list = new ArrayList<>();
        int[] ans = new int[n];

        for(int i=0;i<n;i++) {
            int h = height[i];
            if(!stack.isEmpty() && h > height[stack.get(stack.size()-1)]) {
                int top = stack.get(stack.size()-1);
                ans[top] = i;
            }
            stack.add(i);
        }
        for(int i=0;i<n;i++) {
            System.out.print(ans[i] + " ");
        }
        System.out.println();
    }
}
// @hw code=end