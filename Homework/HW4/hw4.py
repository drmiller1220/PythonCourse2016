import random

list = range(1,800)
random.shuffle(list)

### Implementing sorting algorithm "slowsort."  According to the
### Big-O Algorithm Complexity Cheat Sheet, slowsort has complexity
### O(n^(log n)) for best, worst, and average case.

### slowsort operates as follows.  First, the list is divided into two
### sublists of equal length.  Then, 

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
			iter_max = a_1
		else:
			right.remove(b_1)
			iter_max = b_1
		list = left + right
		slowsort(list)
	else:
		iter_max = list[0]
	sorted_list.append(iter_max)
	return sorted_list