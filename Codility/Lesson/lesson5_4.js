// Min Avg Two Slice    O(N)
function solution(A) {
  // A는 N개의 배열, 빈배열이 아니당~
  let min = Number.MAX_SAFE_INTEGER;
  let minIndex = 0;
  for (let i = 0; i < A.length - 1; i++) {
    // 예제를 보면 보통 2~3개의 합에서 최소값이 정해짐
    // i부터 연속된 2개 체크
    let twoSum = (A[i] + A[i + 1]) / 2;
    if (min > twoSum) {
      min = twoSum;
      minIndex = i;
    }
    // i부터 연속된 3개 체크
    if (i + 2 <= A.length - 1) {
      let threeSum = (A[i] + A[i + 1] + A[i + 2]) / 3;
      if (min > threeSum) {
        min = threeSum;
        minIndex = i;
      }
    }
  }
  return minIndex;
}
