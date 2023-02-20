function solution(A) {
  // Implement your solution here
  let peakNum = Number.MIN_SAFE_INTEGER;
  let checkPeak = 0;
  let peakLi = [];
  // 피크 지점 구하기
  for (let i = 0; i < A.length; i++) {
    if (peakNum < A[i]) {
      peakNum = A[i];
      checkPeak = i;
    } else {
      peakLi.push(checkPeak);
      peakNum = A[i];
    }
  }
  //
  let answer = 1;
  for (let i = 2; i < peakLi.length + 1; i++) {
    let startPeak = peakLi[0];
    // console.log('i: ', i)
    let check = 1;
    for (let j = 1; j < peakLi.length + 1; j++) {
      let curPeak = peakLi[j];
      if (startPeak + i < curPeak) {
        // console.log(curPeak)
        startPeak = curPeak;
        check++;
      }

      if (check === i) {
        answer = i;
        break;
      }
    }
  }
  console.log(answer)
  return answer;
}
solution([1,3,2])