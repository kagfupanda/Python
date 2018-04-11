#!/usr/bin/env python3

def printBin(remlist):
  remlen = len(remlist)
  if remlen < 5:
      print(''.join(str(i) for i in remlist))
  else:
      for i in remlist:
         if remlen % 4 ==0:
            print(".",end="")
         print(str(i), end="")
         remlen = remlen - 1 
      print("")
  return

def neg2bin(val):
   val = ~val #take ones compliment
   twosval = val + 1 # 2s compliment
   # call bin2dec to get twosval's binary rep
   twosbinrep = bin2dec(twosval)
   #print the reseult as binary bits
   printBin(twosbinrep)
   return

# bin2dec prints binary representation of postive numbers
def bin2dec(val):
   print("enter bin2dec input = {0} ".format(val))
   if val < 0:
       print("{0} is invalid value".format(val))
       neg2bin(val) # call neg to bin function for negative value 
       return
   remlist = [] # create an empty list to save remainders
   while val > 0:
       bit = val % 2 # get a bit by saving the remainder
       remlist.insert(0, bit) #insert the beginning of the list
       val = val // 2 #get integer quotient, update val for next loop iteratio
   print("{0} is the length of the remlist".format(len(remlist)))
   if len(remlist) > 0:
       print(''.join(str(i) for i in remlist))
   else:
      print(0)
      return [0] # return a list with just 1 bit, zero
      return remlist # return the bits
   print("binary string in an easy to read format")
   printBin(remlist)
   print("after printBin returned")
   return remlist
   

if __name__ == "__main__":
    print("in {0}".format ("main"))
    print("call bin2dec function")
    bin2dec(15)
    bin2dec(-1)

