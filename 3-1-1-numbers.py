# Copied from https://docs.python.org/3/tutorial/introduction.html

# ______________________________________________________________________________
# Numbers

2 + 2
# => 4

50 - 5*6
# => 20

(50 - 5*6) / 4
# => 5.0

8 / 5 # division always returns a floating point number
# => 1.6


17 / 3 # classic division returns a float
# => 5.666666666666667

17 // 3 # floor division discards the fractional part
# => 5

17 % 3 # the % operator returns the remainder of the division
# => 2

5 * 3 + 2 # result * divisor + remainder
# => 17

5 ** 2 # 5 squared
# => 25

2 ** 7 # 2 to the power of 7
# => 128


# ______________________________________________________________________________
# Assignment

width = 20
height = 5 * 9
width * height
# => 900


# ______________________________________________________________________________
# Undefined variable

no_such_variable
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File ".../python_tutorial/3-1-1-numbers.py", line 48, in <module>
#     no_such_variable
# NameError: name 'no_such_variable' is not defined


# ______________________________________________________________________________
# Mixed type operands and conversion

4 * 3.75 - 1
# => 14.0


# ______________________________________________________________________________
# Underscore

# In interactive mode, the last printed expression is assigned to the variable
# `_`.


# ______________________________________________________________________________
# Imaginary and complex numbers

(0+2j) ** 2
# => (-4+0j)

2j ** 2
# => (-4+0j)

(2+2j) ** 2
# => 8j
