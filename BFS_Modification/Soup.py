from RootedRelation import *  # Importation des relations de base
import copy  # Importation de la bibliothèque pour effectuer des copies profondes d'objets

# Définition d'une règle avec un nom, une garde (condition) et une action
class Rule:
    def _init_(self, name, guard, action):
        self.name = name  # Nom de la règle
        self.guard = guard  # Fonction de garde (condition pour appliquer l'action)
        self.action = action  # Fonction représentant l'action à exécuter

    # Méthode pour exécuter l'action de la règle sur une configuration donnée
    def execute(self, config):
        return [self.action(config)]  # Applique l'action sur la configuration

# Classe représentant un programme basé sur des règles, avec une configuration initiale
class SoupProgram:
    def _init_(self, ini):
        self.ini = ini  # Configuration initiale du programme
        self.pieces = []  # Liste des règles associées au programme

    # Méthode pour ajouter une règle au programme
    def add(self, rule):
        self.pieces.append(rule)

# Classe pour définir la sémantique d'un programme de type "Soup"
class SoupSemantics(SemanticRootedRelation):
    def _init_(self, program):
        self.program = program  # Programme dont on veut définir la sémantique

    # Méthode pour récupérer les configurations initiales
    def initialConfigurations(self):
        return [self.program.ini]

    # Méthode pour identifier les actions activées (valides) dans une configuration source
    def enabledActions(self, source):
        # Retourne une liste des actions pour lesquelles la garde est satisfaite
        return list(map(lambda r: r.action,
                        filter(lambda r: r.guard(source),
                               self.program.pieces)))

    # Méthode pour exécuter une action sur une configuration source
    def execute(self, source, action):
        target = copy.deepcopy(source)  # Crée une copie de la configuration source
        r = action(target)  # Exécute l'action sur la copie
        return target  # Retourne la nouvelle configuration

# Classe pour définir la sémantique d'un programme avec entrée (InputSoup)
class InputSoupSemantics(InputSemanticRootedRelation):
    def _init_(self, program):
        self.program = program  # Programme dont on veut définir la sémantique

    # Méthode pour récupérer la configuration initiale
    def initial(self):
        return [self.program.init]

    # Méthode pour identifier les actions activées en fonction d'une entrée et d'une configuration source
    def enabledActions(self, input, source):
        # Filtre les règles dont la garde est satisfaite par l'entrée et la configuration source
        return filter(lambda r: r.guard(input, source), self.program.pieces)

    # Méthode pour exécuter une action avec une entrée sur une configuration source
    def execute(self, action, input, source):
        target = copy.deepcopy(source)  # Crée une copie de la configuration source
        n = action(input, target)  # Exécute l'action en utilisant l'entrée et la copie
        return [target]  # Retourne la nouvelle configuration