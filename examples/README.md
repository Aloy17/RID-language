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

### 8. guessing_game.rid
**Difficulty:** Intermediate  
**Concepts:** Input, conditionals, variables  
**Description:** Interactive number guessing game with user input.

```bash
python main.py examples/guessing_game.rid
```

---

## Learning Path

If you're new to RID, we recommend following this order:

1. **hello_world.rid** - Get familiar with output
2. **calculator.rid** - Learn variables and operators
3. **conditionals.rid** - Understand decision making
4. **loops.rid** - Master repetition
5. **functions.rid** - Write reusable code
6. **fibonacci.rid** - Apply loops to algorithms
7. **factorial.rid** - Explore recursion
8. **guessing_game.rid** - Build interactive programs

## Example Output

### hello_world.rid
```
Hello, World!
Welcome to RID Programming Language!
```

### calculator.rid
```
Number 1: 10
Number 2: 3

Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333333335
Modulo: 1
```

### fibonacci.rid
```
Fibonacci Sequence:
0
1
1
2
3
5
8
13
21
34
```

## Tips

- Read the comments in each file (between `~` symbols)
- Try modifying the values and see what happens
- Experiment by combining concepts from different examples
- If you get an error, read the error message carefully - RID provides helpful hints!

## Contributing

Have a cool example to share? Feel free to submit a pull request!

---

**Happy Coding with RID! 🚀**