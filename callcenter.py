class Call(object):
	"""docstring for Call"""
	def __init__(self, name, number, time, reason):
		self.name = name
		self.number = number
		self.time = time
		self.reason = reason
	def displayCall(self):
		print "id: {} Name: {} Call Number: {} Time of Call: {} Reason for Call: {}".format(self.__str__, self.name, self.number, self.time, self.reason)
		return self

class CallCenter(object):
	"""docstring for CallCenter"""
	def __init__(self, calls = [], queueSize = 0):
		self.calls = calls
		self.queueSize = queueSize
	def add(self, newCall):
		self.calls.append(newCall)
		self.queueSize+=1
		return self
	def remove(self):
		self.calls.pop(0)
		if self.queueSize > 0:
			self.queueSize-= 1
		return self
	def info(self):
		print "Queue Size: {}".format(self.queueSize)
		for idx in range(0,len(self.calls)):
			print "Name: {} Phone Number: {}".format(self.calls[idx].name, self.calls[idx].number)
		return self
#Ninja Level: add a method to call center class that can find and remove a call from the queue according to the phone number of the caller.
	def removeByNum(self, number):
		for idx in range(0, len(self.calls)):
			if self.calls[idx].number == number:
				self.calls.pop(idx)
				self.queueSize-=1
				break
		return self
# Hacker Level: If everything is working properly, your queue should be sorted by time, 
# but what if your calls get out of order? Add a method to the call center class that sorts the calls 
# in the queue according to time of call in ascending order.
#
#I Will Come back to the Hacker Challange when I have a better understanding of how to hash out and evaluate a Time Stamp or Date Stamp.



call1 = Call('Stephen Silverstein', '703-622-0531', '6:00 PM', 'Freaking out for PM Class homework backlog')
call2 = Call('Stephen Silverstein', '703-622-0531', '6:00 PM', 'Freaking out for PM Class homework backlog')
call3 = Call('Stephen Silverstein', '703-622-0531', '6:00 PM', 'Freaking out for PM Class homework backlog')
call4 = Call('Stephen Silverstein', '703-622-0531', '6:00 PM', 'Freaking out for PM Class homework backlog')
call5 = Call('Stephen Silverstein', '703-622-0531', '6:00 PM', 'Freaking out for PM Class homework backlog')
call6 = Call('Stephen Silverstein', '703-622-0531', '6:00 PM', 'Freaking out for PM Class homework backlog')
call7 = Call('Stephen Silverstein', '703-622-0531', '6:00 PM', 'Freaking out for PM Class homework backlog')
callCenter = CallCenter()
callCenter.add(call1)
callCenter.add(call2)
callCenter.add(call3)
callCenter.add(call4)
callCenter.add(call5)
callCenter.add(call6)
callCenter.add(call7)
callCenter.info()
callCenter.remove().remove().remove().info()
callCenter.removeByNum('703-622-0531').info()
