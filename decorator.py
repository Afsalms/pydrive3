


def exception_handle_decorator(function):
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