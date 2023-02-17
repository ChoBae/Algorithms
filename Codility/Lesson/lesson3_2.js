// PermMissingElem
function solution(A) {
  let answer = 0;
  const maxNum = A.length + 1;
  if (maxNum === 1) {
    return answer;
  }
  const check = Array(maxNum - 1).fill(false);
  for (let i = 0; i < A.length; i++) {
    check[A[i] - 1] = true;
  }
  answer = check.indexOf(false) + 1;
  return answer || maxNum;
}