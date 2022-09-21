import re
from tqdm import tqdm
if __name__ == '__main__':
	count=0
	num_lines = 2105324624
	divisor=300
	trgt_lines = int(num_lines/divisor)
	src='en.txt'
	trgt='train.txt'

	f2=open(trgt, 'a')
	with open(src, 'r') as f1:
		#for line in f1:
		for i in tqdm(range(trgt_lines)):
			line=f1.readline()

			#replace numbers with num token
			data=re.sub('[0123456789]+\.?[0123456789]+', '<num>', line.lower())

			#replaces periods with a space
			data=re.sub('[\.]', ' ', data)

			#remove all punctuation
			data=re.sub('[\$,!?\'\"-;:\]\[\{\}\(\)@–]<>', '', data)

			#filter out unicode
			data=data.encode('ascii', 'ignore').decode()

			#strip the trailing and leading white space
			data=data.strip()
			f2.write(data + '\n')

	f2.close()
			
