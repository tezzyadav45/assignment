name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
height = float(input("Enter your Height: "))
country = input("Enter your Country: ")

name = name.upper()
height = float(f"{height:.2f}")
country = country.title()
nickname = name[:2] + name[-2:]

print("Details")
print("Hello", name)
print(f"You are {age} years old")
print(f"Your height is {height} feet")
print("Your are from", country)
print("Your nickname is", nickname)
