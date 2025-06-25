# Write a program to mine va log file and fird Out whether it contains "python"

with open("log.txt") as f:
    content = f.read()


if("python" in content):
    print("Yes, python is present")
else:
    print("No, python is not present")


