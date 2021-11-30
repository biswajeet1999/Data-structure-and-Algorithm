# O(n) time | o(n) space
def validateIp(ip):
   oct1, oct2, oct3, oct4 = ip.split(".")
   if(oct1 == "" or int(oct1) < 0 or int(oct1) > 255 or oct1[0] == "0"):
      return False
   if(oct2 == "" or int(oct2) < 0 or int(oct2) > 255 or oct2[0] == "0"):
      return False
   if(oct3 == "" or int(oct3) < 0 or int(oct3) > 255 or oct3[0] == "0"):
      return False
   if(oct4 == "" or int(oct4) < 0 or int(oct4) > 255 or oct4[0] == "0"):
      return False
   return True


# O(27*n) time | O(n) space
def generateIp(string):
   for i in range(0, min(3, len(string))):
      for j in range(i + 1, min(i + 4, len(string))):
         for k in range(j + 1, min(j + 4, len(string))):
            ip = string[: i+1] + "." + string[i+1 : j+1] + "." + string[j+1 : k + 1] + "." + string[k+1 :]
            if(validateIp(ip)):
               print(ip)

string = "25525511135"
generateIp(string)
