# Quadratic Equation Solver

If you have an equation of the form _ax^2 + bx + c = 0_, I can solve it for you.

# How to use:

In a file there is a function
``` python
get_roots(a, b, c)
```
**Input**: It takes 3 numbers - coefficiens a, b, c from the formula

_ax^2 + bx + c = 0_

**Output**: Discriminant = _b^2 − 4*a*c_
 
 * two roots: (x1, x2) - if discriminant > 0 
 * one root, None: (x1, None) - if discriminant == 0 
 * None, None: (None, None) - if discriminant < 0    

# How to launch:

You need pre-installed Python 3.5 of higher

**Usage Example**:

```python 
#import the function
from quadratic_equation import get_roots

a, b, c = map(int, input().split())
x1, x2 = get_roots(a, b, c)
print(x1, x2)
```

# Project Goals

For educational purposes only. [DEVMAN.org](https://devman.org)
