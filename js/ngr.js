class NearestGreaterRight {
  constructor(values) {
    this.values = values;
    Array.prototype.top = function () {
      if (this.length == 0) {
        return -1;
      } else {
        return this[this.length - 1];
      }
    };
  }

  calculate = () => {
    const results = [];
    const stack = [];
    const values = this.values;

    const compare = (val1, val2) => {
      let bool;
      if (val1 > val2) {
        bool = true;
      } else {
        bool = false;
      }
      return bool;
    };

    let start = values.length;
    for (let i = start; i >= 0; i--) {
      if (stack.length == 0) {
        results.push(-1);
      } else if (compare(stack.top(), values[i])) {
        results.push(stack.top());
      } else if (stack.length != 0 && compare(values[i], stack.top())) {
        while (stack.length != 0 && compare(values[i], stack.top())) {
          stack.pop();
        }

        if (stack.length == 0) {
          results.push(-1);
        } else {
          results.push(stack.top());
        }
      }
      stack.push(values[i]);
    }
    return results.reverse();
  };
}

const ngr = new NearestGreaterRight([1, 3, 2, 4], false);
console.log(ngr.calculate());
