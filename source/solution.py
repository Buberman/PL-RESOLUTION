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
    def NegativeList(self, list):
        res = []
        for clause in list:
            new_list = []
            for atom in list:
                new_list.append(self.getNegative(atom))
            res.append(new_list)
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

    def resolve(self, clause_i, clause_j):
        new_clauses = []
        for atom in clause_i:
            neg_atom = self.getNegative_atom(atom)
            if neg_atom in clause_j:
                new_clause = self.resolve_single(atom, neg_atom, clause_i, clause_j)
                if new_clause:
                    new_clauses.append(new_clause)
        return new_clauses

    def resolve_single(self, atom_i, atom_j, clause_i, clause_j):
        temp_c_i = clause_i.copy()
        temp_c_j = clause_j.copy()
        temp_c_i.remove(atom_i)
        temp_c_j.remove(atom_j)
        if not temp_c_i and not temp_c_j:
            return ['{}']
        else:
            merged_clause = temp_c_i + temp_c_j
            merged_clause = self.normClause(merged_clause)
            if not self.checkComplementary(merged_clause) and merged_clause not in self.clauses:
                return merged_clause
        return None

    def PL_Resolution(self, query):
        tempKB = KnowledgeBase()
        tempKB.clauses = self.clauses.copy()

        neg_query = self.getNegative_query(query)
        for neg_atom in neg_query:
            tempKB.addClause(neg_atom)

        while True:
            new_clauses = []
            for i in range(len(tempKB.clauses)):
                for j in range(i + 1, len(tempKB.clauses)):
                    resolvents = tempKB.resolve(tempKB.clauses[i], tempKB.clauses[j])
                    for res in resolvents:
                        if res not in new_clauses:
                            new_clauses.append(res)

            if not new_clauses:
                return [], False
            elif ['{}'] in new_clauses:
                return [], True

            for clause in new_clauses:
                tempKB.addClause(clause)
    

        

