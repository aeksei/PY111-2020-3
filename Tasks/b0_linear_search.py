"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
	"""
	Function that find minimal element in array

	:param arr: Array containing numbers
	:return: index of first occurrence of minimal element in array
	"""
	min_index = 0
	min_ = arr[min_index]

	for index, value in enumerate(arr):
		if value < min_:
			min_index = index

	return min_index
