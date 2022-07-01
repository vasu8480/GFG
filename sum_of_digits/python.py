##-----------------------------------------		Method   ------------------------------------------------------
def getSum(n):
	sum = 0
	for i in n:
		sum = sum + int(i)
	return sum
n = "123456789123456789123422"
print(getSum(n))
##-----------------------------------------		Method   ------------------------------------------------------
def sumDigits(no):
	return 0 if no == 0 else int(no % 10) + sumDigits(int(no/10))
print(sumDigits(687))

##-----------------------------------------		Method   ------------------------------------------------------
def getSum(n):
	sum = 0
	while(n > 0):
		sum += int(n % 10)
		n = int(n/10)
	return sum
n = 687
print(getSum(n))
