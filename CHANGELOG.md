# Changelog

All notable changes to the RID Programming Language will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- **Type conversion functions**: `num()`, `dec()`, `word()`, `bool()`
  - `num()` converts values to integers (Python's `int()`)
  - `dec()` converts values to decimals (Python's `float()`)
  - `word()` converts values to strings (Python's `str()`)
  - `bool()` converts values to booleans (Python's `bool()`)
- **Comma delimiter** support for cleaner syntax
- Comprehensive test suite (`test_lexer_parser.py`) for validating lexer and parser functionality
- Example program demonstrating type conversions (`type_conversion_test.rid`)

---

## [1.0.0] - 2024-10-18

### Initial Release

This is the first stable release of RID Programming Language.

### Added

#### Core Language Features
- **Variable declaration** with `Let` keyword
- **Variable assignment** with type inference
- **Data types**: Numbers (int/float), Strings, Booleans
- **Identifiers** can contain letters, numbers, and underscores
- **Arithmetic operators**: `+`, `-`, `*`, `/`, `%`
- **Comparison operators**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Unary minus** for negative numbers (e.g., `-5`)
- **String concatenation** using the `+` operator

#### Control Flow
- **Conditional statements**: `agar` (if), `ya_fir` (elif), `warna` (else)
- **Fixed-count loops**: `Run(n)` executes a block n times
- **While loops**: `Run while(condition)` for conditional iteration

#### Functions
- **Function definition** with `func` keyword
- **Function parameters** and argument passing
- **Return statements** with `give` keyword
- **Recursion support**: Functions can call themselves
- **Function calls** in expressions and as statements

#### Input/Output
- **Output**: `out()` prints without newline
- **Newline**: `line` keyword prints a newline
- **Input**: `in()` reads user input with optional prompt

#### Comments
- **Single-line comments**: `~ comment ~` syntax

#### Transpiler
- **Lexer**: Tokenizes RID source code
- **Parser**: Validates syntax and generates Python code
- **Error messages**: Clear, helpful error reporting
  - Syntax errors with context
  - Name errors for undefined variables/functions
  - Type errors for invalid operations

#### Documentation
- Comprehensive README with examples
- Detailed language specification with BNF grammar
- 8 example programs demonstrating all features:
  - hello_world.rid
  - calculator.rid
  - conditionals.rid
  - loops.rid
  - functions.rid
  - fibonacci.rid
  - factorial.rid
  - guess_the_number.rid
- MIT License

### Technical Details

- **Language**: Python 3.7+
- **Architecture**: Lexer → Parser → Transpiler → Python execution
- **No external dependencies**: Uses only Python standard library

---

## Known Limitations (as of v1.0.0)

- No arrays/lists
- No logical operators (`and`, `or`, `not`)
- No `break`/`continue` in loops
- No multiline strings
- No import/module system
- No exception handling

---

## Future Considerations

Potential features for future versions:
- [ ] Arrays and list support
- [ ] Logical operators
- [ ] Loop control statements (break/continue)
- [ ] File I/O operations
- [ ] Standard library
- [ ] Interactive REPL mode
- [ ] Better error messages with line numbers

---


**Note**: Version numbers follow [Semantic Versioning](https://semver.org/):
- **MAJOR** version for incompatible changes
- **MINOR** version for new features (backwards-compatible)
- **PATCH** version for bug fixes (backwards-compatible)