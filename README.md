# Module for solution quadratic equations
---
## Module **quadratic_equation.py** calculates the roots of the quadratic equation
---

### How to use
+ When importing the **quadratic_equation.py** module, use the function **get_ruts (a, b, c)**
+ If the equation is degenerate, function returns one equation and None or None and None
+ If *discriminant > 0* function returns two solutions
+ If *discriminant == 0* function returns one solution and None
+ If *discriminant < 0* function returns two None
+ If an incorrect data was submitted to the **get_ruts**, it returns None

### Example of use
```python
from quadratic_equation import get_roots
get_roots(1, 2, 1)
```

### It is also possible to solve the quadratic equation so:
```bash
python quadratic_equation.py
```

### How to start test
+ For running please use python3.5
+ Launch on Linux
```bash
python test.py
```
+ Launch on Windows similarly

### Objectives of the project
The code was created for educational purposes. In the framework of the training course on web development - [DEVMAN.org](https://devman.org)