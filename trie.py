import heapq

class Trie:
    class TrieNode:
        def __init__(self, char):
            self.char = char
            self.children = []
            self.word_finished = False

            # how many words finish here
            self.count = 1


    def __init__(self):
        self.root = self.TrieNode('*')
    
    def add(self, word):
        node = self.root
        for char in word:
            found = False
            for child in node.children:
                if child.char == char:
                    node = child
                    node.count += 1
                    found = True
                    break;
            
            if not found:
                new_node = self.TrieNode(char)
                node.children.append(new_node)
                node = new_node

        node.word_finished = True


    def find_prefix(self, prefix: str) -> int:
        node = self.root

        for char in prefix:
            found = False

            for child in node.children:
                if child.char == char:
                    found = True
                    node = child
                    break
            
            if not found:
                return 0

        return node.count, node

    def find_all_suffix(self, prefix: str) -> [str]:
        count, node = self.find_prefix(prefix[:])
        heap = []
        stack = []
        stack.append((node, ''))
        while len(stack) != 0:
            current_node, curr_str = stack.pop()

            for child in current_node.children:
                stack.append((child, curr_str + child.char))

            if not current_node.children or current_node.word_finished:
                heap.append((-current_node.count, curr_str))
            
        heapq.heapify(heap)
        results = []
        for i in range(len(heap)):
            results.append(heapq.heappop(heap)[1])
        return results


    
trie = Trie()
trie.add('appl')
trie.add('apple')
trie.add('apply')
trie.add('application')
trie.add('application')
trie.add('application')
trie.add('appcelerator')
trie.add('appcelerator')
trie.add('mango')

print(trie.find_all_suffix('app'))


                    

