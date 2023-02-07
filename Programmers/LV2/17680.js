// function solution(cacheSize, cities) {
//   let answer = 0;
//   let cache = [];
//   while (cities.length > 0) {
//     let nextCity = cities.shift().toUpperCase();
//     // 캐시 히트
//     if (cache.length > 0 && cache.includes(nextCity)) {
//       let target = cache.indexOf(nextCity);
//       cache.splice(target, 1);
//       cache.push(nextCity);
//       answer++;
//       continue;
//     }
//     // 캐시 미스
//     answer += 5;
//     cache.push(nextCity.toUpperCase());
//     if (cache.length > cacheSize) cache.shift();
//   }
//   return answer;
// }

// solution(3, ["a", "b", "c", "a", "b", "d", "c"]);

