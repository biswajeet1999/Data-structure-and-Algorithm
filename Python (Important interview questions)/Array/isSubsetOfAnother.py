def check(arr1, arr2):
   cache = {ele: True for ele in arr1}
   for ele in arr2:
      if ele not in cache:
         return False
   return True

