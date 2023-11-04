# Problem Set

## Multiple Choice

1. Which of the following is NOT a basic object type in Python?

   A) Boolean  
   B) Float  
   C) Character  
   D) String  

2. What is the purpose of the `open()` function in Python?

   A) To open a new Python shell  
   B) To open a new Python file for reading or writing  
   C) To open a new Python module for importing  
   D) To open a new Python class for instantiation  

## Long Answer

1. Explain the difference between a tuple and a list in Python. Give an example of when you would use each.

2. Describe the purpose of the `if-else` statement in Python. Provide an example of its usage.

3. What is the difference between the assignment operator `=` and the comparison operator `==` in Python? Give an example of each.

# Solution Set

## Multiple Choice

1. Which of the following is NOT a basic object type in Python?

   A) Boolean  
   B) Float  
   C) Character  
   D) String  

   **Answer: C) Character**

2. What is the purpose of the `open()` function in Python?

   A) To open a new Python shell  
   B) To open a new Python file for reading or writing  
   C) To open a new Python module for importing  
   D) To open a new Python class for instantiation  

   **Answer: B) To open a new Python file for reading or writing**

## Long Answer

1. Explain the difference between a tuple and a list in Python. Give an example of when you would use each.

   **Answer:** A tuple is an immutable sequence of objects, while a list is a mutable sequence of objects. This means that once a tuple is created, its elements cannot be changed, while a list allows for adding, removing, or modifying elements. Tuples are typically used for storing related pieces of information together, while lists are more versatile and can be used for a variety of purposes.

   Example:
   ```
   # Tuple
   person = ('John', 25, 'Male')

   # List
   numbers = [1, 2, 3, 4, 5]
   ```

2. Describe the purpose of the `if-else` statement in Python. Provide an example of its usage.

   **Answer:** The `if-else` statement is used for conditional execution in Python. It allows the program to make decisions based on certain conditions. If the condition specified in the `if` statement is met, the code block within the `if` statement is executed. If the condition is not met, the code block within the `else` statement is executed.

   Example:
   ```
   age = 18

   if age >= 18:
       print("You are an adult.")
   else:
       print("You are a minor.")
   ```

3. What is the difference between the assignment operator `=` and the comparison operator `==` in Python? Give an example of each.

   **Answer:** The assignment operator `=` is used to assign a value to a variable in Python. It is used to store a value in a variable or update the value of an existing variable.

   Example:
   ```
   x = 5
   y = "Hello World"
   ```

   On the other hand, the comparison operator `==` is used to compare two values for equality. It returns `True` if the values are equal, and `False` otherwise.

   Example:
   ```
   a = 10
   b = 5

   print(a == b)  # Output: False
   ```