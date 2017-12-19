#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
import numpy as np

### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop("TOTAL",0)
data = featureFormat(data_dict, features)


### your code below
# for point in data:
#     salary = point[0]
#     bonus = point[1]
#     matplotlib.pyplot.scatter( salary, bonus )

# matplotlib.pyplot.xlabel("salary")
# matplotlib.pyplot.ylabel("bonus")
# matplotlib.pyplot.show()

print data

array1 = data[:,0]
array2 = data[:,1]
for key in data_dict.keys():
	new_dict = data_dict[key]
	if new_dict['salary'] != 'NaN' and new_dict['salary'] > 1000000 and new_dict['bonus'] != 'NaN' and new_dict['bonus'] > 5000000:
		print key
		print new_dict

# print p1
# print maxkey