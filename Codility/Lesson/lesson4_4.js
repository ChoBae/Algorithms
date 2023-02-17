// MissingInteger;
function solution(A) {
  let set = new Set(A);

  let smallest = 1;

  while (set.has(smallest)) {
    smallest++;
  }

  return smallest;
}
