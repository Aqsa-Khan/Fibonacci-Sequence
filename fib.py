#program to return fib numbers under 50

#previous number variable
prev_num = 1
#current number variable
cur_num = 1

#print first base case
print(prev_num)

#while loop, while cur_num is less than 50
while(cur_num < 50):
	print(cur_num)

	#update values with temporary variables
	prevTemp = prev_num
	curTemp = cur_num

	#yes i'm doing this with an excessive number of variables
	#you can do this with 3 variables
	prev_num = curTemp
	cur_num = prevTemp + curTemp
