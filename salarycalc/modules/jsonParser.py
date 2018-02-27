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
	data = jsonFile("../data/BCtax2017.json").load()
	print(data['province'].keys())
	print(data['province']['brk1'][1])
