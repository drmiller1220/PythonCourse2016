#Exercise 1
#Write a function to calculate the greatest common divisor of two numbers

def gcf(num1, num2):
	if num1 and num2 <1:
		return "Both inputs must be greater than or equal to 1."
	if num1%num2 == 0:
		return num2
	elif num2%num1 == 0:
		return num1
	else:
		if num1>num2:
			for i in range(num2-1,0,-1):
				#if num2%i==0 and num1%i==0:
					if gcf(num1,i)==i and num2%i==0:
						return i
		else:
			for i in range(num1-1,0,-1):
				#if num1%i==0 and num2%i==0:
					if gcf(num2,i)==i and num1%i==0:
						return i
					

#def gcf(num1, num2):
#	if num1 and num2 <1:
#		return "Both inputs must be greater than or equal to 1."
#	if num1%num2 == 0:
#		return num2
#	elif num2%num1 == 0:
#		return num1
#	else:
#		if num1>num2:
#			num2_a = num2-1
#			gcf_1 = gcf(num1,num2_a)
#			if num2%gcf_1 ==0:
#				return gcf_1
#			else:
#				gcf(num1, num2_a)
#		else:
#			num1_a = num1-1
#			gcf_2 = gcf(num1_a,num2)
#			if num1%gcf_2 ==0 & num2%gcf_2==0:
#				return gcf_2
#			else:
#				gcf(num1_a, num2)

#Exercise 2
#Write a function that returns prime numbers less than 121

list=[]

def prime_list(num):
	in_list = []
	for j in range(num-1,1,-1):
		if num%j==0:
			pass
		else:
			in_list.append(j)
	if range(num-1,1,-1) == in_list:
			list.append(num)
	if num>2:
		prime_list(num-1)
	else:
		print list

#Exercise 3
#Write a function that gives a solution to Tower of Hanoi game
#https://www.mathsisfun.com/games/towerofhanoi.html



