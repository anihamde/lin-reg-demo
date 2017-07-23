import numpy as np

print "Linear Regression where y = 2x exactly"

x_template = [1,-2,5,-4,3]
x_data = [[1,1,1,1,1]]
y_data = [2,-4,10,-8,6]

for i in range(1,5): # building design matrix with the terms 1, x, x^2, x^3, x^4
	vec = []
	for j in range(0,len(x_data[0])):
		vec.append((x_template[j])**i)
	x_data.append(vec)

print x_data

x_data_fin = np.array(x_data).transpose()
y_data_fin = np.array(y_data)
pseudoinv = np.dot(np.linalg.inv(np.dot(x_data_fin.transpose(),x_data_fin)),x_data_fin.transpose()) # moore-penrose pseudoinverse

print np.dot(pseudoinv,y_data_fin)

# Weights: [0  2  0  0  0]




print "Linear Regression where y = 2x with noise"

x_template = [1,-2,5,-4,3]
x_data = [[1,1,1,1,1]]
y_data = [2,-4,10,-8,6] + np.random.normal(0,1,5) # this time, adding in random noise according to a normal distribution

for i in range(1,5): # building design matrix with the terms 1, x, x^2, x^3, x^4
	vec = []
	for j in range(0,len(x_data[0])):
		vec.append((x_template[j])**i)
	x_data.append(vec)

print x_data

x_data_fin = np.array(x_data).transpose()
y_data_fin = np.array(y_data)
pseudoinv = np.dot(np.linalg.inv(np.dot(x_data_fin.transpose(),x_data_fin)),x_data_fin.transpose()) # moore-penrose pseudoinverse

print np.dot(pseudoinv,y_data_fin)

# Weights: [-0.79923854  2.91644087  0.02145831 -0.04581286  0.00318398]