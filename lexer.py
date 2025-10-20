KEYWORDS = {
    "Let": "LET",
    "out": "OUT",
    "in": "IN",
    "Run": "RUN",
    "while": "WHILE",
    "agar": "IF",
    "ya_fir": "ELIF",
    "warna": "ELSE",
    "func": "FUNC",
    "give": "RETURN",
    "True": "BOOL",
    "False": "BOOL",
    "line": "NEWLINE",
    "num": "NUM_CONVERT",
    "dec": "DEC_CONVERT",
    "word": "WORD_CONVERT",
    "bool": "BOOL_CONVERT"
}

OPERATORS = {
    "=": "ASSIGN",
    "+": "PLUS",
    "-": "MINUS",
    "*": "MULT",
    "/": "DIV",
    "%": "MOD",
    "==": "EQ",
    "!=": "NEQ",
    "<": "LT",
    ">": "GT",
    "<=": "LTE",
    ">=": "GTE"
}

DELIMITERS = {
    "(": "LPAREN",
    ")": "RPAREN",
    "{": "LBRACE",
    "}": "RBRACE",
    ",": "COMMA"
}

TOKEN_TYPES = [
    "IDENTIFIER",
    "NUMBER",
    "STRING"
]


def get_keyword_token(word):
    return KEYWORDS.get(word, "IDENTIFIER")


def lex(words):
    position = 0
    tokens = []
    line_number = 1

    while position < len(words):
        char = words[position]

        if char == '\n':
            line_number += 1
            position += 1

        elif char.isspace():
            position += 1

        elif char in DELIMITERS:
            tokens.append((char, DELIMITERS[char], line_number))
            position += 1

        elif char in OPERATORS:
            if position + 1 < len(words):
                two_char = char + words[position + 1]
                if two_char in OPERATORS:
                    tokens.append((two_char, OPERATORS[two_char], line_number))
                    position += 2
                    continue

            tokens.append((char, OPERATORS[char], line_number))
            position += 1

        elif char.isalpha() or char == "_":
            current = ""
            start_line = line_number
            while position < len(words) and (words[position].isalnum() or words[position] == "_"):
                current += words[position]
                position += 1

            if current in KEYWORDS:
                tokens.append((current, KEYWORDS[current], start_line))
            else:
                tokens.append((current, "IDENTIFIER", start_line))

        elif char == '"':
            start_line = line_number
            position += 1
            current = ""
            while position < len(words) and words[position] != '"':
                if words[position] == '\n':
                    line_number += 1
                current += words[position]
                position += 1
            position += 1
            tokens.append((current, "STRING", start_line))

        elif char.isdigit():
            current = ""
            dot_count = 0
            start_line = line_number

            while position < len(words) and (words[position].isdigit() or words[position] == "."):
                if words[position] == ".":
                    dot_count += 1
                    if dot_count > 1:
                        break
                current += words[position]
                position += 1

            tokens.append((current, "NUMBER", start_line))

        elif char == "~":
            position += 1
            while position < len(words) and words[position] != "~":
                if words[position] == '\n':
                    line_number += 1
                position += 1
            position += 1

        else:
            position += 1

    return tokens