var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
var PriorityQueue = /** @class */ (function () {
    function PriorityQueue(elems) {
        this.heapSize = elems.length;
        this.heapCapacity = elems.length * 2;
        this.heap = __spreadArray([], elems, true).concat(elems.map(function () { return 0; }));
        // construct the heap using heapify
        for (var i = Math.max(0, (this.heapSize / 2 - 1) | 0); i >= 0; i--) {
            this.sink(i);
        }
        console.log(this.isMinHeap(0));
    }
    PriorityQueue.prototype.isMinHeap = function (i) {
        if (i > this.heapSize)
            return true;
        var _a = this.getChildren(i), left = _a[0], right = _a[1];
        var val = this.heap[i];
        if (left < this.heapSize && !this.less(val, this.heap[left])) {
            return false;
        }
        if (right < this.heapSize && !this.less(val, this.heap[right])) {
            return false;
        }
        return this.isMinHeap(left) && this.isMinHeap(right);
    };
    PriorityQueue.prototype.poll = function () {
    };
    PriorityQueue.prototype.peek = function () {
    };
    PriorityQueue.prototype.removeAt = function (i) {
        if (this.isEmpty())
            return null;
    };
    PriorityQueue.prototype.insert = function (value) {
        if (value === null) {
            throw new Error('value must not be null');
        }
        if (this.heapSize < this.heapCapacity) {
            this.heap[this.heapSize] = value;
        }
        else {
            this.heap.push(value);
            this.heapCapacity += 1;
        }
        this.swim(this.heapSize);
        this.heapSize += 1;
    };
    PriorityQueue.prototype.less = function (val1, val2) {
        return this.heap[val1] < this.heap[val2];
    };
    PriorityQueue.prototype.isEmpty = function () {
        return false;
    };
    PriorityQueue.prototype.clear = function () {
    };
    PriorityQueue.prototype.getParent = function (i) {
        return (i / 2 | 0);
    };
    PriorityQueue.prototype.getChildren = function (i) {
        return [2 * i + 1, 2 * i + 2];
    };
    PriorityQueue.prototype.swim = function (i) {
        var parent = (i - 1) / 2 | 0;
        while (i > 0 && this.less(i, parent)) {
            this.swap(this.heap, parent, i);
            i = parent;
            parent = (i - 1) / 2 | 0;
        }
    };
    PriorityQueue.prototype.sink = function (i) {
        while (true) {
            var _a = this.getChildren(i), left = _a[0], right = _a[1];
            var smallest = left;
            if (right < this.heapSize && this.less(right, left)) {
                smallest = right;
            }
            if (left >= this.heapSize && this.less(i, smallest))
                break;
            this.swap(this.heap, smallest, i);
            console.log('hahaha');
            i = smallest;
        }
    };
    PriorityQueue.prototype.swap = function (arr, from, to) {
        if (from > this.heapSize || to > this.heapSize)
            return;
        var temp = arr[from];
        arr[from] = arr[to];
        arr[to] = temp;
    };
    return PriorityQueue;
}());
var pq = new PriorityQueue([1, 9, 0, 4, 6, -1, 2000]);
