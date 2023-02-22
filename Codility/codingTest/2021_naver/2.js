// 배열 A와 기준 R이 주어진다.
// 배열 A에서 R 길이만큼을 빼고 남은 값들의 종류의 개수가 최대가 되는 경우를 찾아, 그 종류의 개수를 반환하라
// 배열의 순서는 바꿀 수 없다. A의 길이는 최대 10만. 배열의 원소 값도 최대 10만이었던걸로 기억한다.
// A=[2, 3, 1, 4, 2, 2], R=3 일때 [4, 2, 2]를 빼면 남은 값의 종류의 개수가 3으로 최대가 된다.
function solution(A, R) {
  let aWord = {};
  let rWord = {};
  for (let i = 0; i < A.length; i++) {
    if (aWord[A[i]] === undefined) aWord[A[i]] = 1;
    else aWord[A[i]] += 1;
  }

  for (let i = 0; i < R.length; i++) {
    if (rWord[R[i]] === undefined) rWord[R[i]] = 1;
    else rWord[R[i]] += 1;
  }
  for (let [key, value] of Object.entries(aWord)) {
    if (rWord[key] !== undefined) aWord[key] -= rWord[key];
  }
  console.log(aWord, rWord);
  let answer = 0;
  for (let value in aWord) {
    answer += aWord[value];
  }
  console.log(answer);
}
solution([2, 3, 1, 4, 2, 2], [4, 2, 2]);
