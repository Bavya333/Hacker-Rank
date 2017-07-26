import csv

with open("number.csv","rb") as f1:
	reader=csv.reader(f1)
	reader=list(reader)
	dicts=[]
	for i in reader:
		for j in i:
			d={'ID':j}
			dicts.append(d)	
with open("fruits.csv","rb") as f2:
	read1=csv.reader(f2)
	read1=list(read1)
	for i,j in enumerate(dicts):
			if i%2==0:
				j['ID']="-1"
	for a in read1:
		for b,k in zip(a,dicts):			
			k['Fruits']=b
	for j,i in enumerate(dicts):
		if i['Fruits']=="":
			no=j-10
			i['Fruits']=dicts[no]['Fruits']
	for r in dicts:
			if r['ID']=="-1": 
				dicts.remove(r)
with open("rotten.csv","rb") as f3:
	with open("price.csv","rb") as f4:
		r3=csv.reader(f3)
		r3=list(r3)
		r4=csv.reader(f4)
		r4=list(r4) 
		for i,j in zip(r3,r4):
			for m,n,k in zip(i,j,dicts):
				if m=='t' or m=='1':
					n='0'
					m='t'
				elif n=="":
					n='0'
				else:
					m='f'
				n=float(n)
				k['Rotten']=m
				k['Price']=n
		
keys=dicts[0].keys()
with open("data.csv","wb") as f:
	dic=csv.DictWriter(f,keys)
	dic.writeheader()
	for i in dicts:
		if i['ID']!="":		
			dic.writerow(i)
				
	 
			
				
				
	

				
				
				
		
