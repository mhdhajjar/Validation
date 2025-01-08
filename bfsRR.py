from HanoiRR import HanoiRR
from ParentTracer import ParentTracer
from collections import deque

n = 3
opaque = {"target": ((), tuple(range(n, 0, -1)), ())}

# L'initialisation de `roots` est maintenant gérée par la classe `HanoiRR`
hanoi_rr = HanoiRR(n)
parent_tracer = ParentTracer()

def pred(state, opaque):
    return state == opaque.get("target")

# Modifier bfsTraversal pour utiliser actions et execute
def bfsTraversalWithHanoiRR(graph, pred, opaque, parent_tracer):
    i = True
    k = set()
    F = deque()

    while len(F) > 0 or i:
        if i:
            N = [graph.roots]  # Utilisation des racines générées par HanoiRR
            i = False
            current = None
        else:
            current = F.popleft()
            possible_actions = graph.actions(current)  # Utilise actions pour calculer les transitions possibles
            N = [graph.execute(current, action) for action in possible_actions]  # Exécute les actions pour obtenir les nouveaux états

        for n in N:
            if n not in k:
                k.add(n)
                F.append(n)
                if current is not None:
                    parent_tracer.set_parent(n, current)
                terminates = pred(n, opaque)
                if terminates:
                    trace = parent_tracer.get_trace(n)
                    return trace

    return [], opaque, k, F

result = bfsTraversalWithHanoiRR(hanoi_rr, pred, opaque, parent_tracer)
print("HanoiRR Graph Result:", result)
