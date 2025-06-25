# A program to generate multiplication tables Write a from and write to files. Place these files in a folder for a 13-year old.

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n*i}\n"

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)




for i in range(2, 21):
    generateTable(i)
    
