from collections import deque

def bfsTraversal(graph, pred, opaque):
    i = True 
    k = set([])  # Use set([]) for compatibility with Python 2
    F = deque()  

    while len(F) > 0 or i:
        if i:
            N = graph.roots
            i = False
        else:
            current = F.popleft()
            N = graph.neighbours(current)

        for n in N:
            if n not in k:
                k.add(n)
                F.append(n)
                terminates = pred(n, opaque)
                if terminates:
                    return opaque, k, F

    return opaque, k, F


class SimpleGraph:
    def __init__(self, graph_dict, roots):  # Corrected constructor
        self.graph_dict = graph_dict  # Dictionary representing the graph
        self.roots = roots  # List of root nodes

    def neighbours(self, S):
        return self.graph_dict.get(S, [])


class NBits:
    def __init__(self, roots, N):  # Corrected constructor
        self.roots = roots  # List of roots
        self.N = N          # Size of the graph

    def neighbours(self, S):
        # Returns the neighbors of node S based on bit representation
        neighbours = []
        for i in range(self.N):  # Use xrange for Python 2
            if S & (1 << i):  # If the ith bit is set, then i is a neighbor of S
                neighbours.append(i)
        return neighbours


def pred(n, opaque):
    target = opaque.get("target")
    if n == target:
        return True  # Terminate as soon as we find the target
    return False


# Example with a graph represented by a dictionary
graph_dict = {
    1: [3, 2],
    2: [1, 3, 4],
    3: [3],
    4: []
}
roots = [1]
opaque = {"target": 2}
graph_dict_example = SimpleGraph(graph_dict, roots)
result = bfsTraversal(graph_dict_example, pred, opaque)
print(result)  # Use print statement (no parentheses)

# Example with a graph represented by bits
N = 5  # For example, a graph with 5 nodes
roots = [0]  # Start from node 0
opaque = {"target": 3}
graph_bits_example = NBits(roots, N)
result = bfsTraversal(graph_bits_example, pred, opaque)
print(result) # Use print statement (no parentheses)
