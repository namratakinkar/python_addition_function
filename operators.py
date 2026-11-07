#  ========================
#    OPERATOR
#  ========================

#  ===================================================================
#    Operator :- An Operator any specific opration between two oprands.
#  ===================================================================

# Example :- 

# a = 10
# b = 50
# print(a + b) # outpu = 60

#  ========================
#   Types of Operator 
#  ========================

# 1. Arithmetic Operator
# 2. Assignment Operator
# 3. Logical Operator
# 4. Bitwise Operator
# 5. Identity Operator
# 6. Membership Operator

#  ===============================
#    1. Arithmetic Operator
#  ===============================

# Arithmetic operator are used to perform methematical calculations.

# operators :- +, -, *, /, %(Modulus), //(Floor division), **(Exponentiation),

# Examples :- addition (+)

# a = 25
# b = 66
# print(a + b)  # output :-  91 
# ---------------------------------------------------------

# Examples :- Subtraction (-)

# a = 75
# b = 66
# print(a - b)  # output :-  9
# ----------------------------------------------------------

# Examples :- Multiplication (*)

# a = 7
# b = 8
# print(a * b)  # output :-  56
# -----------------------------------------------------------

# Examples :- Divison (/)

# it gives us the Quatient parts after performing the division opration.
# it gives us float data type value.

# a = 25
# b = 5
# print(a / b)  # output :-  5.0
# -------------------------------------------------------------

# Examples :- Modules (%)

# it gives us the reminder value after performing the division opration.


# a = 12
# b = 5
# print(a % b)  # output :-  2
# --------------------------------------------------------------

# Examples :- floor Division (//) 

# it also gives Quatient parts after performing the division opration.
# it gives us integer data type value.

# a = 18
# b = 2
# print(a // b)  # output :-  9
# ----------------------------------------------------------------

# Examples :- Exponentiation (**) 

#  used to calculat power of a number.

# a = 2
# b = 6
# print(a ** b)  # output :-  64
# ----------------------------------------------------------------

#  ===============================
#   2. Assignment Operator
#  ===============================

# Assignment Operator are used to assign value to variable.

# Operators :- =, +=, -=, /=, *=, %=, //=, **=

# Example :- 

# a = 10
# a += 5
# print(a) # Output :- 15

# a -= 3
# print(a) # Output :- 12

# a /= 2
# print(a) # Output :- 6.0

# a *= 4
# print(a) # Output :- 10.0

# a %= 6
# print(a) # Output :- 60.0

# a //= 5
# print(a) # Output :- 12.0

# a **= 7
# print(a) # Output :- 35831808.0 

#  =====================================
#   3. Logical Operator
#  =====================================

# Logical Operator are used to combine two or more condition.

# Oprators :- 

# AND Operator :- if both condition are true -> True
#                 Outherwise  -> False


# OR Operator :- if both condition are false -> false
#                 Outherwise  -> true

# NOT Operator :- it gives the opposite value.

# Examples :- 

# a = True
# b = False
# print(a and b) # False
# print(a or b) # True
# print(not a) # False
# print(not b) # True 
# -----------------------------------------------------------------

# Second Example :- 

# a = True 
# b = False
# c = True
# d = False
# print(a and b) # output :- False
# print(a and c) # output :- True
# print(a and d) # output :- False
# print(b and d) # output :- False
# print(a or b) # output :- True
# print(a or c) # output :- True
# print(a or d) # output :- True
# print(b or d) # output :- False
# print(a or c) # output :- True
# print(not a) # output :- False
# print(not b) # output :- True
# print(not c) # output :- False
# print(not d) # output :- True
# -------------------------------------------------------------------

# Third Example:-  

# a = 10
# b = 5
# print(a > 5 and b < 10) # output :- True
# print(a > 15 or b < 10) # output :- True
# print(not(a > 5)) # output :- False
# ---------------------------------------------------------------------

#  ================================
#   4. Bitwise Operator
#  ================================

# Bitwise Operator are used to perform opration on binary number (bits).

# Operators :- &, |, ^, ~, <<, >>

#  =====================================
#   BINERY NUMBER
#  =====================================

# 0 => 0000
# 1 => 0001
# 2 => 0010
# 3 => 0011
# 4 => 0100
# 5 => 0101
# 6 => 0110
# 7 => 0111
# 8 => 1000
# 9 => 1001
# 10 => 1010
# 11 => 1011
# 12 => 1100
# 13 => 1101
# 14 => 1110
# 15 => 1111

# Bitwise ( & ) :-

#  if both case are 1, it gives 1 outherwise it gives 0.

# Bitwise ( | ) :- 

# if both case are 0, it gives 0 outherwise it gives 1. 

# Examples :- 

# a = 10  binary number of 10 => 1010
# b = 3   binary number of 3 => 0011
# print(a & b)

#   1010
# & 0011
# --------
#   0010  This is a binary number of 2.
# output :- 2
# ------------------------------------------------------------------


#  Second Example :-

# a = 15  binary number of 10 => 1111
# b = 5  binary number of 3 => 0101
# print(a | b)

#   1111
# | 0101
# --------
#   1111      This is a binary number of 15.
# output :- 15

#  ================================
#   5. Identity Operator
#  ================================

# Identity Operator are used to check whether two variable refer to the same object or not.

# Operator :- is, is not 

# Example :- 

# a = [10, 20]
# b = a
# c = [10, 20]

# print(a is b)      # True
# print(a is c)      # False
# print(a is not c)  # True

#  ==================================
#   6. Membership Operator 
#  ==================================

# Membership Operator are used to check whether a value present in a sequence or not.

# Operator :- in, not in

# Example :- 

# fruits = ["Apple", "Mango", "Banana"]

# print("Apple" in fruits)       # True
# print("Grapes" in fruits)      # False
# print("Grapes" not in fruits)  # True








 



