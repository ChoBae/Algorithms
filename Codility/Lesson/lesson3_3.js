// TapeEquilibrium
function solution(A) {
  let answer = Number.MAX_SAFE_INTEGER;
  let totalSum = A.reduce((acc, cur) => acc + cur);
  let leftSum = 0;
  let rightSum = 0;
  // 시간 복잡도 : O(n)
  for (let i = 0; i < A.length - 1; i++) {
    leftSum += A[i];
    rightSum = totalSum - leftSum;
    let diff = Math.abs(leftSum - rightSum);
    if (answer > diff) answer = diff;
  }
  return answer;
}
