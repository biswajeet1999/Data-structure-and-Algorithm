# logic:- n th number can be found in (startNumber + gap + gap + gap...... n times)
# which is also termed as startNumber + n*gap = nth term.
# so if nth term is integer it means the nth term number exists

# O(1) time | O(1) space
def checkExists(startNumberInSeq, gap, targetNumber):
   return (targetNumber - startNumberInSeq) / gap == (targetNumber - startNumberInSeq) // gap

print(checkExists(1, 2, 3))