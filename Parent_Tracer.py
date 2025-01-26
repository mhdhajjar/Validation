class Transition_Relation:
    def initial(self): pass
    def next(self, c): pass


class AcceptingSet:
    def is_accepting(c): pass


class Identity_Proxy:
    def __init__(self, operand):
        self.operand = operand

    def __getattr__(self, attr):
        return getattr(self.operand, attr)


class ParentStore_Proxy (Identity_Proxy):

    def __init__(self, op):
        super().__init__(op)
        self.parent = {}

    def next(self, conf):
        nS = self.operand.next(conf)

        for n in nS:
            if n not in self.parent:
                self.parent[n] = conf

        return nS

class SemanticTransitionRelation: 
    def initial (self):pass
    def actions (self, conf): pass
    def execute (self, conf, action):pass