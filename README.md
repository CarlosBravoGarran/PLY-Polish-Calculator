# Polish Notation Math Interpreter
This project is part of the Compilers course at [Universidad Carlos III de Madrid (UC3M)](https://www.uc3m.es/home), offered by the [Computer Science and Engineering Department](https://www.uc3m.es/computer-science-engineering-department/home).

More details about the course can be found at the following link: [UC3M - Compilers Course](https://aplicaciones.uc3m.es/cpa/generaFicha?est=218&anio=2023&plan=489&asig=13890&idioma=2).

#### Developed by
- Carlos Bravo Garrán - [@carlosbravogarran](https://github.com/carlosbravogarran)
- Luis Gandarillas Fernández - [@lgandarillas](https://github.com/lgandarillas)

## Introduction

This project implements a **lexical and syntactic analyzer** for mathematical expressions written in **Polish notation** (prefix notation). It is developed in **Python** using the **PLY** library, which provides tools for lexical and syntax analysis.

The project consists of:
- A **lexer** that tokenizes mathematical expressions.
- A **parser** that evaluates the expressions and follows Polish notation rules.
- A **test suite** to validate correct functionality.

## Features

- **Lexical Analysis (Lexer)**
  - Supports:
    - **Integer numbers** (e.g., `10`, `240`)
    - **Floating-point numbers** (e.g., `1.34`, `33.0`)
    - **Binary numbers** (e.g., `0b1011`, `0b1`)
    - **Hexadecimal numbers** (e.g., `0xFED123`, `0xAA`)
  - Recognizes arithmetic operators: `+`, `-`, `*`, `/`
  - Supports scientific functions: `exp`, `log`, `sin`, `cos`
  - Handles single-line (`# comment`) and multi-line (`''' comment '''`) comments.
  - Supports special values: `inf` (infinity) and `nan` (not-a-number).
  - Implements a memory variable `{MEMORY}` to store and retrieve values.

- **Syntactic Analysis (Parser)**
  - Implements a **context-free grammar** for parsing expressions in Polish notation.
  - Evaluates arithmetic expressions and function calls.
  - Supports unary negation (`neg`).
  - Handles **syntax errors** and provides detailed error messages.

## Project Setup and Execution Guide
### 1. Check Python Installation
```bash
python3 --version
```
### 2. Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the Interpreter
```bash
python src/main.py test/01_basic_operations
```

## Project Structure
```bash
.
├── requirements.txt                # Dependencies
├── README.md                       # Project documentation
├── docs/
│   ├── P1-Subject-PDL-2025.pdf     # Project description document
├── src/
│   ├── lexer.py                    # Lexical analyzer
│   ├── parser.py                   # Syntactic analyzer
│   ├── main.py                     # Main entry point
├── test/
│   ├── 01_basic_operations         # Test cases for basic operations
│   ├── 02_math_functions           # Test cases for math functions
│   ├── 03_inf_and_nan              # Test cases for infinity and NaN
│   ├── 04_negation                 # Test cases for unary negation
│   ├── 05_bin_and_hex              # Test cases for binary/hex numbers
│   ├── 06_memory                   # Test cases for memory variable
│   ├── 07_combined_ops             # Mixed operations test cases
│   ├── 08_function_ops             # Function operations test cases
│   ├── 09_comments                 # Test cases for comments
│   ├── 10_all_ops                  # Comprehensive test cases
│   ├── 11_lexic_errors             # Lexical error tests
│   ├── 12_syntax_erros             # Syntax error tests
│   ├── 13_syntax_error_empty_neg   # Test cases for empty negation
│   ├── 14_syntax_error_empty_func  # Test cases for empty functions
│   ├── 15_syntax_error_invalid_op  # Test cases for invalid operators
│   ├── 16_empty_file               # Test for empty files
```
