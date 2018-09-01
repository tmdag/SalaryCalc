#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Little Json file parsing module helper
'''
import json

class JsonFile:
    ''' Little Json file parsing module helper '''
    def __init__(self, file):
        self.file = file
        if self.file == '':
            raise Exception('no file name provided') 

    def load(self):
        ''' load json file '''
        try:
            with open(self.file, 'r') as jsonfile:
                data = json.load(jsonfile)
                return data
        except Exception as error_msg:
            print("Error loading json file: {}".format(error_msg))

    def save(self, data):
        ''' save json file '''
        if not self.file.lower().endswith(('.json')):
            self.file += ".json"
        try:
            with open(self.file, 'w') as jsonfile:
                json.dump(data, jsonfile, sort_keys=False, indent=2,
                          separators=(',', ': '), ensure_ascii=False)
                print("file saved: {}".format(self.file))
        except Exception as error_msg:
            print("Error saving json file: {}".format(error_msg))

if __name__ == '__main__':

    TESTDATA = JsonFile("../data/BCtax2017.json").load()
    print(TESTDATA)
