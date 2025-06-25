# 1) Python program to display a user entered name followed by Good Afternoon using input() function

name = input("Enter your name: ")
print(f"Good Afternoon! {name}" )

# 2) Program to fill in a letter template given below with name and date
letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>", "piya").replace("<|Date|>", "24 September 2025"))

# 3) Program to detect double space in a string
name= "I  am a good girl"
print(name.find("  "))

# 4)Replace the double space from problem 3 with single space
name= "I  am a good girl"
print(name.replace("  "," "))

# 5) Program to format the following letter using escape sequence
letter= "Dear girl,\n\tThis is very nice.\nThanks!"
print(letter)