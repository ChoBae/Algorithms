class HashTable {
  constructor(size) {
    this.size = size;
    this.buckets = new Array(size);
  }
  _hash(key) {
    let hash = 0;
    for (let i = 0; i < key.length; i++) {
      hash += key.charCodeAt(i);
    }
    return hash % this.size;
  }
  insert(key, value) {
    const idx = this._hash(key);
    if (!this.buckets[idx]) {
      this.buckets[idx] = new Node(key, value);
    } else {
      let curNode = this.buckets[idx];
      while (curNode) {
        curNode = curNode.next;
      }
      curNode.next = new Node(key, value);
    }
  }
  search(key) {
    const idx = this._hash(key);
    let curNode = this.buckets[idx];
    while (curNode) {
      if (curNode.key === key) {
        return curNode.value;
      }
      curNode = curNode.next;
    }
    return null;
  }
  delete(key) {
    const idx = this._hash(key);
    let curNode = this.buckets[idx];
    let prevNode = null;
    if (!curNode) return console.log("없는 키값임");
    while (curNode) {
      if (curNode.key === key) {
        console.log("제거 되었습니다.");
        if (!prevNode) return;
        prevNode.next = curNode.next;
        return;
      }
      prevNode = curNode;
      curNode = curNode.next;
    }
  }
}

class Node {
  constructor(key, value) {
    this.key = key;
    this.value = value;
    this.next = null;
  }
}

const myHashTable = new HashTable(10);
myHashTable.insert("apple", 5);
myHashTable.insert("banana", 8);
myHashTable.insert("orange", 3);

console.log(myHashTable.search("apple")); // 출력: 5
console.log(myHashTable.search("bananaa")); // 출력: 8
console.log(myHashTable.search("orange")); // 출력: 3

console.log(myHashTable.delete("apple"));
console.log(myHashTable);
