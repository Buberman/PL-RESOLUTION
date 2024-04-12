import itertools
class KnowledgeBase:
    def __init__(self):
        self.clauses = []
    
    def negativetify(self, atom):
        if atom[0] == '-':
            return atom[1:]
        else:
            return '-' + atom
    
    def negativeQuery(self, query):
        res = []
        for clause in query:
            new = []
            for atom in clause:
                new.append([set.netativetify(atom)])
            res.append(new)
        
        if len(res) == 1:
             return list(itertools.chain.from_iterable(res))
        else:
            return self.toCNF(res)

