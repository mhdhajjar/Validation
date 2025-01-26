import inspect
from collections import deque
from RootedRelation import *


# Implémentation de l'algorithme BFS (Breadth-First Search)
# Les paramètres `on_entry`, `on_known` et `on_exit` permettent de personnaliser
# les actions effectuées lors de l'entrée dans un nœud, la visite d'un nœud connu,
# ou la sortie d'un nœud.
def bfs(graph, accumulation, on_entry=lambda source, noeud, accumulation: False, 
        on_known=lambda source, noeud, accumulation: False, 
        on_exit=lambda source, accumulation: False):
    k = set()
    F = deque()
    debut = True
    while F or debut:
        source = None
        if debut:
            N = graph.roots()  # Récupérer les racines du graphe
            debut = False
        else:
            source = F.popleft()  # Extraire un nœud de la file d'attente
            N = graph.next(source)
        for noeud in N:
            if noeud in k:
                if on_known(source, noeud, accumulation):
                    return accumulation, k
                continue
            k.add(noeud)
            F.append(noeud)
            if on_entry(source, noeud, accumulation):
                return accumulation, k
        if on_exit(source, accumulation):
            return accumulation, k
    return accumulation, k


# Parcours BFS simple pour vérifier si un état "acceptant" est atteignable
def bfs_traversal(graph):
    k = []
    F = deque()
    i = True
    while len(F) != 0 or i:
        if i:
            N = graph.roots()
            i = False
        else:
            noeud = F.popleft()
            N = graph.next(noeud)
        for voisin in N:
            if voisin not in k:
                if graph.isAccepting(voisin):  # Vérifier si l'état est "acceptant"
                    return True
                F.append(voisin)
                k.append(voisin)
    return False


# Fonction pour trouver un prédicat spécifique dans un graphe
def predicate_finder(
        graph,
        predicate=lambda noeud: False):
    def verifier_predicat(source, noeud, accumulation):
        accumulation[2] += 1
        accumulation[1] = predicate(noeud)
        if accumulation[1]:
            accumulation[3] = noeud
        return accumulation[1]

    return bfs(graph, [predicate, False, 0, None], on_entry=verifier_predicat)


# Vérifie un prédicat donné en construisant une relation de transition
def check_pred(semantic, predicate):
    transition = RR2RG(semantic)
    transition = IsAcceptingInstance(transition, predicate)
    predicate_mc(transition, predicate)
    return bfs_traversal(transition)


# Génère une trace d'exécution en utilisant les relations parent-enfant
def get_trace(parents, noeud, racines):
    trace = [noeud]
    try:
        parent = parents[noeud]
    except KeyError:
        parent = None
    if isinstance(parent, list):
        parent = parent[0] if len(parent) > 0 else None
    while parent is not None:
        trace.append(parent)
        if parent in racines:
            return trace
        try:
            parent = parents[parent]
            if isinstance(parent, list):
                parent = parent[0] if len(parent) > 0 else None
        except KeyError:
            parent = None
    return trace


# Vérifie les modèles pour un prédicat donné et affiche les résultats
def predicate_mc(transition_relation, predicate):
    print(f'{"-" * 50}\nVérification du modèle pour le prédicat :\n{inspect.getsource(predicate)}')

    traceur_parents = ParentTracer(transition_relation)

    [predicat, trouvé, compteur, cible], k = predicate_finder(traceur_parents, predicate)
    print(f'Un état acceptant est atteignable : {trouvé} après avoir exploré', compteur, 'configurations')

    la_trace = []
    if trouvé is True:
        la_trace = get_trace(traceur_parents.dict, cible, traceur_parents.roots())
        trace_string = f'\n{"-" * 20}\n'.join(str(x) for x in la_trace)
        print(f'La trace est : \n{trace_string}')
