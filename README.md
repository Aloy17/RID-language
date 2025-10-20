# RID Programming Language

A simple, intuitive programming language with Hindi-inspired syntax, built from scratch in Python.

## What is RID?

RID is a custom programming language that makes coding more accessible by using familiar Hindi words for control structures. It transpiles to Python, which means your RID code is converted to Python and executed immediately.

## Features

- Simple syntax perfect for beginners
- Hindi-inspired keywords (`agar` for if, `warna` for else, `Run` for loops)
- Variables with support for numbers in names (`var1`, `count2`)
- Functions with recursion support
- Loops (fixed-count and while)
- Conditionals (if/elif/else)
- String concatenation
- Negative numbers
- **Type conversion functions** (`num()`, `dec()`, `word()`, `bool()`)
- Transpiles to Python for fast execution
- Clear error messages to help you learn

## Installation

Download **RIDLEY IDE** from [https://github.com/Aloy17/RIDLEY](https://github.com/Aloy17/RIDLEY)

No additional installation needed - RIDLEY is a standalone application with everything built-in.

## Using RIDLEY IDE

**RIDLEY IDE** is the dedicated desktop IDE for writing and running RID programs.

**✨ No Installation Required!** RIDLEY IDE is a **standalone application** - just download and run. No Python, no dependencies, no setup. Everything you need is built right in.

**Features:**
- Syntax highlighting for RID code
- Built-in code editor with line numbers
- Run RID programs directly from the IDE
- Interactive tutorials and lessons to learn RID
- Clean, modern interface with Quiet Light and Dark Modern themes
- File management for RID projects
- RID interpreter built-in - no external tools needed

**Get RIDLEY IDE:**
- Download from: [https://github.com/Aloy17/RIDLEY](https://github.com/Aloy17/RIDLEY)
- **Available for Windows** (macOS and Linux support coming soon)
- Completely portable and ready to use

## Usage

**To run RID programs, use RIDLEY IDE:**

1. Download and open RIDLEY IDE
2. Create a new `.rid` file or open an existing one
3. Write your RID code
4. Click the Run button to execute your program

**That's it!** RIDLEY handles everything - editing, running, and debugging your RID code.

## Quick Example

Create a new file in RIDLEY IDE and type:

```rid
Let name = "World"
out("Hello, " + name)
line
```

Click the Run button in RIDLEY IDE to see the output:
```
Hello, World!
```

## Basic Syntax

### Variables
```rid
Let x = 10
Let name = "Alice"
Let num1 = 5        ~ Numbers in variable names are allowed ~
x = 20              ~ Reassigning ~
```

### Output
```rid
out("Hello!")       ~ Prints without newline ~
out(x)
line                ~ Prints a newline ~

~ You can also concatenate strings ~
out("Hello, " + name)
line
```

The `out()` function prints without adding a newline. Use `line` to print a newline when needed. You can concatenate strings and variables using the `+` operator.

### Input
```rid
Let name = ""
name = in("Enter your name: ")
out("Hello, " + name)
line
```

### Arithmetic
```rid
Let a = 10
Let b = 3
Let sum = a + b      ~ Addition ~
Let diff = a - b     ~ Subtraction ~
Let prod = a * b     ~ Multiplication ~
Let quot = a / b     ~ Division ~
Let mod = a % b      ~ Modulo ~
Let neg = -5         ~ Negative numbers ~
```

### String Operations
```rid
Let first = "Hello"
Let second = "World"
Let greeting = first + " " + second  ~ String concatenation ~
out(greeting)  ~ Prints: Hello World ~

~ You can mix strings and variables ~
Let age = 25
out("I am " + word(age) + " years old")
line

~ Note: Use word() to convert numbers to strings for concatenation ~
```

### Type Conversions
```rid
~ Convert string to number ~
Let str_num = "42"
Let number = num(str_num)
out(number)  ~ Prints: 42 ~

~ Convert to decimal/float ~
Let str_dec = "3.14"
Let decimal = dec(str_dec)
out(decimal)  ~ Prints: 3.14 ~

~ Convert to string ~
Let value = 100
Let text = word(value)
out(text)  ~ Prints: 100 ~

~ Convert to boolean ~
Let zero = 0
Let one = 1
out(bool(zero))  ~ Prints: False ~
out(bool(one))   ~ Prints: True ~

~ Useful with user input ~
Let user_input = ""
user_input = in("Enter a number: ")
Let squared = num(user_input) * num(user_input)
out("Result: " + word(squared))
line
```

### If-Else (Conditionals)
```rid
Let x = 15

agar(x > 10) {
    out("x is large")
}
ya_fir(x > 5) {
    out("x is medium")
}
warna {
    out("x is small")
}
```

### Loops

**Fixed-count loop:**
```rid
Run(5) {
    out("Hello!")
    line
}
```

**While loop:**
```rid
Let i = 0
Run while(i < 5) {
    out(i)
    line
    i = i + 1
}
```

### Functions
```rid
func add(a, b) {
    give a + b
}

Let result = add(5, 3)
out(result)  ~ Prints: 8 ~
```

**Recursion is supported:**
```rid
func factorial(n) {
    agar(n <= 1) {
        give 1
    }
    warna {
        give n * factorial(n - 1)
    }
}

Let result = factorial(5)
out(result)  ~ Prints: 120 ~
```

### Comments
```rid
~ This is a comment ~
Let x = 10  ~ Inline comments work too ~
```

## Language Keywords

| Keyword | Meaning | Example |
|---------|---------|---------|
| `Let` | Declare variable | `Let x = 10` |
| `out` | Print output (no newline) | `out("Hello")` |
| `line` | Print newline | `line` |
| `in` | Get input | `name = in("Prompt: ")` |
| `Run` | Loop | `Run(5) { }` |
| `while` | While loop modifier | `Run while(x < 10) { }` |
| `agar` | If | `agar(x > 0) { }` |
| `ya_fir` | Else if | `ya_fir(x < 0) { }` |
| `warna` | Else | `warna { }` |
| `func` | Define function | `func add(a, b) { }` |
| `give` | Return from function | `give x + y` |
| `True` | Boolean true | `Let flag = True` |
| `False` | Boolean false | `Let flag = False` |
| `num` | Convert to integer | `num("42")` |
| `dec` | Convert to decimal | `dec("3.14")` |
| `word` | Convert to string | `word(100)` |
| `bool` | Convert to boolean | `bool(1)` |

## Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition / String concatenation | `5 + 3`, `"Hi" + " there"` |
| `-` | Subtraction / Unary minus | `10 - 3`, `-5` |
| `*` | Multiplication | `4 * 7` |
| `/` | Division | `10 / 2` |
| `%` | Modulo | `10 % 3` |
| `==` | Equal to | `x == 5` |
| `!=` | Not equal to | `x != 5` |
| `<` | Less than | `x < 10` |
| `>` | Greater than | `x > 10` |
| `<=` | Less than or equal | `x <= 10` |
| `>=` | Greater than or equal | `x >= 10` |

## Example Programs

Check the `examples/` folder in this repository for complete working programs:

- **hello_world.rid** - Basic output
- **calculator.rid** - Arithmetic operations
- **conditionals.rid** - If/elif/else examples
- **loops.rid** - Fixed and while loops
- **functions.rid** - Function definitions and calls
- **fibonacci.rid** - Fibonacci sequence generator
- **factorial.rid** - Factorial with recursion
- **guess_the_number.rid** - Interactive guessing game
- **type_conversion_test.rid** - Type conversion examples

Open any example in RIDLEY IDE and click Run to see it in action!

## Project Structure

```
RID-language/
├── lexer.py           # Tokenizes RID code into tokens
├── parser.py          # Parses tokens and transpiles to Python
├── main.py            # Backend transpiler (used by RIDLEY IDE)
├── language_spec.md   # Formal grammar specification
├── LICENSE            # MIT License
├── README.md          # This file
└── examples/          # Example RID programs
    ├── README.md
    ├── hello_world.rid
    ├── calculator.rid
    ├── conditionals.rid
    ├── loops.rid
    ├── functions.rid
    ├── fibonacci.rid
    ├── factorial.rid
    ├── guess_the_number.rid
    └── type_conversion_test.rid
```

**Note:** The Python files in this repository are the backend transpiler used by RIDLEY IDE. To run RID programs, use RIDLEY IDE.

## Documentation

- **[Language Specification](language_spec.md)** - Complete formal grammar with examples
- **[Examples](examples/)** - Working RID programs demonstrating all features
- **[License](LICENSE)** - MIT License details

## How It Works

1. **Write Code** in RIDLEY IDE's editor
2. **Click Run** to execute
3. **Lexer** (`lexer.py`) - Converts RID source code into tokens
4. **Parser** (`parser.py`) - Parses tokens, validates syntax, and transpiles to Python
5. **Execution** - Runs the generated Python code and displays output

```
RID Code (in RIDLEY) → Lexer → Tokens → Parser → Python Code → Execute → Output
```

## Known Limitations

- No arrays/lists yet
- No logical operators (`and`, `or`, `not`) yet
- No `break`/`continue` in loops
- No import/module system

## License

MIT License - Copyright (c) 2025 Ryane Bose

See [LICENSE](LICENSE) file for details.

## Author

**Ryane Bose**

Created as a learning project to explore:
- Compiler design
- Language development
- Lexical analysis and parsing
- Python programming

---

## Support

If you find a bug or have a question, feel free to open an issue on GitHub.

---

**Happy Coding with RID!**