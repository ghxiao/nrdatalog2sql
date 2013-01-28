'''
Created on Jan 27, 2013

@author: xiao
'''

class Term(object):
    pass

class Variable(Term):
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name
        
class Constant(Term):
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name

class NafLiteral(object):
    def __init__(self, predicate, terms, neg=False, naf=False):
        self.predicate = predicate
        self.terms = terms
        self.neg = neg
        self.naf = naf
        
    def __str__(self):
        return "%s%s%s(%s)" % (
            "not " if self.naf else "", 
            "-" if self.neg else "", 
            self.predicate, ",".join(str(x) for x in self.terms))
        

class Rule(object):
    def __init__(self, head, body):
        self.head = head
        self.body = body
        
    def __str__(self):
        return "%s :- %s." % (self.head, ", ".join(str(x) for x in self.body))
    
class Program(object):
    def __init__(self, rules):
        self.rules = rules

    def __str__(self):
        return "\n".join(str(x) for x in self.rules)
