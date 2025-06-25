def goodDay(name, ending):
    print(f"Good Day {name}")
    print(ending)

    return "ok"

goodDay("Harry", "Thank you") 
goodDay("Hania", "Thanks") 

a = goodDay("Shumi", "Thanks")

print(a)

# Default argument

def GoodDay(name, ending="Thank you"):
    print("Good Day" + name)
    print(ending)

GoodDay("Yalina")    
GoodDay("ina", "Thanks")    