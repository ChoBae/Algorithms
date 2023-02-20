function solution(N) {
  // 1. 약수 구함
  // 2. 2씩 곱해서 제일 작은거 찾음.
  let rect = [];
  let answer = Number.MAX_SAFE_INTEGER;
    for (let i = 1; i <= Math.sqrt(N); i++) {
    // 약수 일때
    if (N % i === 0) {
      let target = N / i;
      rect.push([i, target]);
    }
  }
  // 최소값 구하기
  for (let i = 0; i < rect.length; i++) {
    answer = Math.min(answer, rect[i][0] * 2 + rect[i][1] * 2);
  }
  return answer;
}

solution(36);