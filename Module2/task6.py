import random


code_3_digit = [random.randint(0, 9),random.randint(0, 9),random.randint(0, 9)]

code_4_digit = [ random.randint(1, 6),random.randint(1, 6),random.randint(1, 6),random.randint(1, 6)]

print("3-digit code (0-9):", code_3_digit)
print("4-digit code (1-6):", code_4_digit)