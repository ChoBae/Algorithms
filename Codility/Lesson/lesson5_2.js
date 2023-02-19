// CountDiv
function solution(A, B, K) {
  let numRange = B - A + 1;
  let answer = Math.floor(B / K) - Math.floor((A - 1) / K);
  return answer;
}
