# Problem Set

## True or False

1. In Python, code blocks are delineated by curly brackets.
2. It is recommended to use tabs instead of spaces for indentation in Python.
3. The Python naming convention for constants is ALL_CAPS.
4. A tuple in Python is a mutable list.
5. The bitwise operator | is used for set difference in Python.

## Multiple Choice

1. Which of the following is not a basic object type in Python?
   a) Boolean
   b) string
   c) array
   d) integer

2. What is the purpose of the "pickle" module in Python?
   a) To serialize objects to a file
   b) To perform regular expression operations
   c) To manipulate strings
   d) To perform mathematical calculations

3. What is the purpose of the "numpy" library in Python?
   a) To manipulate dates and times
   b) To perform core math functions
   c) To perform numerical calculations
   d) To plot and chart data

## Long Answer

Explain the difference between the "import" method and the "from ... import" method for importing modules in Python. When would you use each method?

# Solution Set

## True or False

1. False
2. False
3. True
4. False
5. False

## Multiple Choice

1. c) array
2. a) To serialize objects to a file
3. c) To perform numerical calculations

## Long Answer

The "import" method is used to import an entire module in Python. You can then access the functions, variables, and classes of the module using the module name followed by a dot and the item you want to access.

Example:
```
import math
math.cos(math.pi/3)
```

The "from ... import" method is used to import specific items from a module in Python. This allows you to access those specific items directly without needing to use the module name.

Example:
```
from math import cos, pi
cos(pi/3)
```

You would use the "import" method when you want to access multiple items from a module and don't mind using the module name to access them. You would use the "from ... import" method when you only need to access specific items from a module and don't want to use the module name. This can make your code more concise and easier to read.