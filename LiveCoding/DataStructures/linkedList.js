class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  addToTail(value) {
    const node = new Node(value);
    if (!this.head) {
      this.head = node;
    }
    if (this.tail) {
      this.tail.next = node;
    }
    this.tail = node;
  }

  removeHead() {
    if (!this.head) {
      return null;
    }
    const value = this.head.value;
    this.head = this.head.next;
    return value;
  }

  contains(target) {
    let node = this.head;
    while (node) {
      if (node.value === target) {
        return true;
      }
      node = node.next;
    }
    return false;
  }
}

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

const linkedList = new LinkedList();
linkedList.addToTail(1);
linkedList.removeHead();
linkedList.addToTail(2);
linkedList.addToTail(3);
console.log(linkedList); // true
