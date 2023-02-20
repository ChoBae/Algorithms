// MaxDoubleSliceSum
function solution(A) {
  let len = A.length;

  let left = new Array(len).fill(0);
  let right = new Array(len).fill(0);

  for (let i = 1; i < len - 1; i++) {
    left[i] = Math.max(left[i - 1] + A[i], 0);
  }

  for (let i = len - 2; i >= 1; i--) {
    right[i] = Math.max(right[i + 1] + A[i], 0);
  }
  let answer = 0;
  for (let i = 1; i < len - 1; i++) {
    answer = Math.max(answer, left[i - 1] + right[i + 1]);
  }
  return answer;
}

solution([3,2,6,-1,4,5,-1,2])