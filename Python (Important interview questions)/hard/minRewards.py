# O(n) time | O(n) space
# expand arround local minima method
# def minRewards(lst = []):
#    rewards = [None for _ in lst]
#    for i in range(len(lst)):
#       if (i == 0 and lst[i] < lst[i+1]) or (i == len(lst)-1 and lst[i-1] > lst[i]) or (lst[i-1] > lst[i] < lst[i+1]):
#          rewards[i] = 1
#          lft = i - 1
#          while lft >=  0 and lst[lft] > lst[lft + 1]:
#             if rewards[lft] is None:
#                rewards[lft] = rewards[lft + 1] + 1
#                lft -= 1
#             else:
#                # update maxima between 2 minima 
#                rewards[lft] = max(rewards[lft], rewards[lft+1] + 1)
#                break
#          rgt = i + 1
#          while rgt < len(lst) and rewards[rgt] is None and lst[rgt] > lst[rgt - 1]:
#             rewards[rgt] = rewards[rgt - 1] + 1
#             rgt += 1
#    return rewards



# O(n) time | O(n) space
def minRewards(lst = []):
   rewards = [1 for _ in lst]
   for i in range(1, len(lst)):
      if lst[i] > lst[i-1]:
         rewards[i] = rewards[i-1] + 1
   for i in range(len(lst) - 2, 0, -1):
      if lst[i] > lst[i+1]:
         rewards[i] = max(rewards[i], rewards[i+1] + 1)
   return rewards



# lst = [8, 4, 2, 1, 3, 6, 7, 9, 5]
lst = [2, 6, 4, 2, 1, 2, 4, 8, 4, 2, 1, 2]
print(minRewards(lst))