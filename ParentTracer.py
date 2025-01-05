class ParentTracer:
    def __init__(self):
        self.parents = {}

    def set_parent(self, child, parent):
        self.parents[child] = parent

    def get_trace(self, target):
        trace = []
        current = target
        while current in self.parents:
            trace.append(current)
            current = self.parents[current]
        trace.append(current)  # Ajouter la racine
        trace.reverse()
        return trace