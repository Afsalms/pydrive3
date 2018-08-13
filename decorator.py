


def exceptions_handler(function):
	"""
	Decorator for pydrive3 for handling the exceptions:
	:params function: ipnut function
	:return the wrapper funcation if no exception else raise the exceptions
	"""

	def wrapper(*args, **kwargs):
		"""
		Wrapper function for fuction
		:params args: Poistion arguments for the function
		:params kwargs: Keyword argument for the function
		:return the fucntion case of no exception occured else raise the excption
		"""

		try:
			return function(*args, **kwargs)
		except Exception as e:
			print(e)
			# print(type(e))
	return wrapper