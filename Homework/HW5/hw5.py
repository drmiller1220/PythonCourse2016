class Node(object):
	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next
	
	def __str__(self):
		return str(self.value)

class LinkedList(object):
	def __init__(self,value=None):	
		if type(value) is int:
			self.value = Node(value)
		elif value==None:
			self.value = None
		else:
			raise NotImplementedError("Node values must be integers.")
	
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
	
	def length(self):
		node = self.value
		i = 1
		while node.next != None:
			i += 1
			node = node.next
		return i
	
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
					node = node.next
					if node != None:
						continue
					else:
						raise NotImplementedError("%d Node does not exist in list." %after_node)
				new_node.next = node.next
				node.next = new_node
		else:
			raise NotImplementedError("Node values must be integers.")
	
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
					node = node.next
					if node != None:
						continue
					else:
						raise NotImplementedError("%d Node does not exist in list." %after_node)
				new_node.next = node.next
				node.next = new_node
		else:
			raise NotImplementedError("Node values must be integers.")
	
	def removeNode(self, node_to_remove):
		if type(node_to_remove) is int:
			first_node = self.value
			target_node = Node(node_to_remove)
			if first_node.value == target_node.value:
				first_node.next = target_node.next
				target_node.next = None
			elif first_node.next.value == target_node.value:
				first_node.next = first_node.next.next
				target_node.next = None
			else:
				node = first_node.next
				while node.next.value != node_to_remove:
					node = node.next
					if node != None:
						continue
					else:
						raise NotImplementedError("%d Node does not exist in list." %after_node)
				node.next = node.next.next
				target_node.next = None
		else:
			raise NotImplementedError("Node values must be integers.")	
	
	#def removeNodesByValue(self, value):
	
	#def reverse(self):
	



