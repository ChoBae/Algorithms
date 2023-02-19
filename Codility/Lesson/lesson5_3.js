// GenomicRangeQuery
// O(N+M)
function solution(S, P, Q) {
  let answer = [];
  for (let i = 0; i < P.length; i++) {
    let start = P[i];
    let end = Q[i];
    let sliceSeq = S.slice(start, end + 1);

    if (sliceSeq.indexOf("A") !== -1) answer.push(1);
    else if (sliceSeq.indexOf("C") !== -1) answer.push(2);
    else if (sliceSeq.indexOf("G") !== -1) answer.push(3);
    else answer.push(4);
  }
  return answer;
}