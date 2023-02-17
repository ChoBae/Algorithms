// CyclicRotation
function solution(A, K) {
  // Implement your solution here
  // K번 반복하며 팝 -> unshift
  let ALen = A.length;
  // 예외 조건(길이 0), K랑 길이랑 같으면 연산 필요 X
  if (ALen === K || ALen === 0) return A;
  // 시간복잡도 최대 100 * 100 -> 통과는 하겠는데 크면 좀 모르곘네(큐 구현하면 개선)
  for (let i = 0; i < K; i++) {
    A.unshift(A.pop());
  }
  return A;
}