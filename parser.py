'''**************************************************************************'''
'''                                                                          '''
'''    parser.py                                                             '''
'''                                                                          '''
'''    By: carlosbravo && lgandarillas @ Procesadores del Lenguaje UC3M      '''
'''                                                                          '''
'''**************************************************************************'''

import ply.yacc as yacc
import math
from lexer import tokens

def p_program_empty(p):
    '''
    program :
    '''
    p[0] = []

def p_program_expressions(p):
    '''
    program : program expression
    '''
    p[0] = p[1]
    p[0].append(p[2])

# Binary operators
def p_expression_binop(p):
    '''
    expression : PLUS expression expression
               | MINUS expression expression
               | MULTIPLY expression expression
               | DIVIDE expression expression
    '''
    line = p.lineno(1)
    if p[1] == '+':
        val = p[2][1] + p[3][1]
    elif p[1] == '-':
        val = p[2][1] - p[3][1]
    elif p[1] == '*':
        val = p[2][1] * p[3][1]
    elif p[1] == '/':
        val = p[2][1] / p[3][1] if p[3][1] != 0 else float('nan')
    p[0] = (line, val)

# Function calls
def p_expression_func(p):
    '''
    expression : EXP expression
               | LOG expression
               | SIN expression
               | COS expression
    '''
    line = p.lineno(1)
    if p[1] == 'exp':
        val = math.exp(p[2][1])
    elif p[1] == 'log':
        val = math.log(p[2][1]) if p[2][1] > 0 else float('nan')
    elif p[1] == 'sin':
        val = math.sin(p[2][1])
    elif p[1] == 'cos':
        val = math.cos(p[2][1])
    p[0] = (line, val)

# Number literals
def p_expression_number(p):
    '''
    expression : INTEGER
               | FLOAT
               | BINARY
               | HEXADECIMAL
    '''
    line = p.lineno(1)
    p[0] = (line, p[1])

# Unary minus operator
def p_expression_neg(p):
    '''
    expression : NEG expression
    '''
    line = p.lineno(1)
    if p[2] is not None:
        val = -p[2][1]
    else:
        print("Error: 'neg' received an invalid value.")
        val = float('nan')
    p[0] = (line, val)

# Infinity and NaN
def p_expression_inf_nan(p):
    '''expression : INF
                  | NAN'''
    line = p.lineno(1)
    p[0] = (line, p[1])


memory = 0

def p_assignment(p):
    '''expression : MEMORY EQUALS expression'''
    global memory
    memory = p[3][1]
    p[0] = (p.lineno(1), memory)

def p_expression_memory(p):
    '''expression : MEMORY'''
    global memory
    p[0] = (p.lineno(1), memory)

# Error rule for syntax errors
def p_error(p):
    if p is None:
        print("Syntax error: Incomplete expression, unexpected end of input.")
    else:
        print(f"Syntax error at: {p}")

parser = yacc.yacc(debug=False)
