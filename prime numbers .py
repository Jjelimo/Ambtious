def primechecker(numbers):
	""" this is a function that checks my numbers"""
	for number in numbers:
		if number<2:
			print ("It is not prime number")
		elif number==2:
			print ("it is a prime number")
		elif number%2==0:
			print ("it is an even number but  not a prime number")
		elif number%2:
			print ("it is an odd number but not a prime number")
		else:
		    print("it is a prime number")
		print(number)
		
