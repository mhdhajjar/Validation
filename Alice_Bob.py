class StateMachine:
    def __init__(self):
        self.states = ["etat initial", "wait", "section critique"]
        self.alice_state = "etat initial"
        self.bob_state = "etat initial"

    def update_state(self, person, next_state):
        if person not in ["alice", "bob"]:
            raise ValueError("Person must be 'alice' or 'bob'")

        current_state = getattr(self, f"{person}_state")
        other_person = "bob" if person == "alice" else "alice"
        other_state = getattr(self, f"{other_person}_state")

        if next_state == "wait" and current_state == "etat initial":
            setattr(self, f"{person}_state", "wait")
            return f"{person} moved to wait."

        elif next_state == "section critique" and current_state == "wait" and other_state == "etat initial":
            setattr(self, f"{person}_state", "section critique")
            return f"{person} moved to section critique."

        elif next_state == "etat initial" and current_state == "section critique":
            setattr(self, f"{person}_state", "etat initial")
            return f"{person} moved to etat initial."

        else:
            return f"Invalid state transition for {person} from {current_state} to {next_state}."

    def get_states(self):
        return {
            "alice": self.alice_state,
            "bob": self.bob_state
        }

# Exemple d'utilisation
sm = StateMachine()
print(sm.get_states())

print(sm.update_state("alice", "wait"))
print(sm.get_states())

print(sm.update_state("alice", "section critique"))
print(sm.get_states())

print(sm.update_state("alice", "etat initial"))
print(sm.get_states())

print(sm.update_state("bob", "wait"))
print(sm.get_states())

print(sm.update_state("bob", "section critique"))
print(sm.get_states())