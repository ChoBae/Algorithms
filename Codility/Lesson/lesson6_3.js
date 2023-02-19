// Triangle
function solution(A) {
  const sortA = A.sort((a, b) => a - b);
  for (let i = 0; i < sortA.length - 2; i++) {
    const a = sortA[i];
    const b = sortA[i + 1];
    const c = sortA[i + 2];

    if (a + b > c && b + c > a && c + a > b) return 1;
  }
  return 0;
}
