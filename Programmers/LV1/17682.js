// 다트 게임
// 3번 쏨, 횟수당 0~10점 획득가능
// *(해당점수와 전의점수 2배) , # (해당 점수 마이너스 변환)
// *는 첫번째로 등장할수도있는데 첫번째만 적용 (예제 4번)
// *와 #은 중첩될 수 있다. -2배(예제 5번)
// input은 점수 | 보너스 | 옵션 으로 이루어짐
function solution(dartResult) {
  var answer = [];
  let status = [];
  let stack = "";
  for (let i = 0; i < dartResult.length; i++) {
    // S,D,T 일 경우
    if (
      (dartResult[i] === "S") |
      (dartResult[i] === "D") |
      (dartResult[i] === "T")
    ) {
      if (dartResult[i] === "S") {
        status.push(Number(stack) ** 1);
      } else if (dartResult[i] === "D") {
        status.push(Number(stack) ** 2);
      } else {
        status.push(Number(stack) ** 3);
      }

      stack = "";
    }
    // *, # 이나 숫자일 경우
    else {
      if (dartResult[i] === "*") {
        status[status.length - 2] *= 2;
        status[status.length - 1] *= 2;
      } else if (dartResult[i] === "#") {
        status[status.length - 1] *= -1;
      } else {
        stack += dartResult[i];
      }
    }
  }
  answer = status.reduce((a, b) => a + b, 0);
  return answer;
}

