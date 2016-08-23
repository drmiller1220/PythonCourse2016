list = range(1,100)
random.shuffle(list)

sorted_list=[]

def slowsort(list):
	if len(list)>1:
		a = 1
		b = len(list)
		m = (a+b)/2
		left = list[:m]
		right = list[m:]
		a_1 = max(left)
		b_1 = max(right)
		if a_1>b_1:
			left.remove(a_1)
			sorted_list.append(a_1)
		else:
			right.remove(b_1)
			sorted_list.append(b_1)
		list = left + right
		slowsort(list)
	else:
		sorted_list = sorted_list + list
		return sorted_list