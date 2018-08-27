"Create a function that takes a list of numbers and returns the following statistics:
Minimum Value
Maximum Value
Sequence Length
Average Value"

def minMaxLengthAverage(arr):
	return [min(arr), max(arr), len(arr), sum(arr)/len(arr)]
