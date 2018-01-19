import csv
from linkcost import Link_cost

f = open('data.csv','r')
reader = csv.reader(f)
column = [row[0] for row in reader]
column = column[1::]               
data_amount = len(column)         #amount of link 

reader = csv.reader(open('data.csv','r'))
ftt = [row0[0] for row0 in reader][1::]
for i in range(data_amount):
	ftt[i] = float(ftt[i])
	
reader = csv.reader(open('data.csv','r'))
xa = [row[1] for row in reader][1::]
for i in range(data_amount):
	xa[i] = float(xa[i])
	
reader = csv.reader(open('data.csv','r'))
ca = [row[2] for row in reader][1::]
for i in range(data_amount):
	ca[i] = float(ca[i])

reader = csv.reader(open('data.csv','r'))
al = [row[3] for row in reader][1::]
for i in range(data_amount):
	al[i] = float(al[i])
	
reader = csv.reader(open('data.csv','r'))
be = [row[4] for row in reader][1::]
for i in range(data_amount):
	be[i] = float(be[i])

data_amount_list = range(data_amount)

global ODcars
ODcars = 1200.0 # the amount of xa

Z = 0.0
z = []
t = []   # the cost value of each path
y = [] 
d = []
xi = 0.0

# initial the z list and Z
for i in range(data_amount):
	formula = float(ftt[i])*(float(xa[i])**float(be[i]))+ 0.5 *float(ftt[i])*float(al[i])*(float(ca[i])**(-float(be[i])))*(float(xa[i])**(2*float(be[i])))
	z.append(formula)

def linkcost(i):
	linkcost = Link_cost(float(ftt[i]),float(xa[i]),float(ca[i]),float(al[i]),float(be[i]))
	return linkcost

# initial the t list
for i in range(data_amount):
	t.append(linkcost(i).count())
	
def z_count():
	global Z
	for i in range(data_amount):
		formula = float(ftt[i])*(float(xa[i])**float(be[i]))+ (float(be[i])+1) *float(ftt[i])*float(al[i])*(float(ca[i])**(-float(be[i])))*(float(xa[i])**( 1 + float(be[i])))
		z[i] = formula
		Z +=float(z[i])
		
def t_count():
	for i in range(data_amount):
		t[i] = linkcost(i).count()
		
def d_count():
		for i in range(data_amount):
			d[i] = y[i] - xa[i]
		
# initial y list
for i in range(data_amount):
	y.append(0.0)
# initial d list
for i in range(data_amount):
	d.append(0.0)

def xi_count():
'''
	up = []
	UP = 0.0
	down = []
	DOWN = 0.0
	for i in range(data_amount):
		up.append(0.0)
	for i in range(data_amount):
		down.append(0.0)
	for i in range(data_amount):
		up[i] = d[i]*(linkcost(i).count())
		UP += up[i] 
	for i in range(data_amount):
		down[i] = (float(ftt[i]) * float(al[i]))/(float(ca[i])**float(be[i]))*(float(d[i])**2)
		DOWN += down[i]
'''
	for i in range(data_amount):
		xi[i] = (-float(xa[i])+(((-float(ftt[i])*float(d[i])*(float(ca[i])**float(be[i])))/(float(ftt[i])*float(al[i])))**(1/float(be[i]))))/float(d[i])
	return xi
	
	



def start(limit):
	# 'n = 1' = 'round 1'
	n = 1   
	#found the location of min cost link
	location = t.index(min(t))
	# updata the xa list
	xa[location] = ODcars 
	while n <= limit:
		#count t list
		t_count()
		
		#count y list
		y[location] = 0.0
		
		#updata location
		location = t.index(min(t))
		
		#updata y list
		y[location] = ODcars
		
		#count Z
		z_count()
		
		#count d list
		d_count()
		
		xi = xi_count()
		
		for i in range(data_amount):
			xa[i] = xa[i] + xi * d[i]
		print xa
		n +=1

start(50)













