// MaxSliceSum
function solution(A) {
  // 순서가 보장되어야함.
  // 갯수는 상관 없어보이네 음..
  let answer = A[0];
  let dp = [A[0]];
  for (let i = 1; i < A.length; i++) {
    dp[i] = Math.max(A[i], dp[i - 1] + A[i]);
    answer = Math.max(answer, dp[i]);
  }
  return answer;
}