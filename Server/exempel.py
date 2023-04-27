s = "b'0-0.06,-0.24,9.9'"

# Extract the string containing the numbers and split it into a list
numbers = s.split("'")[1].split(",")
numbers[0] = numbers[0][1:]

# Convert the list of strings to a list of floats
numbers = [float(x) for x in numbers]

# Check if the list contains exactly 3 numbers
if len(numbers) == 3:
    x, y, z = numbers
    print(f"x = {x}, y = {y}, z = {z}")
else:
    print("Invalid string format")