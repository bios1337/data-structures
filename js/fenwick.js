class FenwickTree {
  constructor(values) {
    if (!Array.isArray(values)) {
      throw new Error("values must be an array");
    }
    this.tree = [0, ...values];

    this.length = this.tree.length;

    for (let i = 1; i < this.length; i++) {
      let j = i + this.lsb(i);
      if (j < this.length) this.tree[j] += this.tree[i];
    }
  }

  lsb = (i) => {
    return i & -i;
  };

  add = (index, value) => {
    let i = index + 1;
    while (i < this.length) {
      this.tree[i] += value;
      i += this.lsb(i);
    }
  };

  prefixSum = (index) => {
    let total = 0;
    let i = index + 1;
    while (i != 0) {
      total += this.tree[i];
      i -= this.lsb(i);
    }
    return total;
  };

  sum = (left, right) => {
    return this.prefixSum(right) - this.prefixSum(left - 1);
  };
}

fenwickTree = new FenwickTree([0, 4, 6, 19, 2000, -2000]);
console.log(fenwickTree.sum(0, 2));
fenwickTree.add(0, 2);
console.log(fenwickTree.sum(4, 5));
fenwickTree.add(0, 2);
console.log(fenwickTree.sum(4, 5));
console.log(fenwickTree.sum(0, 5));

