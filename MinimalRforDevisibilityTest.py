prime = int(input("Please insert a prime number: ")) 

integersArray = [1,2,3,4,5,6,7,8,9]
primeMultiplied = []
theOnesWithNineOrOne = [] 


if prime >=3 & prime <= 999983 & prime != 5: 
  for element in integersArray: 
    temp = element * prime
    primeMultiplied.append(temp)
  
#for testing purposes  for N in primeMultiplied: 
#for testing purposes    print(N)


print()
print()


for elem in range(0,9): 
  temp1 = primeMultiplied[elem]
  temp2 = str(temp1)


  if temp2[-1] == '9' or temp2[-1] == '1': 
    theOnesWithNineOrOne.append(temp2)


theMinimalNumber = min(theOnesWithNineOrOne)
theNumberWeNeed = len(theMinimalNumber)
print(theNumberWeNeed)

