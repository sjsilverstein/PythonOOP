class Patient(object):
	"""docstring for Patient"""
	def __init__(self, name, allergies, bednum = 'none'):
		self.name = name
		self.allergies = allergies
		self.bednum = bednum

class Hospital(object):
	"""docstring for Hospital"""
	def __init__(self, name, capactiy, patients = []):
		self.name = name
		self.capactiy = capactiy
		self. patients = patients
	def admit(self, patient):
		if len(self.patients) <= self.capactiy:
			self.patients.append(patient)
			patient.bednum = len(self.patients)
			print "Patient {} addmited in Bed Number {}".format(patient.name, patient.bednum)
		else:
			print "Patient {} not addmited Hospital {} at capactiy".format(patient.name, self.name)
		return self
	def discharge(self, patient):
		for idx in range(0, len(self.patients)):
			if self.patients[idx] == patient or self.patients[idx].name == patient:
				self.patients[idx].bednum = 'none'
				print "Discharging {} from {}".format(self.patients[idx].name, self.name)
				self.patients.pop(idx)
				break
			else:
				print "{} not found in {}".format(patient, self.name)
		return self


stephen = Patient('Stephen Silverstein', 'None')
ccd = Hospital('CCD', 2)
ccd.admit(stephen).discharge('Stephen Silverstein')