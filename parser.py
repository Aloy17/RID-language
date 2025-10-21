class Parser:
    def __init__(self, token):
        self.token = token
        self.output = []
        self.symbols = {}
        self.functions = {}
        self.position = 0
        self.current_params = []
        self.handlers = {
            "LET": self.var_declare,
            "IDENTIFIER": self.assignment,
            "OUT": self.print_stmt,
            "RUN": self.loop_stmt,
            "IF": self.conditional_stmt,
            "ELIF": self.conditional_stmt,
            "ELSE": self.conditional_stmt,
            "FUNC": self.func_def,
            "RETURN": self.return_stmt,
            "NEWLINE": self.newline_stmt
        }

    def get_line_num(self):
        """Get the current line number from token"""
        if self.position < len(self.token) and len(self.token[self.position]) > 2:
            return self.token[self.position][2]
        return "?"

    def error(self, message, error_type="Syntax Error"):
        """Format error message with line number and error type"""
        line = self.get_line_num()
        return f"Line {line} -> {error_type}: {message}"

    def parse(self):
        while self.position < len(self.token):
            current_token = self.token[self.position]
            token_type = current_token[1]

            if token_type == "IDENTIFIER":
                if self.position + 1 < len(self.token) and self.token[self.position + 1][1] == "LPAREN":
                    handler = self.func_call
                else:
                    handler = self.assignment
            else:
                handler = self.handlers.get(token_type, self.unknown_token)

            handler(current_token)

    def var_declare(self, current_token):
        self.position += 1
        var_token = self.token[self.position]

        if var_token[1] != "IDENTIFIER":
            raise SyntaxError(self.error(f"Expected variable name after 'Let', got '{var_token[0]}'"))

        var_name = var_token[0]
        self.position += 1

        if self.token[self.position][1] != "ASSIGN":
            raise SyntaxError(
                self.error(f"Expected '=' after variable '{var_name}', got '{self.token[self.position][0]}'"))

        self.position += 1
        expr = self.expression()

        self.output.append(f"{var_name} = {expr.strip()}")
        self.symbols[var_name] = expr

    def assignment(self, current_token):
        var_name = current_token[0]

        if var_name not in self.symbols and var_name not in self.current_params:
            raise NameError(
                self.error(f"Variable '{var_name}' is not defined. Use 'Let {var_name} = ...' to declare it first", "Name Error"))

        self.position += 1
        if self.token[self.position][1] != "ASSIGN":
            raise SyntaxError(
                self.error(f"Expected '=' after variable '{var_name}', got '{self.token[self.position][0]}'"))

        self.position += 1
        expr = self.expression()

        self.symbols[var_name] = expr
        self.output.append(f"{var_name} = {expr.strip()}")

    def print_stmt(self, current_token):
        self.position += 1
        if self.position >= len(self.token):
            raise SyntaxError(self.error(f"Expected '(' after 'out', but reached end of file"))
        if self.token[self.position][1] != "LPAREN":
            raise SyntaxError(self.error(f"Expected '(' after 'out', got '{self.token[self.position][0]}'"))
        self.position += 1

        value = self.expression()

        if self.position >= len(self.token):
            raise SyntaxError(self.error(f"Expected ')' to close 'out' statement, but reached end of file"))
        if self.token[self.position][1] != "RPAREN":
            raise SyntaxError(
                self.error(f"Expected ')' to close 'out' statement, got '{self.token[self.position][0]}'"))
        self.position += 1
        self.output.append(f"print({value}, end='')")

    def newline_stmt(self, current_token):
        self.position += 1
        self.output.append("print()")

    def loop_stmt(self, current_token):
        if current_token[1] != "RUN":
            raise SyntaxError(self.error(f"Expected 'Run' keyword, got '{current_token[0]}'"))
        self.position += 1
        next_token = self.token[self.position]

        if next_token[1] == "LPAREN":
            self.position += 1
            num_token = self.token[self.position]

            if num_token[1] != "NUMBER":
                raise TypeError(self.error(f"Expected numeric value inside 'Run()', got '{num_token[0]}'", "Type Error"))
            loop_template = f"for _ in range(int({num_token[0]})):"
            self.position += 1

            if self.token[self.position][1] != "RPAREN":
                raise SyntaxError(self.error(f"Expected ')' after loop count, got '{self.token[self.position][0]}'"))
            self.position += 1

            if self.token[self.position][1] != "LBRACE":
                raise SyntaxError(
                    self.error(f"Expected '{{' to begin loop block, got '{self.token[self.position][0]}'"))
            self.position += 1

            block_lines = self.block()
            self.output.append(loop_template)
            self.output.extend(["    " + line for line in block_lines])

        elif next_token[1] == "WHILE":
            self.position += 1

            if self.token[self.position][1] != "LPAREN":
                raise SyntaxError(self.error(f"Expected '(' after 'while', got '{self.token[self.position][0]}'"))
            self.position += 1
            cond_str = self.condition()

            if self.token[self.position][1] != "RPAREN":
                raise SyntaxError(
                    self.error(f"Expected ')' after while condition, got '{self.token[self.position][0]}'"))
            self.position += 1

            if self.token[self.position][1] != "LBRACE":
                raise SyntaxError(
                    self.error(f"Expected '{{' to begin while loop block, got '{self.token[self.position][0]}'"))
            self.position += 1
            block_lines = self.block()

            self.output.append(f"while {cond_str}:")
            self.output.extend(["    " + line for line in block_lines])

        else:
            raise SyntaxError(self.error(f"Expected '(' or 'while' after 'Run', got '{next_token[0]}'"))

    def conditional_stmt(self, current_token):
        keyword = current_token[1]
        if keyword not in ("IF", "ELIF", "ELSE"):
            raise SyntaxError(
                self.error(f"Expected conditional keyword (agar/ya_fir/warna), got '{current_token[0]}'"))
        self.position += 1

        cond_str = ""
        if keyword in ("IF", "ELIF"):
            if self.token[self.position][1] != "LPAREN":
                raise SyntaxError(
                    self.error(f"Expected '(' after '{current_token[0]}', got '{self.token[self.position][0]}'"))
            self.position += 1
            cond_str = self.condition()

            if self.token[self.position][1] != "RPAREN":
                raise SyntaxError(self.error(f"Expected ')' after condition, got '{self.token[self.position][0]}'"))
            self.position += 1

        if self.token[self.position][1] != "LBRACE":
            raise SyntaxError(
                self.error(f"Expected '{{' to begin conditional block, got '{self.token[self.position][0]}'"))
        self.position += 1
        block_lines = self.block()

        if keyword == "IF":
            self.output.append(f"if {cond_str}:")
        elif keyword == "ELIF":
            self.output.append(f"elif {cond_str}:")
        else:
            self.output.append("else:")

        for line in block_lines:
            self.output.append("    " + line)

    def func_def(self, current_token):
        if current_token[1] != "FUNC":
            raise SyntaxError(self.error(f"Expected 'func' keyword, got '{current_token[0]}'"))
        self.position += 1

        func_name = self.token[self.position][0]
        self.position += 1

        if self.token[self.position][1] != "LPAREN":
            raise SyntaxError(
                self.error(f"Expected '(' after function name '{func_name}', got '{self.token[self.position][0]}'"))
        self.position += 1
        parameters = []

        while self.position < len(self.token) and self.token[self.position][1] != "RPAREN":
            if self.token[self.position][1] == "IDENTIFIER":
                parameters.append(self.token[self.position][0])
                self.position += 1
            elif self.token[self.position][1] == "COMMA":
                self.position += 1
            else:
                raise SyntaxError(
                    self.error(f"Invalid token in function parameters, expected parameter name or ',', got '{self.token[self.position][0]}'"))

        if self.position >= len(self.token) or self.token[self.position][1] != "RPAREN":
            raise SyntaxError(self.error(f"Expected ')' after function parameters"))
        self.position += 1

        if self.token[self.position][1] != "LBRACE":
            raise SyntaxError(
                self.error(f"Expected '{{' to begin function body, got '{self.token[self.position][0]}'"))
        self.position += 1

        self.functions[func_name] = {"params": parameters, "body": []}
        self.current_params = parameters

        block_lines = self.block()

        params_str = ", ".join(parameters)
        self.output.append(f"def {func_name}({params_str}):")
        if block_lines:
            self.output.extend(["    " + line for line in block_lines])
        else:
            self.output.append("    pass")

        self.functions[func_name]["body"] = block_lines
        self.current_params = []

    def block(self):
        block_lines = []
        temp_output = []

        while self.position < len(self.token) and self.token[self.position][1] != "RBRACE":
            current_token = self.token[self.position]
            token_type = current_token[1]

            original_output = self.output
            self.output = temp_output

            if token_type == "IDENTIFIER":
                if self.position + 1 < len(self.token) and self.token[self.position + 1][1] == "LPAREN":
                    self.func_call(current_token)
                else:
                    self.assignment(current_token)
            else:
                handler = self.handlers.get(token_type, self.unknown_token)
                handler(current_token)

            self.output = original_output
            block_lines.extend(temp_output)
            temp_output = []

        if self.position < len(self.token) and self.token[self.position][1] == "RBRACE":
            self.position += 1

        return block_lines

    def condition(self):
        lhs = self.expression()

        if self.position >= len(self.token):
            raise SyntaxError(self.error("Incomplete condition"))

        op_token = self.token[self.position]
        op_map = {"EQ": "==", "NEQ": "!=", "LT": "<", "GT": ">", "LTE": "<=", "GTE": ">="}

        if op_token[1] not in op_map:
            raise SyntaxError(
                self.error(f"Invalid comparison operator, expected one of (==, !=, <, >, <=, >=), got '{op_token[0]}'"))
        op = op_map[op_token[1]]
        self.position += 1

        rhs = self.expression()

        return f"{lhs} {op} {rhs}"

    def func_call(self, current_token):
        """Statement-level function call"""
        call_str = self.parse_function_call()
        self.output.append(call_str)

    def return_stmt(self, current_token):
        if current_token[1] != "RETURN":
            raise SyntaxError(self.error(f"Expected 'give' keyword for return statement, got '{current_token[0]}'"))
        self.position += 1

        if (self.position >= len(self.token) or
                self.token[self.position][1] in ["RBRACE", "RPAREN"]):
            expr = ""
        else:
            expr = self.expression()

        self.output.append(f"return {expr}".strip())

    def expression(self):
        return self.parse_additive()

    def parse_additive(self):
        left = self.parse_multiplicative()

        while self.position < len(self.token) and self.token[self.position][1] in ("PLUS", "MINUS"):
            op = self.token[self.position][0]
            self.position += 1
            right = self.parse_multiplicative()
            if op == "+":
                # Smart concatenation: convert to string if either operand is a string
                left = f"({left} + {right} if isinstance({left}, (int, float)) and isinstance({right}, (int, float)) else str({left}) + str({right}))"
            else:
                left = f"{left} {op} {right}"

        return left

    def parse_multiplicative(self):
        left = self.parse_primary()

        while self.position < len(self.token) and self.token[self.position][1] in ("MULT", "DIV", "MOD"):
            op = self.token[self.position][0]
            self.position += 1
            right = self.parse_primary()
            left = f"{left} {op} {right}"

        return left

    def parse_primary(self):
        if self.position >= len(self.token):
            raise SyntaxError(self.error("Unexpected end of expression"))

        current = self.token[self.position]
        value_token, key_token = current[0], current[1]

        if key_token == "MINUS":
            self.position += 1
            if self.position >= len(self.token):
                raise SyntaxError(self.error("Expected expression after '-'"))

            next_token = self.token[self.position]
            if next_token[1] == "NUMBER":
                self.position += 1
                return f"-{next_token[0]}"
            else:
                expr = self.parse_primary()
                return f"-({expr})"

        if key_token == "NUMBER":
            self.position += 1
            return value_token

        elif key_token == "STRING":
            self.position += 1
            return f'"{value_token}"'

        elif key_token == "BOOL":
            self.position += 1
            return value_token

        elif key_token == "NUM_CONVERT":
            return self.parse_type_conversion("int")

        elif key_token == "DEC_CONVERT":
            return self.parse_type_conversion("float")

        elif key_token == "WORD_CONVERT":
            return self.parse_type_conversion("str")

        elif key_token == "BOOL_CONVERT":
            return self.parse_type_conversion("bool")

        elif key_token == "IN":
            self.position += 1
            if self.position >= len(self.token) or self.token[self.position][1] != "LPAREN":
                raise SyntaxError(self.error(f"Expected '(' after 'in'"))
            self.position += 1

            next_token = self.token[self.position]
            if next_token[1] == "RPAREN":
                self.position += 1
                return "input()"
            elif next_token[1] == "STRING":
                prompt = f'"{next_token[0]}"'
                self.position += 1
                if self.position >= len(self.token) or self.token[self.position][1] != "RPAREN":
                    raise SyntaxError(self.error(f"Expected ')' after prompt string in 'in()'"))
                self.position += 1
                return f"input({prompt})"
            else:
                raise SyntaxError(self.error(f"Expected ')' or prompt string in 'in()', got '{next_token[0]}'"))

        elif key_token == "IDENTIFIER":
            if self.position + 1 < len(self.token) and self.token[self.position + 1][1] == "LPAREN":
                return self.parse_function_call()
            else:
                if (value_token not in self.symbols and
                        value_token not in self.current_params and
                        value_token not in self.functions):
                    raise NameError(self.error(f"Variable '{value_token}' is not defined", "Name Error"))
                self.position += 1
                return value_token

        elif key_token == "LPAREN":
            self.position += 1
            expr = self.parse_additive()

            if self.position >= len(self.token) or self.token[self.position][1] != "RPAREN":
                raise SyntaxError(self.error("Expected ')' to close expression"))
            self.position += 1
            return f"({expr})"

        else:
            raise SyntaxError(self.error(f"Unexpected token '{value_token}' in expression"))

    def parse_type_conversion(self, conversion_type):
        self.position += 1

        if self.position >= len(self.token) or self.token[self.position][1] != "LPAREN":
            raise SyntaxError(
                self.error(f"Expected '(' after type conversion '{conversion_type}', got '{self.token[self.position][0] if self.position < len(self.token) else 'EOL'}'"))
        self.position += 1

        arg = self.expression()

        if self.position >= len(self.token) or self.token[self.position][1] != "RPAREN":
            raise SyntaxError(
                self.error(f"Expected ')' to close type conversion '{conversion_type}', got '{self.token[self.position][0] if self.position < len(self.token) else 'EOL'}'"))
        self.position += 1

        return f"{conversion_type}({arg})"

    def parse_function_call(self):
        func_name = self.token[self.position][0]

        if func_name not in self.functions:
            raise NameError(self.error(f"Function '{func_name}' is not defined", "Name Error"))

        self.position += 1

        if self.position >= len(self.token) or self.token[self.position][1] != "LPAREN":
            raise SyntaxError(
                self.error(f"Expected '(' after function name '{func_name}', got '{self.token[self.position][0]}'"))
        self.position += 1

        args = []

        while self.position < len(self.token) and self.token[self.position][1] != "RPAREN":
            arg_expr = self.expression()
            args.append(arg_expr)

            if self.position < len(self.token) and self.token[self.position][1] == "COMMA":
                self.position += 1
            elif self.position < len(self.token) and self.token[self.position][1] != "RPAREN":
                raise SyntaxError(
                    self.error(f"Expected ',' or ')' in function call '{func_name}', got '{self.token[self.position][0]}'"))

        if self.position >= len(self.token) or self.token[self.position][1] != "RPAREN":
            raise SyntaxError(self.error(f"Expected ')' to close function call '{func_name}'"))
        self.position += 1

        return f"{func_name}({', '.join(args)})"

    def unknown_token(self, current_token):
        raise SyntaxError(self.error(f"Unexpected token '{current_token[0]}' of type '{current_token[1]}'"))