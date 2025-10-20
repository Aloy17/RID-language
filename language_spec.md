# RID Language Specification

**Version:** 1.1  
**Author:** Ryane Bose  
**Last Updated:** October 2025

This document provides the complete formal grammar specification for the RID programming language.

> **💡 Tip:** The best way to write and run RID code is using [**RIDLEY IDE**](https://github.com/Aloy17/RIDLEY) - a dedicated desktop IDE with syntax highlighting, built-in tutorials, and an intuitive interface. **No installation required** - it's a standalone application with the RID interpreter built right in!

---

## Table of Contents

1. [Overview](#overview)
2. [Lexical Structure](#lexical-structure)
3. [Grammar Rules](#grammar-rules)
4. [Operator Precedence](#operator-precedence)
5. [Semantics](#semantics)
6. [Examples](#examples)

---

## Overview

RID is a dynamically-typed, imperative programming language with Hindi-inspired keywords. It transpiles to Python and supports:

- Variables (with numbers in identifiers)
- Arithmetic and comparison operations
- String operations
- Type conversion functions (num, dec, word, bool)
- Control flow (conditionals and loops)
- Functions with recursion
- Comments

---

## Lexical Structure

### Keywords

```
Let      - Variable declaration
out      - Output (print without newline)
line     - Print newline
in       - Input
Run      - Loop keyword
while    - While loop modifier
agar     - If
ya_fir   - Else if
warna    - Else
func     - Function definition
give     - Return statement
True     - Boolean literal
False    - Boolean literal
num      - Convert to integer
dec      - Convert to decimal/float
word     - Convert to string
bool     - Convert to boolean
```

### Operators

```
Arithmetic:   +  -  *  /  %
Comparison:   ==  !=  <  >  <=  >=
Assignment:   =
```

### Delimiters

```
(  )    - Parentheses
{  }    - Braces
,       - Comma
```

### Identifiers

- Must start with a letter (a-z, A-Z) or underscore (_)
- Can contain letters, numbers (0-9), and underscores
- Case-sensitive
- Cannot be a keyword

**Valid:** `x`, `myVar`, `count1`, `user_name`, `_temp`  
**Invalid:** `1var`, `my-var`, `Let`

### Literals

**Numbers:**
- Integers: `42`, `0`, `1000`
- Floats: `3.14`, `0.5`, `2.0`
- Negative: `-5`, `-3.14`

**Strings:**
- Enclosed in double quotes: `"Hello"`, `"RID"`
- No escape sequences supported

**Booleans:**
- `True` or `False`

### Comments

```rid
~ Single-line comment ~
```

Comments are enclosed between `~` symbols and are ignored by the lexer.

---

## Grammar Rules

### Program Structure

```
program        → statement*
```

A RID program consists of zero or more statements.

**Example:**
```rid
Let x = 10
out(x)
```

---

### Statements

```
statement      → var_decl
               | assignment
               | print_stmt
               | newline_stmt
               | input_stmt
               | loop_stmt
               | conditional_stmt
               | func_def
               | func_call
               | return_stmt
```

---

### Variable Declaration

```
var_decl       → "Let" IDENTIFIER "=" expression
```

Declares a new variable and initializes it with a value.

**Examples:**
```rid
Let x = 10
Let name = "Alice"
Let sum = 5 + 3
Let result = add(10, 20)
```

**Note:** Variables must be declared with `Let` before use.

---

### Assignment

```
assignment     → IDENTIFIER "=" expression
```

Assigns a new value to an existing variable.

**Examples:**
```rid
Let x = 10
x = 20
x = x + 5
```

**Error if variable not declared:**
```rid
y = 10  ~ ERROR: Variable 'y' is not defined ~
```

---

### Output Statement

```
print_stmt     → "out" "(" expression ")"
newline_stmt   → "line"
```

`out()` prints an expression without adding a newline.  
`line` prints a newline character.

**Examples:**
```rid
out("Hello")
out(" ")
out("World")
line
~ Output: Hello World (with newline) ~

out(42)
line
~ Output: 42 (with newline) ~

Let x = 10
out(x + 5)
line
~ Output: 15 (with newline) ~
```

---

### Input Statement

```
input_stmt     → IDENTIFIER "=" "in" "(" STRING? ")"
```

Reads input from the user and stores it in a variable.

**Examples:**
```rid
Let name = ""
name = in()
~ Waits for user input ~

Let age = ""
age = in("Enter your age: ")
~ Displays prompt and waits for input ~
```

**Note:** 
- Variable must be declared before using `in()`
- Input is always returned as a string

---

### Expressions

```
expression     → additive

additive       → multiplicative (("+"|"-") multiplicative)*

multiplicative → unary (("*"|"/"|"%") unary)*

unary          → "-" unary
               | primary

primary        → NUMBER
               | STRING
               | IDENTIFIER
               | "(" expression ")"
               | func_call
               | type_conversion
               
type_conversion → ("num"|"dec"|"word"|"bool") "(" expression ")"
```

**Type Conversion Examples:**
```rid
~ Convert string to integer ~
Let str_num = "42"
Let number = num(str_num)     ~ 42 (as integer) ~

~ Convert string to decimal ~
Let str_dec = "3.14"
Let decimal = dec(str_dec)    ~ 3.14 (as float) ~

~ Convert number to string ~
Let value = 100
Let text = word(value)        ~ "100" (as string) ~

~ Convert to boolean ~
Let zero = 0
Let one = 1
Let bool_zero = bool(zero)    ~ False ~
Let bool_one = bool(one)      ~ True ~

~ Useful with user input ~
Let input = ""
input = in("Enter a number: ")
Let squared = num(input) * num(input)
out(squared)
line
```

**Standard Examples:**
```rid
5 + 3           ~ 8 ~
10 - 4          ~ 6 ~
2 * 6           ~ 12 ~
15 / 3          ~ 5 ~
10 % 3          ~ 1 ~
-5              ~ -5 ~
(2 + 3) * 4     ~ 20 ~
"Hello" + " " + "World"  ~ "Hello World" ~
```

---

### Conditions

```
condition      → expression ( "==" | "!=" | "<" | ">" | "<=" | ">=" ) expression
```

Used in conditional statements and while loops.

**Examples:**
```rid
x == 10
y != 5
a < b
count >= 0
name == "Alice"
```

---

### Conditional Statements

```
conditional_stmt → "agar" "(" condition ")" block
                   ("ya_fir" "(" condition ")" block)*
                   ("warna" block)?
```

**Examples:**

**Simple if:**
```rid
agar(x > 0) {
    out("Positive")
    line
}
```

**If-else:**
```rid
agar(x > 0) {
    out("Positive")
}
warna {
    out("Not positive")
}
```

**If-elif-else chain:**
```rid
agar(score >= 90) {
    out("A")
}
ya_fir(score >= 80) {
    out("B")
}
ya_fir(score >= 70) {
    out("C")
}
warna {
    out("F")
}
```

---

### Loop Statements

```
loop_stmt      → "Run" "(" expression ")" block
               | "Run" "while" "(" condition ")" block
```

**Fixed-count loop:**
```rid
Run(5) {
    out("Hello")
    line
}
~ Prints "Hello" 5 times ~
```

**While loop:**
```rid
Let i = 0
Run while(i < 5) {
    out(i)
    line
    i = i + 1
}
~ Prints: 0 1 2 3 4 ~
```

**Complex example:**
```rid
Let sum = 0
Let n = 1
Run while(n <= 10) {
    sum = sum + n
    n = n + 1
}
out(sum)  ~ Prints: 55 ~
```

---

### Function Definition

```
func_def       → "func" IDENTIFIER "(" param_list? ")" block
param_list     → IDENTIFIER ("," IDENTIFIER)*
```

**Examples:**

**Simple function:**
```rid
func greet(name) {
    out("Hello, ")
    out(name)
    line
}
```

**Function with return:**
```rid
func add(a, b) {
    give a + b
}
```

**Recursive function:**
```rid
func factorial(n) {
    agar(n <= 1) {
        give 1
    }
    warna {
        give n * factorial(n - 1)
    }
}
```

**Multiple parameters:**
```rid
func calculate(x, y, z) {
    give x * y + z
}
```

---

### Function Call

```
func_call      → IDENTIFIER "(" arg_list? ")"
arg_list       → expression ("," expression)*
```

**Examples:**

**As statement:**
```rid
greet("Alice")
```

**In expression:**
```rid
Let result = add(5, 3)
Let sum = add(10, multiply(2, 3))
```

**With literals:**
```rid
func multiply(a, b) {
    give a * b
}

Let x = multiply(5, 3)      ~ x = 15 ~
Let y = multiply(2 + 3, 4)  ~ y = 20 ~
```

---

### Return Statement

```
return_stmt    → "give" expression
```

Returns a value from a function.

**Examples:**
```rid
func square(x) {
    give x * x
}

func max(a, b) {
    agar(a > b) {
        give a
    }
    warna {
        give b
    }
}
```

---

### Block

```
block          → "{" statement* "}"
```

A block contains zero or more statements enclosed in braces.

**Example:**
```rid
agar(x > 0) {
    out("x is positive")
    line
    x = x - 1
}
```

---

## Operator Precedence

From highest to lowest:

1. **Parentheses**: `()`
2. **Unary minus**: `-`
3. **Multiplicative**: `*`, `/`, `%`
4. **Additive**: `+`, `-`
5. **Comparison**: `==`, `!=`, `<`, `>`, `<=`, `>=`

**Examples:**
```rid
2 + 3 * 4       ~ 14 (not 20) ~
(2 + 3) * 4     ~ 20 ~
-5 + 3          ~ -2 ~
10 / 2 + 3      ~ 8 ~
```

---

## Semantics

### Type System

RID is **dynamically typed**. Types are determined at runtime by the Python transpiler.

**Supported types:**
- Number (int/float)
- String
- Boolean

### Variable Scope

- **Global scope**: Variables declared outside functions
- **Function scope**: Variables in function parameters
- **Block scope**: Shares outer scope (no separate block scope)

**Example:**
```rid
Let x = 10          ~ Global ~

func test(y) {      ~ y is local to test ~
    Let z = 5       ~ z is local to test ~
    out(x)          ~ Can access global x ~
}
```

### String Concatenation

Strings can be concatenated with the `+` operator:

```rid
Let greeting = "Hello" + " " + "World"
Let message = "Value: " + 42  ~ Error in Python: can't concat str and int ~
```

**Note:** RID transpiles directly to Python, so type errors are caught at runtime.

### Recursion

Functions can call themselves:

```rid
func countdown(n) {
    agar(n > 0) {
        out(n)
        line
        countdown(n - 1)
    }
}

countdown(5)  ~ Prints: 5 4 3 2 1 ~
```

---

## Complete Examples

### Example 1: Fibonacci Sequence

```rid
~ Print first 10 Fibonacci numbers ~

Let a = 0
Let b = 1
Let count = 0

Run while(count < 10) {
    out(a)
    line
    
    Let temp = a + b
    a = b
    b = temp
    
    count = count + 1
}
```

### Example 2: Factorial with Recursion

```rid
func factorial(n) {
    agar(n <= 1) {
        give 1
    }
    warna {
        give n * factorial(n - 1)
    }
}

Let num = 5
Let result = factorial(num)
out("Factorial of ")
out(num)
out(" is ")
out(result)
line
~ Output: Factorial of 5 is 120 ~
```

### Example 3: Number Guessing Game

```rid
Let secret = 42
Let guess = ""
Let attempts = 0

out("Welcome to the Guessing Game!")
line
out("I'm thinking of a number between 1 and 100")
line

guess = in("Enter your guess: ")
attempts = attempts + 1

agar(guess == secret) {
    out("Congratulations! You guessed it!")
    line
}
ya_fir(guess < secret) {
    out("Too low!")
    line
}
warna {
    out("Too high!")
    line
}
```

### Example 4: Grade Calculator

```rid
func getGrade(score) {
    agar(score >= 90) {
        give "A"
    }
    ya_fir(score >= 80) {
        give "B"
    }
    ya_fir(score >= 70) {
        give "C"
    }
    ya_fir(score >= 60) {
        give "D"
    }
    warna {
        give "F"
    }
}

Let score = 85
Let grade = getGrade(score)
out("Your grade is: ")
out(grade)
line
~ Output: Your grade is: B ~
```

---

## Error Handling

RID provides clear error messages:

### Syntax Errors

```
Syntax Error: Expected '=' after variable 'x', got '+'
Syntax Error: Expected ')' to close 'out' statement, got 'EOL'
Syntax Error: Unexpected token 'xyz' of type 'IDENTIFIER'
```

### Name Errors

```
Name Error: Variable 'x' is not defined. Use 'Let x = ...' to declare it first
Name Error: Function 'myFunc' is not defined
```

### Type Errors

```
Type Error: Expected numeric value inside 'Run()', got '"hello"'
```

---

## Language Limitations

Current limitations (may be addressed in future versions):

1. **No arrays/lists** - Cannot store collections
2. **No logical operators** - No `and`, `or`, `not`
3. **No break/continue** - Cannot exit loops early
4. **No multiline strings** - Strings must be on one line
5. **No import system** - Cannot split code across files

---

## BNF Grammar Summary

```bnf
program        → statement*

statement      → var_decl | assignment | print_stmt | newline_stmt
               | input_stmt | loop_stmt | conditional_stmt
               | func_def | func_call | return_stmt

var_decl       → "Let" IDENTIFIER "=" expression
assignment     → IDENTIFIER "=" expression
print_stmt     → "out" "(" expression ")"
newline_stmt   → "line"
input_stmt     → IDENTIFIER "=" "in" "(" STRING? ")"

expression     → additive
additive       → multiplicative (("+"|"-") multiplicative)*
multiplicative → unary (("*"|"/"|"%") unary)*
unary          → "-" unary | primary
primary        → NUMBER | STRING | IDENTIFIER | "(" expression ")" 
               | func_call | type_conversion

type_conversion → ("num"|"dec"|"word"|"bool") "(" expression ")"

condition      → expression ("=="|"!="|"<"|">"|"<="|">=") expression

loop_stmt      → "Run" "(" expression ")" block
               | "Run" "while" "(" condition ")" block

conditional_stmt → "agar" "(" condition ")" block
                   ("ya_fir" "(" condition ")" block)*
                   ("warna" block)?

func_def       → "func" IDENTIFIER "(" param_list? ")" block
param_list     → IDENTIFIER ("," IDENTIFIER)*

func_call      → IDENTIFIER "(" arg_list? ")"
arg_list       → expression ("," expression)*

block          → "{" statement* "}"
return_stmt    → "give" expression
```

---

**End of Specification**

For more examples, see the `examples/` directory in the repository.