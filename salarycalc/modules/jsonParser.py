#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Little Json file parsing module
'''
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

	data = jsonFile("../data/BCtax2017.json").load()
	print(type(data))
