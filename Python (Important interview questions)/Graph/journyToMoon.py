
def find(sett, u):
   if sett[u] < 0:
      return u
   sett[u] = find(sett, sett[u])
   return sett[u]

def fact(n):
   fact = 1
   for num in range(1, n+1):
      fact *= num
   return fact

def combination(n, r):
   return fact(n)/(fact(n-r)*fact(r))


# O(V + E + V + V + V) time | O(V) space
# V = no of countries, E = no of pairs
def journyToMoon(pairs, n):
   countries = {i: -1 for i in range(n)}

   for pair in pairs:
      u = find(countries, pair[0])
      v = find(countries, pair[1])
      if u != v:
         noOfElementsInU = countries[u]
         countries[u] = v
         countries[v] += noOfElementsInU
   countryList = []

   for count in countries.values():
      if count < 0:
         countryList.append(-count)
   totalCombinations = combination(n, 2)
   invalidCombinations = 0
   for c in countryList:
      invalidCombinations += combination(c, 2)
   return int(totalCombinations - invalidCombinations)

print(journyToMoon([[0, 1], [2, 3], [0, 4]], 5))
