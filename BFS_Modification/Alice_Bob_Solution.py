from RootedRelation import *
from Soup import *
from BFS import *

# Classe représentant la configuration des états d'Alice et Bob
class AliceBobConf:
    """
    Modèle pour représenter les états des deux entités, Alice et Bob, dans un système avec exclusion mutuelle.
    Attributs :
    - PC_alice : État d'Alice (0 : Initial, 1 : Attente, 2 : Section critique).
    - PC_bob : État de Bob (0 : Initial, 1 : Attente, 2 : Section critique).
    - Flag_alice : Intention explicite d'Alice d'accéder à la section critique.
    - Flag_bob : Intention explicite de Bob d'accéder à la section critique.
    """

    def __init__(self):
        """
        Initialisation des états et drapeaux des deux entités à 0 (aucune action en cours).
        """
        self.PC_alice = 0  # État initial d'Alice
        self.PC_bob = 0  # État initial de Bob
        self.Flag_alice = 0  # Intention d'Alice (non active)
        self.Flag_bob = 0  # Intention de Bob (non active)

    def __hash__(self):
        """
        Génère un hachage basé sur les états et les drapeaux d'Alice et Bob.
        Permet d'utiliser cette configuration dans des ensembles ou comme clé de dictionnaire.
        """
        return hash(self.PC_alice + self.PC_bob) + hash(self.Flag_alice + self.Flag_bob)

    def __eq__(self, other):
        """
        Vérifie l'égalité entre deux configurations.
        Deux configurations sont égales si leurs états et drapeaux respectifs sont identiques.
        """
        if other is None:
            return False
        return (
            self.PC_alice == other.PC_alice and
            self.PC_bob == other.PC_bob and
            self.Flag_alice == other.Flag_alice and
            self.Flag_bob == other.Flag_bob
        )

    def _repr_(self):
        """
        Retourne une représentation lisible de la configuration pour le débogage.
        Affiche les états d'Alice et Bob.
        """
        return str(self.PC_alice) + str(self.PC_bob)

# Fonctions de transition pour Alice
def I_W_Alice(c):
    """
    Transition d'Alice de l'état Initial (0) à l'état Attente (1) avec intention déclarée.
    """
    c.PC_alice = 1
    c.Flag_alice = 1  # Déclare son intention d'accéder à la section critique

def W_SC_Alice(c):
    """
    Transition d'Alice de l'état Attente (1) à la Section critique (2).
    """
    c.PC_alice = 2
    c.Flag_alice = 1  # Maintient son intention

def SC_I_Alice(c):
    """
    Transition d'Alice de la Section critique (2) à l'état Initial (0).
    """
    c.PC_alice = 0
    c.Flag_alice = 0  # Retire son intention

# Fonctions de transition pour Bob
def I_W_Bob(c):
    """
    Transition de Bob de l'état Initial (0) à l'état Attente (1) avec intention déclarée.
    """
    c.PC_bob = 1
    c.Flag_bob = 1  # Déclare son intention d'accéder à la section critique

def W_SC_Bob(c):
    """
    Transition de Bob de l'état Attente (1) à la Section critique (2).
    """
    c.PC_bob = 2
    c.Flag_bob = 1  # Maintient son intention

def SC_I_Bob(c):
    """
    Transition de Bob de la Section critique (2) à l'état Initial (0).
    """
    c.PC_bob = 0
    c.Flag_bob = 0  # Retire son intention

# Fonctions pour vérifier si Alice ou Bob sont dans la section critique
def AliceIsInCS(c):
    """
    Vérifie si Alice est dans la section critique (état 2).
    """
    return c.PC_alice == 2

def BobIsInSC(c):
    """
    Vérifie si Bob est dans la section critique (état 2).
    """
    return c.PC_bob == 2

# Programme principal pour gérer les transitions d'états
def AliceAndBob():
    """
    Programme basé sur des règles pour gérer les transitions d'états d'Alice et Bob.
    Implémente un mécanisme d'exclusion mutuelle où une seule entité peut accéder
    à la section critique à un moment donné.
    """
    soup = SoupProgram(AliceBobConf())  # Initialise le programme avec la configuration initiale

    # Règle 1 : Alice passe de l'état Initial (0) à l'état Attente (1)
    soup.add(Rule(
        "Alice : Initial state to critical section",
        lambda c: c.PC_alice == 0,  # Condition : Alice est dans l'état Initial
        I_W_Alice  # Action : Transition vers l'état Attente
    ))

    # Règle 2 : Alice passe de l'état Attente (1) à la Section critique (2)
    soup.add(Rule(
        "Alice : Waiting state to critical section",
        lambda c: c.PC_bob != 2 and c.PC_alice == 1,  # Condition : Bob n'est pas dans la section critique
        W_SC_Alice  # Action : Transition vers la Section critique
    ))

    # Règle 3 : Alice retourne de la Section critique (2) à l'état Initial (0)
    soup.add(Rule(
        "Alice : Critical section to Initial state",
        lambda c: c.PC_alice == 2,  # Condition : Alice est dans la Section critique
        SC_I_Alice  # Action : Retour à l'état Initial
    ))

    # Règle 4 : Bob passe de l'état Initial (0) à l'état Attente (1)
    soup.add(Rule(
        "Bob : Initial state to Waiting state",
        lambda c: c.PC_bob == 0,  # Condition : Bob est dans l'état Initial
        I_W_Bob  # Action : Transition vers l'état Attente
    ))

    # Règle 5 : Bob passe de l'état Attente (1) à la Section critique (2)
    soup.add(Rule(
        "Bob : Waiting state to critical section",
        lambda c: c.PC_bob == 1 and c.PC_alice != 2,  # Condition : Alice n'est pas dans la section critique
        W_SC_Bob  # Action : Transition vers la Section critique
    ))

    # Règle 6 : Bob retourne de la Section critique (2) à l'état Initial (0)
    soup.add(Rule(
        "Bob : Critical section to Initial state",
        lambda c: c.PC_bob == 2,  # Condition : Bob est dans la Section critique
        SC_I_Bob  # Action : Retour à l'état Initial
    ))

    return soup