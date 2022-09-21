import re
from tqdm import tqdm
if __name__ == '__main__':
	count=0
	num_lines = 2105324624
	divisor=80
	trgt_lines = int(num_lines/divisor)
	src='en.txt'
	trgt='train.txt'

	f2=open(trgt, 'a')
	with open(src, 'r') as f1:
		#for line in f1:
		for i in tqdm(range(trgt_lines)):
			line=f1.readline()
			data=re.sub('[.,!?\'\"-;:\]\[\{\}\(\)@–]', '', line.lower())
			data=data.encode('ascii', 'ignore').decode()
			data=data.strip()
			f2.write(data)

	f2.close()
			
