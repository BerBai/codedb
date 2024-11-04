import java.util.*;

public class Main {
    public static int backtrack(int[] arrayA, int index, int sumA, int sumB, int A, int B) {
        if (index == arrayA.length) {
            if (sumA % 10 == A && sumB % 10 == B) {
                return 1;
            }
            return 0;
        }
        // 选择数字加入第一组
        int countA = backtrack(arrayA, index + 1, sumA + arrayA[index], sumB, A, B);
        // 选择数字加入第二组
        int countB = backtrack(arrayA, index + 1, sumA, sumB + arrayA[index], A, B);
        return countA + countB;
    }

    public static int solution(int n, int A, int B, int[] array_a) {
        int ans = backtrack(array_a, 0, 0, 0, A, B);
        // 计算特殊情况
        int sumNum = Arrays.stream(array_a).sum();
        if (sumNum % 10 == A || sumNum % 10 == B) {
            ans += 1;
        }
        return ans;
    }

    public static void main(String[] args) {
        int[] array1 = { 1, 1, 1 };
        int[] array2 = { 1, 1, 1 };
        int[] array3 = { 1, 1 };

        System.out.println(solution(3, 1, 2, array1) == 3);
        System.out.println(solution(3, 3, 5, array2) == 1);
        System.out.println(solution(2, 1, 1, array3) == 2);
    }
}