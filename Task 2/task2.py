# Task 1
sen1: str = " day-fun "
print(sen1.strip())
# Task 2
sen2: str = "hello"
print(sen2.isalpha())
# Task 3
sen3: str = "777"
print(sen3.isdigit())
# Task 4
sen4: str = " "
print(sen4.isspace())
# Task 5
a: list[str] = ["N", "I", "N", "J", "A"]
print("".join(a))
# Task 6
print("*".join(a))
# Task 7
sen7: str = "hELLo"
print(True if "e" in sen7.lower() else False)
# Task 8
word: str = input("Please enter a word: ")
task8: list[str] = [c.upper() for c in word if c.isalpha()]
print(task8)
