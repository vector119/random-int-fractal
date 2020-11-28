## Algorithm for generating a fractal

1. Choose any regular polygon. Store its number of sides in an _int_ variable, let it be called **n**.
2. Plot the corners of the polygon on the plane and label them.  
Steps to plot the polygon:  
   1. Find the **n**th roots of _Unity_ and store them in an _indexed_ array, call it **l**.
   2. Using a _for loop_, plot each of these roots on the plane, preferrably by individually plotting the real part  
      **Re(z)** and the imaginary part **Im(z)** for each **z** in **l**.
      
Now consider a hypothetical dice of _n(n-1)_ number of numbered sides. If this dice is rolled, the possibilities would be any  
integer within **[1, n(n-1)]**. Hence, we need to store the possibilities in the following very specific manner:

3. Construct an _indexed_ array containing **n** _tuples_ each in turn containing sets of **(n-1)** integers _in order_
   starting from **1** through **n(n-1)**, call this array **fl** (short for **Factor List**).
   * _The pseudo-code for accomplishing the above task is mentioned in [another file](https://github.com/vector119/random-int-fractal/blob/main/pseudocode_fl.md)_  
   For example, if we consider a _pentagon_, then **n** == 5, thus **fl** will look like this:  
   **[(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12), (13, 14, 15, 16), (17, 18, 19, 20)]**
   
At this point, there are _two arrays_: **l**, containing the **n**th roots of _Unity_; and **fl**, containing the  
possible outcomes when a **n(n-1)** faced dice were rolled, in **n** _tuples_ each storing **n-1** integers in order, from  
**1** to **n(n-1)**.

4. Ask the user to input a random abscissa and a random ordinate to get a random point, and plot it.  
   * (_Store the abscissa and ordinate in two **float** variables **x** and **y**, respectively._)
5. Ask the user for the number of iterations, store in an _int_ variable **m**.
6. Now this is going to be the main step in generating the fractal. Its broken into substeps as follows:
   1. Generate a random integer within the interval **[1, n(n-1)]**, store it in an _int_ variable **d**.
   2. Start a _for loop_ to sequentially check each of the _tuples_ in **fl** for the existence of **d** in it.
   3. If the desired _tuple_ is found, remember its index, which, let's say, is **i**.
   4. Now call the element in **l** which has its index equal to **i**, let's denote it with **z[i]**.
   5. Plot the point having coordinates as:
      * Abscissa: **(x + _Re(z[i])_)/(n - 1)**
      * Ordinate: **(y + _Im(z[i])_)/(n - 1)**
   6. Overwrite **x** and **y**:
      * **x = (x + _Re(z[i])_)/(n - 1)**
      * **y = (y + _Im(z[i])_)/(n - 1)**
   7. Break the loop.
7. Iterate **_Step 6_** **m** times.
