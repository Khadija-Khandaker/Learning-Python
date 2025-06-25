# 1) Program to create a dictionary of bangla words with values as their english translation. Provide user with an option to took it up!
words = {
   "Valo"    : "Good",
   "Shundor" : "Nice",
   "Brishti" : "Rain"
}

word = input("Enter the word you want meaning of: ")
print(words[word])

# 2) Program to input 8 numbers from the user and display all the unique numbers(once)
s = set()

n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))

print(s)

# 3) Can we have a set with 18(int) and '18'(str) as a value in it
s1 = set()

s1.add(18)
s1.add("18")
print(s1)

# 4) What will be the length of the following set
'''s=set()
s.add(20)
s.add(20.0)
s.add('20')'''

s2=set()
s2.add(20)
s2.add(20.0)
s2.add('20')
print(len(s2))

# 5) s={} what is the type of s here
s = {}
print(type(s)) # Type = Dictionary

# 6) Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique
d = {}

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

print(d)

# 7) If the number of 2 friends are same; what will happen to the program in problem 6
# Ans: It will show the  language which entered at the last

# 8) If the number of 2 languages are same; what will happen to the program in problem 6
# Ans: The program will be same as number 6 because values can be same

# 9) Can you change the values inside a list which is contained in set S
s3 = {5, 8, "Hello", [1,2]}

# It is not possible to have a list inside a set and also set are immutable
