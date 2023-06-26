# Python - Everything is object

![alt text](i[mageURL](https://github.com/NahuelSilva28/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/image-43.png))
![alt text](i[mageURL](https://github.com/NahuelSilva28/holbertonschool-higher_level_programming/blob/main/python-everything_is_object/image-43.png))

# Understanding Mutable and Immutable Objects in Python

Introduction:
In Python, objects can be classified as mutable or immutable, which affects how they are stored in memory and treated by the language. Let's explore the key concepts and differences between mutable and immutable objects, and why they matter in Python.

Mutable Objects:
Mutable objects can be modified after creation without changing their identity. Examples include lists, dictionaries, sets, and byte arrays.

Immutable Objects:
Immutable objects cannot be changed once created, and any modification results in a new object. Examples include numbers, strings, tuples, frozen sets, and bytes.

Python's Treatment:
Python handles mutable and immutable objects differently when it comes to memory management and assignment. Changes to mutable objects are made directly, while modifications to immutable objects create new objects with different identities.

Implications for Function Arguments:
Python uses a "pass-by-assignment" mechanism for passing arguments to functions. Immutable objects are straightforward since their values cannot change. However, modifications made to mutable objects within a function affect the original object.

Memory Management:
Immutable objects are stored in memory with unique addresses, ensuring modifications create new objects. Pre-allocation mechanisms, like NSMALLPOSINTS, optimize memory usage for frequently used small integers.

Example with Memory Schema:
Consider the following example:
a = 5
b = 5
In memory, both 'a' and 'b' are allocated the same memory space, pointing to the integer value 5. This is possible due to a pre-allocation mechanism called "NSMALLPOSINTS," which assigns memory to frequently used small integers to optimize memory usage.

Aliases and Assignment:
Aliases occur when multiple variables refer to the same object. Assignment statements create aliases in Python. Care should be taken when working with mutable objects to avoid unintended changes through aliases.

Special Cases: Tuple and Frozen Set:
Tuples and frozen sets are immutable objects but can contain mutable objects. While the container itself cannot be modified, the mutable objects it holds can be changed.

Understanding the distinctions between mutable and immutable objects is crucial for effective Python programming. It empowers us to make informed decisions, avoid unexpected behavior, and optimize our code.
