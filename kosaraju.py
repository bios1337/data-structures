from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, fro, to):
        self.graph[fro].append(to)

    def printGraph(self):
        print(self.graph)

    def getStrongComponents(self):
        visited = set()
        stack = []
        main_stack = []
        for node in self.graph.keys():
            print(node)
            if node not in visited:
                visited.add(node)
                stack.append(node)
            
            while len(stack) != 0:
                top = stack.pop()
                visited.add(top)
                main_stack.append(top)
                for next in self.graph[top]:
                    if next not in visited:
                        stack.append(next)

        print(main_stack)
        reverse_graph = defaultdict(list)
        for key in self.graph.keys():
            for next in self.graph[key]:
                reverse_graph[next].append(key)

        results = []
        visited = set()
        stack = []
        while len(main_stack) != 0:
            top = main_stack.pop()
            if top in visited:
                continue
            visited.add(top)

            # perform a DFS now
            stack = [top]
            subgraph = [top]
            while len(stack) != 0:
                elem = stack.pop()
                visited.add(elem)
                for next in reverse_graph[elem]:
                    if next not in visited:
                        stack.append(next)
                        subgraph.append(next)
            results.append(tuple(subgraph))
        return results

graph = Graph()

graph.addEdge(1, 1)
graph.addEdge(4, 4)
graph.addEdge(3, 3)
graph.addEdge(5, 5)
graph.addEdge(2, 8)
graph.addEdge(8, 8)
graph.printGraph()

sccs = graph.getStrongComponents()
print('sccs', sccs, len(sccs))
