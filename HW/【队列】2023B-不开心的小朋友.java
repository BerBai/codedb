/*
 * @hw id=2023B lang=java
 *
 * 不开心的小朋友
 */

// @hw code=start
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String s = in.nextLine();
        String[] arr = s.split(" ");
        Queue<Integer> wq = new LinkedList<>();
        Map<String, List<Boolean>> state = new HashMap<>();
        int playNum = 0;
        int angryNum = 0;
        for(String c : arr) {
            if(!state.containsKey(c)) {
                state.put(c, new ArrayList<>(false, false, false));
            }
            if(!state.get(c).get(0)) {
                state.get(c).set(0, true);
                if(playNum>0) {
                    state.get(c).set(1, true);
                    playNum++;
                } else {
                    wq.add(c);
                }
            } else {
                state.get(c).set(2, true);
                if(state.get(c).get(1)) {
                    playNum--;
                    while(!wq.isEmpty() && playNum < n) {
                        String nextc = wq.poll();
                        if(!state.get(nextc).get(2)) {
                            state.get(nextc).set(1, true);
                            playNum++;
                        }
                    }
                } else {
                    angryNum++;
                }
            }
        }
    }
    System.out.println(angryNum);
}
// @hw code=end