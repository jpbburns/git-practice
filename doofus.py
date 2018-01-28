import sys

print("Hello.")
try:
	x = int(input("Enter a number! "))
except ValueError:
	print("That's not a number and you know it.")

for i in range(1, x+1):
	print(i)

print("And that's how you count to", x)