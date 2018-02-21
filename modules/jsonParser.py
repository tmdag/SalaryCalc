import json

class jsonFile:
	def __init__(self, file):
		self.file = file

	def load(self):
		try:
			with open(self.file, 'r') as f:
				data = json.load(f)
				return data
		except Exception as e:
			print("Error loading json file: {}".format(e))

	def save(self, data):
		try:
			with open(self.file, 'w') as f:
				json.dump(data, f,sort_keys=False, indent=2, separators=(',', ': '))
				print("file saved.")
		except Exception as e:
			print("Error saving json file: {}".format(e))

if __name__ == '__main__':
	# Load and test data
	data = jsonFile("BCtax2017.json").load()
	print(data['province'].keys())
	print(data['province']['brk1'][1])

	# DATA --------------------------------------
	provBC={
	"brk1" : [0, 38898, 5.06],
	"brk2" : [38898, 77797, 7.70],
	"brk3" : [77797.01, 89320, 10.5],
	"brk4" : [89320.01, 108460, 12.29],
	"brk5" : [108460, 150000, 14.70],
	"PersonalAmount" : [10208, 5.06]
	}
	federal={
	"brk1" : [0, 45916, 15],
	"brk2" : [45916, 91831, 20.5],
	"brk3" : [91831, 142353, 26],
	"brk4" : [142353, 202800, 29],
	"brk5" : [202800, 999000, 33],
	"PersonalAmount" : [11635, 15]
	}
	ei={
	"maxei" : [51300, 1.63]
	}
	cpp={
	"maxcppContrib" : [55300, 4.95],
	"cppExempt" : 3500
	}
