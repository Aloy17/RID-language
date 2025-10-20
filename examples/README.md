# RID Example Programs

This folder contains example programs demonstrating various features of the RID programming language.

## How to Run Examples

From the main RID-language directory:

```bash
python main.py examples/hello_world.rid
```

Or specify an output file:

```bash
python main.py examples/calculator.rid output.py
```

## Available Examples

### 1. hello_world.rid
**Difficulty:** Beginner  
**Concepts:** Output, strings  
**Description:** The classic "Hello, World!" program. Shows basic output functionality.

```bash
python main.py examples/hello_world.rid
```

---

### 2. calculator.rid
**Difficulty:** Beginner  
**Concepts:** Variables, arithmetic operators  
**Description:** Demonstrates all arithmetic operations (+, -, *, /, %)

```bash
python main.py examples/calculator.rid
```

---

### 3. conditionals.rid
**Difficulty:** Beginner  
**Concepts:** agar (if), ya_fir (elif), warna (else)  
**Description:** Shows how to use conditional statements for decision making.

```bash
python main.py examples/conditionals.rid
```

---

### 4. loops.rid
**Difficulty:** Beginner  
**Concepts:** Run (fixed-count), Run while (conditional loop)  
**Description:** Demonstrates both types of loops with practical examples.

```bash
python main.py examples/loops.rid
```

---

### 5. functions.rid
**Difficulty:** Intermediate  
**Concepts:** func, give (return), function calls  
**Description:** Shows how to define and call functions with parameters.

```bash
python main.py examples/functions.rid
```

---

### 6. fibonacci.rid
**Difficulty:** Intermediate  
**Concepts:** Loops, variables, arithmetic  
**Description:** Generates the first 10 Fibonacci numbers using a while loop.

```bash
python main.py examples/fibonacci.rid
```

---

### 7. factorial.rid
**Difficulty:** Intermediate  
**Concepts:** Functions, recursion, conditionals  
**Description:** Calculates factorial using recursive function calls.

```bash
python main.py examples/factorial.rid
```

---

### 8. guess_the_number.rid
**Difficulty:** Intermediate  
**Concepts:** Input, conditionals, variables  
**Description:** Interactive number guessing game with user input.

```bash
python main.py examples/guess_the_number.rid
```

---

### 9. type_conversion_test.rid
**Difficulty:** Intermediate  
**Concepts:** Type conversions (num, dec, word, bool), input, expressions  
**Description:** Demonstrates all type conversion functions with practical examples.

```bash
python main.py examples/type_conversion_test.rid
```

**Features demonstrated:**
- `num()` - Convert strings to integers
- `dec()` - Convert to decimal/float values
- `word()` - Convert numbers to strings
- `bool()` - Convert values to boolean
- Using conversions with user input
- Type conversions in arithmetic expressions

---

## Learning Path

**Recommended order for beginners:**

1. Start with `hello_world.rid` to understand output
2. Try `calculator.rid` for variables and arithmetic
3. Learn `conditionals.rid` for decision making
4. Practice `loops.rid` for iteration
5. Move to `functions.rid` for code organization
6. Challenge yourself with `fibonacci.rid` and `factorial.rid`
7. Explore `type_conversion_test.rid` for working with different data types
8. Build something fun with `guess_the_number.rid`

## Creating Your Own Programs

Use these examples as templates for your own RID programs. Key tips:

- Always declare variables with `Let` before use
- Use `line` to print newlines after `out()` statements
- Remember Hindi-inspired keywords: `agar`, `ya_fir`, `warna`
- Use type conversion functions when working with user input
- Functions must use `give` to return values

Happy coding in RID!
