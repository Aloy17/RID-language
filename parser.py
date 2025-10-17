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
            "IN": self.input_stmt,
            "RUN": self.loop_stmt,
            "IF": self.conditional_stmt,
            "ELIF": self.conditional_stmt,
            "ELSE": self.conditional_stmt,
            "FUNC": self.func_def,
            "RETURN": self.return_stmt
        }


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
            raise SyntaxError(f"Syntax Error: Expected variable name after 'Let', got '{var_token[0]}'")

        var_name = var_token[0]
        self.position += 1

        if self.token[self.position][1] != "ASSIGN":
            raise SyntaxError(f"Syntax Error: Expected '=' after variable '{var_name}', got '{self.token[self.position][0]}'")

        self.position += 1
        expr = self.expression(self.token[self.position])

        self.output.append(f"{var_name} = {expr.strip()}")
        self.symbols[var_name] = expr


    def assignment(self, current_token):
        var_name = current_token[0]

        if var_name not in self.symbols:
            raise NameError(f"Name Error: Variable '{var_name}' is not defined. Use 'Let {var_name} = ...' to declare it first")

        self.position += 1
        if self.token[self.position][1] != "ASSIGN":
            raise SyntaxError(f"Syntax Error: Expected '=' after variable '{var_name}', got '{self.token[self.position][0]}'")

        self.position += 1
        expr = self.expression(self.token[self.position])

        self.symbols[var_name] = expr
        self.output.append(f"{var_name} = {expr.strip()}")


    def print_stmt(self, current_token):
        self.position += 1
        if self.token[self.position][1] != "LPAREN":
            raise SyntaxError(f"Syntax Error: Expected '(' after 'out', got '{self.token[self.position][0]}'")
        self.position += 1

        value = self.expression(self.token[self.position])

        if self.token[self.position][1] != "RPAREN":
            raise SyntaxError(f"Syntax Error: Expected ')' to close 'out' statement, got '{self.token[self.position][0]}'")
        self.position += 1
        self.output.append(f"print({value})")


    def input_stmt(self, current_token):
        self.position += 1
        if self.token[self.position][1] != "IDENTIFIER":
            raise SyntaxError(f"Syntax Error: Expected variable name after 'in', got '{self.token[self.position][0]}'")
        var_name = self.token[self.position][0]

        if var_name not in self.symbols:
            raise NameError(f"Name Error: Variable '{var_name}' is not defined. Declare it with 'Let {var_name} = ...' before using 'in'")

        self.position += 1

        if self.token[self.position][1] != "LPAREN":
            raise SyntaxError(f"Syntax Error: Expected '(' after variable name in 'in' statement, got '{self.token[self.position][0]}'")

        self.position += 1
        next_token = self.token[self.position]

        if next_token[1] == "RPAREN":
            self.output.append(f"{var_name} = input()")
            self.position += 1

        elif next_token[1] == "STRING":
            prompt = f'"{next_token[0]}"'
            self.position += 1

            if self.token[self.position][1] != "RPAREN":
                raise SyntaxError(f"Syntax Error: Expected ')' after prompt string in 'in' statement, got '{self.token[self.position][0]}'")
            self.output.append(f"{var_name} = input({prompt})")
            self.position += 1

        else:
            raise SyntaxError(f"Syntax Error: Expected ')' or prompt string in 'in' statement, got '{next_token[0]}'")


    def loop_stmt(self, current_token):

        if current_token[1] != "RUN":
            raise SyntaxError(f"Syntax Error: Expected 'Run' keyword, got '{current_token[0]}'")
        self.position += 1
        next_token = self.token[self.position]

        if next_token[1] == "LPAREN":
            self.position += 1
            num_token = self.token[self.position]

            if num_token[1] != "NUMBER":
                raise TypeError(f"Type Error: Expected numeric value inside 'Run()', got '{num_token[0]}'")
            loop_template = f"for _ in range({num_token[0]}):"
            self.position += 1

            if self.token[self.position][1] != "RPAREN":
                raise SyntaxError(f"Syntax Error: Expected ')' after loop count, got '{self.token[self.position][0]}'")
            self.position += 1

            if self.token[self.position][1] != "LBRACE":
                raise SyntaxError(f"Syntax Error: Expected '{{' to begin loop block, got '{self.token[self.position][0]}'")
            self.position += 1

            block_lines = self.block(current_token)
            self.output.append(loop_template)
            self.output.extend(["    " + line for line in block_lines])

        elif next_token[1] == "WHILE":
            self.position += 1

            if self.token[self.position][1] != "LPAREN":
                raise SyntaxError(f"Syntax Error: Expected '(' after 'while', got '{self.token[self.position][0]}'")
            self.position += 1
            cond_str = self.condition(self.token[self.position])

            if self.token[self.position][1] != "RPAREN":
                raise SyntaxError(f"Syntax Error: Expected ')' after while condition, got '{self.token[self.position][0]}'")
            self.position += 1

            if self.token[self.position][1] != "LBRACE":
                raise SyntaxError(f"Syntax Error: Expected '{{' to begin while loop block, got '{self.token[self.position][0]}'")
            self.position += 1
            block_lines = self.block(current_token)

            self.output.append(f"while {cond_str}:")
            self.output.extend(["    " + line for line in block_lines])

        else:
            raise SyntaxError(f"Syntax Error: Expected '(' or 'while' after 'Run', got '{next_token[0]}'")


    def conditional_stmt(self, current_token):

        keyword = current_token[1]
        if keyword not in ("IF", "ELIF", "ELSE"):
            raise SyntaxError(f"Syntax Error: Expected conditional keyword (agar/ya_fir/warna), got '{current_token[0]}'")
        self.position += 1

        cond_str = ""
        if keyword in ("IF", "ELIF"):

            if self.token[self.position][1] != "LPAREN":
                raise SyntaxError(f"Syntax Error: Expected '(' after '{current_token[0]}', got '{self.token[self.position][0]}'")
            self.position += 1
            cond_str = self.condition(self.token[self.position])

            if self.token[self.position][1] != "RPAREN":
                raise SyntaxError(f"Syntax Error: Expected ')' after condition, got '{self.token[self.position][0]}'")
            self.position += 1

        if self.token[self.position][1] != "LBRACE":
            raise SyntaxError(f"Syntax Error: Expected '{{' to begin conditional block, got '{self.token[self.position][0]}'")
        self.position += 1
        block_lines = self.block(current_token)

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
            raise SyntaxError(f"Syntax Error: Expected 'func' keyword, got '{current_token[0]}'")
        self.position += 1

        func_name = self.token[self.position][0]
        self.position += 1

        if self.token[self.position][1] != "LPAREN":
            raise SyntaxError(f"Syntax Error: Expected '(' after function name '{func_name}', got '{self.token[self.position][0]}'")
        self.position += 1
        parameters = []

        while self.token[self.position][1] != "RPAREN":

            if self.token[self.position][1] == "IDENTIFIER":
                parameters.append(self.token[self.position][0])
                self.position += 1

            elif self.token[self.position][0] == ",":
                self.position += 1

            else:
                raise SyntaxError(f"Syntax Error: Invalid token in function parameters, expected parameter name or ',', got '{self.token[self.position][0]}'")
        self.position += 1

        if self.token[self.position][1] != "LBRACE":
            raise SyntaxError(f"Syntax Error: Expected '{{' to begin function body, got '{self.token[self.position][0]}'")
        self.position += 1
        self.current_params = parameters

        block_lines = self.block(current_token)
        params = ",".join(parameters)
        self.output.append(f"def {func_name}({params}):")
        self.output.extend(["    " + line for line in block_lines])
        self.functions[func_name] = {"params": parameters, "body": block_lines}
        self.current_params = []


    def block(self, current_token):
        block_lines = []

        while self.position < len(self.token) and self.token[self.position][1] != "RBRACE":
            current_token = self.token[self.position]
            token_type = current_token[1]

            if token_type == "IDENTIFIER":

                if self.position + 1 < len(self.token) and self.token[self.position + 1][1] == "LPAREN":
                    handler = self.func_call
                else:
                    handler = self.assignment

            else:
                handler = self.handlers.get(token_type, self.unknown_token)

            old_output = self.output
            self.output = []
            handler(current_token)
            block_lines.extend(self.output)
            self.output = old_output

        if self.position < len(self.token) and self.token[self.position][1] == "RBRACE":
            self.position += 1

        if len(block_lines) == 0:
            block_lines.append("pass")

        return block_lines


    def condition(self, current_token):

        lhs = self.expression(self.token[self.position])
        op_token = self.token[self.position]
        op_map = {"EQ": "==", "NEQ": "!=", "LT": "<", "GT": ">", "LTE": "<=", "GTE": ">="}

        if op_token[1] not in op_map:
            raise SyntaxError(f"Syntax Error: Invalid comparison operator, expected one of (==, !=, <, >, <=, >=), got '{op_token[0]}'")
        op = op_map[op_token[1]]
        self.position += 1

        rhs = self.expression(self.token[self.position])

        return f"{lhs} {op} {rhs}"

    def func_call(self, current_token):
        func_name = current_token[0]

        if func_name not in self.functions:
            raise NameError(f"Name Error: Function '{func_name}' is not defined")
        self.position += 1

        if self.token[self.position][1] != "LPAREN":
            raise SyntaxError(f"Syntax Error: Expected '(' after function name '{func_name}', got '{self.token[self.position][0]}'")
        self.position += 1
        args = []

        while self.position < len(self.token) and self.token[self.position][1] != "RPAREN":
            arg_token = self.token[self.position]

            if arg_token[1] in ("NUMBER", "BOOL"):
                args.append(str(arg_token[0]))

            elif arg_token[1] == "STRING":
                args.append(f'"{arg_token[0]}"')

            elif arg_token[1] == "IDENTIFIER":

                if arg_token[0] in self.symbols or arg_token[0] in self.current_params:
                    args.append(arg_token[0])
                else:
                    raise NameError(f"Name Error: Variable '{arg_token[0]}' is not defined")

            else:
                raise TypeError(f"Type Error: Unsupported argument type '{arg_token[1]}' in function call")
            self.position += 1

            if self.position < len(self.token) and self.token[self.position][1] != "RPAREN":

                if self.token[self.position][0] != ",":
                    raise SyntaxError(f"Syntax Error: Expected ',' between function arguments, got '{self.token[self.position][0]}'")
                self.position += 1

                if self.position < len(self.token) and self.token[self.position][1] == "RPAREN":
                    raise SyntaxError(f"Syntax Error: Trailing comma not allowed in function call '{func_name}'")

        if self.position >= len(self.token) or self.token[self.position][1] != "RPAREN":
            raise SyntaxError(f"Syntax Error: Expected ')' to close function call '{func_name}'")
        self.position += 1
        call_str = f"{func_name}({', '.join(args)})"
        self.output.append(call_str)


    def return_stmt(self, current_token):

        if current_token[1] != "RETURN":
            raise SyntaxError(f"Syntax Error: Expected 'give' keyword for return statement, got '{current_token[0]}'")
        self.position += 1

        expr = self.expression(self.token[self.position])

        self.output.append(f"return {expr}")


    def expression(self, current_token):
        return self.parse_additive()

    def parse_additive(self):
        left = self.parse_multiplicative()

        while self.position < len(self.token) and self.token[self.position][1] in ("PLUS", "MINUS"):
            op = self.token[self.position][0]
            self.position += 1
            right = self.parse_multiplicative()
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
            raise SyntaxError("Syntax Error: Unexpected end of expression")

        current = self.token[self.position]
        value_token, key_token = current

        if key_token == "NUMBER":
            self.position += 1
            return value_token

        elif key_token == "STRING":
            self.position += 1
            return f'"{value_token}"'

        elif key_token == "BOOL":
            self.position += 1
            return value_token

        elif key_token == "IDENTIFIER":

            if self.position + 1 < len(self.token) and self.token[self.position + 1][1] == "LPAREN":
                return self.parse_function_call()

            else:
                if value_token not in self.symbols and value_token not in self.current_params:
                    raise NameError(f"Name Error: Variable '{value_token}' is not defined")
                self.position += 1
                return value_token

        elif key_token == "LPAREN":
            self.position += 1
            expr = self.parse_additive()

            if self.position >= len(self.token) or self.token[self.position][1] != "RPAREN":
                raise SyntaxError("Syntax Error: Expected ')' to close expression")
            self.position += 1
            return f"({expr})"

        else:
            raise SyntaxError(f"Syntax Error: Unexpected token '{value_token}' in expression")

    def parse_function_call(self):
        func_name = self.token[self.position][0]

        if func_name not in self.functions:
            raise NameError(f"Name Error: Function '{func_name}' is not defined")
        self.position += 1

        if self.token[self.position][1] != "LPAREN":
            raise SyntaxError(f"Syntax Error: Expected '(' after function name '{func_name}', got '{self.token[self.position][0]}'")
        self.position += 1

        args = []

        while self.position < len(self.token) and self.token[self.position][1] != "RPAREN":
            arg_expr = self.parse_additive()
            args.append(arg_expr)

            if self.position < len(self.token) and self.token[self.position][1] != "RPAREN":
                if self.token[self.position][0] != ",":
                    raise SyntaxError(f"Syntax Error: Expected ',' between function arguments in '{func_name}', got '{self.token[self.position][0]}'")
                self.position += 1
                if self.position < len(self.token) and self.token[self.position][1] == "RPAREN":
                    raise SyntaxError(f"Syntax Error: Trailing comma not allowed in function call '{func_name}'")

        if self.position >= len(self.token) or self.token[self.position][1] != "RPAREN":
            raise SyntaxError(f"Syntax Error: Expected ')' to close function call '{func_name}'")
        self.position += 1

        return f"{func_name}({', '.join(args)})"


    def unknown_token(self, current_token):
        raise SyntaxError(f"Syntax Error: Unexpected token '{current_token[0]}' of type '{current_token[1]}'")