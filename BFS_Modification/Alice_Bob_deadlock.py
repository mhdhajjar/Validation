from RootedRelation import *
from Soup import *
from BFS import *

# Classe représentant la configuration des états d'Alice et Bob
class AliceBobConf:
    """
    Modèle pour représenter les états d'Alice et Bob dans un système simple :
    - PC_alice : État d'Alice (0 : Initial, 1 : Section critique).
    - PC_bob : État de Bob (0 : Initial, 1 : Section critique).
    """

    def _init_(self):
        self.PC_alice = 0  # État initial d'Alice (Initial)
        self.PC_bob = 0  # État initial de Bob (Initial)

    def _hash_(self):
        """
        Fonction de hachage pour permettre l'utilisation des configurations dans des ensembles ou des dictionnaires.
        Le hachage est basé sur la somme des états d'Alice et Bob.
        """
        return hash(self.PC_alice + self.PC_bob)

    def _eq_(self, other):
        """
        Vérifie l'égalité entre deux configurations.
        Deux configurations sont égales si les états d'Alice et Bob sont identiques.
        """
        return self.PC_alice == other.PC_alice & self.PC_bob == other.PC_bob

    def _repr_(self):
        """
        Représentation lisible de la configuration pour le débogage.
        Retourne une chaîne montrant les états d'Alice et Bob.
        """
        return str(self.PC_alice) + str(self.PC_bob)

# Fonctions de transition pour Alice
def I_CS_Alice(c):
    """
    Transition d'Alice de l'état Initial (0) à la Section critique (1).
    """
    c.PC_alice = 1

def SC_I_Alice(c):
    """
    Transition d'Alice de la Section critique (1) à l'état Initial (0).
    """
    c.PC_alice = 0

# Fonctions de transition pour Bob
def I_SC_Bob(c):
    """
    Transition de Bob de l'état Initial (0) à la Section critique (1).
    """
    c.PC_bob = 1

def SC_I_Bob(c):
    """
    Transition de Bob de la Section critique (1) à l'état Initial (0).
    """
    c.PC_bob = 0

# Fonction principale pour créer un programme basé sur les règles
def StateCounter():
    """
    Programme basé sur des règles pour modéliser l'accès d'Alice et Bob à une section critique :
    - Alice et Bob commencent tous deux à l'état Initial (0).
    - Ils peuvent accéder à la section critique s'ils ne se gênent pas mutuellement.
    """
    soup = SoupProgram(AliceBobConf())  # Initialise le programme avec une configuration de départ

    # Règle 1 : Alice passe de l'état Initial à la Section critique
    soup.add(Rule(
        "Alice : Initial to critical section",
        lambda c: c.PC_alice == 0,  # Condition : Alice est dans l'état Initial
        I_CS_Alice  # Action : Transition vers la Section critique
    ))

    # Règle 2 : Alice passe de la Section critique à l'état Initial
    soup.add(Rule(
        "Alice : Critical section to Initial state",
        lambda c: c.PC_alice == 1,  # Condition : Alice est dans la Section critique
        SC_I_Alice  # Action : Retour à l'état Initial
    ))

    # Règle 3 : Alice peut accéder à la Section critique si Bob n'y est pas
    soup.add(Rule(
        "Alice : Initial state to critical section",
        lambda c: c.PC_bob == 0,  # Condition : Bob est dans l'état Initial
        I_CS_Alice  # Action : Alice passe à la Section critique
    ))

    # Règle 4 : Bob passe de la Section critique à l'état Initial
    soup.add(Rule(
        "Bob: Critical section to Initial state",
        lambda c: c.PC_bob == 1,  # Condition : Bob est dans la Section critique
        SC_I_Bob  # Action : Retour à l'état Initial
    ))

    return soup