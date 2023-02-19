//  PassingCars
function solution(A) {
  let east = 0; // 동쪽으로 간 차의 수
  let passing = 0; // 페어 차량 수
  for (let value of A) {
    // 동쪽으로 간 차를 찾았을때
    if (value === 0) east++;
    // 서쪽으로 간 차량일때, 현재 동쪽으로 간 차 개수만큼 더함.
    // 현재 동쪽으로 간 차 개수만큼 짝이 될 수 있어서
    else passing += east;
    // 예외 처리 : 1,000,000,000 제한
    if (passing > 1000000000) return -1;
  }
  return passing;
}
