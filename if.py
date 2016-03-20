name=raw_input("What is your name? ")
age=input("How old are you? ")
if age > 2000:
  print name+(" you are an immortal undying vampire")
elif age >90:
  print name+(" you are an extremely old grandpa/grandma")
elif age > 50:
  print name+(" you are very old ")
elif age == 50:
	print name+(" you are middle aged")
elif age < 1:
  print name+(" you do not exist ")
else:
  print name+(" you are quite young")