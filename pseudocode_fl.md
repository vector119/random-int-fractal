### Algorithm for **_fl_** 

initialize a mutable indexed array '**fl**'  
define integer variable **k**, assign the value **1**    

**for** each **i** in **interval [0, n)**    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;define an integer variable **k0** and assign **k** to it  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;define a tuple variable **t** and store the integers in interval **[n * i + k, n * i + k + n - 1)** to it in sequence  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;append **t** to **fl**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**decrease** the value of **k** by **1** and reassign it to **k**, i.e overwrite  
end **for**
