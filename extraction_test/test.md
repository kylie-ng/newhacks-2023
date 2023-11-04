# Problem Set

1. Which naming convention is recommended for identifying constants in Python?
   a) camelCase
   b) Joined_lower
   c) ALL_CAPS
   d) StudlyCase

2. Which operator is used for string concatenation in Python?
   a) +
   b) -
   c) *
   d) /

3. Explain the difference between a tuple and a list in Python.

4. What is the purpose of the "datetime" module in Python? Give an example of how to use it.

5. Write a Python code snippet to calculate the factorial of a given number.

# Solution Set

1. Answer: c) ALL_CAPS

2. Answer: a) +

3. A tuple is an immutable sequence of elements, while a list is a mutable sequence of elements. This means that once a tuple is created, its elements cannot be changed, added, or removed. However, in a list, elements can be modified, added, or removed.

4. The "datetime" module in Python provides classes and functions for working with dates and times. It enables us to create, manipulate, and format dates and times. Here's an example of how to use it:

```python
import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()

# Print the current date and time
print(current_datetime)

# Get the current year
current_year = current_datetime.year

# Print the current year
print(current_year)
```

Output:
```
2021-11-26 15:30:00
2021
```

5. ```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test the factorial function
print(factorial(5))
```

Output:
```
120
```