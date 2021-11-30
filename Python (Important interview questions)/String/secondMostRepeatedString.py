def getSecondMostRepeatedWord(words):
   counter = {}
   for word in words:
      if word not in counter:
         counter[word] = 0
      counter[word] += 1
   maxWord = words[0]
   secondMaxWord = ""

   for word in words[1:]:
      if counter[word] > counter[maxWord]:
         secondMaxWord = maxWord
         maxWord = word
      elif secondMaxWord == "" or (counter[word] > counter[secondMaxWord] and counter[word] < counter[maxWord]):
         secondMaxWord = word
   return secondMaxWord

string = ["geek", "for", "geek", "for", "geek", "aaa"]
print(getSecondMostRepeatedWord(string))
string = ["aaa", "bbb", "ccc", "bbb", "aaa", "aaa"]
print(getSecondMostRepeatedWord(string))