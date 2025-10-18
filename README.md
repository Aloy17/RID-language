# RID Programming Language

A simple, intuitive programming language with Hindi-inspired syntax, built from scratch in Python.

## What is RID?

RID is a custom programming language that makes coding more accessible by using familiar Hindi words for control structures. It transpiles to Python, which means your RID code is converted to Python and executed immediately.

## Features

- Simple syntax perfect for beginners
- Hindi-inspired keywords (`agar` for if, `warna` for else, `Run` for loops)
- Variables, functions, loops, and conditionals
- Transpiles to Python for fast execution
- Clear error messages to help you learn

## Installation

**Requirements:** Python 3.7 or higher

1. Clone this repository:
```bash
git clone https://github.com/yourusername/RID-language.git
cd RID-language
```

2. That's it! No dependencies needed.

## Quick Example

Create a file `hello.rid`:

```rid
Let name = "World"
out("Hello, ")
out(name)
```

Run it:

```bash
python main.py hello.rid
```

Output:
```
Hello, World!
```

## Basic Syntax

### Variables
```rid
Let x = 10
Let name = "Alice"
x = 20  ~ Reassigning ~
```

### Output
```rid
out("Hello!")
out(x)
```

### Input
```rid
Let name = ""
name = in("Enter your name: ")
```

### If-Else (Conditionals)
```rid
agar(x > 10) {
    out("x is large")
}
warna {
    out("x is small")
}
```

### Loops
```rid
~ Fixed count ~
Run(5) {
    out("Hello!")
}

~ While loop ~
Let i = 0
Run while(i < 5) {
    out(i)
    i = i + 1
}
```

### Functions
```rid
func add(a, b) {
    give a + b
}

Let result = add(5, 3)
out(result)
```

### Comments
```rid
~ This is a comment ~
```

## Usage

```bash
python main.py <input_file.rid> [output_file.py]
```

**Examples:**

Run a RID file:
```bash
python main.py myprogram.rid
```

Specify output file name:
```bash
python main.py myprogram.rid output.py
```

## Language Keywords

| Keyword | Meaning | Example |
|---------|---------|---------|
| `Let` | Declare variable | `Let x = 10` |
| `out` | Print output | `out("Hello")` |
| `in` | Get input | `name = in()` |
| `Run` | Loop | `Run(5) { }` |
| `while` | While loop | `Run while(x < 10) { }` |
| `agar` | If | `agar(x > 0) { }` |
| `ya_fir` | Else if | `ya_fir(x < 0) { }` |
| `warna` | Else | `warna { }` |
| `func` | Define function | `func add(a, b) { }` |
| `give` | Return | `give x + y` |

## More Examples

Check the `examples/` folder for complete programs including:
- Calculator
- Factorial calculator
- Guessing game
- And more!

## Project Structure

```
RID-language/
├── lexer.py           # Tokenizes RID code
├── parser.py          # Parses and transpiles to Python
├── main.py            # Main entry point
├── language_spec.md   # Formal grammar specification
└── README.md          # This file
```

## Documentation

- **[Language Specification](language_spec.md)** - Formal grammar rules
- **Examples** - See the `examples/` folder (coming soon)

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## License

MIT License - feel free to use this project for learning and development.

## Author

Created as a learning project to explore compiler design and language development.

---

**Questions?** Open an issue on GitHub!

**Want to learn more?** Check out the language specification and examples.
