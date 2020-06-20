# Angkan Biswas
# Numpy Array Initialization
# 20.06.2020

import pickle
import os

a = [1, 23.45, 'Angkan', 'Dhaka', [12, 33, 4]]
print('a: {}'.format(a))

'''	To save the previous list into a pickle file.	
	*	Pickle deal with binary format, therefore 'b'
		is necessary with 'w', i.e., 'wb' needs to be 
		written.
	*	Any string is fine as extension. However,
		'.pkl' or '.pickle' are widely used since they
		are used in the Python2 or Python3 documentation.
'''
saveFile = '/home/dell/PythonCode/Code/BasicPython/List.pkl'
fp = open(saveFile, 'wb')
pickle.dump(a, fp)
fp.close()


'''	To load a list from an existing pickle file.	'''
loadFile = '/home/dell/PythonCode/Code/BasicPython/List.pkl'
if (os.path.exists(loadFile) == True):
	fp = open(loadFile, 'rb')
	b = pickle.load(fp)
	fp.close()
	
	print('b: {}'.format(b))
