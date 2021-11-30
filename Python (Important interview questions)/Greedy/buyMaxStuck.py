def getMaxStocks(price, targetPrice):
   priceWithDay = [(p, i+1) for i, p in enumerate(price)]
   priceWithDay.sort(key=lambda x: x[0])
   itemCount = 0
   for day in priceWithDay:
      p = day[0]
      maxProdCount = day[1]
      maxProductCanBeBought = targetPrice // p
      noOfProductsBought = min(maxProdCount, maxProductCanBeBought)
      itemCount += noOfProductsBought
      targetPrice -= noOfProductsBought * p
      if targetPrice == 0:
         break
   return itemCount

print(getMaxStocks([10, 7, 19], 45))