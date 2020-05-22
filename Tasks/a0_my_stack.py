"""
My little Stack
"""
from typing import Any

stack_list = []  # стек, с которым мы работаем


def push(elem: Any) -> None:
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	global stack_list

	stack_list.append(elem)
	print(elem)
	return None


def pop() -> Any:
	"""
	Pop element from the top of the stack

	:return: popped element
	"""
	global stack_list

	return stack_list.pop() if stack_list else None


def peek(ind: int = 0) -> Any:
	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
	print(ind)
	global stack_list
	if ind >= 0:
		return stack_list[-ind-1]


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	global stack_list

	stack_list = []

	return None
