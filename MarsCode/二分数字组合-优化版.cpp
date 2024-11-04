#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

int backstrack(vector<int> arrayA, int index, int sumA, int sumB, int A, int B,
               unordered_map<string, int> &memo) {
  if (index == arrayA.size()) {
    if (sumA % 10 == A && sumB % 10 == B) {
      return 1;
    }
    return 0;
  }

  // 查找缓存，避免重复计算
  string key = to_string(index) + "," + to_string(sumA) + "," + to_string(sumB);
  if (memo.find(key) != memo.end()) {
    return memo[key];
  }

  int countA =
      backstrack(arrayA, index + 1, sumA + arrayA[index], sumB, A, B, memo);
  int countB =
      backstrack(arrayA, index + 1, sumA, sumB + arrayA[index], A, B, memo);
  // 缓存计算结果
  memo[key] = countA + countB;
  return memo[key];
}

int solution(int n, int A, int B, std::vector<int> array_a) {
  unordered_map<string, int> memo;
  int ans = backstrack(array_a, 0, 0, 0, A, B, memo);

  // 计算特殊情况
  int sumNum = 0;
  for (int n : array_a) {
    sumNum += n;
  }
  if (sumNum % 10 == A || sumNum % 10 == B) {
    ans += 1;
  }
  return ans;
}

int main() {
  //  You can add more test cases here
  std::vector<int> array1 = {1, 1, 1};
  std::vector<int> array2 = {1, 1, 1};
  std::vector<int> array3 = {1, 1};

  std::cout << (solution(3, 1, 2, array1) == 3) << std::endl;
  std::cout << (solution(3, 3, 5, array2) == 1) << std::endl;
  std::cout << (solution(2, 1, 1, array3) == 2) << std::endl;

  return 0;
}