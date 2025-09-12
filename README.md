# Python-Assignment-Operators
Assignment Operators in Python  Assignment operators in Python are used to assign values to variables. They can be simple (like =) or combined with arithmetic/bitwise operators to perform an operation and assign the result in one step.

# 📘 Assignment Operators in Python

Assignment operators in Python are used to **assign values to variables**.  
They can be simple (like `=`) or combined with arithmetic/bitwise operators to perform an operation and assign the result in one step.  

---

## 🔹 Basic Assignment Operator
- **`=`** → Assigns a value to a variable.  

```python
x = 10       # assigns 10 to x
y = "Hello"  # assigns string to y
```

---

## 🔹 Compound Assignment Operators
These operators **perform an operation and update the variable** at the same time.

| Operator | Example  | Equivalent To | Description              |
|----------|----------|---------------|--------------------------|
| `+=`     | `x += 5` | `x = x + 5`   | Adds and assigns         |
| `-=`     | `x -= 3` | `x = x - 3`   | Subtracts and assigns    |
| `*=`     | `x *= 2` | `x = x * 2`   | Multiplies and assigns   |
| `/=`     | `x /= 4` | `x = x / 4`   | Divides (float) and assigns |
| `//=`    | `x //= 2`| `x = x // 2`  | Floor division and assigns |
| `%=`     | `x %= 3` | `x = x % 3`   | Modulus and assigns      |
| `**=`    | `x **= 2`| `x = x ** 2`  | Exponentiation and assigns |
| `&=`     | `x &= 2` | `x = x & 2`   | Bitwise AND and assigns  |
| `|=`     | `x |= 3`| `x = x | 3`  | Bitwise OR and assigns   |
| `^=`     | `x ^= 1` | `x = x ^ 1`   | Bitwise XOR and assigns  |
| `>>=`    | `x >>= 1`| `x = x >> 1`  | Right shift and assigns  |
| `<<=`    | `x <<= 2`| `x = x << 2`  | Left shift and assigns   |

---

## 🔹 Examples

```python
# Arithmetic assignment
a = 10
a += 5   # a = 15
a *= 2   # a = 30

# Division assignment
b = 20
b //= 3  # b = 6
b /= 2   # b = 3.0

# Modulus and power
c = 7
c %= 3   # c = 1
c **= 4  # c = 1

# Bitwise assignment
d = 8      # 1000 (binary)
d >>= 2    # d = 2 (0010)
d <<= 3    # d = 16 (10000)
```

---

## 🔹 Key Notes
- Compound assignment operators make the code **shorter and cleaner**.
- They work with **numbers, booleans, and even objects** that define special methods (e.g., `__iadd__`, `__imul__`).
- Useful for **loops, counters, and bitwise operations**.

---

## ✅ Summary
Assignment operators in Python provide a concise way to:
- Assign values,
- Perform arithmetic or bitwise operations,
- Update variables in a single step.  

They are essential for writing **efficient, readable, and clean Python code**.

