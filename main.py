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

# ANSI color codes for error messages
RED = "\033[91m"
NC = "\033[0m"

def main():
    
    # Ensure a filename is provided as an argument
    if len(sys.argv) < 2:
        sys.exit(f"{RED}Usage: python main.py <filename>{NC}")

    filename = sys.argv[1]

    try:
        # Read the file contents    
        with open(filename, 'r') as f:
            data = f.read()

    except Exception as e:
        sys.exit(f"{RED}Error: {e}{NC}")

    # Parse the input file using the lexer and parser
    result_list = parser.parse(data, lexer=lexer)

    # Handle parsing errors or empty results
    if not result_list:
        sys.exit(f"{RED}Error: Parsing failed or file is empty{NC}")

    # Print parsed results
    for line_number, value in result_list:
        print(f"[Line {line_number}] {value}")

if __name__ == "__main__":
    main()
