import re


# Lexer: Tokenizing the code
def lexer(code):
    tokens = []
    token_spec = [
        ('printout', r'printout'),  # CALL command
        ('entstr', r'"[^"]*"'),  # String (anything inside double quotes)
        ('if', r'if'),  # IF command
        ('then', r'then'),  # THEN command
        ('CLOSE', r'CLOSE'),  # CLOSE command
        ('GETNUM', r'\d+'),  # Numbers (GETNUM)
        ('EQUALS', r'=='),  # Equality check
        ('WHITESPACE', r'\s+'),  # Whitespaces (ignored)
    ]

    for tok_type, tok_regex in token_spec:
        matches = re.finditer(tok_regex, code)
        for match in matches:
            if tok_type != 'WHITESPACE':  # Ignore whitespaces
                tokens.append((tok_type, match.group()))
    return tokens


# Parser: Converts tokens into a meaningful structure
def parser(tokens):
    if not tokens:
        raise SyntaxError(
            "nothing has been founded, please control your code again.")

    if tokens[0][0] == 'printout' and tokens[1][0] == 'entstr':
        return ('printout', tokens[1][1].strip('"'))
    elif tokens[0][0] == 'if' and tokens[1][0] != 'then':
        condition = tokens[1][1]
        return ('if', condition)
    else:
        raise SyntaxError(
            "ERROR_SYNAX_READER: invalid or or illegal nal syntax, please control your code again."
        )


# Interpreter: Executes the parsed code
def interpreter(parsed_code):
    if parsed_code[0] == 'printout':
        print(parsed_code[1])
    elif parsed_code[0] == 'if':
        print(
            f"if condition: {parsed_code[1]} - Will execute if the condition is true."
        )


# File reading: Reads a `.now` file
def read_file(file_path):
    if not file_path.endswith('.rub'):
        raise ValueError(
            "ERROR_FILE: there must be a file that ends with .rub!"
        )

    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"{file_path} not found.")


# Running a `.now` file
def run_nal_file(file_path):
    try:
        # 1. Read the file
        code = read_file(file_path)

        # 2. Tokenize the code
        tokens = lexer(code)
        print("Entered token:", tokens)

        # 3. Parse the tokens
        parsed_code = parser(tokens)
        print("Parsed code:", parsed_code)

        # 4. Execute the parsed code
        interpreter(parsed_code)

    except (ValueError, SyntaxError, FileNotFoundError) as e:
        print(f"Error: {e}")


# Example: Running a `.now` file
run_nal_file('program.rub')
