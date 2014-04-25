

def is_prime(number):
	"""
	Function to check if the number is prime or not
	"""
	if number <=1:
		return False
	
	for index in range(2,number):
		if(number%index==0):
			return False
	
	return True