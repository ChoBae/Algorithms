// fish
function solution(A, B) {
  let stack = [];
  let answer = 0;
  for (let i = 0; i < A.length; i++) {
    if (B[i] === 1) stack.push(A[i]);
    else {
      while (stack.length > 0) {
        // 하류 물고기가 잡아먹음
        if (stack[stack.length - 1] > A[i]) break;
        // 상류 물고기가 잡아먹음
        else stack.pop();
      }
    }
    // 모든 하류 물고기가 상류 물고기를 잡아먹음.
    if (stack.length === 0) answer++;
  }
  return answer + stack.length;
}