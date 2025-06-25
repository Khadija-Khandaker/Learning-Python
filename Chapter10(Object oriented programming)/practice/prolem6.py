# Can you change the self-parameter inside a class to something else(say "harry"). Try changing self to "slf" or "harry" and see trhe effects
# Ans: No change will occur

from random import randint

class train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo
    
    def book(slf, fro, to):
        print(f"Ticket is booked in train no: {slf.trainNo} from {fro} to {to}")
        

    def getStatus(slf):
        print(f"Train no: {slf.trainNo} is running successfully")
        

    def getFare(slf, fro, to):
       print(f"Ticket fare in train no: {slf.trainNo} from {fro} to {to} is {randint(222, 5555)}")



t = train(12399)
t.book("Dhaka", "Chattagram")
t.getStatus()
t.getFare("Dhaka", "Chattagram")
