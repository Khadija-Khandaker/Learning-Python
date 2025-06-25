st = "Hello! This is a new file"


f = open("myfile.txt", "a") # Append mode

f.write(st)

f.close()