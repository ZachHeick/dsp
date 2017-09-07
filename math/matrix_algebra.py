# Matrix Algebra
import numpy as np

A = np.array([[1,2,3], [2,7,4]])
B = np.array([[1,-1], [0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1], [1,2,3]])
u = np.array([[6,2,-3,5]])
v = np.array([[3,5,-1,4]])
w = np.array([[1,8,0,5]]).reshape(4,1)

# Matrix Dimensions
# A
dim_A = A.shape  # 2x3

# B
dim_B = B.shape  # 2x2

# C
dim_C = C.shape  # 3x2

# D
dim_D = D.shape  # 2x3

# u
dim_u = u.shape  # 1x4

# w
dim_w = w.shape  # 4x1

# Vector Operations
# u+v
ans_2_1 = np.add(u,v)  # [9,7,-4,9]

# u-v
ans_2_2 = np.subtract(u,v)  # [3,-3,-2,1]

# au
ans_2_3 = np.multiply(6,u)  # [36,12,-18,30]

# u*v
ans_2_4 = np.dot(u,v.T)  # 51

# ||u||
ans_2_5 = np.linalg.norm(u)  # 8.602

# Matrix Operations
# A+C
ans_3_1 = np.add(A,C)  # Not defined

# A-C.T
ans_3_2 = np.subtract(A,C.T)  # [[-4,-7,-3], [3,6,4]]

# C.T+3D
ans_3_3 = np.add(C.T, np.multiply(3,D))  # [[14,3,3], [2,7,9]]

# BA
ans_3_4 = np.matmul(B,A)  # [[-1,-5,-1], [2,7,4]]

# B(A.T)
ans_3_5 = np.matmul(B,A.T) # Not defined

# BC
ans_3_6 = np.matmul(B,C)  # Not defined

# CB
ans_3_7 = np.matmul(C,B)  # [[5,-6], [9,-8], [6,-6]]

# BBBB
ans_3_8 = np.linalg.matrix_power(B,4)  # [[1,-4], [0,1]]

# A(A.T)
ans_3_9 = np.matmul(A,A.T)  # [[14,28], [28,69]]

# (D.T)D
ans_3_10 = np.matmul(D.T,D)  # [[10,-4,0], [-4,8,8], [0,8,10]]
