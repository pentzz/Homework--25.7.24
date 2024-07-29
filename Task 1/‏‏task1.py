details: str = "ofir baranes even-yehudah"
# Task 1
print(len(details))
# Task 2
print(details.upper())
# Task 3
print(details.lower())
# Task 4
print(True if details.startswith("ofir") else False)
# Task 5
print(True if details.endswith("even-yehudah") else False)
# Task 6
print(details.split())
# Task 7
details.replace(" ", "*")
print(details.split("*"))
# Task 8
print(details.center(50, "="))
# Task 9
print(details[5:])
# Task 10
print(details[:4])
# Task 11
print(details[1::2])
# Task 12
print(details.title())