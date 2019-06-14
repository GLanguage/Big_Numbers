# Big_Numbers
A python module for the calculations of big numbers, including integers and floats.  
To use the module, you should download `Big_Numbers.py` and enter: `import Big_Numbers` in the python shell.
## BigInt
A class for big integers.  
Use `BigInt(str)` to creat a BigInt object.  
For instance:
```
a = BigInt("-1234567890")
```
Now, the following calculations are available:
```
len(a) # including the symbol '-'
+a
-a
abs(a)
a < b
a > b
a == b
a != b
a <= b
a >= b
a + b
a - b
a * b
a // b
a % b
```
Wait for more!  
_Notes:_ Two constants are available: 
```
ZERO = BigInt("0")
ONE = BigInt("1")
```
