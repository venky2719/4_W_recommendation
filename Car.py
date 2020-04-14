class Car(object):
	"""docstring for Car"""
	model = "" 
	brand = ""
	price = ""
	engineSize = ""
	fuelType = ""
	overall_rat = ""
	
	def __init__(self, attributes):
		super(Car, self).__init__()
		self.attributes = attributes
		self.merge_attributes()

	def merge_attributes(self):
		self.model = self.attributes[0] 
		self.brand = self.attributes[1]
		self.price = self.attributes[3]
		self.engineSize = self.attributes[4]
		self.fuelType = self.attributes[5]
		self.overall_rat = self.attributes[6]
		
	def print_attributes(self):
		s = "Model: " + self.model + "\nBrand: " + self.brand + "\nPrice: " + self.price + "\nEngine Size: " + self.engineSize + "\nFuel Type: " + self.fuelType + "\nOverall Ratings: " + self.overall_rat
		return s

class Maruti(Car):
	"""docstring for Maruti"""
	def __init__(self, attributes):
		super().__init__(attributes)
		self.label = "Maruti"

	def print_attributes(self):
		s = "Label: " + self.label + "\nModel: " + self.model + "\nBrand: " + self.brand + "\nPrice: " + self.price + "\nEngine Size: " + self.engineSize + "\nFuel Type: " + self.fuelType + "\nOverall Ratings: " + self.overall_rat
		return s

class SUV(Car):
	"""docstring for SUV"""
	def __init__(self, attributes):
		super().__init__(attributes)
		self.label = "SUV"
	def print_attributes(self):
		s = "Label: " + self.label + "\nModel: " + self.model + "\nBrand: " + self.brand + "\nPrice: " + self.price + "\nEngine Size: " + self.engineSize + "\nFuel Type: " + self.fuelType + "\nOverall Ratings: " + self.overall_rat
		return s

class MPV(Car):
	"""docstring for SUV"""
	def __init__(self, attributes):
		super().__init__(attributes)
		self.label = "MPV"

	def print_attributes(self):
		s = "Label: " + self.label + "\nModel: " + self.model + "\nBrand: " + self.brand + "\nPrice: " + self.price + "\nEngine Size: " + self.engineSize + "\nFuel Type: " + self.fuelType + "\nOverall Ratings: " + self.overall_rat
		return s

class Hatchback(Car):
	"""docstring for SUV"""
	def __init__(self, attributes):
		super().__init__(attributes)
		self.label = "Hatchback"

	def print_attributes(self):
		s = "Label: " + self.label + "\nModel: " + self.model + "\nBrand: " + self.brand + "\nPrice: " + self.price + "\nEngine Size: " + self.engineSize + "\nFuel Type: " + self.fuelType + "\nOverall Ratings: " + self.overall_rat
		return s

class Pickup(Car):
	"""docstring for Sedan"""
	def __init__(self, attributes):
		super().__init__(attributes)
		self.label = "Pickup"

	def print_attributes(self):
		s = "Label: " + self.label + "\nModel: " + self.model + "\nBrand: " + self.brand + "\nPrice: " + self.price + "\nEngine Size: " + self.engineSize + "\nFuel Type: " + self.fuelType + "\nOverall Ratings: " + self.overall_rat
		return s
