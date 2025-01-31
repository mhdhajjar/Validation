import pandas as pd
import copy
import sys
from RootedRelation import *
from hanoi import *
from Soup import *
from BFS import *
from Alice_Bob_livelock import *  # Suppression du deadlock
from Alice_Bob_Solution import *
from Nbits import *

# Initialisation de la liste des résultats
results = []

# ======== Fonction pour tester tous les cas de Hanoi ========
def test_Hanoi():
    for num_disques in range(1, 5):  # Teste de 1 à 4 disques
        for num_piles in range(3, 5):  # Teste avec 3 ou 4 piles
            soup = Hanoi_Instance(num_piles, num_disques)
            comportement_soup = SoupSemantics(soup)
            etat_initial = comportement_soup.initialConfigurations()[0]
            actions_possibles = comportement_soup.enabledActions(etat_initial)
            
            result = {
                "Type": "Hanoi",
                "Num Disques": num_disques,
                "Num Piles": num_piles,
                "État Initial": str(etat_initial),
                "Actions Possibles": len(actions_possibles)
            }
            results.append(result)

# ======== Fonction pour tester Alice et Bob (V2, V3) ========
def test_AliceBob():
    for version in [2, 3]:  # On exclut Alice & Bob V1 (Deadlock)
        if version == 2:
            semantic = SoupSemantics(StateCounter())
            graphe = RR2RG(semantic)
            graphe = IsAcceptingInstance(graphe, lambda c: c.PC_alice == 0)
            res1 = check_pred(semantic, lambda c: c.PC_alice == 0 and c.PC_bob == 1)
            res2 = len(graphe.roots())
        else:
            semantic = SoupSemantics(AliceAndBob())
            res1 = check_pred(semantic, lambda c: c.PC_alice == 2 and c.PC_bob == 2)
            res2 = check_pred(semantic, lambda c: len(semantic.enabledActions(c)) == 0)

        result = {
            "Type": f"AliceBob_V{version}",
            "Condition 1": res1,
            "Condition 2": res2
        }
        results.append(result)

# ======== Fonction pour tester NBits ========
def test_NBits():
    for x in [16, 5, 1, 7, 10]:  # Plusieurs valeurs testées
        resultat, connu = predicate_finder(NBits([0], 3), lambda n: n == x)
        result = {
            "Type": "NBits",
            "Valeur": x,
            "Atteignable": resultat[2],
            "Nœuds Explorés": resultat[3],
            "Connu": binary_print(connu)
        }
        results.append(result)

# ======== Exécution des tests et sauvegarde des résultats ========
def save_results():
    test_Hanoi()
    test_AliceBob()
    test_NBits()

    # Convert results to DataFrame
    df = pd.DataFrame(results)

    # Separate the DataFrame into different test types
    df_hanoi = df[df["Type"] == "Hanoi"].drop(columns=["Condition 1", "Condition 2", "Valeur", "Atteignable", "Nœuds Explorés", "Connu"], errors="ignore")
    df_alicebob = df[df["Type"].str.contains("AliceBob")].drop(columns=["Num Disques", "Num Piles", "État Initial", "Actions Possibles", "Valeur", "Atteignable", "Nœuds Explorés", "Connu"], errors="ignore")
    df_nbits = df[df["Type"] == "NBits"].drop(columns=["Num Disques", "Num Piles", "État Initial", "Actions Possibles", "Condition 1", "Condition 2"], errors="ignore")

    # Save each type separately
    df_hanoi.to_csv("resultats_hanoi.csv", index=False, sep=";", encoding="utf-8")
    df_alicebob.to_csv("resultats_alicebob.csv", index=False, sep=";", encoding="utf-8")
    df_nbits.to_csv("resultats_nbits.csv", index=False, sep=";", encoding="utf-8")

    print("\nRésultats sauvegardés dans plusieurs fichiers CSV avec succès!")


# ======== Lancement du programme ========
if __name__ == "__main__":
    save_results()