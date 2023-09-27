# -*- coding: utf-8 -*-
"""basic_math_for_cv_part_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FG-1WepZwwTfgmJMui2xlKJ9vFADbFDS

<a href="https://colab.research.google.com/github/labviros/computer-vision-topics/blob/version2020/lesson01-basics/basic_math_for_cv_part_2.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# Basic Mathematics for Computer Vision with Python - Part 2 - Matrices
In this notebook we will cover some  linear algebraic operations and properties of matrices.

##Libraries required
The main library used here is [Numpy](http://www.numpy.org/), wich is part of [Scipy](https://www.scipy.org/) "Python-based ecosystem of open-source software for mathematics, science, and engineering".

To begin with the codes, we use this common import:
"""

import numpy as np
import scipy

"""## Matrices
Two-dimensional arrays are referred to as matrices and, in computer vision, these play a significant role. An image in the digital world is represented as a matrix; hence, the operations that we will study here are applicable to images as well.

Matrix $\mathbf{\mathit{A}}$ is denoted as follows:
> \begin{bmatrix}
a_{11} & a_{12} & \cdots  & a_{1n} \\
a_{21} & a_{22} & \cdots  & a_{2n} \\
\vdots & \vdots  & \vdots  & \vdots \\
a_{m1} & a_{m2} & \cdots  & a_{mn} \\
\end{bmatrix}

Here, the shape of the matrix is $m \times n$ with $m$ rows and $n$ collumns. If $m=n$, the matrix is called a square matrix.
In Python, we can make a sample matrix, as follows:
"""

A = np.array([[1,1.2,3,0],[4,5,6,0],[7,8,92,1]])
print(A)

"""You can also access some properties of the matrix using the basic methods."""

print('Data type:', A.dtype)
print('Matrix size:', A.size)
print('Matrix shape:', A.shape)
print('Rows:', A.shape[0], ' Columns: ', A.shape[1])
print('Data: \n', A)

"""**Attention:** In Python the first index of a row or column of a matrix is represented as 0 (zero).

In order to select one element, one line or one column of the matrix, you can do as follows:
"""

print(A)
# Element from the second line and third column
a23 = A[1,2]
print("Element a23: ", a23)
# First line of the matrix
l = A[0,:]
print("First line: ", l)
# Third colunm
c = A[:,2]
print("Terceira coluna: ", c)
# Accessing a submatrix
s = A[0:2,1:3]
print("Submatrix:\n",s)
s = A[-2,0:-1]
print("Submatrix:\n",s)
s = A[-2,2:]
print("Submatrix:\n",s)

"""## Operation on matrices
We will be performing similar operations on matrices as we did on vectors. The only difference will be in the way we perform these operations. To understand this in detail, go through the following sections.

### Addtion
In order to perform the addition of two matrices $\mathbf{\mathit{A}}$ and $\mathbf{\mathit{B}}$, both of them should be of the same shape. The addition operation is an element-wise addition done to create a matrix C of the same shape as $\mathbf{\mathit{A}}$ and $\mathbf{\mathit{B}}$.

>$C = A + B$

Here is an example:
"""

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[1,1,1],[1,1,1],[1,1,1]])
C = A+B
print(A, '\n')
print(B, '\n')
print(C)

"""### Subtraction
Similar to addition, subtracting matrix $\mathbf{\mathit{B}}$ from matrix $\mathbf{\mathit{A}}$ requires both of them to be of the same shape. The resulting matrix $\mathbf{\mathit{C}}$ will be of the same shape as $\mathbf{\mathit{A}}$ and $\mathbf{\mathit{B}}$.
> $C = A - B$

The following is an example of subtracting $\mathbf{\mathit{B}}$ from $\mathbf{\mathit{A}}$:
"""

A = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
B = np.array([[1,1,1], [1,1,1], [1,1,1]])
C = A - B
print(A, '\n')
print(B, '\n')
print(C)

"""### Matrix multiplication by a scalar"""

A = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])

B = 5*A
print(A, '\n')
print(B, '\n')

"""### Matrix multiplication
Consider two matrices: $\mathbf{\mathit{A}}$ with size $m \times  n$  and $\mathbf{\mathit{B}}$ with size $n \times p$. Now, the two matrices of sizes m x n and n x p are compatible for matrix multiplication, and will result on a matrix of size m x p.

The multiplication is given as follows:
> $C_{m \times p} =A_{m \times n} . B_{n \times p}$

Here, each element in $C$ is given as follows:
> $c_{i,j}=\sum_{k=1}^{n}a_{i,k}b_{k,j}$

Since matrix multiplication depends on the order of multiplication, reversing the order may result in a different matrix or an invalid multiplication due to size mismatch.

This is performed with Python, as follows:
"""

# A matrix of size (2x3)
A = np.array([[1,2,3],[4,5,6]])
# A matrix of size (3x2)
B = np.array([[1,0],[0,1],[1,0]])
C = np.dot(A,B) # size (2x2)

print(A, '\n')
print(B, '\n')
print(C, '\n')

"""##Using np.matrix instead of np.array
Instead of using np.array you can also use np.matrix to define a matrix and perform some operations.
"""

A = np.matrix('1 2 3; 4 5 6')
B = np.matrix('1 0; 0 1; 1 0')
print(A)
print('Matrix shape:',A.shape, '\n')
print(B)
print('Matrix shape:',B.shape, '\n')

"""###Addition"""

A = np.matrix('1 2 3; 4 5 6')
B = np.matrix('1 1 1; 1 1 1')
C = A+B

print(A, '\n')
print(B, '\n')
print(C, '\n')

"""###Subtration"""

A = np.matrix('1 2 3; 4 5 6')
B = np.matrix('1 1 1; 1 1 1')
C = A-B
print(A, '\n')
print(B, '\n')
print(C, '\n')

"""###Multiplication
Note the difference on using np.array and np.matrix for multiplying matrices.
"""

A = np.matrix('1 2 3; 4 5 6')
B = np.matrix('1 0; 0 1; 1 0')
C = A*B
# Also works with np.dot
D = np.dot(A,B)
print(A, '\n')
print(B, '\n')
print(C, '\n')
print(D)

"""We have seen the basic operations with matrices; now we will see some of their properties."""

v = np.array([1,2,3])
v1 = np.array([[1],[2],[3]])
print(v)
print(v1)

print(v[1])
print(v1[1])

"""#Interesting:
A*B also works even if one of the matrices is defined as np.array.
"""

A = np.matrix('1 2 3; 4 5 6')
B = np.array([[1, 1],[0, 1],[1, 2]])
print(A, '\n')
print(B, '\n')
C = A*B
print(C, '\n')
D = B*A
print(D, '\n')

"""## Matrix properties
There are a few properties that are used on matrices for executing mathematical operations. They are mentioned in detail in this section.

### Transpose
When we interchange columns and rows of a matrix with each other, the resulting matrix is called the transpose of the matrix and is denoted as $A^T$ from the original matrix $A$.
An example of this is as follows:
"""

# using np.array
A = np.array([[1, 2, 3],[4, 5, 6]])
print('Matrix A:')
print(A, '\n')
print('A_transpose:')
print(np.transpose(A), '\n')
# A simpler way
print(A.T,'\n')

#using np.matrix
B = np.matrix ('1 2 3; 4 5 6')
print('Matrix B:')
print(B, '\n')
print('B_transpose:')
print(np.transpose(B),'\n')
# A simpler way
print(B.T)

"""### Identity matrix
This is a special kind of matrix with diagonal elements as $1$ and all other elements as zero:
"""

I = np.identity(3) #size of identity matrix
print(I,'\n')
I = np.identity(6) #size of identity, matrix
print(I,'\n')

# Another way
I = np.eye(5)
print(I,'\n')

# Attention
# If we use 2 parameters we get a matrix that is not square
I = np.eye(5,7)
print(I)

I = np.eye(7,5)
print(I)

"""An interesting property of the identity matrix is that it doesn't modify the target matrix after multiplication, that is
> $C=A$.$I$

> or

> $C=I$.$A$

will result in

> $C = A$

### Zero matrix
Some times we need to initialize a matrix with zeros. You can do as:
"""

A = np.zeros((5,3))
print(A,'\n')

B = np.zeros(5)
print(B)

"""### Diagonal matrix
Extending the definition of an identity matrix, in a diagonal matrix, the elements of a matrix along the main diagonal are non-zero and the rest of the values are zero. An example is as follows:
"""

A = np.array([[12,0,0],[0,50,0],[0,0,43]])
print(A)

B = np.diag((12,50,43))
print(B)

"""### Symetric matrix
In a symmetric matrix, the elements follow the property:
> $a_{i,j}=a_{j,i}$

This property, for a given symmetric matrix $A$, can also be defined in terms of its transpose as $A^T=A$

Let's consider an asymmetric $M$ square matrix (with size $n \times n$ ) given as follows:
"""

M = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
print(M)

"""You can compute it's transpose as follows"""

M_T = np.transpose(M)
print(M_T)

"""We can show that  $M+M^T$ is a symetric matrix:"""

print(M + M_T)

"""It can be seen that the elements $m_{i,j}=m_{j,i}$.


### Skew-symmetric Matrix

In a skew-symmetric matrix, the elements follow the property:
> $a_{i,j}=-a_{j,i}$

while the elements of the diagonal are all zero.

> $A = \begin{bmatrix}
0 & -a_{12} &  a_{13} \\
a_{12} &0 &  -a_{23} \\
-a_{13} & a_{23} &  0 \\
\end{bmatrix}$

For a given skew-symmetric matrix $A$, its transpose can be defined as $A^T= -A$.

Following the examples above that used an asymetric $M$ square matrix, we can also compute a skew matrix as $M-M^T$, where each element:
"""

print(M - M_T)

"""An important property arises from this. We can break any square matrix into a summation of a symmetric and a skew  matrix, as follows:
> $M = 0.5 \times \left ( M + M^T \right)+ 0.5 \times \left(M - M^T \right)$

The corresponding Python script to do that is:

"""

print(M,'\n')
symm = M + M_T
skew_symm = M - M_T
print(0.5*symm + 0.5*skew_symm)

"""### Trace of a matrix
The trace of a matrix is the sum of all its diagonal elements:
"""

# using np.array
A = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
print('Matrix: \n', A)
print('Trace: ', np.trace(A),'\n')

#using np.matrix
A = np.matrix('1 2 3; 4 5 6; 7 8 9')
print('Matrix: \n', A)
print('Trace: ', np.trace(A),'\n')

"""### Determinant
Geometrically, it can be viewed as the volume scaling factor of the linear transformation described by the matrix. Or its absolute value can also be considered as the volume enclosed by taking each row of the natrix as a vector. This can be computed, as follows:
"""

A = np.array([[2, 3],[ 5, 6]])
print('Matrix: \n', A)
print('Determinant: ', np.linalg.det(A))

"""### Norm of a matrix
Continuing the norm formulation from the notebook on vectors, in a matrix, the most common type of norm is the Frobenius norm:
> $\left \|  A \right \|= \sqrt{\left({\sum_{i}\sum_{j}a^2_{i,j}} \right )}=\sqrt{tr \left(A^TA \right )}$

In Python we compute this way:
"""

A = np.matrix([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
print('Matrix: \n', A)
print('Norm: ', np.linalg.norm(A),'\n')

# Checking...
R = np.transpose(A)*A
n = np.sqrt(np.trace(R))
print('Matrix: \n', A)
print('Norm: ', n)

"""### Getting the inverse of a square matrix
The inverse of a matrix is usually denoted as $A^{-1}$, and has the following property:
> $AA^{-1} = I = A^{-1}A$

The inverse is unique for each matrix; however, not all matrices have inverse matrices. An example of the inverse of a matrix can be seen below:
"""

A = np.array([[1, 2, 3],[5, 4, 6], [9, 8, 7]])
A_inv = np.linalg.inv(A)
print(A_inv)

"""So, if we ge the product of $A$ and $A^{-1}$, we get the following result"""

np.dot(A,A_inv)

"""We can see that the diagonal elements are *1* and all others are approximately *0*.

### Orthogonality
Another property associated with a square matrix is orthogonality.


If:
> $A^TA=I$

and
> $AA^T=I$

This also leads to
> $A^T=A^{-1}$

This is what happens with a rotation matrix, where $R^T=R^{-1}$ and $det(R) = +1$.
"""

ang = np.pi/7
c_ang = np.cos(ang)
s_ang = np.sin(ang)

R = np.matrix([[c_ang, -s_ang,0 ],[s_ang, c_ang, 0],[0,0,1]])
print (R, '\n')
print (np.transpose(R),'\n')
print (np.linalg.inv(R),'\n')
print(np.dot(R,R.T))

"""### Computing eigenvalues and eigenvectors
The eigenvalue $\lambda$ of a square matrix $A$ has the property such that any transformation on $A$ with the corresponding eigenvector $x$ is equal to the scalar multiplication of $\lambda$ by $x$:
> $Ax=\lambda x$

where
> $x \neq 0$

To compute eigenvalues and eigenvectors of $A$, we need to solve the characteristic equation, as follows:

> $\left | \lambda I-A \right |=0$

Here, $I$ is an identity martix of the same size as $A$.

We can do this using Numpy as follows:
"""

A = np.array([[1, 2, 3],[5, 4, 6], [9, 8, 7]])
eigvals, eigvectors = np.linalg.eig(A)
print("Eigen Values: ", eigvals,'\n')
print("Eigen Vectors:\n", eigvectors)

"""### Singular Value Decomposition
Singular Value Decomposition (SVD) is used to perform decomposition of a matrix $A$ into:
>> $A = U\Sigma V^{T}$

where $U$ and $V^{T}$ are orthogonal matrices and $\Sigma$ is a diagonal matrix:

"""

A = np.array([[10, 2, 3],[5, 43, 6], [93, 8, 71]])
print(A)

U, s, Vt = np.linalg.svd(A, full_matrices=True)
print('Matrix U:\n',U, '\n')
print(np.linalg.det(U),'\n')
print('Diagonal values s: ',s, '\n')
print('Matrix Vt: \n',Vt,'\n')
print(np.linalg.det(Vt),'\n')

S = np.diag(s)

print(S,'\n')

A1 = np.dot(U,np.dot(S,Vt))

print(A1,'\n')