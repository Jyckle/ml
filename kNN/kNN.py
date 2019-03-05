import math
import pandas as pd

df=pd.read_csv('train.csv')
df.head()


def distance(point_a,point_b):
	dist = 0
	for a,b in zip(point_a,point_b):
		dist=dist+(a-b)**2
	return math.sqrt(dist)

a = [2,4]
b = [6,1]

print(distance(a,b))
