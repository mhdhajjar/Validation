from RootedRelation import *
from Soup import *
from BFS import *

# Classe représentant la configuration des états d'Alice et Bob
class AliceBobConf:
    """
    Modèle pour représenter les états d'Alice et Bob dans un système avec exclusion mutuelle.
    - PC_alice : État d'Alice (0 : Initial, 1 : Attente, 2 : Section critique).
    - PC_bob : État de Bob (0 : Initial, 1 : Attente, 2 : Section critique).
    """

    def __init__(self):
        """
        Initialisation des états d'Alice et Bob à 0 (Initial).
        """
        self.PC_alice = 0  # État initial d'Alice
        self.PC_bob = 0  # État initial de Bob

    def __hash__(self):
        """
        Fonction de hachage pour permettre l'utilisation des configurations dans des ensembles ou des dictionnaires.
        Le hachage est basé sur la somme des états d'Alice et Bob.
        """
        return hash(self.PC_alice + self.PC_bob)

    def __eq__(self, other):
        """
        Vérifie l'égalité entre deux configurations.
        Deux configurations sont égales si les états d'Alice et Bob sont identiques.
        """
        return self.PC_alice == other.PC_alice & self.PC_bob == other.PC_bob

    def __repr__(self):
        """
        Représentation lisible de la configuration pour le débogage.
        Retourne une chaîne indiquant les états d'Alice et Bob.
        """
        return str(self.PC_alice) + str(self.PC_bob)

# Fonctions de transition pour Alice
def I_W_Alice(c):
    """
    Transition d'Alice de l'état Initial (0) à l'état Attente (1).
    """
    c.PC_alice = 1

def W_SC_Alice(c):
    """
    Transition d'Alice de l'état Attente (1) à la Section critique (2).
    """
    return 1  # Action réussie (rien à modifier directement dans cette fonction).

def SC_I_Alice(c):
    """
    Transition d'Alice de la Section critique (2) à l'état Initial (0).
    """
    c.PC_alice = 0

# Fonctions de transition pour Bob
def I_W_Bob(c):
    """
    Transition de Bob de l'état Initial (0) à l'état Attente (1).
    """
    c.PC_bob = 1

def W_SC_Bob(c):
    """
    Transition de Bob de l'état Attente (1) à la Section critique (2).
    """
    return 1  # Action réussie (rien à modifier directement dans cette fonction).

def SC_I_Bob(c):
    """
    Transition de Bob de la Section critique (2) à l'état Initial (0).
    """
    c.PC_bob = 0

# Fonction principale pour modéliser les transitions d'états
def StateCounter():
    """
    Programme basé sur des règles pour gérer l'accès d'Alice et Bob à une section critique :
    - Alice et Bob passent par les états : Initial (0), Attente (1), Section critique (2).
    - Une exclusion mutuelle est garantie : seule une entité peut être dans la section critique à un moment donné.
    """
    soup = SoupProgram(AliceBobConf())  # Initialise le programme avec la configuration de départ

    # Règle 1 : Alice passe de l'état Initial (0) à l'état Attente (1)
    soup.add(Rule(
        "Alice : Initial to critical section",
        lambda c: c.PC_alice == 0,  # Condition : Alice est dans l'état Initial
        I_W_Alice  # Action : Transition vers l'état Attente
    ))

    # Règle 2 : Alice passe de l'état Attente (1) à la Section critique (2)
    soup.add(Rule(
        "Alice : Waiting to critical section",
        lambda c: c.PC_bob == 0 and c.PC_alice == 1,  # Condition : Bob n'est pas dans la section critique et Alice est en attente
        W_SC_Alice  # Action : Transition vers la Section critique
    ))

    # Règle 3 : Alice retourne de la Section critique (2) à l'état Initial (0)
    soup.add(Rule(
        "Alice : Critical section to initial state",
        lambda c: c.PC_alice == 1,  # Condition : Alice est dans la Section critique
        SC_I_Alice  # Action : Retour à l'état Initial
    ))

    # Règle 4 : Bob passe de l'état Initial (0) à l'état Attente (1)
    soup.add(Rule(
        "Bob : Initial to waiting state",
        lambda c: c.PC_bob == 0,  # Condition : Bob est dans l'état Initial
        I_W_Bob  # Action : Transition vers l'état Attente
    ))

    # Règle 5 : Bob passe de l'état Attente (1) à la Section critique (2)
    soup.add(Rule(
        "Bob : Waiting to critical section",
        lambda c: c.PC_alice == 0 and c.PC_bob == 1,  # Condition : Alice n'est pas dans la section critique et Bob est en attente
        W_SC_Bob  # Action : Transition vers la Section critique
    ))

    # Règle 6 : Bob retourne de la Section critique (2) à l'état Initial (0)
    soup.add(Rule(
        "Bob : Critical section to Initial",
        lambda c: c.PC_bob == 1,  # Condition : Bob est dans la Section critique
        SC_I_Bob  # Action : Retour à l'état Initial
    ))

    return soup
