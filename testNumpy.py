import numpy as np, cv2
import matplotlib

test = np.arange(5, dtype = np.int64)
test2 = np.linspace(0, 10, 5, dtype = np.int64)

# print(test)

test12 = np.concatenate(([test], [test2]))

# test12 = test12[:, np.newaxis]

# fiveup = (test12>5)

#axis = 0 is for rows
#axis = 1 is for columns
#don't go beyond 2d arrays bro

maxtestRow = test12.max(axis = 0)
maxtestCol = test12.max(axis = 1)
print(maxtestRow)
print(maxtestCol)

print(test12)
print(test12.shape, test12.size, test12.ndim)
#print(test, test2)
#testing numpy