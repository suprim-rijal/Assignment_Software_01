
TALENT_TO_KG = 20.0
POUND_TO_KG = 0.5
LOT_TO_GRAM = 13.3

talents = float(input("Enter talents:\n"))
pounds = float(input("Enter pounds:\n"))
lots = float(input("Enter lots:\n"))


total_kg = talents * TALENT_TO_KG + pounds * POUND_TO_KG
total_grams = lots * LOT_TO_GRAM


total_kg += int(total_grams // 1000)
total_grams = total_grams % 1000


print("\nThe weight in modern units:")
print(f"{int(total_kg)} kilograms and {total_grams:.2f} grams.")