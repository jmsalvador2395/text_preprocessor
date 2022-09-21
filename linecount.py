
import re
if __name__ == '__main__':
	count=0
	num_lines = 2105324624
	trgt_lines = num_lines/2
	src='en.txt'
	with open(src, 'r') as f1:
		for line in f1:
			count+=1
	
	print(f'{count} lines')
