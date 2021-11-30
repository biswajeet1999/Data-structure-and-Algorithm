# O(n) time | O(min(n, 26)) space = O(1) space
def runCustomerSimulation(noOfComputers, users):
   noOfUsersDontUseComputer = 0
   tracker = {} # key is user and value is wether user get computer(i.e. 1 ) or not (i.e 0) 
   for user in users:
      if user in tracker: # user arrived before. time to departure
         noOfComputers += tracker[user]
      if user not in tracker:
         if noOfComputers == 0:
            tracker[user] = 0
            noOfUsersDontUseComputer += 1
         else:
            tracker[user] = 1
            noOfComputers -= 1
   return noOfUsersDontUseComputer



print(runCustomerSimulation(2, "ABBAJJKZKZ")) 
print(runCustomerSimulation(3, "GACCBDDBAGEE")) 
print(runCustomerSimulation(3, "GACCBGDDBAEE")) 
print(runCustomerSimulation(1, "ABCBCA")) 
print(runCustomerSimulation(1, "ABCBCADEED"))
print(runCustomerSimulation(1, "ABAB"))