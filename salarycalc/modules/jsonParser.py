import json

class jsonFile:
	def __init__(self, file):
		self.file = file
		if(self.file==''):
			raise Exception('no file name provided')

	def load(self):
		try:
			with open(self.file, 'r') as f:
				data = json.load(f)
				return data
		except Exception as e:
			print("Error loading json file: {}".format(e))

	def save(self, data):
		if not self.file.lower().endswith(('.json')):
			self.file += ".json"
		try:
			with open(self.file, 'w') as f:
				json.dump(data, f,sort_keys=False, indent=2, separators=(',', ': '), ensure_ascii=False)
				print("file saved: {}".format(self.file))
		except Exception as e:
			print("Error saving json file: {}".format(e))

if __name__ == '__main__':
	# Load and test data
	data = jsonFile("../data/BCtax2017.json").load()
	# print(data['province'].keys())
	# print(data['province']['brk1'][1])
	data = {'info': {'year': 2018, 'prov': 'BC'}, 'privince': {}, 'federal': {}, 'employeeInsurance': {}, 'cpp': {}}
	print(type(data))
	# jsonFile("test.json").save(data)