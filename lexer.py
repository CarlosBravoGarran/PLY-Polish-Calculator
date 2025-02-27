'''**************************************************************************'''
'''                                                                          '''
'''    lexer.py                                                              '''
'''                                                                          '''
'''    By: carlosbravo && lgandarillas @ Procesadores del Lenguaje UC3M      '''
'''                                                                          '''
'''**************************************************************************'''

import ply.lex as lex

# List of tokens
tokens = (
    'FLOAT', 'BINARY', 'HEXADECIMAL', 'INTEGER',
    'INF', 'NAN', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE',
    'EXP', 'LOG', 'SIN', 'COS', 'NEG', 'MEMORY', 'EQUALS'
)

# Exclusive states for multiline comments
states = (
    ('comment', 'exclusive'),
)

# Single-line comments (# ...)
def t_COMMENT(t):
    r'\#.*'
    pass  # Ignore everything after '#'

# Multiline comments with '''
def t_begin_comment(t):
    r"'''"
    t.lexer.begin('comment')

def t_comment_content(t):
    r'[^\'\n]+'
    pass

def t_comment_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comment_end(t):
    r"'''"
    t.lexer.begin('INITIAL')

# Ignore spaces/tabs in 'comment' state
t_comment_ignore = ' \t'

def t_comment_error(t):
    t.lexer.skip(1)


# Tokens in the INITIAL state
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_MULTIPLY  = r'\*'
t_DIVIDE    = r'/'
t_EXP       = r'exp'
t_LOG       = r'log'
t_SIN       = r'sin'
t_COS       = r'cos'
t_NEG       = r'neg'
t_EQUALS    = r'='


def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_BINARY(t):
    r'0b[01]+'
    t.value = int(t.value, 2)
    return t

def t_HEXADECIMAL(t):
    r'0x[0-9A-F]+'
    t.value = int(t.value, 16)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Infinity
def t_INF(t):
    r'inf'
    t.value = float('inf')
    return t

# NaN (Not a Number)
def t_NAN(t):
    r'nan'
    t.value = float('nan')
    return t

# Memory variable
def t_MEMORY(t):
    r'\{MEMORY\}'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignore spaces and tabs
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character: {t.value[0]!r} at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
