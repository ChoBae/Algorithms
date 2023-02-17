// MaxCounters;
// O(N*K)
function solution(N, A) {
  // Implement your solution here
  // 두가지의 오퍼레이션(증가, 맥스 카운터)
  // A는 빈배열 아님
  // max 값을 갱신하고 있다가 배열보다 큰값일때는 맥스값을 모두 더해줌?
  // 순서는 보장해야함.
  let answer = Array(N).fill(0);
  let maxLen = N;
  let numCnt = -1;
  // 시간복잡도 n * n
  for (let i = 0; i < A.length; i++) {
    if (A[i] > maxLen && numCnt > 0) {
      // 모든 배열을 더해주는게 맞는 건인가..
      // answer = answer.map((value) => numCnt);
      answer = Array(N).fill(numCnt);
      continue;
    } else if (A[i] < maxLen) answer[A[i] - 1] += 1;

    if (numCnt < answer[A[i] - 1]) numCnt = answer[A[i] - 1];
  }
  return answer;
}

solution(5, [6, 6, 6, 6, 6, 6]);


// O(N + M)
function solution(N, A) {
  let answer = Array(N).fill(0);
  let maxCnt = 0;
  let lastMaxCnt = 0;

  for (let i = 0; i < A.length; i++) {
    if (A[i] > N) {
      lastMaxCnt = maxCnt;
    } else {
      answer[A[i] - 1] = Math.max(answer[A[i] - 1], lastMaxCnt) + 1;
      maxCnt = Math.max(maxCnt, answer[A[i] - 1]);
    }
  }

  for (let i = 0; i < N; i++) {
    answer[i] = Math.max(answer[i], lastMaxCnt);
  }

  return answer;
}