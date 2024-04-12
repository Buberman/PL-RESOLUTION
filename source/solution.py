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
    
    def NegativeQuery(self, query):
        res = []
        for clause in query:
            new_query = []
            for atom in new_query:
                new_query.append(self.getNegative(atom))
            res.append(new_query)
        return res
    
    def toCNF(self, clauses):
        res = []
        product_all = [[]]
        for clause in clauses:
            new_product = []
            for p in product_all:
                for q in clause:
                    new_product.append(p + [q])
            product_all = new_product

        for i in product_all:
            new = self.normClause(sum(i, []))
            if not self.checkComplementary(new) and new not in res:
                res.append(new)
        res.sort(key=len)
        res = self.remove(res)
        return res

    def norClause(self, clause):
        seen = set()
        unique_clause = []
        for atom in clause:
            if atom not in seen:
                seen.add(atom)
                unique_clause.append(atom)

        unique_clause.sort()

        res = []
        for atom in unique_clause:
            res.append(atom)
        return res
    

    def remove_redundant_clauses(self, clauses):
        res = []
        for c in clauses:
            redundant = False
            for r in res:
                if set(r).issubset(set(c)):
                    redundant = True
                    break
            if not redundant:
                res.append(c)
        return res
    
  
    
        
    
    

        

