// FrogRiverOne
function solution(X, A) {
  if (A.length === 1 && A[0] !== 1) return -1;
  let visited = Array(X).fill(false);
  let answer = 0;
  let Li = [];
  for (let i = 0; i < A.length; i++) {
    if (Li.length === X) break;
    if (visited[A[i] - 1]) continue;
    answer++;
    visited[A[i] - 1] = true;
    Li.push(A[i]);
  }
  answer = Li.length === X ? answer + 1 : -1;

  return answer;
  // 발판이 다 생겨야 넘을 수 있음. 그냥 올 true 됐을때
}

solution(5, [1, 1, 1, 1, 1]);
