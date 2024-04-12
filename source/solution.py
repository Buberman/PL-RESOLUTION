class KnowledgeBase:
    def __init__(self):
        self.clauses = []
    
    
    def getNegative(self, atom):
        if atom[0] == '-':
            return atom[1:]
        else:
            return '-' + atom
    

    def checkcomp(self, clause):
        for atom in clause:
            if self.getNegative(atom) in clause:
                return True
        return False
    
    def addClause(self, clause):
        if clause not in self.clauses and not self.checkcomp(clause):
            self.clauses.append(clause)
    

  
    
        
    
    

        

