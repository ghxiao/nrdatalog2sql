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
    def __init__(self, classicLiteral, naf=False):
        self.classicLiteral = classicLiteral
        self.naf = naf
        
    def __str__(self):
        return "%s%s" % ("not " if self.naf else "", self.classicLiteral)
        
class ClassicLiteral(object):
    def __init__(self, atom, neg=False):
        self.atom = atom
        self.neg = neg 
        
    def __str__(self):
        return "%s%s" % ("-" if self.neg else "", self.atom)
        
class Atom(object):
    def __init__(self, predicate, terms):
        self.predicate = predicate
        self.terms = terms
        
    def __str__(self):
        return "%s(%s)" % (self.predicate, ",".join(str(x) for x in self.terms))

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
