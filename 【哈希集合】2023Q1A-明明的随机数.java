/*
 * @hw id=2023Q1A lang=java
 *
 * 明明的随机数
 */

// @hw code=start
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        Set<Integer> numset = new HashSet<>();
        for(int i=0;i<n;i++) {
            numset.add(in.nextInt());
        }
        List<Integer> numlist = new ArrayList<>(numset);
        Collections.sort(numlist);

        for(int num : numlist) {
            System.out.println(num);
        }
    }
}
// @hw code=end