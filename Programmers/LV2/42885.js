// 구명보트
function solution(people, limit) {
  let answer = 0;
  let save = 0;
  let 구명보트 = [];
  people.sort((a, b) => b - a);
  while (people.length > 0) {
    let nextMen = people.pop();
    if (구명보트.length === 0) {
      구명보트.push(nextMen);
    } else if (구명보트.length === 1) {
      if (구명보트[0] + nextMen <= limit) {
        answer++;
        구명보트 = [];
      } else {
        answer++;
        구명보트 = [nextMen];
      }
    }
  }
  if (구명보트.length > 0) answer++;
  console.log(answer);
  return answer;
}

// function 구명보트합(구명보트){
//     return 구명보트.reduce(function add(sum, currValue) {
//   return sum + currValue;
// }, 0);

// }
solution([70, 50, 80, 50], 100);
