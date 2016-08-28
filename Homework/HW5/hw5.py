### Creating class Node.  Adding an attribute "reversal" which will
### be used to reverse the linked list

class Node(object):
	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next
		self.reversal = None
	def __str__(self):
		return str(self.value)

### Creating class LinkedList.  If user tries to create a linked list
### with an initial node value that is not an integer, an error will
### be returned.		
		
class LinkedList(object):
	def __init__(self,value=None):	
		if type(value) is int:
			self.value = Node(value)
		elif value==None:
			self.value = None
		else:
			raise NotImplementedError("Node values must be integers.")

### Established easily readable format for list to be printed for user
### to examine
			
	def __str__(self):
		list_nodes = "Key: (Node Number, Node Value)"
		node = self.value
		counter = 1
		while node.next != None:
			list_nodes += ("\nNode %d: %d" %(counter, node.value))
			counter += 1
			node = node.next
		list_nodes += ("\nNode %d: %d" %(counter, node.value))
		return str(list_nodes)

### Returns the length of the list.  Function begins at the first node,
### and while the node has a next node attached to it, increases the
### counter.  Then, returns the counter.
		
	def length(self):
		node = self.value
		i = 1
		while node.next != None:
			i += 1
			node = node.next
		return i

### Adds node to linked list.  If node that user tries to add is not
### an integer, an error is returned.  Function works by first checking
### if the list has a first node; if it does not, the new node is made
### the first node.  Then, the function checks if the list has only one
### node; if it does, the new node becomes the second node.  Otherwise,
### the function runs through all of the extant nodes with the while loop,
### until it finds the last node in the list and adds the new node to the
### end of the list.
		
	def addNode(self,new_value):
		if type(new_value) is int:
			first_node = self.value
			new_node = Node(new_value)
			if first_node == None:
				first_node = new_node
			elif first_node.next == None:
				first_node.next = new_node
			else:
				node = first_node.next
				while node.next != None:
					node = node.next
				node.next = new_node
		else:
			raise NotImplementedError("Node values must be integers.")

### Adds a new node after a specified node.  If the user tries to add
### a node that is not an integer, and error is returned.  If the
### user tries to add a new node after a node value that does not exist,
### an error is returned.  The function works by first checking if the
### after node is the first node; if it is, the new node's "next" becomes
### the first node's "next," and the first node's "next" then becomes
### the new node.  Then, the function checks if the after node is the
### second node; if it is, then the new node's "next" becomes the second
### node's "next," and then the second node's "next" becomes the new node.
### Otherwise, a while loop is used to pass through the nodes until the
### after node value is found; when it is found, the new node's "next" becomes
### the after node's "next," and then the after node's "next" becomes
### the new node.
			
	def addNodeAfter(self, new_value, after_node):
		if type(new_value) is int:
			first_node = self.value
			new_node = Node(new_value)
			if first_node.value == after_node:
				new_node.next = first_node.next
				first_node.next = new_node
			elif first_node.next.value == after_node:
				second_node = first_node.next
				new_node.next = second_node.next
				second_node.next = new_node
			else:
				node = first_node.next
				while node.value != after_node:
					try:
						node = node.next
						node.next.value != None
					except AttributeError:
						raise NotImplementedError("Node with value %d does not exist in list." %after_node)
				new_node.next = node.next
				node.next = new_node
		else:
			raise NotImplementedError("Node values must be integers.")

### Adds a node before a specified node value.  Works almost identically to
### the after node function, with some slight reordering of whether "nexts"
### are assigned before or after the extant before node.			
			
	def addNodeBefore(self, new_value, before_node):
		if type(new_value) is int:
			first_node = self.value
			new_node = Node(new_value)
			if first_node.value == before_node:
				new_node.next = first_node
				new_node = self.value
			elif first_node.next.value == before_node:
				second_node = first_node.next
				new_node.next = second_node
				first_node.next = new_node
			else:
				node = first_node.next
				while node.next.value != before_node:
					try:
						node = node.next
						node.next.value != None
					except AttributeError:
						raise NotImplementedError("Node with value %d does not exist in list." %before_node)
				new_node.next = node.next
				node.next = new_node
		else:
			raise NotImplementedError("Node values must be integers.")

### Removes the first instance of a node with a specified value. Works similarly
### to the functions which add nodes, but instead of assigning the "nexts"
### to the new node and the before/after node, it reassigns the "next" of the node
### preceding the node to be removed to be the next of the node to be removed.
			
	def removeNode(self, node_to_remove):
		if type(node_to_remove) is int:
			first_node = self.value
			target_node = Node(node_to_remove)
			if first_node.value == target_node.value:
				self.value = first_node.next
			elif first_node.next.value == target_node.value:
				self.value.next = first_node.next.next
			else:
				node = first_node.next
				while node.next.value != node_to_remove:
					try:
						node = node.next
						node.next.value != None
					except AttributeError:
						raise NotImplementedError("Node with value %d does not exist in list." %node_to_remove)	
				node.next = node.next.next
				target_node.next = None
		else:
			raise NotImplementedError("Node values must be integers.")	

### Removes all nodes with a specified value.  Function works similarly
### to the function which removes only the first instance of a node with
### a specified value, but includes a counter which will report how
### many instances of nodes with the value were removed.  If no nodes with
### the value were removed, the user is told that the list did not
### contain any nodes with that value.
			
	def removeNodesByValue(self, node_value_to_remove):
		if type(node_value_to_remove) is int:
			nodes_removed = 0
			first_node = self.value
			target_node = Node(node_value_to_remove)
			if first_node.value == target_node.value:
				self.value = first_node.next
				nodes_removed += 1
			if first_node.next.value == target_node.value:
				self.value.next = first_node.next.next
				nodes_removed += 1
			node = first_node
			while node.next != None:
				if node.next.value == target_node.value:
					node.next = node.next.next
					target_node.next = None
					nodes_removed += 1
					try:
						node = node.next
						node.next.value != None
					except:
						if nodes_removed > 0:
							print "%d nodes with value %d removed." %(nodes_removed,node_value_to_remove)
							break
						else:
							print "No nodes with value% existed in the list." %(node_value_to_remove)
							break
				else: 
					try:
						node = node.next
						node.next.value != None
					except:
						if nodes_removed > 0:
							print "%d nodes with value %d removed." %(nodes_removed,node_value_to_remove)
							break
						else:
							print "No nodes with value %d existed in the list." %(node_value_to_remove)
							break
		else:
			raise NotImplementedError("Node values must be integers.")

### Function reverses the order of the list.  Function first checks if
### the list is of length 1; if it is, the list is returned as-is.
### Otherwise, the function works its way through the list as it exists,
### adding to each node the attribute "reversal," which takes as a value
### the node which precedes it.  When the end of the list is reached, the 
### last node is assigned to be the new first node, and the function
### works through the preceding nodes via the reversal attribute to reassigns
### the reversal attribute value to the next attribute value, such that the list
### is reversed.
			
	def reverse(self):
		first_node = self.value
		if self.value.next == None:
			pass
		else:
			node = self.value
			while node.next != None:
				node.next.reversal = node
				node = node.next
			self.value = node
			current_node = self.value
			while current_node != None:
				current_node.next = current_node.reversal
				current_node =  current_node.reversal
				
		
	
	
	

#######
####### Testing functionality
#######

### Create a new list
test_list = LinkedList(2)

### Add nodes to list, appending at end of list
test_list.addNode(9)
test_list.addNode(7)
test_list.addNode(5)
test_list.addNode(3)

### Print list
print test_list

### Obtain length of list--should be 5
test_list.length()

### Add a node with value 8 to the list before the node with
### value 5
test_list.addNodeBefore(8,5)

### Print list to verify node was added correctly
print test_list

### Obtain length to make sure length now equals 6
test_list.length()

### Add a node with value 11 to the list after the node with value 7
test_list.addNodeAfter(11,7)

### Print list to verify node was added correctly
print test_list

### Obtain length to make sure length now equals 7
test_list.length()

### Add nodes with duplicate values to the end of the list
test_list.addNode(9)
test_list.addNode(7)
test_list.addNode(5)
test_list.addNode(3)

### Remove first instance of node with value 9
test_list.removeNode(9)

### Print list to verify node was removed correctly
print test_list

### Obtain length to make sure length now equals 10
test_list.length()

### Removes all nodes with value 7
test_list.removeNodesByValue(7)

### Print list to verify all nodes with values of 7 were removed
print test_list

### Reverses order of list
test_list.reverse()

### Print list to verify that order was reversed
print test_list

###################
### Testing exceptions

### Cannot create list with a starting node with a non-integer value
str_list=LinkedList("string")

### Cannot add node with non-integer value
test_list.addNode("string")
test_list.addNodeBefore("string",9)
test_list.addNodeAfter("string",9)

### Cannot add node if before or after value does not exist
test_list.addNodeBefore(10,75)
test_list.addNodeAfter(10,75)
test_list.removeNode(75)

### User will be informed that no nodes with specified value
### existed in the list to be removed
test_list.removeNodesByValue(12)

##########################

### Complexity guesstimates? (I am not sure if I am calculating these
### correctly) (using worst case to calculate)

### initialization: O(1)

### str : O(3(n-1) +1)-- for each n-1, three operations are conducted
### in the while loop, and then for the one remaining node there is
### an operations

### length: O(2n)-- for each n, two operations are conducted in the
### while loop

### addNode: O(3+(n-2))--three if conditions are checked, and then the n-2 remaining
### nodes are cycled through in the while loop

### addNodeBefore and addNodeAfter: O(3+(n-2))--three conditions are
### checked, and then the nodes are cycled through the while loop

### removeNode: O(3+(n-2))--three conditions are
### checked, and then the nodes are cycled through the while loop

### removeNodesByValue: O(3+(n-1+1))---three conditions are checked, and then 
### the nodes are cycled through the while loop which contains an if/
### else statement.  Then, once the list reaches its end, a final if/else
### statement is executed

### reverse: O(3n)--each node is subjected to an if/else statement, and two
### while loops

### the functions which involve adding/removing notes are probably suboptimal
### because they involve additional if/else statements for the first and
### second nodes, rather than running one while statement which accounts for
### all nodes, so adjusting the function to have one while loop would probably
### reduce complexity slightly