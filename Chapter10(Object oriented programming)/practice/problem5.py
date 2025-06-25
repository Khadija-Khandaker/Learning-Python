# Write a class Train which has methods to book a ticket, get status(no of seats) and get fare information of train running unnder kamalapur railway

from random import randint

class train:

    def __init__(self, trainNo):
        self.trainNo = trainNo
    
    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
        

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running successfully")
        

    def getFare(self, fro, to):
       print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")



t = train(12399)
t.book("Dhaka", "Chattagram")
t.getStatus()
t.getFare("Dhaka", "Chattagram")
