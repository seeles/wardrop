
class Link_cost(object):
	
	def __init__(self,free_trip_time,link_traffic_volume,traffic_capacity,alpha=0.48,beta=2.82):
		self.free_trip_time = free_trip_time
		self.link_traffic_volume = link_traffic_volume
		self.traffic_capacity = traffic_capacity
		self.alpha = 1
		self.beta = 1
		
		#self.alpha = 0.48       # the volume from matsui and yamata in 1998.
		#self.beta = 2.82        # the volume from matsui and yamata in 1998.
		

	def count(self):
		ftt = self.free_trip_time
		xa = self.link_traffic_volume
		ca = self.traffic_capacity
		al = self.alpha
		be = self.beta
		
		result = ftt*(1+al*((float(xa)/ca)**be)) # BPR function
		return result
		
	def simplification(self):
		ftt = self.free_trip_time
		xa = self.link_traffic_volume
		ca = self.traffic_capacity
		al = self.alpha
		be = self.beta

		formula = ftt + ftt * al * (float(1) / ca**be ) * xa**be
		ftt = ftt
		a = ftt * al * (float(1) / ca**be )
		u = xa**be
		simple =  ftt + a * u
		return simple
		
# test start
'''
a = Linkcost(0.74,800,400)  
b = a.count()
print b
'''
# test succesed