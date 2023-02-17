function solution(survey, choices) {
  var answer = "";
  var res = {};
  var temp;
  for (let i = 0; i < survey.length; i++) {
    if (choices[i] < 4) {
      temp = choices[i];
      if (res[survey[i][0]] === undefined) {
        if (choices[i] === 0) {
          temp = 3;
        } else if (choices[i] === 3) {
          temp = 1;
        }
        res[survey[i][0]] = temp;
      } else res[survey[i][0]] += temp;
    } else {
      if (res[survey[i][1]] === undefined) {
        res[survey[i][1]] = choices[i] - 4;
      } else res[survey[i][1]] += choices[i] - 4;
    }
  }
  console.log(res);
  return answer;
}
