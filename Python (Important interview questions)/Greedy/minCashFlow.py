
# We can calculate the net amount of every person as-

# Net amount = sum of all received money  - the sum of all sent money.

# Find the person with the maximum and the minimum net amount, suppose ‘x’ person has maximum net amount ‘maxAmount’ and ‘y’ person has a minimum amount ‘minAmount’, then ‘y’ person will pay ‘minAmount’ to ‘x’ person after this transaction net amount of ‘x’ person is ‘maxAmount = maxAmount - abs( minAmouny)), and the net amount of ‘y’ person is ‘0’,

# Repeat this process until all the amount will not settle or ‘0’.

 

# Algorithm-

# Create a net amount array ‘netAmount’
# Fill this array, Now for every friend ‘i’
# ‘netAmount[i]’= sum of all received money by ‘i-th’ friend - the sum of all sent money by ‘i-th’ friend.
# Create a 2-D matrix to store the ‘answer’.
# Iterate a while loop until all the values of ‘netAmount’ is not ‘0’
# Find the minimum and maximum of ‘netAmount’
# Suppose ‘x’ index value is the max net amount and ‘y’ index is min net amount, then:
# ‘netAmount[x] = netAmount[x]- abs( netAmount[y])’
# Update ‘answer[y][x] = abs(netAmount[y])
# It represents that the ‘y-th’ friend will pay ‘netAmount[y]’ to ‘x-th’ friend.
# Set ‘netAmount[y] = 0’.
# In the end, return ‘answer’.

# https://www.codingninjas.com/codestudio/problem-details/minimize-cash-flow-among-a-given-set-of-friends-who-have-borrowed-money-from-each-other_1170048

def minCashFlow(mat):
   netBal = [0 for _ in mat]
   result = [[0 for col in row] for row in mat]
   # find net bal
   for i in range(len(mat)):
      for j in range(len(mat[0])):
         netBal[i] += (mat[j][i] - mat[i][j])
   
   while not isAllBalanced(netBal):
      minBal = min(netBal)
      minBalIdx = netBal.index(minBal)
      maxBal = max(netBal)
      maxBalIndex = netBal.index(maxBal)
      netBal[maxBalIndex] += minBal 
      netBal[minBalIdx] = 0
      result[minBalIdx][maxBalIndex] = abs(minBal)
   return result

def isAllBalanced(netBal):
   for bal in netBal:
      if bal != 0:
         return False
   return True


print(minCashFlow([[0, 2000, 4000], [0, 0, 3000], [0, 0, 0]]))