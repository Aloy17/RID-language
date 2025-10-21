# RID Language - Reserved Keywords

## ⚠️ **IMPORTANT: Cannot be used as variable names**

The following words are reserved keywords in RID and **CANNOT** be used as variable names:

### Control Flow Keywords
- `Let` - Variable declaration
- `agar` - If statement
- `ya_fir` - Else-if statement  
- `warna` - Else statement
- `Run` - Loop statement
- `while` - While condition
- `func` - Function declaration
- `give` - Return statement

### Built-in Functions
- `out` - Output/print function
- `in` - Input function
- `line` - Newline

### Type Conversion Functions
- ⚠️ `num` - Convert to integer
- ⚠️ `dec` - Convert to decimal/float
- ⚠️ `word` - Convert to string
- ⚠️ `bool` - Convert to boolean

### Boolean Literals
- `True`
- `False`

## ❌ **Common Mistakes**

```rid
~ WRONG - 'num' is a reserved keyword ~
Let num = 42

~ CORRECT - Use a different name ~
Let number = 42
Let myNum = 42
Let count = 42
```

```rid
~ WRONG - 'line' is a reserved keyword ~
Let line = "Hello"

~ CORRECT ~
Let text = "Hello"
Let message = "Hello"
```

```rid
~ WRONG - 'word' is a reserved keyword ~
Let word = "test"

~ CORRECT ~
Let text = "test"
Let str = "test"
```

## ✅ **Safe Variable Names**

Use descriptive names that don't conflict:
- `number`, `myNum`, `value`, `count`, `total`
- `text`, `message`, `str`, `content`
- `flag`, `isValid`, `status`, `result`
- `index`, `counter`, `position`
- `score`, `age`, `price`, `quantity`

## 📝 **Best Practice**

Use clear, descriptive variable names that indicate their purpose:
```rid
Let playerScore = 100
Let userName = "Alice"
Let isGameOver = False
Let totalAmount = 250.50
```
