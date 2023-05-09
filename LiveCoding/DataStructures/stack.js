class Stack {
  constructor() {
    this.storage = {};
    this.size = 0;
  }

  push(value) {
    this.storage[this.size] = value;
    this.size++;
  }
  pop() {
    if (this.size === 0) return null;
    this.size--;
    const result = this.storage[this.size];
    delete this.storage[this.size];
    return result;
  }
  size() {
    return this.size;
  }
}

const stack = new Stack();
stack.push(1);
stack.push(2);
stack.push(3);
console.log(stack, stack.pop()); // 3
