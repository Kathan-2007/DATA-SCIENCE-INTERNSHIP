import numpy as np 

#1D Numpy array
arr1=np.array([1,2,3,4,5,6])
print(arr1)

#2D array
arr2=np.array([[1,2,3],[4,5,6]])
print(arr2)

#array oprations
arr = np.array([[10, 20, 30], [40, 50, 60]])

print("Shape:", arr.shape)     # (2, 3) → 2 rows, 3 columns
print("Size:", arr.size)       # 6 → total elements
print("Dimensions:", arr.ndim) # 2 → 2D array
print("Data type:", arr.dtype) # int64 (or int32 on Windows)

print(np.zeros((3, 3)))        # 3x3 array of zeros
print(np.ones((2, 4)))         # 2x4 array of ones
print(np.full((2, 2), 7))      # 2x2 array filled with 7
print(np.eye(4))               # 4x4 identity matrix
print(np.arange(1, 10, 2) )    # [1, 3, 5, 7, 9] (like range)
print(np.linspace(0, 1, 5))    # [0. 0.25 0.5 0.75 1.] (evenly spaced)

print("Addition :" , (arr+arr2))
print("multiplication:" ,(arr*arr2))
print("Scalar Multiplication" ,(arr2*5))

# Statistical Calculations
print("Dataset:", arr1)     
print("Sum:",np.sum(arr1))
print("Mean (Average):",np.mean(arr))
print("Standard Deviation:",np.std(arr1).round(2))
print("Minimum Value:",np.min(arr1))
print("Maximum Value:",np.max(arr1))

#Sliceing and indexing
arr3 = np.array([10, 20, 30, 40, 50, 60])
print(arr3[0])  
print(arr3[-1]) 

 
print(arr3[1:4])  
print(arr3[:3])   
print(arr3[::2])