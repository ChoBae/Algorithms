class HashTable {
  constructor() {
    this.table = {};
  }

  // 해시 함수를 이용하여 키를 인덱스로 변환하는 메서드
  hash(key) {
    let hash = 0;
    for (let i = 0; i < key.length; i++) {
      hash += key.charCodeAt(i);
    }
    return hash % 37; // 37은 임의의 소수입니다.
  }

  // 키와 값을 추가하는 메서드
  put(key, value) {
    const index = this.hash(key);
    console.log(index);
    this.table[index] = value;
  }

  // 인덱스에 해당하는 값을 반환하는 메서드
  get(key) {
    const index = this.hash(key);
    return this.table[index];
  }

  // 인덱스에 해당하는 값을 삭제하는 메서드
  remove(key) {
    const index = this.hash(key);
    delete this.table[index];
  }
}

const myTable = new HashTable();

myTable.put("apple", 1500);
myTable.put("banana", 1000);
myTable.put("cherry", 2000);

console.log(myTable.get("apple")); // 1500
console.log(myTable.get("banana")); // 1000
console.log(myTable.get("cherry")); // 2000

myTable.remove("banana");

console.log(myTable.get("banana")); // undefined
