from RootedRelation import RootedRelation  # Importation de la classe de base RootedRelation

# Classe représentant un graphe des nombres binaires à n bits
class NBits(RootedRelation):
    """
    Modélise un espace d'états où chaque état est un entier représenté sur n bits.
    Les états voisins sont obtenus en inversant un bit (passage de 0 à 1 ou de 1 à 0).
    """

    def __init__(self, roots: list, n: int):
        """
        Initialise le graphe binaire.
        :param roots: Liste des états initiaux (racines du graphe).
        :param n: Nombre de bits utilisé pour représenter les états.
        """
        self.initial = roots  # États initiaux du graphe
        self.nBits = n  # Nombre de bits par état

    def roots(self):
        """
        Retourne les états racines du graphe.
        :return: Liste des états initiaux.
        """
        return self.initial

    def next(self, source):
        """
        Calcule les états voisins d'un état donné.
        Un état voisin est obtenu en inversant un seul bit de l'état courant.
        :param source: État source (entier).
        :return: Liste des voisins (états accessibles en inversant un bit).
        """
        neighbours = []
        for i in range(self.nBits):  # Parcourt chaque bit
            neighbours.append(source ^ (1 << i))  # Inverse le i-ème bit en utilisant XOR
        return neighbours


# Fonction pour afficher un ensemble d'états en représentation binaire
def binary_print(s):
    """
    Convertit un ensemble d'entiers en chaînes binaires de longueur fixe.
    :param s: Ensemble des états (entiers).
    :return: Ensemble des états sous forme binaire (chaînes de longueur 3).
    """
    return set(map(
        lambda x: "{0:03b}".format(x),  # Formate chaque entier en chaîne binaire sur 3 bits
        s))
