'''
Created on Jan 27, 2013

@author: xiao
'''

import ply.yacc as yacc

from datalog.model import Variable, Constant, Atom, ClassicLiteral, NafLiteral,\
    Rule, Program

from datalog.lex import tokens

start = 'program'

def p_program(p):
    '''program : rules'''
    p[0] = Program(p[1])
    
def p_rules_list(p):
    '''rules : rules rule'''
    p[0] = p[1] + [p[2]]
    
def p_rules(p):
    '''rules :  rule'''
    p[0] = [p[1]]    
    
def p_rule(p):
    '''rule :  head CONS body DOT'''
    p[0] = Rule(p[1], p[3])
    
def p_head(p): 
    '''head : atom'''
    p[0] = p[1]
    
def p_body(p):
    '''body : conjunction'''
    p[0] = p[1]
    
def p_conjunction_list(p):
    '''conjunction     : conjunction COMMA naf_literal''' 
    p[0] = p[1] + [p[3]]

def p_conjunction(p):
    '''conjunction     : naf_literal'''
    p[0] = [p[1]]
    
def p_naf_literal_naf(p):
    '''naf_literal     : NAF classic_literal'''
    p[0] = NafLiteral(p[1])

def p_naf_literal(p):
    '''naf_literal     : classic_literal'''
    p[0] = NafLiteral(p[1])
    
def p_classic_literal_neg(p):
    '''classic_literal  : NEG atom'''
    p[0] = ClassicLiteral(p[2], True)

def p_classic_literal(p):    
    '''classic_literal  : atom'''
    p[0] = ClassicLiteral(p[1])
    
def p_atom(p):
    '''atom : predicate_name PARAM_OPEN terms PARAM_CLOSE '''
    p[0] = Atom(p[1], p[3]) 
    
def p_predication_name(p):
    '''predicate_name : identifier'''
    p[0] = p[1]

def p_terms_term(p):
    '''terms : term'''
    p[0] = [p[1]]
    
def p_terms_terms(p):
    '''terms : term COMMA terms'''
    p[0] = [p[1]] + p[3] 
    
def p_term(p):
    '''term : basic_term '''
    p[0] = p[1]
    
def p_basic_term(p):
    '''basic_term : ground_term 
                | variable_term'''
    p[0] = p[1]

def p_ground_term(p):
    '''ground_term : SYMBOLIC_CONSTANT'''

    p[0] = Constant(p[1])
    
def p_variable_term(p):
    '''variable_term : VARIABLE
                    | ANON_VAR'''
    p[0] = Variable(p[1])

def p_identifier(p):
    '''identifier : SYMBOLIC_CONSTANT 
            | STRING 
            | VARIABLE'''
    p[0] = p[1]

def p_error(p):
    print "Syntax error in input! ", p
    
parser = yacc.yacc(start='program')

if __name__ == '__main__':
    # Build the parser
    parser = yacc.yacc(start='program')
    
    while True:
        try:
            s = raw_input('datalog > ')
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        print "\n".join(str(x) for x in result)