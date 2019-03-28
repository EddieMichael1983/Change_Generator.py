#make_change.py
import random

unconverted_pennies = input("Enter an amount of money in pennies:  E.G. 136 for $1.36: ")
unconverted_pennies = int(unconverted_pennies)

quarters = unconverted_pennies // 25
unconverted_pennies = unconverted_pennies % 25
dimes = unconverted_pennies // 10
unconverted_pennies = unconverted_pennies % 10
nickels = unconverted_pennies // 5
unconverted_pennies = unconverted_pennies % 5
pennies = unconverted_pennies // 1
unconverted_pennies = unconverted_pennies % 1

print(f'{quarters} quarters')
print(f'{dimes} dimes')
print(f'{nickels} nickels')
print(f'{pennies} pennies')
