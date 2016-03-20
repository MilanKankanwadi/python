print "Enter the number till where Fibinocci to be generated"

num = input ()

lastOneNumber = 1
lastTwoNumber = 1
print lastOneNumber
print lastTwoNumber
NewNumber = lastOneNumber + lastTwoNumber
while NewNumber < num :
	print NewNumber

	NewNumber = lastOneNumber + lastTwoNumber
	lastOneNumber = lastTwoNumber
	lastTwoNumber = NewNumber
