// NumberOfDiscIntersections
function solution(A) {
  const N = A.length;
  const start = Array(N).fill(0);
  const end = Array(N).fill(0);
  // 각 좌표별 시작, 끝값 구하기
  for (let i = 0; i < N; i++) {
    start[i] = i - A[i];
    end[i] = i + A[i];
  }
  // 오름 차순 정렬
  start.sort((a, b) => a - b);
  end.sort((a, b) => a - b);
  //   console.log(start, end)
  let count = 0;
  let j = 0;
  for (let i = 0; i < N; i++) {
    while (j < N && end[i] >= start[j]) {
      //   console.log(`j=${j} i=${i} end = ${end[i]} start = ${start[j]}`)
      count += j - i;
      j++;
    }
    // 예외처리
    if (count > 10000000) return -1;
  }

  return count;
}