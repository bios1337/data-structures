class PriorityQueue {
    heapSize: number;
    heap: Array<number>;
    heapCapacity: number;
    constructor(elems: Array<number>) {
        this.heapSize = elems.length;
        this.heapCapacity = elems.length * 2;
        this.heap = [...elems].concat(elems.map(() => 0));

        // construct the heap using heapify
        for(let i = Math.max(0, (this.heapSize / 2 - 1) | 0); i >= 0; i--) {
            this.sink(i);
        }

        console.log(this.isMinHeap(0));
    }

    isMinHeap(i: number) {
        if(i > this.heapSize) return true;

        let [left, right] = this.getChildren(i);

        let val = this.heap[i]

        if(left < this.heapSize && !this.less(val, this.heap[left])) {
            return false;
        }

        if(right < this.heapSize && !this.less(val, this.heap[right])) {
            return false;
        }

        return this.isMinHeap(left) && this.isMinHeap(right);
    }

    poll() {

    }

    peek() {

    }

    removeAt(i: number) {
        if(this.isEmpty()) return null;

    }

    insert(value: number) {
        if(value === null) {
            throw new Error('value must not be null');
        }

        if(this.heapSize < this.heapCapacity) {
            this.heap[this.heapSize] = value;
        } else {
            this.heap.push(value);
            this.heapCapacity += 1;
        }

        this.swim(this.heapSize);
        this.heapSize += 1;
    }

    less(val1: number, val2: number): boolean {
        return this.heap[val1] < this.heap[val2];
    }

    isEmpty() {
        return false;
    }

    clear() {

    }

    getParent(i: number): Number {
        return (i / 2 | 0);
    }

    getChildren(i: number): [number, number] {
        return [2 * i + 1, 2 * i + 2];
    }

    swim(i: number) {
        let parent = (i - 1) / 2 | 0;
        while(i > 0 && this.less(i, parent)) {
            this.swap(this.heap, parent, i);
            i = parent;
            parent = (i - 1) / 2 | 0;
        }
    }

    sink(i: number) {
        while(true) {
            let [left, right] = this.getChildren(i);
            let smallest = left;
            if(right < this.heapSize && this.less(right, left)) {
                smallest = right;
            }
            if(left >= this.heapSize && this.less(i, smallest)) break;
            this.swap(this.heap, smallest, i);
            console.log('hahaha')
            i = smallest;
        }
    }

    swap(arr: Array<number>, from: number, to:number): void {
        if(from > this.heapSize || to > this.heapSize) return;
        let temp = arr[from]
        arr[from] = arr[to];
        arr[to] = temp;
    }
}

const pq = new PriorityQueue([1, 9, 0, 4, 6, -1, 2000])