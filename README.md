# Python-Assignment-Operators
Assignment Operators in Python  Assignment operators in Python are used to assign values to variables. They can be simple (like =) or combined with arithmetic/bitwise operators to perform an operation and assign the result in one step.
# 📘 Assignment Operators in Python (Complete with Examples)

Assignment operators in Python are used to assign values to variables.  
Some also perform operations (arithmetic/bitwise) and then assign the result.  

---

## 🔹 Assignment Operators Table

| Operator | Example     | Equivalent To  | Description |
|----------|------------|----------------|-------------|
| `=`      | `x = 5`    | `x = 5`        | Assigns a value |
| `+=`     | `x += 3`   | `x = x + 3`    | Add and assign |
| `-=`     | `x -= 3`   | `x = x - 3`    | Subtract and assign |
| `*=`     | `x *= 3`   | `x = x * 3`    | Multiply and assign |
| `/=`     | `x /= 3`   | `x = x / 3`    | Divide and assign (float) |
| `%=`     | `x %= 3`   | `x = x % 3`    | Modulus and assign |
| `//=`    | `x //= 3`  | `x = x // 3`   | Floor division and assign |
| `**=`    | `x **= 3`  | `x = x ** 3`   | Exponentiation and assign |
| `&=`     | `x &= 3`   | `x = x & 3`    | Bitwise AND and assign |
| `|=`     | `x |= 3`   | `x = x | 3`    | Bitwise OR and assign |
| `^=`     | `x ^= 3`   | `x = x ^ 3`    | Bitwise XOR and assign |
| `>>=`    | `x >>= 3`  | `x = x >> 3`   | Right shift and assign |
| `<<=`    | `x <<= 3`  | `x = x << 3`   | Left shift and assign |
| `:=`     | `print(x := 3)` | `x = 3; print(x)` | Walrus operator (assign inside expressions) |

---

## 🔹 Examples in Python

```python
# Basic assignment
x = 5
print(x)  # 5

# Addition assignment
x = 5
x += 3
print(x)  # 8

# Subtraction assignment
x = 5
x -= 3
print(x)  # 2

# Multiplication assignment
x = 5
x *= 3
print(x)  # 15

# Division assignment
x = 5
x /= 3
print(x)  # 1.666...

# Modulus assignment
x = 5
x %= 3
print(x)  # 2

# Floor division assignment
x = 5
x //= 3
print(x)  # 1

# Exponentiation assignment
x = 5
x **= 3
print(x)  # 125

# Bitwise AND assignment
x = 5   # 101 (binary)
x &= 3  # 011 (binary)
print(x)  # 1

# Bitwise OR assignment
x = 5   # 101 (binary)
x |= 3  # 011 (binary)
print(x)  # 7

# Bitwise XOR assignment
x = 5   # 101 (binary)
x ^= 3  # 011 (binary)
print(x)  # 6

# Right shift assignment
x = 8   # 1000 (binary)
x >>= 2
print(x)  # 2 (0010)

# Left shift assignment
x = 3   # 0011 (binary)
x <<= 2
print(x)  # 12 (1100)

# Walrus operator (:=)
print(x := 3)  # assigns 3 to x and prints it
print(x)       # 3
```

---

# Bitwise Operators Truth Table

This table shows how bitwise operators work on two single-bit inputs `A` and `B`.

| A | B | AND `&` | OR `\|` | XOR `^` | NOT `~A` | Left Shift `<<` | Right Shift `>>` |
|---|---|---------|---------|---------|----------|-----------------|------------------|
| 0 | 0 |    0    |    0    |    0    |    1     |        0        |        0         |
| 0 | 1 |    0    |    1    |    1    |    1     |        0        |        0         |
| 1 | 0 |    0    |    1    |    1    |    0     |        0        |        0         |
| 1 | 1 |    1    |    1    |    0    |    0     |        0        |        1         |



---

### Explanation

- **A AND B (`&`)** → Result is `1` only if both inputs are `1`.  
- **A OR B (`|`)** → Result is `1` if at least one input is `1`.  
- **A XOR B (`^`)** → Result is `1` if inputs are different.  
- **~A (NOT)** → Inverts the bit: `0 → 1`, `1 → 0`.  
- **A << 1 (Left Shift)** → Shifts bits to the left, fills with `0`, equivalent to multiplying by 2.  
- **A >> 1 (Right Shift)** → Shifts bits to the right, fills with `0` (for positive numbers), equivalent to integer division by 2.  


## ✅ Summary
- Assignment operators are essential in Python.  
- They make code **shorter, cleaner, and more readable**.  
- The **walrus operator** (`:=`) is new in Python 3.8 and allows assignment inside expressions.  
