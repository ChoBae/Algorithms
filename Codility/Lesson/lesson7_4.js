// distinct
function solution(A) {
  // n개의 배열 A
  let setA = new Set(A);
  return setA.size;
}
