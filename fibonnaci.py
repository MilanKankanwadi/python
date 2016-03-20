print "Enter the number till where Fibinocci to be generated"

num = input ()

lastOneNumber = 1
lastTwoNumber = 1
print lastOneNumber
NewNumber = lastOneNumber + lastTwoNumber
while lastTwoNumber  < num :
	print lastTwoNumber

	NewNumber = lastOneNumber + lastTwoNumber
	lastOneNumber = lastTwoNumber
	lastTwoNumber = NewNumber
