import random

list = range(1,100)
random.shuffle(list)

### Bubble Sort w/ complexity O(n^2) in the worst case.  Bubble Sort works
### by examining the first two numbers in the list, i and i+1=j, and comparing
### their values.  If i<j, then the numbers remain in their positions and
### the algorithm continues on to the second set of numbers in the list (indexes 1 and 2).
### If i>j, then the positions of i and j are exchanged, and the algorithm continues on
### to the second set of numbers in the current form of the list, which are
### the first and third numbers of the original list.  This process continues
### until the algorithm reaches the final pair of numbers and performs
### the comparison.

def bubblesort(list_numbers):
	for i in range(len(list_numbers)):
		for j in range(i+1, len(list_numbers)):
			if list_numbers[i]>list_numbers[j]:
				list_numbers[i], list_numbers[j] = list_numbers[j], list_numbers[i]
	return list_numbers

### Mergesort w/ complexity O(n log n).  Mergesort works by dividing the original
### unsorted list into sublists, each of which contain one element--and thus
### all of the sublists are internally sorted.  Then, the algorithm merges
### these sublists of equal size, and sorts the list elements as the merges
### is executed; thus, in the first iteration of the 
### algorithm, it merges all lists of length 1 with other lists of length 1
### such that all lists are then of length 2.  The process repeats until
### only 1 list exists.

def mergesort(list_numbers):
	if len(list_numbers) < 2:
		return list_numbers
	midpoint = len(list_numbers)/2
	a = mergesort(list_numbers[:midpoint])
	b = mergesort(list_numbers[midpoint:])
	return merge(a,b)
	
def merge(a,b):
	new_list =[]
	i=0
	j=0
	list_lengths = len(a) + len(b)
	while len(new_list) < list_lengths:
		if a[i] < b[j]:
			new_list.append(a[i])
			i += 1
		else:
			new_list.append(b[j])
			j += 1
		if i == len(a) or j == len(b):
			new_list.extend(a[i:] or b[j:])
	return new_list
	
