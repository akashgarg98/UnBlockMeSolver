class Stack(object):

	def __init__(self):
		self.stack = []

	def put(self, obj):
		"""
		Put object into stack.

		@type obj:  any type
		@param obj: object to be placed into the stack
		"""
		self.stack.append(obj)

	def get(self):
		"""
		Gets the most recent item and pops it.

		rtype:   any type
		@return: Object from stack that was popped.
		"""
		return self.stack.pop()

	def empty(self):
		"""
		Checks whether this stack is empty or not

		@rtype:  boolean
		@return: Stack is empty
		"""
		return len(self.stack) == 0