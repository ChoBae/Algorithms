// MaxProductOfThree
function solution(A) {
  // 음수끼리의 연산을 생각을 안했음.
  // 순서를 안지키고 가능한방법이..

  let answer = 0;
  let len = A.length;
  // 내림차순 정렬
  A.sort((a, b) => b - a);
  // 음수를 포함한 3개의 수의 조합을 생각해보면 음수 * 음수 * 양수가 되어야함. 
  answer =
    A[len - 1] * A[len - 2] * A[0] > A[0] * A[1] * A[2]
      ? A[len - 1] * A[len - 2] * A[0]
      : A[0] * A[1] * A[2];
  return answer;
}
