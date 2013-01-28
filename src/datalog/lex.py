'''
Created on Jan 27, 2013

@author: xiao
'''

import ply.lex as lex

# List of token names.   This is always required
tokens = (
          'SYMBOLIC_CONSTANT',
          'VARIABLE',
          'STRING',
          'COMMA',
          'ANON_VAR',
          'CONS',
          'PARAM_OPEN',
          'PARAM_CLOSE',
          'DOT',
          'NAF',
          'NEG'
)

# Regular expression rules for simple tokens
t_SYMBOLIC_CONSTANT = r'[a-z][A-Za-z0-9_]*'
t_VARIABLE          = r'[A-Z][A-Za-z0-9_]*'
t_STRING            = r'"[^\"]*"'
t_COMMA             = r','
t_ANON_VAR          = r'_'
t_CONS              = r':-'
t_PARAM_OPEN        = r'\('
t_PARAM_CLOSE       = r'\)'
t_DOT               = r'\.'
t_NAF               = r'not'
t_NEG               = r'-'

t_ignore  =         ' \t\n'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == '__main__':
    data = """p(X) :- q(Y), Z(X,Y).
            p(X) :- q_1(X), Z_2().
            """
    
    lexer = lex.lex()
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: break      # No more input
        print tok

