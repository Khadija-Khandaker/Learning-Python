# Write va program to f find out the line rumber Where python is present from question 6

with open("log.txt") as f:
    lines = f.readlines()


lineno = 1
for line in lines:
    if("python" in line):
        print(f"Yes, python is present. Line no: {lineno}")
        break
    lineno += 1


else:
    print("No, python is not present")
        
        
 