### Numerical Iterator
A collection of python scripts to show the iteration process for various algorithms from Numerical Analysis like bisection, False position, Fixed Point iteration, Newton – Raphson, secant, golden search etc.

### Example Usage:

Bisection method (bisection.py)
> x^3 - 2x - 5
```python
# set upper & lower limit with number of iterations you want in main() function
xl = 1
xu = 10
iterations = 10
```
Running the code will show the iteration results:
```   
  xl   		  xu   		  xr   		 error 		  fxl  		  fxu  		  fxr  		
 1.00000	10.00000	 5.50000	 0.00000	-6.00000	975.00000	150.37500	
 1.00000	 5.50000	 3.25000	69.23077	-6.00000	150.37500	22.82812	
 1.00000	 3.25000	 2.12500	52.94118	-6.00000	22.82812	 0.34570	
 1.00000	 2.12500	 1.56250	36.00000	-6.00000	 0.34570	-4.31030	
 1.56250	 2.12500	 1.84375	15.25424	-4.31030	 0.34570	-2.41983	
 1.84375	 2.12500	 1.98438	 7.08685	-2.41983	 0.34570	-1.15474	
 1.98438	 2.12500	 2.05469	 3.42193	-1.15474	 0.34570	-0.43499	
 2.05469	 2.12500	 2.08984	 1.68195	-0.43499	 0.34570	-0.05245	
 2.08984	 2.12500	 2.10742	 0.83420	-0.05245	 0.34570	 0.14467	
 2.08984	 2.10742	 2.09863	 0.41884	-0.05245	 0.14467	 0.04563
```

Other descriptions will be added later
