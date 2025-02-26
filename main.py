'''**************************************************************************'''
'''                                                                          '''
'''    main.py                                                               '''
'''                                                                          '''
'''    By: carlosbravo && lgandarillas @ Procesadores del Lenguaje UC3M      '''
'''                                                                          '''
'''**************************************************************************'''

import sys
from lexer import lexer
from parser import parser

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename, 'r') as f:
        data = f.read()

    # Parse everything in one call
    result_list = parser.parse(data, lexer=lexer)

    if result_list is not None:
        for (line_number, value) in result_list:
            print(f"[Line {line_number}] {value}")
    else:
        print("Error: Parsing failed or file is empty")

if __name__ == "__main__":
    main()
