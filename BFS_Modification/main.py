from RootedRelation import *
from hanoi import *
from Soup import *
from BFS import *
from Alice_Bob_deadlock import *
from Alice_Bob_livelock import *
from Alice_Bob_Solution import *
from Nbits import *

# Fonction principale pour les tours de Hanoi
def Hanoi_Main():
    # Initialisation du nombre de disques et de piles
    num_disques = 3
    num_piles = 3
    
    # Exemple sans "Soup"
    hanoi_tower = IdentifyInstance(Hanoi(num_disques, num_piles))
    etat_initial = hanoi_tower.initial()[0]
    print("\n==== Tours de Hanoi (Sans Soup) ====")
    for i, j in [(0, 2), (0, 1), (2, 1), (0, 2), (1, 0), (1, 2), (0, 2)]:
        condition = guard(i, j)
        action = action_def(i, j)
        valide = condition(etat_initial)
        if valide:
            action(etat_initial)
        print(f'{i} -> {j} : {"Valide" if valide else "Invalide"} | Etat: {etat_initial}')

    # Exemple avec "Soup"
    print("\n==== Tours de Hanoi (Avec Soup) ====")
    soup = Hanoi_Instance(num_disques, num_piles)
    comportement_soup = SoupSemantics(soup)
    etat_initial = comportement_soup.initialConfigurations()[0]
    print("Etat initial: ", etat_initial)
    actions_possibles = comportement_soup.enabledActions(etat_initial)

    if actions_possibles:
        for action in actions_possibles:
            resultat = comportement_soup.execute(etat_initial, action)
            print("Action exécutée : ", resultat)

    graphe = RR2RG(comportement_soup)
    racine = graphe.roots()[0]
    suivants = graphe.next(racine)
    print("Depuis la racine", racine, ":", suivants)

# Fonction principale pour Alice et Bob Version 1
def AliceBobV1_Main():
    print("\n==== Alice et Bob - Version 1 ====")
    semantic = SoupSemantics(StateCounter())
    resultat1 = check_pred(semantic, lambda c: c.PC_alice == 1 and c.PC_bob == 0)
    print("Condition 1 (Alice=1, Bob=0) :", resultat1)
    resultat2 = check_pred(semantic, lambda c: len(semantic.enabledActions(c)) == 0)
    print("Condition 2 (Aucune action possible) :", resultat2)

# Fonction principale pour Alice et Bob Version 2
def AliceBobV2_Main():
    print("\n==== Alice et Bob - Version 2 ====")
    semantic = SoupSemantics(StateCounter())
    graphe = RR2RG(semantic)
    graphe = IsAcceptingInstance(graphe, lambda c: c.PC_alice == 0)
    print("Racines acceptantes :", graphe.roots())
    print("Transitions depuis la racine :", graphe.next(graphe.roots()[0]))
    resultat = check_pred(semantic, lambda c: c.PC_alice == 0 and c.PC_bob == 1)
    print("Condition (Alice=0, Bob=1) :", resultat)

# Fonction principale pour Alice et Bob Version 3
def AliceBobV3_Main():
    print("\n==== Alice et Bob - Version 3 ====")
    semantic = SoupSemantics(AliceAndBob())
    resultat1 = check_pred(semantic, lambda c: c.PC_alice == 2 and c.PC_bob == 2)
    print("Condition 1 (Alice et Bob en section critique) :", resultat1)  # Faux car interdit
    resultat2 = check_pred(semantic, lambda c: len(semantic.enabledActions(c)) == 0)
    print("Condition 2 (Aucune action possible) :", resultat2)

# Fonction principale pour NBits
def Nbits_Main():
    print("\n==== NBits ====")
    for x in [16, 5, 1]:
        resultat, connu = predicate_finder(NBits([0], 3), lambda n: n == x)
        print(f'{x} atteignable: ', resultat[2], '| Exploré :', resultat[3], 'nœuds, connu:', binary_print(connu))

if __name__ == "__main__":
    while True:
        # Menu d'exécution organisé et interactif
        choix = input('\n*************************************************************\n'
                      'Choisissez une option parmi la liste suivante : \n'
                      '1. Exécuter NBits \n'
                      '2. Exécuter les Tours de Hanoi \n'
                      '3. Exécuter Alice et Bob (Version 1)\n'
                      '4. Exécuter Alice et Bob (Version 2)\n'
                      '5. Exécuter Alice et Bob (Version 3)\n'
                      '6. Quitter\n')

        if choix == '1':
            Nbits_Main()
        elif choix == '2':
            Hanoi_Main()
        elif choix == '3':
            AliceBobV1_Main()
        elif choix == '4':
            AliceBobV2_Main()
        elif choix == '5':
            AliceBobV3_Main()
        elif choix == '6':
            print("Fin de l'exécution.")
            break
        else:
            print("Veuillez choisir une option valide.")
