import ply.lex as lex

# List of tokens
tokens = (
    'FLOAT', 'BINARY', 'HEXADECIMAL', 'INTEGER',
    'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE',
    'EXP', 'LOG', 'SIN', 'COS', 'NEG'
)

# Regular expressions for simple tokens
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_MULTIPLY  = r'\*'
t_DIVIDE    = r'/'
t_EXP       = r'exp'
t_LOG       = r'log'
t_SIN       = r'sin'
t_COS       = r'cos'
t_NEG       = r'neg'

# TOKENS
# floating point numbers
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Binary numbers
def t_BINARY(t):
    r'0b[01]+'
    t.value = int(t.value, 2)
    return t

# Hexadecimal numbers
def t_HEXADECIMAL(t):
    r'0x[0-9A-F]+'
    t.value = int(t.value, 16)
    return t

# Integer numbers
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignore single-line comments (# ...)
def t_COMMENT(t):
    r'\#.*'
    pass 

# Ignore multi-line comments (''' ... ''')
def t_MULTILINE_COMMENT(t):
    r"'''[\s\S]*?'''"
    t.lexer.lineno += t.value.count("\n")
    pass 

# Count lines 
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignore spaces and tabs
t_ignore = ' \t'

# Lexical error handling
def t_error(t):
    print(f"Illegal character: {t.value[0]} at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()