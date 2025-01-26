from abc import ABC, abstractmethod

# Classe abstraite représentant une relation enracinée. 
# Toute classe dérivée doit implémenter les méthodes `roots` et `next`.
class RootedRelation(ABC):
    @abstractmethod
    def roots(self):
        pass  # Doit retourner les éléments racines de la relation.

    @abstractmethod
    def next(self, source):
        pass  # Doit retourner les éléments suivants de la relation à partir d'une source donnée.

# Classe permettant d'étendre les fonctionnalités d'une autre classe en déléguant l'accès
# aux attributs à un objet existant (appelé operand).
class IdentifyInstance(object):
    def __init__(self, operand):
        self.operand = operand  # L'objet dont les fonctionnalités sont étendues.

    def __getattr__(self, attr):
        return getattr(self.operand, attr)  # Délègue l'accès aux attributs à l'objet `operand`.

# Classe représentant des actions possibles, mais actuellement non définie.
class PossibleActions:
    def is_accepting(c):
        pass  # Méthode non implémentée, à définir selon le besoin.

# Classe qui trace les parents des nœuds dans une relation enracinée.
class ParentTracer(IdentifyInstance):
    def __init__(self, operand, dict=None):
        super().__init__(operand)
        if dict == None:
            dict = {}  # Initialisation d'un dictionnaire pour tracer les parents.
        self.dict = dict

    def roots(self):
        # Récupère les voisins racines et les ajoute au dictionnaire s'ils ne sont pas encore tracés.
        neighbours = self.operand.roots()
        for n in neighbours:
            if n not in self.dict:
                self.dict[n] = None
        return neighbours

    def next(self, source):
        # Récupère les voisins suivants et met à jour le dictionnaire avec leurs parents.
        neighbours = self.operand.next(source)
        for n in neighbours:
            if n not in self.dict:
                self.dict[n] = [source]
        return neighbours

    # Méthode statique pour reconstruire le chemin de traçage depuis une cible.
    def get_trace(dic, target):
        result = []
        current = target
        while current in dic:
            result.append(current)
            current = dic[current]
        return result[::-1]  # Retourne le chemin dans l'ordre.

# Classe qui enrichit une instance avec une méthode `isAccepting` basée sur un prédicat donné.
class IsAcceptingInstance(IdentifyInstance):
    def __init__(self, operand, predicate):
        super().__init__(operand)
        self.predicate = predicate  # Le prédicat à évaluer.

    def isAccepting(self, c):
        return self.predicate(c)  # Retourne le résultat du prédicat appliqué à `c`.

# Classe représentant une relation enracinée sémantique. 
# Elle doit être complétée pour définir ses méthodes spécifiques.
class SemanticRootedRelation:
    def initialConfigurations(self):
        pass  # Doit retourner les configurations initiales.

    def enablesdActions(self, source):
        pass  # Doit retourner les actions activées à partir de la source.

    def execute(self, action, source):
        pass  # Doit exécuter une action donnée à partir de la source.

# Classe représentant une relation enracinée sémantique basée sur des entrées.
# Les méthodes doivent être implémentées pour gérer des configurations dépendantes de l'entrée.
class InputSemanticRootedRelation:
    def initial(self):
        pass  # Doit retourner l'état initial.

    def enablesdActions(self, input, source):
        pass  # Doit retourner les actions activées en fonction de l'entrée et de la source.

    def execute(self, action, input, source):
        pass  # Doit exécuter une action donnée en fonction de l'entrée et de la source.

class RR2RG(RootedRelation):
    def __init__(self, astr):
        self.astr = astr

    def roots(self):
        return self.astr.initialConfigurations()

    def next(self, s):
        targets = []
        for a in self.astr.enabledActions(s):
            target = self.astr.execute(s, a)
            targets.append(target)
        return targets