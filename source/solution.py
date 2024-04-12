class KnowledgeBase:
    #Initialize
    def __init__(self):
        self.clauses = []
    
    #phủ định
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
    
    #thêm clause vào KB
    def addClause(self, clause):
        if clause not in self.clauses and not self.checkcomp(clause):
            self.clauses.append(clause)
    
    #Phủ định nguyên cái hàng chờ
    def NegativeQuery(self, query):
        res = []
        for clause in query:
            new_query = []
            for atom in new_query:
                new_query.append(self.getNegative(atom))
            res.append(new_query)
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
    
    #Loại bỏ trùng lặp
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
    
    def toCNF(self, clauses):
        res = []
        for clause_combination in self.cartesian_product(clauses):
            new = self.normClause(sum(clause_combination, []))
            if not self.checkComplementary(new) and new not in res:
                res.append(new)
        res.sort(key=len)
        res = self.remove_redundant_clauses(res)
        return res
    
    def cartesian_product(self, lists):
        if not lists:
            yield []
        else:
            for item in lists[0]:
                for rest in self.cartesian_product(lists[1:]):
                    yield [item] + rest

    
    
    

        

