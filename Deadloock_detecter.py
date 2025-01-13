from itertools import product

from Alice_Bob import StateMachine

def test_all_scenarios():
    sm = StateMachine()

    # Définir les états possibles pour chaque personne
    states = sm.states  # ["etat initial", "wait", "section critique"]

    # Générer toutes les combinaisons possibles des états de Alice et Bob
    all_combinations = product(states, repeat=2)

    deadlock_detected = False

    for alice_state, bob_state in all_combinations:
        # Réinitialiser les états initiaux
        sm = StateMachine()
        
        # Définir les transitions pour atteindre les combinaisons
        transitions = [
            ("alice", alice_state),
            ("bob", bob_state),
        ]

        print(f"\nTesting combination: Alice -> {alice_state}, Bob -> {bob_state}")
        
        # Appliquer les transitions
        for person, target_state in transitions:
            result = sm.update_state(person, target_state)
            print(result)
        
        # Vérifier les états finaux
        final_states = sm.get_states()
        print(f"Final states: {final_states}")
        
        # Vérifier si les deux sont bloqués en "wait" (deadlock potentiel)
        if final_states["alice"] == "wait" and final_states["bob"] == "wait":
            print("Deadlock detected!")
            deadlock_detected = True

    if not deadlock_detected:
        print("\nNo deadlocks detected in any scenario.")
    else:
        print("\nDeadlock(s) were detected.")

# Exécuter le test
test_all_scenarios()
