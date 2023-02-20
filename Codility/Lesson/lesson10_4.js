// peak
function solution(A) {
  const N = A.length;
  if (N < 3) return 0;

  let peaks = [];

  for (let i = 1; i < N - 1; i++) {
    if (A[i] > A[i - 1] && A[i] > A[i + 1]) peaks.push(i);
  }

  const peakN = peaks.length;
  if (peakN === 0) return 0; //peak인 숫자가 없는 경우

  for (let i = peakN; i >= 2; i--) {
    //블럭의 최대 개수는 peak의 개수 이하이다.
    if (N % i === 0) {
      const K = N / i; // 블럭 안의 원소 개수

      let idx = 0; //peak이 배치된 블럭의 수

      for (let i in peaks) {
        //peak을 블럭에 배치한다.
        let start = idx * K;
        let end = (idx + 1) * K;
        if (peaks[i] >= start && peaks[i] < end) {
          idx++;
        }
      }

      if (idx === i) return i;
    }
  }

  return 1;
}
