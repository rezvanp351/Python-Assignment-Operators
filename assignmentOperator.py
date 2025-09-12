# Python Assignment Operators with Detailed Explanations
"""
What this does:
Addition (+=) → adds value to x
Subtraction (-=) → subtracts value from x
Multiplication (*=) → multiplies x
Division (/=) → divides x (returns float)
Floor division (//=) → divides x and takes integer part
Modulo (%=) → remainder of division
Exponent (**=) → raises x to power
Bitwise AND (&=) → compares each bit; 1&1=1, else 0
Bitwise OR (|=) → compares each bit; 0|1=1, 1|0=1, 1|1=1, 0|0=0
Bitwise XOR (^=) → compares bits; 1^1=0, 0^0=0, 1^0=1, 0^1=1
Right shift (>>=) → moves bits to the right; fills left with 0
Left shift (<<=) → moves bits to the left; fills right with 0
Walrus (:=) → assign and return value in a single expression
"""

x = 10  # Initial value
print(f"x = {x} → Initial value of x")

# Addition assignment (+=)
x += 5  # Equivalent to: x = x + 5
print(f"x += 5 → Add 5 to x → New x = {x} (Logic: x was 10, add 5, result is 15)")

# Subtraction assignment (-=)
x -= 3  # Equivalent to: x = x - 3
print(f"x -= 3 → Subtract 3 from x → New x = {x} (Logic: 15 - 3 = 12)")

# Multiplication assignment (*=)
x *= 2  # Equivalent to: x = x * 2
print(f"x *= 2 → Multiply x by 2 → New x = {x} (Logic: 12 * 2 = 24)")

# Division assignment (/=)
x /= 4  # Equivalent to: x = x / 4
print(f"x /= 4 → Divide x by 4 → New x = {x} (Logic: 24 / 4 = 6.0, note: result is float)")

# Floor division assignment (//=)
x //= 2  # Equivalent to: x = x // 2
print(f"x //= 2 → Floor divide x by 2 → New x = {x} (Logic: 6.0 // 2 = 3.0)")

# Modulus assignment (%=)
x %= 3  # Equivalent to: x = x % 3
print(f"x %= 3 → Remainder of x divided by 3 → New x = {x} (Logic: 3.0 % 3 = 0.0)")

# Exponentiation assignment (**=)
x **= 3  # Equivalent to: x = x ** 3
print(f"x **= 3 → Raise x to the power of 3 → New x = {x} (Logic: 0.0 ** 3 = 0.0)")

# Convert x to int before bitwise operations
x = int(x)
print(f"x = int(x) → Convert x to integer to allow bitwise operations → x = {x}")

# Bitwise AND assignment (&=)
a = 8  # 8 in binary: 1000
a &= 2  # Equivalent to: a = a & 2 → 1000 & 0010
print(f"a &= 2 → Bitwise AND assignment → New a = {a} → Binary: {bin(a)[2:]} (Logic: 1000 & 0010 = 0000)")

# Bitwise OR assignment (|=)
x |= 4  # Equivalent to: x = x | 4 → 0 | 4
print(f"x |= 4 → Bitwise OR assignment → New x = {x} → Binary: {bin(x)[2:]} (Logic: 0000 | 0100 = 0100 → 4)")

# Bitwise XOR assignment (^=)
x ^= 3  # Equivalent to: x = x ^ 3 → 4 ^ 3
print(f"x ^= 3 → Bitwise XOR assignment → New x = {x} → Binary: {bin(x)[2:]} (Logic: 0100 ^ 0011 = 0111 → 7)")

# Right shift assignment (>>=)
x >>= 1  # Equivalent to: x = x >> 1 → 7 >> 1
print(f"x >>= 1 → Right shift x by 1 → New x = {x} → Binary: {bin(x)[2:]} (Logic: 0111 >> 1 = 0011 → 3)")

# Left shift assignment (<<=)
x <<= 2  # Equivalent to: x = x << 2 → 3 << 2
print(f"x <<= 2 → Left shift x by 2 → New x = {x} → Binary: {bin(x)[2:]} (Logic: 0011 << 2 = 1100 → 12)")

# Walrus operator (Python 3.8+)
print(f"x := 5 → Walrus operator assigns 5 to x while printing → x = {x := 5}")
