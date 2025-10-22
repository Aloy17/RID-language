
<div align="center">

# RID Programming Language

A simple, intuitive programming language with Hindi-inspired syntax, built from scratch in Python.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: Cross-Platform](https://img.shields.io/badge/Platform-Cross--Platform-blue.svg)]()
[![Built with Python](https://img.shields.io/badge/Built%20with-Python-3776AB.svg)](https://www.python.org)

</div>

---

## Overview

**RID** is a beginner-friendly programming language that uses familiar Hindi-style keywords to make programming more accessible.  
It **transpiles to Python**, meaning RID code is converted to Python internally and executed immediately.

Use the dedicated **[RIDLEY IDE](https://github.com/Aloy17/RIDLEY)** to write, run, and manage RID programs with no setup required.

---

## Key Features

- Simple, readable syntax for beginners  
- Hindi-inspired control keywords (`agar`, `warna`, `Run`)  
- Variables, conditionals, and loops
- String concatenation  
- Functions with recursion support  
- Type-conversion utilities (`num()`, `dec()`, `word()`, `bool()`)  
- Clear, human-readable error messages  
- Fully integrated into RIDLEY IDE
  

---

## Installation

RID runs directly inside **RIDLEY IDE** — no Python or manual setup needed.

Download the IDE from the official repository:   [RIDLEY IDE on GitHub](https://github.com/Aloy17/RIDLEY)

---

## Quick Example

```rid
Let name = "World"
out("Hello, " + name)
line
````

Output:

```
Hello, World!
```

---

## Syntax Reference

### Variables

```rid
Let x = 10
Let name = "Alice"
x = 20
```

### Input and Output

```rid
Let name = in("Enter your name: ")
out("Hello, " + name)
line
```

### Conditionals

```rid
agar(x > 10) {
    out("Large")
}
ya_fir(x > 5) {
    out("Medium")
}
warna {
    out("Small")
}
```

### Loops

```rid
Run(5) {
    out("Hello")
    line
}

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

Let result = add(3, 4)
out(result)
line
```

### Comments

```rid
~ This is a comment ~
```

---

## Reserved Keywords

| Keyword  | Meaning                   | Example                 |
| -------- | ------------------------- | ----------------------- |
| `Let`    | Declare variable          | `Let x = 10`            |
| `out`    | Print output (no newline) | `out("Text")`           |
| `line`   | Print newline             | `line`                  |
| `in`     | Get user input            | `name = in("Prompt: ")` |
| `Run`    | Loop                      | `Run(5) { }`            |
| `while`  | While loop modifier       | `Run while(x < 5) { }`  |
| `agar`   | If                        | `agar(x > 0) { }`       |
| `ya_fir` | Else-if                   | `ya_fir(x < 0) { }`     |
| `warna`  | Else                      | `warna { }`             |
| `func`   | Define function           | `func add(a, b) { }`    |
| `give`   | Return value              | `give a + b`            |
| `True`   | Boolean true              | `Let flag = True`       |
| `False`  | Boolean false             | `Let flag = False`      |
| `num`    | Convert to integer        | `num("42")`             |
| `dec`    | Convert to decimal        | `dec("3.14")`           |
| `word`   | Convert to string         | `word(100)`             |
| `bool`   | Convert to boolean        | `bool(1)`               |

---

## Operators

| Operator             | Description              | Example            |
| -------------------- | ------------------------ | ------------------ |
| `+`                  | Addition / Concatenation | `"Hi" + name`      |
| `-`                  | Subtraction / Negation   | `a - b`, `-5`      |
| `*`                  | Multiplication           | `a * b`            |
| `/`                  | Division                 | `a / b`            |
| `%`                  | Modulo                   | `a % b`            |
| `==`, `!=`           | Equality / Inequality    | `x == 5`, `x != 5` |
| `<`, `>`, `<=`, `>=` | Comparisons              | `x < 10`           |

---

## Example Programs

Explore the [`examples/`](examples/) directory for complete demos:

* `hello_world.rid`
* `calculator.rid`
* `conditionals.rid`
* `loops.rid`
* `functions.rid`
* `fibonacci.rid`
* `factorial.rid`
* `guess_the_number.rid`

All examples can be opened directly in **RIDLEY IDE**.

---

## Internal Architecture

```
RID Code → Lexer → Tokens → Parser → Python Code → Execution → Output
```

Core modules:

* `lexer.py` – Tokenizes RID source
* `parser.py` – Builds syntax tree and transpiles to Python
* `main.py` – Backend interface for RIDLEY IDE

---

## License

MIT License © 2025 **Ryane Bose**
See [`LICENSE`](LICENSE) for details.

---

## Related Project

**RIDLEY IDE** – the official desktop environment for RID
Repository: [https://github.com/Aloy17/RIDLEY](https://github.com/Aloy17/RIDLEY)

---

## Author
Created as a learning project to explore compiler design, parsing, and programming-language development.

---

## Support

Report issues or suggest improvements via GitHub Issues.

---


