'''
Created on Jan 27, 2013

@author: xiao
'''

#class CommonEqualityMixin(object):
#
#    def __eq__(self, other):
#        return (isinstance(other, self.__class__)
#            and self.__dict__ == other.__dict__)
#
#    def __ne__(self, other):
#        return not self.__eq__(other)

class Term(object):
    def __eq__(self, other):
        return self.name == other.name
    
    def __hash__(self):
        return hash(self.name)

class Variable(Term):
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return "datalog.model.Variable('%s')" % self.name
        
class Constant(Term):
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return "datalog.model.Constant('%s')" % self.name

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

    def __repr__(self):
        return "datalog.model.NafLiteral('%s', '%s', '%s', '%s')" % (self.predicate, self.terms, self.neg, self.naf)

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
    
if __name__ == '__main__':
    x1 = Variable('X')
    x2 = Variable('X')
    from collections import defaultdict
    d = defaultdict(list)
    d[x1].append(1)
    d[x2].append(2)
    print d
