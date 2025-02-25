import ply.yacc as yacc
import math
from lexer import tokens

precedence = (
    ('right', 'NEG'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
)

def p_expression_binop(p):
    '''expression : PLUS expression expression
                  | MINUS expression expression
                  | MULTIPLY expression expression
                  | DIVIDE expression expression'''
    if p[1] == '+': p[0] = p[2] + p[3]
    elif p[1] == '-': p[0] = p[2] - p[3]
    elif p[1] == '*': p[0] = p[2] * p[3]
    elif p[1] == '/': p[0] = p[2] / p[3] if p[3] != 0 else float('NaN')

def p_expression_func(p):
    '''expression : EXP expression
                  | LOG expression
                  | SIN expression
                  | COS expression'''
    if p[1] == 'exp': p[0] = math.exp(p[2])
    elif p[1] == 'log': p[0] = math.log(p[2]) if p[2] > 0 else float('NaN')
    elif p[1] == 'sin': p[0] = math.sin(p[2])
    elif p[1] == 'cos': p[0] = math.cos(p[2])

def p_expression_number(p):
    '''expression : INTEGER
                  | FLOAT
                  | BINARY
                  | HEXADECIMAL'''
    p[0] = p[1] 

def p_expression_neg(p):
    '''expression : NEG expression'''
    if p[2] is not None:
        p[0] = -p[2]
    else:
        print("Error: 'neg' recibió un valor inválido.")
        p[0] = float('nan')


def p_empty(p):
    '''expression :'''
    p[0] = None


def p_error(p):
    print(f"Error de sintaxis en la entrada: {p}")

parser = yacc.yacc()

def test_parser(filename):
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            result = parser.parse(line)
            print(f"Entrada: {line} → Resultado: {result}")

if __name__ == "__main__":
    test_parser("test_cases/parser_test.txt")
