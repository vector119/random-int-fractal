## Algorithm for generating a fractal

1. Choose any regular polygon. Store its number of sides in an _int_ variable, let it be called **n**.
2. Plot the corners of the polygon on the plane and label them.  
Steps to plot the polygon:  
   1. Find the **n**th roots of _Unity_ and store them in an _indexed_ array, call it **l**.
   2. Using a _for loop_, plot each of these roots on the plane, preferrably by individually plotting the real part  
      **Re(z)** and the imaginary part **Im(z)** for each **z** in **l**.

3. Ask the user to input a random abscissa and a random ordinate to get a random point, and plot it.  
   * (_Store the abscissa and ordinate in two **float** variables **x** and **y**, respectively._)
4. Ask the user for the number of iterations, store in an _int_ variable **m**.
5. Now this is going to be the main step in generating the fractal. Its broken into substeps as follows:
   1. Generate a random integer within the interval **[1, n(n-1)]**, store it in an _int_ variable **d**.
   2. Now store the value of **(floor of (d / (n - 1)) - 1)** in an _int_ variable **i**.
   3. Plot the point having coordinates as:
      * Abscissa: **(x + _Re(z[i])_)/(n - 1)**
      * Ordinate: **(y + _Im(z[i])_)/(n - 1)**
   4. Overwrite **x** and **y**:
      * **x = (x + _Re(z[i])_)/(n - 1)**
      * **y = (y + _Im(z[i])_)/(n - 1)**
   5. Break the loop.
6. Iterate **_Step 5_** **m** times.
