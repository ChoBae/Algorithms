function solution(fees, records) {
  let answer = [];
  let statusLi = {};
  let feeList = {};
  // console.log(fees, records)
  // 입차 , 출차를 기록해야함
  for (let i = 0; i < records.length; i++) {
    let [time, num, statusLitus] = records[i].split(" ");
    // In
    if (statusLi[num] === undefined) {
      statusLi[num] = time;
      if (feeList[num + ""] === undefined) feeList[num + ""] = 0;
    }
    // Out
    else {
      let curHour = Number(statusLi[num][0] + statusLi[num][1]);
      let curMin = Number(statusLi[num][3] + statusLi[num][4]);
      let outHour = Number(time[0] + time[1]);
      let outMin = Number(time[3] + time[4]);
      let min = (outHour - curHour) * 60 + (outMin - curMin);
      // console.log(min)
      feeList[num + ""] += min;
      statusLi[num] = undefined;
    }
  }
  // 안나간차 찾기
  for (let key in statusLi) {
    if (statusLi[key] !== undefined) {
      let curHour = Number(statusLi[key][0] + statusLi[key][1]);
      let curMin = Number(statusLi[key][3] + statusLi[key][4]);
      feeList[key + ""] += (23 - curHour) * 60 + (59 - curMin);
    }
  }
  // 요금 계산
  const arr = Object.entries(feeList);
  arr.sort(([a], [b]) => Number(a) - Number(b));

  for (let i = 0; i < arr.length; i++) {
    let minus = arr[i][1] - fees[0] > 0 ? arr[i][1] - fees[0] : 0;
    console.log(minus);
    let cost = fees[1] + Math.ceil(minus / fees[2]) * fees[3];
    answer.push(cost);
  }
  return answer;
}
