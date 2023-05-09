class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}
class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  append(value) {
    const curNode = new Node(value);
    if (!this.head) this.head = curNode;
    if (this.tail) this.tail.next = curNode;
    this.tail = curNode;
  }
  popleft() {
    if (!this.head) return console.log("empty queue");
    const targetNode = this.head;
    this.head = this.head.next;
    return targetNode;
  }
  //     appendleft() {
  //     //   if (!)
  //   }
  search(value) {
    let curNode = this.head;
    while (curNode) {
      if (curNode.value === value) return true;
      curNode = curNode.next;
    }
    return false;
  }
}

const q = new Queue();
q.append(1);
q.append(2);
console.log(q.search(3));
// q.popleft();

console.log(q);
