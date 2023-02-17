function solution(want, number, discount) {
  var answer = 0;
  for (let i = 0; i < discount.length - 9; i++) {
    let days = discount.slice(i, i + 10);
    let totalProduct = {};
    let check = true;
    for (let j = 0; j < days.length; j++)
      if (totalProduct[days[j]] === undefined) totalProduct[days[j]] = 1;
      else totalProduct[days[j]] += 1;
    for (let z = 0; z < want.length; z++) {
      if (totalProduct[want[z]] === undefined) {
        check = false;
        break;
      } else if (totalProduct[want[z]] && totalProduct[want[z]] < number[z]) {
        check = false;
        break;
      }
    }
    if (check) answer++;
  }
  return answer;
}

