// FrogJmp
function solution(X, Y, D) {
  let dis = Y - X;
  let answer = Math.ceil(dis / D);

  return answer;
}
