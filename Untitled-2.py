class Emp:
    def works(self):
        print("Emp works for company")
class dept(Emp):
    def dpt(self):
        print("Sales Department")
d=dept()
d.dpt()
d.works()
a=input()
print(a,"is handsome")