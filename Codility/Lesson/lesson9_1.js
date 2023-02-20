// MaxProfit
function solution(A) {
  let minPrice = Infinity; // 최소 가격을 무한대로 초기화
  let maxProfit = 0; // 최대 이익을 0으로 초기화

  for (let i = 0; i < A.length; i++) {
    if (A[i] < minPrice) {
      // 현재 가격이 최소 가격보다 작으면 최소 가격 갱신
      minPrice = A[i];
    } else if (A[i] - minPrice > maxProfit) {
      // 이익 계산
      maxProfit = A[i] - minPrice;
    }
  }

  return maxProfit;
}