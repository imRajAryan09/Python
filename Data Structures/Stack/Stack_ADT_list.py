# Python program for linked list implementation of stack

# Class to represent a node
class StackNode:

	# Constructor to initialize a node
	def __init__(self, data):
		self.data = data
		self.next = None


class Stack:

	# Constructor to initialize the root of linked list
	def __init__(self):
		self.root = None
        
    # Stack is empty when stack size is 0
	def isEmpty(self):
		return True if self.root is None else False
    
    # Function to add an item to stack. It increases size by 1
	def push(self, data):
		newNode = StackNode(data)
		newNode.next = self.root
		self.root = newNode
		print "% d pushed to stack" % (data)
        
    # Function to remove an item from stack. It decreases size by 1
	def pop(self):
		if (self.isEmpty()):
			return float("-inf")
		temp = self.root
		self.root = self.root.next
		popped = temp.data
		return popped
    
    # Function to return the top from stack without removing it
	def peek(self):
		if self.isEmpty():
			return float("-inf")
		return self.root.data


