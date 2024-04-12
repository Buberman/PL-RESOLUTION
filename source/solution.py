class KnowledgeBase:
    def __init__(self):
        self.clauses = []
    
    def negativetify(self, atom):
        if atom[0] == '-':
            return atom[1:]
        else:
            return '-' + atom
    
    def