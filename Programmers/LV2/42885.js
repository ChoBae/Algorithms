// 구명보트
function solution(people, limit) {
  // 최대 두명, 무게 제한
  let answer = 0;
  people.sort((a, b) => a - b); // 오름차순 정렬
  while (people.length > 0) {
    // 가장 무거운놈 꺼내기
    let curHeavy = people.pop();
    // 만약 제일 가벼운놈과 같이 나갈 수 있을때
    if (people[0] + curHeavy <= limit) {
      people.shift();
    }
    answer++;
  }
  return answer;
}
