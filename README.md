# The problem with vectorized functions

The programming technique that you have just learned is known as vectorizing arrays.  It is enormously useful as it allows us to write programs that are very short and that thus have few bugs.  The code in `main.py` shows an example of just how useful these vectorised arrays can be.  If you run this program you will see that it generates the plot of the quadratic that was required for an earlier exercise.  As no for loops are required the code is considerably shorter than the version that you wrote in order to pass that exercise.

As was alluded to in the footnote at the end of the previous exercise there is, nevertheless, a small problem with this vectorising of functions.  This problem is related to the way that a program like the one shown below is interpreted:

````
x, y = np.zeros(3), np.zeros(3)
x[0], x[1], x[2] = 1, 2, 3 
y[0], y[1], y[2] = 4, 5, 6
z = x*y
````

When Python evaluates this code  x*y is vectorised in the code above and as such:

````
z[0] = x[0]*y[0] = 1*4 = 4
z[1] = x[1]*y[1] = 2*5 = 10
z[2] = x[2]*y[2] = 3*6 = 18
````

In mathematics, however, a 1D array of numbers like x or y in the above code is a vector.  Importantly, the product of two vectors is not computed by taking an element-wise product in the manner described above.  In maths if ![](https://render.githubusercontent.com/render/math?math=\mathbf{x}) and ![](https://render.githubusercontent.com/render/math?math=\mathbf{y}) are vectors and if we are asked to evaluate ![](https://render.githubusercontent.com/render/math?math=\mathbf{x}.\mathbf{y}) we must evaluate the dot product using:

![](https://render.githubusercontent.com/render/math?math=\mathbf{x}.\mathbf{y}=\sum_{i=1}^Nx_iy_i)

 where ![](https://render.githubusercontent.com/render/math?math=N) is the number of elements in the vectors ![](https://render.githubusercontent.com/render/math?math=\mathbf{x}) and ![](https://render.githubusercontent.com/render/math?math=\mathbf{y}).  

To conclude, vectorised functions in Python are very useful.  Always remember, however, that when we write the product of two vectors or matrices in a mathematical derivation we are not referring to the `A*B` operation for two np.arrays in Python.  We are often doing something more complicated for good reasons!

__To check if you have understood this idea you must write a function called `dotProduct` to complete this exercise.__  This function should take two np.arrays as input and it should return a single scalar.  The single scalar your function returns should be equal to the dot product of the two input vectors, which you can compute using the formula given above.   
