// 링크드 리스트로 구현하기
class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  append(value) {
    const curNode = new Node(value);
    if (!this.head) {
      this.head = curNode;
    }
    if (this.tail) {
      this.tail.next = curNode;
    }
    this.tail = curNode;
  }
  popleft() {
    if (!this.head) return console.log("큐가 비었습니다.");
    const targetValue = this.head;
    if (this.head.next) this.head = this.head.next;
    else this.head = null;
    return targetValue.value;
  }
  appendleft(value) {
    const curNode = new Node(value);
    if (!this.head) this.head = curNode;
    if (!this.tail) this.tail = curNode;
    else if (this.tail && this.head) {
      curNode.next = this.head;
      this.head = curNode;
    }
  }
}

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

const q = new Queue();
// q.append(1);
q.appendleft(2);
// q.append(2);
q.append(3);
// console.log(q.popleft());
console.log(q);
