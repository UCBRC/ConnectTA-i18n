#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import os
from pprint import pprint

print("Building frontend translations...")

def sortedDictValues3(adict):
    keys = adict.keys()
    keys.sort()
    return map(adict.get, keys)

for subdir, dir, files in os.walk("frontend"):
    for file in files:
        data = json.load(open('frontend/'+file))
        #english = sortedDictValues1(data["en"])
        chinese = sortedDictValues3(data)
        pprint(chinese)


