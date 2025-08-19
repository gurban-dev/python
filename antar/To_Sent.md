## HOME
*What is Python?* 
Python is a very popular general-purpose interpreted, interactive, object-oriented, and high-level programming language. Python is dynamically-typed and garbage-collected programming language. It was created by Guido van Rossum during 1985- 1990. Like Perl, Python source code is also available under the GNU General Public License (GPL).

*What does python supports?*
Python supports multiple programming paradigms, including Procedural, Object Oriented and Functional programming language. Python design philosophy emphasizes code readability with the use of significant indentation.


## Overview
*What is "import this"?*  
this is zen of python explains the philosophy behind python

## History
*Who developed python?*  
Python was developed by Guido van Rossum (a Dutch programmer) in the late 1980s and early nineties at the National Research Institute for Mathematics and Computer Science in the Netherlands.

*Who Invented Python?*  
Python was invented by a Dutch Programmer Guido Van Rossum in the late 1980s. He began working on Python in December 1989 as a hobby project while working at the Centrum Wiskunde & Informatica (CWI) in the Netherlands. Python's first version (0.9.0) was released in 1991.

*Why Python is called Python?*  
Python does not have any relation to Snake. The name of the Python programming language was inspired by a British Comedy Group Monty Python.

*When was Python's first version released?*  
Python's first version was released in February 1991.

*What was the first version of Python?*  
Python's first version was Python 0.9.0

*When was Python 3.0 version released?*  
Python 3.0 version was released in December 2008.

## Features
*Why python is easy to learn?*  
Python has a limited set of keywords. Its features such as simple syntax, usage of indentation to avoid clutter of curly brackets and dynamic typing that doesn't necessitate prior declaration of variable help a beginner to learn Python quickly and easily.

*Why python is called "dynamic?"*  
Python is a dynamically typed programming language. In Python, you don't need to specify the variable type at the time of the variable declaration. The types are specified at the runtime based on the assigned value due to its dynamically typed feature.

*What does it mean "Python is interpreter based"?*  
Instructions in any programming languages must be translated into machine code for the processor to execute them. Programming languages are either compiler based or interpreter based.

The interpreter takes one instruction from the source code at a time, translates it into machine code and executes it. Instructions before the first occurrence of error are executed. With this feature, it is easier to debug the program and thus proves useful for the beginner level programmer to gain confidence gradually. Python therefore is a beginner-friendly language.

*What does REPL mean?*  
REPL (Read – Evaluate – Print – Loop)

*What is interactive mode?*  
The interactive mode executes it based on the REPL principle, basically means it will execute things in real-time.

*How to close a session in "interactive mode?"*  
ctrl+D for Linux and ctrl+Z for Windows or quit()

*What does it mean that Python is a multi-paradigm language?*  
Python supports object-oriented, imperative, procedural, and functional programming paradigms, allowing flexibility in programming styles.

*What is the significance of Python's standard library?*  
Python has a large standard library with many modules and packages, providing out-of-the-box support for tasks like serialization, data compression, and internet data handling.

*What are some popular modules in Python's standard library?*  
Popular modules include NumPy, Pandas, Matplotlib, Tkinter, and Math.

*How is Python categorized in terms of licensing and distribution?*  
Python is open source, distributed under the Python Software Foundation License, and its source code is freely available.

*What platforms does Python support?*  
Python is a cross-platform language, with pre-compiled binaries available for Windows, Linux, Mac OS, and Android OS.

*What is TKinter in Python?*  
TKinter is a graphics library in Python for building user-friendly GUI applications, based on the TCL/Tk toolkit.

*How does Python handle database connectivity?*  
Python can connect to various databases using DB-API specifications and supports both relational and NoSQL databases through third-party libraries.

*What does extensibility mean in the context of Python?*  
Extensibility refers to the ability to add or modify features in Python, allowing modules to be written in C, Java, or C# and integrated into Python.

*What is the role of the Python Software Foundation?*  
The Python Software Foundation promotes, protects, and advances the Python programming language and has a significant member base.

*What are some additional features of Python?*  
Python supports functional and structured programming, can be used as a scripting language, provides dynamic data types, supports automatic garbage collection, and integrates easily with C, C++, and Java.






## Hello world!
*How to say "Hello world!" in python?*  
print ("Hello, World!")

Or 

import sys
sys.stdout.write("Hello world!)

## Interpeter
*How do python interpeter executes the code?*
Python code is executed by one statement at a time method. Python interpreter has two components. 
The translator checks the statement for syntax. If found correct, it generates an intermediate byte code. 
There is a Python virtual machine which then converts the byte code in native binary and executes it.

*what is script mode?*
opposite of the interactive , you can save results in .py and still execute with the one line--style fashon

*what is sheband?*
its a part of code you must add it in order to make the code works "in linux" ,
! /path/to/your/python then to make it executable add chmod +x program.py then ./program.py

*what is IPython an what is it used for?*
#Interactive Python , interactive environment for Python with many functionalities compared to the standard Python shell



## Virtual enviroment
*what is virutal enviroment?*
It's a virtual installation of Python inside a project
directory which users can install and manage Python
packages, without fear of breaking packages installed
in other environments.

## Baisc syntax
*What is Python syntax?*  
It's a set of rules that are used to create a Python program.

*What is a Python identifier?*  
It's a name used to identify a variable, function, class, module, or other object. It usually starts with A to Z or a to z or an underscore (_) followed by zero or more letters, underscores, and digits (0 to 9). Python does not allow (@, $, and %) within identifiers.

*What type of letters does the class start with?*  
An uppercase letter, while all other identifiers start with a lowercase letter.

*How to know if the identifier is a private identifier?*  
It starts with a single leading underscore.

*What is the strong leading identifier?*  
It starts with two leading underscores.

*What is the identifier that ends with two trailing underscores?*  
It's a language-defined special name.

*What does Python programming provide?*  
No braces to indicate blocks of code for class and function definitions or flow control. Blocks of code are denoted by line indentation.

*What is the difference between '' "", and ''' '''?*  
word = 'word'  
print(word) 
sentence = "This is a sentence." 
print(sentence)  
paragraph = """This is a paragraph. It is made up of multiple lines and sentences."""
print(paragraph)

*What does the semicolon (;) allow?*  
It allows multiple statements on a single line, e.g., import sys; x = 'foo'; sys.stdout.write(x + '\n').

*What are suites in Python?*  
A group of individual statements that make a single code block, such as (if, while, def, and class). All of them require a header line and a suite.

*What does the header begin and end with?*  
It begins with the keyword 'the statement' and terminates with a colon (:).

*What follows the header?*  
One or more lines that make up the suite.

*Example of a suite structure:*  
if expression:
    suite
elif expression:
    suite
else:
    suite






## Variables
*What is a variable?*  
The reserved memory locations used to store values within a Python program.

*How is it decided where to locate?*  
Based on the data type of a variable, the Python interpreter allocates memory and decides what can be stored.

*How is data stored in a computer's memory?*  
Data items of different types are stored in memory locations, each having a unique address represented in binary form. The data itself is also stored in binary, as computers operate on the principle of binary representation.

*How does Python store objects in memory, and how can you find the memory address of an object?*  
Python stores objects in randomly chosen memory locations. You can find the memory address where an object is stored by using the built-in `id()` function.

*How do you print a variable in Python after assigning a value to it?*  
You can use the `print()` function to display the value of a variable.

*How can you delete a variable or multiple variables in Python?*  
You can use the `del` statement to delete a variable or multiple variables.  
`del var1[, var2[, var3[...., varN]]]`

*How can you delete a single object or multiple objects in Python?*  
You can use the `del` statement to delete a single object or multiple objects.  
`del var`

*How can you get the data type of a Python variable using built-in functions?*  
Use `type()` as follows:  
```python
x = "Zara"  
y = 10  
z = 10.10  
print(type(x))  
print(type(y))  
print(type(z))  
```

*How can you specify the data type of a variable with the help of casting?*  
```python
x = str(10)    # x will be '10'  
y = int(10)    # y will be 10  
z = float(10)  # z will be 10.0  
print("x =", x)  
print("y =", y)  
print("z =", z)  
```

*Are Python variables case sensitive? Provide an example.*  
Yes, Python variables are case sensitive, meaning that `Age` and `age` are treated as two different variables.

*How can you initialize multiple variables with the same value in a single statement in Python?*  
You can assign the same value to multiple variables in a single statement:  
`a = b = c = 10`  
Printing the variables:  
```python
print("a =", a)  # Output: a = 10  
print("b =", b)  # Output: b = 10  
print("c =", c)  # Output: c = 10  
```

*How can you combine multiple assignment statements into one in Python?*  
You can combine separate assignment statements by using comma-separated variable names on the left and comma-separated values on the right of the `=` operator.

*What are the rules for naming a variable?*  
- A variable name must start with a letter or the underscore character.  
- A variable name cannot start with a number or any special character like $, (, *, % etc.  
- A variable name can only contain alphanumeric characters and underscores (A-z, 0-9, and _).  
- Python variable names are case-sensitive, meaning `Name` and `NAME` are two different variables.  
- Python reserved keywords cannot be used for naming variables. You can check the list of reserved keywords in Python by using the following code:  
```python
import keyword  
print(keyword.kwlist)  
```

*What if the name consists of multiple words?*  
We will use one of these patterns:  
- Camel case: First letter is lowercase, but the first letter of each subsequent word is uppercase. For example: `kmPerHour`, `pricePerLitre`.  
- Pascal case: First letter of each word is uppercase. For example: `KmPerHour`, `PricePerLitre`.  
- Snake case: Use a single underscore (_) character to separate words. For example: `km_per_hour`, `price_per_litre`.

*What is Python's local variable?*  
Python local variables are defined inside a function. We cannot access the variable outside the function.  
```python
def sum(x, y):  
    sum = x + y  
    return sum  
print(sum(5, 10))  
```

*What is Python's global variable?*  
Any variable created outside a function can be accessed within any function, giving it global scope. Python executes code line-by-line, so if the interpreter doesn't find the mentioned variable, it will look for all the previous code. This can take time, so using local variables is always best practice.
```python
x = 1
def number():
    o = x
    #Then you can use it
```
*Does Python have constants? And if so, how to define them?*  
Python doesn't have any formally defined constants. However, you can indicate a variable to be treated as a constant by using all-caps names with underscores. For example, the name `PI_VALUE` indicates that you don't want the variable redefined or changed in any way.

*What is referred to when using all-caps letters in a variable?*  
The naming convention using all-caps is sometimes referred to as "screaming snake case," where the all-caps (screaming) and the underscores (snakes) are used.

*What does it mean when we say a Python variable refers to an object and not a memory location?*  
A Python variable acts as a label for an object in memory. Multiple variables can refer to the same object, meaning they are just different names for the same underlying data.

*How is an object stored in memory in Python?*  
An object is stored in memory only once, and multiple variables can refer to that same object, acting as multiple labels for it.  
```python
a = b = 100  
print(a is b)  # True  
print(id(a))   # The same memory address  
print(id(b))  
```

*What is garbage collection in Python?*  
Garbage collection is a mechanism that automatically releases memory occupied by objects that are no longer referenced or needed, helping to manage memory efficiently.



## Data types
*What are Python data types in relation to classes?*  
Python data types are actually classes, and the variables defined are instances or objects of these classes.

*What does it mean that Python is dynamically typed?*  
In Python, the data type of a variable is determined at runtime based on the value assigned to it, allowing for flexibility in variable types.

*What is the purpose of data types in Python?*  
Data types define the type of a variable, represent the kind of data stored, and determine what operations can be performed on that data.

*What are the data types of Python?*  
- int  
- float  
- complex  
- String Data Types  
- Sequence Data Types  
  - list  
  - tuple  
  - range  
- Binary Data Types  
  - bytes  
  - bytearray  
  - memoryview  
- Dictionary Data Type  
- Set Data Type  
  - set  
  - frozenset  
- Boolean Data Type  
- None Type  

*What is Numeric Data type in Python, and what are its examples?*  
Python numeric data types store numeric values. Number objects are created when you assign a value to them. Python supports four different numerical types, each with built-in classes in the Python library: int, bool, float, and complex.

*What is a complex Data type? What does it look like and how to denote them?*  
A complex number is a mix between a real and an imaginary number, separated by '+' or '-' signs. The imaginary part is suffixed by 'j'. Complex numbers in Python are represented as x+yj, where x is the real part and y is the imaginary part.

*What are some key characteristics and operations of strings in Python, including their data type, methods, and operators for concatenation and repetition?*  
Strings in Python are non-numeric data types that do not support arithmetic operations but allow slicing and concatenation. The str class provides various methods for string processing. Slicing can be done using the slice operator with indexes starting at 0 and -1 for the end. The plus (+) sign is used for string concatenation, while the asterisk (*) is used for string repetition.

*What is a sequence in Python, and what are the three main sequence data types?*  
A sequence in Python is an ordered collection of items with a positional index starting at 0, similar to arrays in C or C++. The three main sequence data types in Python are List, Tuple, and Range. Python sequences are bounded and iterable, meaning they can be traversed in a loop.

*What are Python lists, and how do they differ from C arrays?*  
Python lists are versatile compound data types that contain items separated by commas and enclosed in square brackets ([]). Unlike C arrays, which store elements of a single data type, Python lists can contain items of different data types, making them more flexible.  
Example: `[2023, "Python", 3.11, 5+6j, 1.23E-4]`  
A list in Python is an object of the list class, which can be checked with the `type()` function.

*How to access the lists?*  
The values stored in a Python list can be accessed using the slice operator ([ ] and [:]) with indexes starting at 0 in the beginning of the list and working their way to the end -1.

*What is a Python tuple, and how does it differ from a list?*  
A Python tuple is a sequence data type similar to a list, consisting of values separated by commas and enclosed in parentheses (...). Like lists, tuples have indexed items starting from 0, but unlike lists, tuples are immutable, meaning their contents cannot be changed after creation.

*What are the main differences between lists and tuples in Python?*  
The main differences between lists and tuples in Python are that lists are enclosed in brackets ([]) and are mutable, meaning their elements and size can be changed, while tuples are enclosed in parentheses (()) and are immutable, meaning they cannot be updated. Tuples can be thought of as read-only lists.

*What is a Python range, and how is it constructed?*  
A Python range is an immutable sequence of numbers used to iterate through a specific number of items, represented by the Range class. It is constructed using the syntax `range(start, stop, step)`, where start (optional, default is 0) specifies the starting position, stop (mandatory) specifies the ending position, and step (optional, default is 1) specifies the increment between numbers.

*What is a binary data type in Python?*  
A way to represent data as a series of binary digits (0's and 1's) for efficient storage and processing.

*Why is binary data commonly used?*  
It is used for files, images, or anything that can be represented using just two possible values (0s and 1s).

*What are the three ways Python provides to represent binary data?*  
- bytes  
- bytearray  
- memoryview  

*What does the binary data type allow computers to do?*  
Store and process information efficiently.

*What does the byte data type in Python represent?*  
A sequence of bytes, each an integer value between 0 and 255, commonly used to store binary data.

*How can you create a bytes object in Python?*  
Using the `bytes()` function or by prefixing a sequence of numbers with `b`.

*What is the output of `bytes([65, 66, 67, 68, 69])`?*  
`b'ABCDE'`

*What is the difference between bytes and bytearray in Python?*  
`bytes` is immutable, while `bytearray` is mutable, allowing modification of its values.

*How do you create a bytearray from a string?*  
By using `bytearray("string", 'encoding')`, e.g., `bytearray("Hello", 'utf-8')`.

*What is a memoryview in Python?*  
A built-in object that provides a view into the memory of the original object, allowing access without copying.

*How can you create a memoryview from a bytearray?*  
By using `memoryview(data)`, where `data` is a bytearray.

*How do you create a memoryview from an array object in Python?*  
You can create a memoryview using the buffer interface. Example:  
```python
import array  
arr = array.array('i', [1, 2, 3, 4, 5])  
view = memoryview(arr)  
print(view)  
```

*What is a Python dictionary?*  
A collection of key-value pairs, where keys can be almost any type and values can be any arbitrary Python object.

*How do you define a dictionary in Python?*  
Using curly braces `{}` with key-value pairs separated by commas, e.g., `{1: 'one', 2: 'two'}`.

*What is a Python set? How to define them and how to separate them?*  
An unordered collection of unique items, defined using curly braces `{}` and separated by commas. For example: `{1, "1", 1.0, 1j, 1, 11E-}`.

*Can an object appear more than once in a set?*  
An object cannot appear more than once in a set, whereas in lists and tuples, the same object can appear more than once.

*What types of objects can be stored in a Python set? And why?*  
Only immutable objects like numbers, strings, and tuples can be stored in a set. This is because mutable objects would raise an unhashable error. Hashing is a mechanism in computer science that enables quicker searching of objects in a computer's memory. Only immutable objects are hashable.

*What are the two possible values of the Python boolean type?*  
True and False.

*How do you check the type of a variable in Python?*  
By using the `type()` function.

*What are some examples of the `bool()` function?*  
```python
a = 2  
b = 4  
print(bool(a == b))  # Output: False
```

*What is the None type in Python?*  
It represents the absence of a value or a null value, indicated by `None`.

*What are the primitive data types in Python?*  
The primitive data types are the fundamental data types that are used to create complex data types (sometimes called complex data structures).

*What are the four primitive data types in Python?*  
Integers, Floats, Booleans, and Strings.

*What are the non-primitive data types in Python?*  
The non-primitive data types store values or collections of values.

*What are the four non-primitive data types in Python?*  
Lists, Tuples, Dictionaries, and Sets.

*What are the Data Type Conversion Functions?*  
There are several built-in functions to perform conversion from one data type to another. These functions return a new object representing the converted value.

*What is Python `int()` function?*  
Converts `x` to an integer. `base` specifies the base if `x` is a string.

*What is Python `long()` function?*  
Converts `x` to a long integer. `base` specifies the base if `x` is a string. This function has been deprecated. **"It's been nerfed , Use int(), In modern python (3) the int() function now can hold large amount of numbers as the long() would do in the old versions of python (2)"**

*What is Python `float()` function?*  
Converts `x` to a floating-point number.

*What is Python `complex()` function?*  
Creates a complex number.

*What is Python `str()` function?*  
Converts object `x` to a string representation.

*What is Python `repr()` function?*  
Converts object `x` to an expression string.

*What is Python `eval()` function?*  
Evaluates a string and returns an object.

*What is Python `tuple()` function?*  
Converts `s` to a tuple.

*What is Python `list()` function?*  
Converts `s` to a list.

*What is Python `set()` function?*  
Converts `s` to a set.

*What is Python `dict()` function?*  
Creates a dictionary. `d` must be a sequence of (key, value) tuples.

*What is Python `frozenset()` function?*  
Converts `s` to a frozen set.

*What is Python `chr()` function?*  
Converts an integer to a character.

*What is Python `unichr()` function?*  
Converts an integer to a Unicode character.

*What is Python `ord()` function?*  
Converts a single character to its integer value.

*What is Python `hex()` function?*  
Converts an integer to a hexadecimal string.

*What is Python `oct()` function?*  
Converts an integer to an octal string.

*What is the output of `bool(0)`?*  
False.

*What is the output of `bool(10)`?*  
True.

*Are integers iterable?*  
No, integers are not iterable.
!




## Type casting
**What are Python data types in relation to classes?**  
Python data types are actually classes, and the variables defined are instances or objects of these classes.

**What is Python Type Casting?**  
Type casting refers to converting an object of one type into another. Python supports two types of casting: implicit and explicit.

**What is implicit Casting in Python?**  
When any language compiler/interpreter automatically converts an object of one type into another, it is called automatic or implicit casting.

**What does it mean when we say "Python is a strongly typed language"?**  
It doesn't allow automatic type conversion between unrelated data types. For example, a string cannot be converted to any number type. However, an integer can be cast into a float.

**What is the memory requirement for an integer object in Python?**  
4 bytes.

**How many bytes does a float object occupy in Python?**  
8 bytes.

**Why doesn't the Python interpreter automatically convert a float to an int?**  
Because it would result in loss of data.

**Can an int be easily converted into a float in Python?**  
Yes, by setting its fractional part to 0.

**What type of casting occurs when performing arithmetic operations between int and float operands in Python?**  
Implicit int to float casting.

**In the example a=10 (int) and b=10.5 (float), what happens to a when performing addition?**  
a is upgraded to 10.0 (float) for the operation.

**What is the result of the addition c=a+b when a=10 and b=10.5?**  
c will be 20.5.

**In implicit type casting, how does Python handle objects with different byte sizes during operations?**  
The object with the smaller byte size is upgraded to match the bigger byte size of the other object.

**What are the integer equivalents of Boolean values in Python?**  
True is equal to 1 and False is equal to 0.

**What is the result of: a = True, b = 10.5, c = a + b, print(c)?**  
The result will be 11.5.

**What does the int() function do?**  
Converts an integer literal to an integer object, a float to an integer, and a string to an integer if the string itself has a valid integer literal representation.

**How to convert float to int?**  
a = int(1.0) results in a = 1.

**How to convert from boolean to integer?**  
a = int(True) results in a = 1.

**When does a string convert into an integer?**  
When it contains a valid integer representation.

**Can you give an example of this?**  
a = int("100") results in a = 100.

**What does the int() function do with binary, octal, and hexadecimal strings?**  
It returns an integer from the string representation, requiring a base parameter (2 for binary, 8 for octal, 16 for hexadecimal).

**What is the valid format for a binary string when using int()?**  
The string should consist of only 1s and 0s, and the base must be 2.

**Convert the binary string "110011" to an integer using int().**  
a = int("110011", 2) results in a = 51.

**What is the valid format for an octal string when using int()?**  
The string should contain digits from 0 to 7, and the base must be 8.

**Convert the octal string "20" to an integer using int().**  
a = int("20", 8) results in a = 16.

**What is the valid format for a hexadecimal string when using int()?**  
The string should contain digits 0-9 and letters A-F, and the base must be 16.

**Convert the hexadecimal string "2A9" to an integer using int().**  
a = int("2A9", 16) results in a = 681.

**What is the float() function?**  
It returns a float object if the argument is a float literal, integer, or a string with valid floating point representation.

**What does the str() function do in Python?**  
It converts an integer or float object to a string representation, surrounding it with quotes (').

**What are the parameters of the str() function?**  
The first parameter is the object to convert, while the other two parameters, encoding and errors, are optional.

**Convert the integer 10 to a string using str().**  
a = str(10) results in a = '10'.

**How does str() convert floating-point numbers?**  
It converts both standard notation and scientific notation to a string object.

Sure! Here’s the continuation without leaving gaps:

**Convert the float 11.10 to a string using str().**  
a = str(11.10) results in a = '11.1'.

**What is the result of converting the expression 2/5 to a string using str()?**  
a = str(2/5) results in a = '0.4'.

**How does str() handle scientific notation?**  
It converts scientific notation to a string, e.g., a = str(10E4) results in a = '100000.0'.

**What will str(True) return?**  
a = str(True) results in a = 'True'.

**Convert a list and a tuple to strings using str().**  
For a list: a = str([1, 2, 3]) results in a = '[1, 2, 3]'. For a tuple: a = str((1, 2, 3)) results in a = '(1, 2, 3)'.

**How can you convert a string and a tuple into a list?**  
Using the list() function: obj = list("Hello") results in ['H', 'e', 'l', 'l', 'o']. obj = list((1, 2, 3, 4, 5)) results in [1, 2, 3, 4, 5].

**How can you convert a list into a tuple?**  
Using the tuple() function: obj = tuple([1, 2, 3, 4, 5]) results in (1, 2, 3, 4, 5).

**What does the str() function do when applied to a list or tuple?**  
It returns a string representation of the list or tuple, e.g., str([1, 2, 3]) results in a = '[1, 2, 3]'.

## Unicode
**What is the Unicode System?**  
The Unicode System allows software applications to display messages in various languages (e.g., English, French, Japanese) by representing characters as a sequence of code points, which are numbers from 0 to 0x10FFFF.

**What is a character in the context of Unicode?**  
A character is the smallest component of text, such as 'A', 'B', 'C', or symbols like '' and '.

**What are code points in Unicode?**  
Code points are numbers that represent characters in Unicode, ranging from 0 to 0x10FFFF (1,114,111 in decimal).

**What is character encoding?**  
Character encoding is the set of rules for translating a Unicode string into a sequence of bytes, represented in memory as code units mapped to 8-bit bytes.

**Name the three types of Unicode encodings and what do they stand for?**  
UTF-8, UTF-16, and UTF-32, which stand for Unicode Transformation Format.

**How does Python support Unicode?**  
From Python 3.0 onwards, the str type contains Unicode characters, and the default encoding for Python source code is UTF-8.

**How can you represent a Unicode character in Python?**  
You can represent a Unicode character using its literal representation (e.g., "3/4") or its Unicode value (e.g., "\u00BE").

**What does the encode() method do in Python?**  
The encode() method converts a string (str) into a bytes object using a specified encoding (e.g., UTF-8).

**What does the decode() method do in Python?**  
The decode() method converts a bytes object back into a string (str) using a specified encoding (e.g., UTF-8).

**What is the output of the following code: var = "\u0031\u0030"; print(var)?**  
The result will be 10.

**What is the output of the following code? string = "\u20B9"; tobytes = string.encode('utf-8'); print(tobytes); string = tobytes.decode('utf-8'); print(string)**  
The output will be b'\xe2\x82\xb9' followed by ₹.

## Literals
**What are Python literals?**  
Python literals, also known as "constants," are notations for representing fixed values in source code. Unlike variables, literals (e.g., 123, 4.3, "Hello") are static values that do not change during the program's execution.

**How is an indirect assignment different from a literal in Python?**  
An indirect assignment, like y = x * 2, evaluates to a value but is not literally included in the source code. In contrast, a literal is a fixed value directly represented in the code, such as x = 10.

**What are the different types of Python literals?**  
The different types of Python literals include:  
- Integer Literal  
- Float Literal  
- Complex Literal  
- String Literal  
- List Literal  
- Tuple Literal  
- Dictionary Literal  

**What are integer literals in Python?**  
Integer literals are representations involving only digit symbols (0-9) and can be decimal, octal (prefixed with 0o), or hexadecimal (prefixed with 0x). For example:  
- Decimal: x = 10  
- Octal: x = 0o34  
- Hexadecimal: x = 0x1C  

**What is a float literal in Python?**  
A float literal consists of an integral part and a fractional part, separated by a decimal point. For example, x = 25.55. Large or small floats can also be represented in scientific notation, e.g., 1.23E5 (equivalent to 123000.0).

**How are complex literals represented in Python?**  
Complex literals consist of a real and an imaginary part, represented as x + yj, where j is the imaginary unit. For example, x = 2 + 3j.

**What are string literals in Python?**  
String literals are sequences of characters enclosed in single quotes ('hello'), double quotes ("hello"), or triple quotes ('''hello''' or """hello"""). They are immutable sequences of Unicode code points.

**How are list literals defined in Python?**  
List literals are defined by enclosing a comma-separated collection of items in square brackets []. For example, L1 = [1, "Ravi", 75.50, True].

**What is a tuple literal in Python?**  
Tuple literals are defined by enclosing a comma-separated collection of items in parentheses (). For example, T1 = (1, "Ravi", 75.50, True). Tuples can also be defined without parentheses, e.g., T1 = 1, "Ravi", 75.50, True.

**How are dictionary literals represented in Python?**  
Dictionary literals are defined by enclosing key-value pairs in curly braces {}. For example, capitals = {"USA": "New York", "France": "Paris"}. Keys must be immutable and unique.

## Operations
**What are Python operations?**  
Python operators are special symbols used to perform specific operations on one or more operands. The variables, values, or expressions can be used as operands. For example, Python's addition operator (+) is used to perform addition operations on two variables, values, or expressions.

**What are terms related to "Python operations"?**  
- Unary operators: Python operators that require one operand to perform a specific operation.  
- Binary operators: Python operators that require two operands to perform a specific operation.  
- Operands: Variables, values, or expressions that are used with the operator to perform a specific operation.

**What are the types of Python operations?**  
- Arithmetic Operators  
- Comparison (Relational) Operators  
- Assignment Operators  
- Logical Operators  
- Bitwise Operators  
- Membership Operators  
- Identity Operators  

**What are Python arithmetic operations?**  
They are used to perform basic mathematical operations (e.g., plus, minus).

**What are the available built-in Python mathematical operations?**  
Operator    | Name          | Example  
+           | Addition      | a + b = 30  
-           | Subtraction   | a - b = -10  
*           | Multiplication| a * b = 200  
/           | Division      | b / a = 2  
%           | Modulus       | b % a = 0  
**          | Exponent      | a ** b = 10 ** 20  
//          | Floor Division| 9 // 2 = 4  

**What are Python comparison operators?**  
They compare the values on either side of them and decide the relation among them. They are also called relational operators.

**What are all the comparison operators in Python?**  
Operator | Name                     | Example  
==       | Equal                    | (a == b) is not true.  
!=       | Not equal                | (a != b) is true.  
>        | Greater than             | (a > b) is not true.  
<        | Less than                | (a < b) is true.  
>=       | Greater than or equal to | (a >= b) is not true.  
<=       | Less than or equal to    | (a <= b) is true.  

**What are Python assignment operations?**  
They are used to assign values to variables.

**What are all Python assignment operations?**  
Operator | Example      | Same As  
=        | a = 10       | a = 10  
+=       | a += 30      | a = a + 30  
-=       | a -= 15      | a = a - 15  
*=       | a *= 10      | a = a * 10  
/=       | a /= 5       | a = a / 5  
%=       | a %= 5       | a = a % 5  
**=      | a **= 4      | a = a ** 4  
//=      | a //= 5      | a = a // 5  
&=       | a &= 5       | a = a & 5  
|=       | a |= 5       | a = a | 5  
^=       | a ^= 5       | a = a ^ 5  
>>=      | a >>= 5      | a = a >> 5  
<<=      | a <<= 5       | a = a << 5  

**What is Python bitwise operation?**  
It works on bits and performs bit-by-bit operations. These operators are used to compare binary numbers.

**What are all bitwise operations?**  
Operator | Name                 | Example  
&        | AND                  | a & b  
|        | OR                   | a | b  
^        | XOR                  | a ^ b  
~        | NOT                  | ~a  
<<       | Zero fill left shift | a << 3  
>>       | Signed right shift   | a >> 3  

**What is the function of bin()?**  
It is used to convert an integer into its binary representation as a string. The output string starts with the prefix '0b', which indicates that the number is in binary format.

**What is a logical operator?**  
Used to combine two or more conditions and check the final result.

**What are the logical operators?**  
Operator    | Name  | Example  
and         | AND   | a and b  
or          | OR    | a or b  
not         | NOT   | not(a)  

**What are Python membership operators?**  
They test for membership in a sequence, such as strings, lists, or tuples.

**What are Python membership operators?**  
Operator | Description                | Example  
in       | Returns True if it finds a variable in the specified sequence, false otherwise.                      | a in b  
not in   | Returns True if it does not find a variable in the specified sequence and false otherwise.         | a not in b  

**What are Python identity operations?**  
They compare the memory locations of two objects.



## Arthemitic operation
**What is Python arithmetic operation?**  
Arithmetic operators are binary operators in the sense they operate on two operands. Python fully supports mixed arithmetic, meaning the two operands can be of different number types.

**What is the addition operation in Python?**  
The addition operator is represented by the + symbol. It is a basic arithmetic operator that adds the two numeric operands on either side and returns the addition result.

**What will happen if we add two different data types (integer and float)?**  
```python
a = 10
b = 20.5
print("Addition of integer and float")
print("a =", a, "b =", b, "addition =", a + b)
```
**The result:**  
Addition of integer and float  
a = 10 b = 20.5 addition = 30.5

**What about complex with float?**  
```python
a = 10 + 5j
b = 20.5
print("Addition of complex and float")
print("a =", a, "b =", b, "addition =", a + b)
```
**The result:**  
Addition of complex and float  
a = (10+5j) b = 20.5 addition = (30.5+5j)

**What is the subtraction operator?**  
The subtraction operator is represented by the - symbol. It subtracts the second operand from the first. The resultant number is negative if the second operand is larger.

**What happens if we subtract an integer and a float?**  
```python
a = 10
b = 20.5
print("Subtraction of integer and float")
print("a =", a, "b =", b, "a-b =", a - b)
print("a =", a, "b =", b, "b-a =", b - a)
```
**The result:**  
Subtraction of integer and float  
a = 10 b = 20.5 a-b = -10.5  
a = 10 b = 20.5 b-a = 10.5

**What if we subtract a complex number and a float?**  
```python
a = 10 + 5j
b = 20.5
print("Subtraction of complex and float")
print("a =", a, "b =", b, "a-b =", a - b)
print("a =", a, "b =", b, "b-a =", b - a)
```
**The result:**  
Subtraction of complex and float  
a = (10+5j) b = 20.5 a-b = (-10.5+5j)  
a = (10+5j) b = 20.5 b-a = (10.5-5j)

**What is the multiplication operation in Python?**  
The * (asterisk) symbol is defined as a multiplication operator in Python. It returns the product of the two operands on either side. If any of the operands is negative, the result is also negative. If both are negative, the result is positive. Changing the order of operands doesn't change the result.

**What will happen if we multiply an integer with a float?**  
```python
a = 10
b = 20.5
print("Multiplication of integer and float")
print("a =", a, "b =", b, "a*b =", a * b)

a = -5.55
b = 6.75E-3
print("Multiplication of float and float")
print("a =", a, "b =", b, "a*b =", a * b)
```
**The result:**  
Multiplication of integer and float  
a = 10 b = 20.5 a*b = 205.0  
Multiplication of float and float  
a = -5.55 b = 0.00675 a*b = -0.037462499999999996

**What if it's multiplied with a complex number?**  
```python
a = 10 + 5j
b = 20.5
print("Multiplication of complex and float")
print("a =", a, "b =", b, "a*b =", a * b)
```
**The result:**  
Multiplication of complex and float  
a = (10+5j) b = 20.5 a*b = (205+102.5j)

**What is the division operator in Python?**  
The "/" symbol is usually called a forward slash. The result of the division operator is the numerator (left operand) divided by the denominator (right operand). The resultant number is negative if any of the operands is negative. Python raises ZeroDivisionError if the denominator is 0.

**What if we divide two different data types (integer and float)?**  
```python
a = 10
b = -20.5
print("Division of integer and float")
print("a =", a```python
print("a =", a, "b =", b, "a/b =", a / b)

a = -2.50
b = 1.25E2
print("Division of float and float")
print("a =", a, "b =", b, "a/b =", a / b)
```
**The result:**  
Division of integer and float  
a = 10 b = -20.5 a/b = -0.4878048780487805  
Division of float and float  
a = -2.5 b = 125.0 a/b = -0.02

**What about division in complex terms?**  
When one of the operands is a complex number, division occurs between the other operand and both parts of the complex number (real and imaginary).  
```python
a = 7.5 + 7.5j
b = 2.5
print("Division of complex and float")
print("a =", a, "b =", b, "a/b =", a / b)
print("a =", a, "b =", b, "b/a =", b / a)
```
**The result:**  
Division of complex and float  
a = (7.5+7.5j) b = 2.5 a/b = (3+3j)  
a = (7.5+7.5j) b = 2.5 b/a = (0.16666666666666666-0.16666666666666666j)

**What is the modulus operator in Python?**  
Python defines the "%" symbol, known as the modulus (or modulo) operator. It returns the remainder after the denominator divides the numerator. It can also be called the remainder operator. For example, when 10 is divided by 3, the quotient is 3 and the remainder is 1. Hence, 10 % 3 results in 1.

**What if we use float and integer with the modulus operator?**  
```python
a = 10
b = 2.5
print("a =", a, "b =", b, "a%b =", a % b)

a = 10
b = 1.5
print("a =", a, "b =", b, "a%b =", a % b)

a = 7.7
b = 2.5
print("a =", a, "b =", b, "a%b =", a % b)

a = 12.4
b = 3
print("a =", a, "b =", b, "a%b =", a % b)
```
**The result:**  
a = 10 b = 2.5 a%b = 0.0  
a = 10 b = 1.5 a%b = 1.0  
a = 7.7 b = 2.5 a%b = 0.20000000000000018  
a = 12.4 b = 3 a%b = 0.40000000000000036

**Does Python accept complex numbers for the modulus operator?**  
No, Python does not accept complex numbers as operands in the modulus operation. It throws a TypeError: unsupported operand type(s) for %.

**What is the exponent operator?**  
Python uses ** (double asterisk) as the exponent operator (sometimes called the raised to operator). For a**b, you say a raised to b, or the bth power of a. If both operands are integers, the result is also an integer. If either operand is a float, the result is a float. Similarly, if either operand is a complex number, the exponent operator returns a complex number. If the base is 0, the result is 0, and if the index is 0, the result is always 1.

**What is the result of the following operations?**  
```python
a = 10
b = 2
print("a =", a, "b =", b, "a**b =", a ** b)

a = 10
b = 1.5
print("a =", a, "b =", b, "a**b =", a ** b)

a = 7.7
b = 2
print("a =", a, "b =", b, "a**b =", a ** b)

a = 1 + 2j
b = 4
print("a =", a, "b =", b, "a**b =", a ** b)

a = 12.4
b = 0
print("a =", a, "b =", b, "a**b =", a ** b)
print("a =", a, "b =", b, "b**a =", b ** a)
```
**The result:**  
a = 10 b = 2 a**b = 100  
a = 10 b = 1.5 a**b = 31.622776601683793  
a = 7.7 b = 2 a**b = 59.290000000000006  
a = (1+2j) b = 4 a**b = (-7-24j)  
a = 12.4 b = 0 a**b = 1.0  
a = 12.4 b = 0 b**a = 0.0  

**What is floor division?**  
Floor division is also called integer division. Python uses the // (double forward slash) symbol for this purpose. Unlike the modulus operator, which returns the remainder, the floor division gives the quotient of the division of operands involved. If both operands are positive, the floor operator returns a number with the fractional part removed. For example, the floor division of 9.8 by 2 returns 4 (pure division is 4.9, strip the fractional part, result is 4). If one of the operands is negative, the result is rounded away from zero (towards negative infinity). For example, floor division of -9.8 by 2 returns -5 (pure division is -4.9, rounded away from 0).

**What is the result of the following operations?**  
```python
a = 9
b = 2
print("a =", a, "b =", b, "a//b =", a // b)

a = 9
b = -2
print("a =", a, "b =", b, "a//b =", a // b)

a = 10
b = 1.5
print("a =", a, "b =", b, "a//b =", a // b)

a = -10
b = 1.5
print("a =", a, "b =", b, "a//b =", a // b)
```
**The result:**  
a = 9 b = 2 a//b = 4  
a = 9 b = -2 a//b = -5  
a = 10 b = 1.5 a//b = 6.0  
a = -10 b = 1.5 a//b = -7.0  

**Some Precedence and Associativity of Arithmetic Operators:**  
| Operator(s) | Description | Associativity |
|-------------|-------------|---------------|
| **          | Exponent Operator | Right to Left |
| %, *, /, // | Modulus, Multiplication, Division, and Floor Division | Left to Right |
| +           | Addition and Subtraction Operators | Left to Right |

The following table shows the precedence and associativity of the arithmetic operators in Python.

**How does the Python interpreter behave when dealing with complex numbers?**  
Arithmetic operators behave slightly differently when both operands are complex number objects. 

- **Addition and Subtraction:** Addition and subtraction of complex numbers is a simple addition/subtraction of respective real and imaginary components.
- **Multiplication:** Multiplication of complex numbers is similar to multiplication of two binomials in algebra. If "a+bj" and "x+yj" are two complex numbers, then their multiplication is given by the formula:  
  \((a+bj)*(x+yj) = ax + ayj + bxyj + byj^2 = (ax - by) + (ay + bx)j\)
- **Division:** To understand how the division of two complex numbers takes place, we should use the conjugate of a complex number. Python's complex object has a `conjugate()` method that returns a complex number with the sign of the imaginary part reversed. To divide two complex numbers, divide and multiply the numerator as well as the denominator with the conjugate of the denominator.

**Does the complex class support the modulus operator (%) and floor division operator (//)?**  
No, the complex class does not support the modulus operator (%) and floor division operator (//). Attempting to use these operators with complex numbers will result in a TypeError.

## Comparasion operation
**What is Python comparison operator?**  
Comparison operators in Python are essential for conditional statements (if, else, and elif) and looping statements (while and for loops). These operators are also known as relational operators. Some well-known operators include "<" for less than and ">" for greater than. Python also uses two additional operators that combine the "=" symbol with these two: "<=" for less than or equal to and ">=" for greater than or equal to. 

Comparison operators are binary in nature, requiring two operands. An expression involving a comparison operator is called a Boolean expression and always returns either True or False. Both operands can be Python literals, variables, or expressions. Since Python supports mixed arithmetic, you can have any number type operands.

**What is the comparison of Booleans?**  
Boolean objects in Python are essentially integers: True is 1 and False is 0. In fact, Python treats any non-zero number as True. Comparison of Boolean objects is possible, and "False < True" evaluates to True.

**Example:**
```python
print("Comparison of Booleans")
a = True
b = False
print("a =", a, "b =", b, "a < b is", a < b)
print("a =", a, "b =", b, "a > b is", a > b)
print("a =", a, "b =", b, "a == b is", a == b)
print("a =", a, "b =", b, "a != b is", a != b)
```
**The result:**  
```
Comparison of Booleans
a = True b = False a < b is False
a = True b = False a > b is True
a = True b = False a == b is False
a = True b = False a != b is True
```

**Can sequences be compared?**  
In Python, only similar sequence objects can be compared. A string object can be compared with another string only. A list cannot be compared with a tuple, even if both contain the same items.

**Is there another way to compare sequences?**  
Sequence objects are compared using a lexicographical ordering mechanism. The comparison starts from the item at the 0th index. If they are equal, the comparison moves to the next index until the items at a certain index are not equal, or one of the sequences is exhausted. If one sequence is an initial subsequence of the other, the shorter sequence is considered the smaller (lesser) one. The comparison result depends on the difference in values of items at the index where they are unequal. For example, `'BAT' > 'BAR'` is True, as T comes after R in Unicode order. If all items of two sequences compare equal, the sequences are considered equal.

**Example:**
```python
print("Comparison of strings")
a = 'BAT'
b = 'BALL'
print("a =", a, "b =", b, "a < b is", a < b)
print("a =", a, "b =", b, "a > b is", a > b)
print("a =", a, "b =", b, "a == b is", a == b)
print("a =", a, "b =", b, "a != b is", a != b)
```
**The result:**  
```
Comparison of strings
a = BAT b = BALL a < b is False
a = BAT b = BALL a > b is True
a = BAT b = BALL a == b is False
a = BAT b = BALL a != b is True
```

**Can we compare dictionaries?**  
The use of "<" and ">" operators for Python dictionaries is not defined. In such cases, a TypeError will be raised: `TypeError: '<' not supported between instances of 'dict' and 'dict'`. 

Equality comparison checks if the lengths of both dictionary items are the same. The length of a dictionary is the number of key-value pairs it contains. Python dictionaries are compared by length, meaning that the dictionary with fewer elements is considered less than a dictionary with more elements.

## Assignment operation
**What are cumulative or augmented assignment operators?**  
Python augmented assignment operators combine an arithmetic operation with assignment in a single statement. These operators allow you to perform an operation on a variable and then assign the result back to that same variable. Since Python supports mixed arithmetic, the two operands may be of different types. However, the type of the left operand changes to the type of the right operand if it is wider.

For example, the `+=` operator is an augmented assignment operator. It is also called the cumulative addition operator, as it adds the value of "b" to "a" and assigns the result back to the variable "a".

**What are the types of augmented assignment operators?**  
1. **Augmented Addition Operator (`+=`)**  
2. **Augmented Subtraction Operator (`-=`)**  
3. **Augmented Multiplication Operator (`*=`)**  
4. **Augmented Division Operator (`/=`)**  
5. **Augmented Modulus Operator (`%=`)**  
6. **Augmented Exponent Operator (`**=`)**  
7. **Augmented Floor Division Operator (`//=`)**  

**What is the syntax of augmented assignment operators?**  
The syntax for using augmented assignment operators is as follows:  
```python
<variable> <arithmetic_operation>= <expression>
```
Where `<variable>` is the variable you want to modify, `<arithmetic_operation>` is the specific operation you want to perform (like `+`, `-`, `*`, `/`, etc.), and `<expression>` can be another value or variable that you want to use in the operation.

**Example of using augmented assignment operators:**
```python
# Augmented Addition
a = 5
a += 3  # Equivalent to a = a + 3
print(a)  # Output: 8

# Augmented Subtraction
b = 10
b -= 4  # Equivalent to b = b - 4
print(b)  # Output: 6

# Augmented Multiplication
c = 2
c *= 5  # Equivalent to c = c * 5
print(c)  # Output: 10

# Augmented Division
d = 20
d /= 4  # Equivalent to d = d / 4
print(d)  # Output: 5.0

# Augmented Modulus
e = 10
e %= 3  # Equivalent to e = e % 3
print(e)  # Output: 1

# Augmented Exponent
f = 2
f **= 3  # Equivalent to f = f ** 3
print(f)  # Output: 8

# Augmented Floor Division
g = 17
g //= 5  # Equivalent to g = g // 5
print(g)  # Output: 3
```

## Logical operation
**What is Python logical operation used for?**  
Python logical operators are used to form compound Boolean expressions. Each operand for these logical operators is itself a Boolean expression. For example:
- `age > 16 and marks > 80`
- `percentage < 50 or attendance < 75`

**What values does Python interpret as False?**  
Python interprets the following values as False:
- The keyword `False`
- `None`
- Numeric zero of all types (e.g., `0`, `0.0`)
- Empty sequences (e.g., `''`, `()`, `[]`)
- Empty dictionaries (`{}`)
- Empty sets (`set()`)

All other values are treated as True.

**What are the symbols of logical operations?**  
There are three logical operators in Python:
- `and`
- `or`
- `not`  
These operators must be written in lowercase.

**When does the "and" operation return True?**  
For a compound Boolean expression using `and` to be True, both operands must be True. If any or both operands evaluate to False, the expression returns False. The `and` operator follows these rules:
- If it encounters a falsy value, it immediately returns that value.
- If all values are truthy, it returns the last value.

**What is the result of `x and y` if `x = 10` and `y = 20?`**  
The expression `x and y` returns `20` because both `x` and `y` are truthy.

**What happens if `x` is falsy, for example, `x = 0`?**  
If `x` is `0`, the expression `x and y` would return `0`, which is the first falsy value encountered.

**When does the "or" operation return True?**  
The `or` operator returns True if any of the operands is True. For the compound Boolean expression to be False, both operands must be False. The `or` operator follows these rules:
- If it encounters a truthy value, it immediately returns that value.
- If all values are falsy, it returns the last value.

**What is the logic of the "not" operation?**  
The `not` operator is a unary operator that reverses the state of the Boolean operand that follows it. As a result:
- `not True` becomes `False`
- `not False` becomes `True`

**How does the Python interpreter evaluate the logical operators?**  
- The expression `x and y` first evaluates `x`. If `x` is false, its value is returned; otherwise, `y` is evaluated, and the resulting value is returned.
- The expression `x or y` first evaluates `x`. If `x` is true, its value is returned; otherwise, `y` is evaluated, and the resulting value is returned.

**Example of logical operations:**
```python
x = 10
y = 20
print(x and y)  # Output: 20

x = 0
print(x and y)  # Output: 0

a = True
b = False
print(a or b)   # Output: True
print(a and b)  # Output: False
print(not a)    # Output: False
print(not b)    # Output: True
```

These logical operations are fundamental in controlling the flow of programs, especially in conditional statements and loops.


## Bitwise operation
**What is Python bitwise operation used for?**  
Python bitwise operators are used to perform bitwise operations on integer-type objects. Instead of treating the object as a whole, it is treated as a string of bits, and different operations are performed on each bit in the string.

**What are the symbols of the bitwise operations?**  
Python has six bitwise operators:
- `&` (Bitwise AND)
- `|` (Bitwise OR)
- `^` (Bitwise XOR)
- `~` (Bitwise NOT)
- `<<` (Bitwise Left Shift)
- `>>` (Bitwise Right Shift)  
All these operators (except `~`) are binary in nature, meaning they operate on two operands. Each operand is a binary digit (bit), either 1 or 0.

**What are the topics of the bitwise operations?**  
1. **Bitwise AND Operator (`&`)**  
2. **Bitwise OR Operator (`|`)**  
3. **Bitwise XOR Operator (`^`)**  
4. **Bitwise NOT Operator (`~`)**  
5. **Bitwise Left Shift Operator (`<<`)**  
6. **Bitwise Right Shift Operator (`>>`)**  

**What is the "&" operation?**  
The Bitwise AND operator is somewhat similar to the logical AND operator. It returns True only if both bit operands are 1 (i.e., True).

**Explain this code:**
```python
a = 60
b = 13
print("a:", a, "b:", b, "a&b:", a & b)
```
**Output:**  
```
a: 60 b: 13 a&b: 12
```
To understand how Python performs the operation, we first obtain the binary equivalent of each variable:
```python
print("a:", bin(a))  # Output: a: 0b111100
print("b:", bin(b))  # Output: b: 0b1101
```
For convenience, we can represent these numbers in an 8-bit format:
- `a` is `00111100`
- `b` is `00001101`

Now, we manually perform the AND operation on each corresponding bit of these two numbers:
```
  0011 1100
&
  0000 1101
-------------
  0000 1100
```
Converting the resultant binary back to an integer gives us 12:
```python
int('00001100', 2)  # Output: 12
```

**What is the "|" operation?**  
The `|` symbol (called pipe) is the Bitwise OR operator. If any bit operand is 1, the result is 1; otherwise, it is 0.

**What is the "^" operation?**  
The term XOR stands for exclusive OR. The result of the OR operation on two bits will be 1 if only one of the bits is 1. In other words, the XOR operation returns True if exactly one of the operands is True, but not both:
- `0 ^ 0` is `0`
- `0 ^ 1` is `1`
- `1 ^ 0` is `1`
- `1 ^ 1` is `0`

**What is the "~" operation?**  
The `~` operator is the binary equivalent of the logical NOT operator. It flips each bit so that 1 is replaced by 0, and 0 by 1, returning the complement of the original number. Python uses the 2's complement method. For positive integers, it is obtained simply by reversing the bits. For negative numbers, `-x` is represented using the bit pattern for `(x-1)` with all of the bits complemented (switched from 1 to 0 or 0 to 1).

**What is the "<<" operator?**  
The left shift operator (`<<`) shifts the most significant bits to the left by the number specified on the right side of the `<<` symbol. For example, `x << 2` shifts the binary representation of `x` two bits to the left.

**Example:**
```python
a = 60
print("a:", a, "a << 2:", a << 2)
```
**Result:**  
```
a: 60 a << 2: 240
```
**Binary Representation:**
```
  0011 1100
<<
    2
-------------
  1111 0000
```
The result is `240` because shifting left by 2 bits is equivalent to multiplying by \(2^2\) (or 4).

**What is the ">>" operator?**  
The right shift operator (`>>`) shifts the least significant bits to the right by the number specified on the right side of the `>>` symbol. For example, `x >> 2` shifts the binary representation of `x` two bits to the right.

**Example:**
```python
a = 60
print("a:", a, "a >> 2:", a >> 2)
```
**Result:**  
```
a: 60 a >> 2: 15
```
**Binary Representation:**
```
  0011 1100
>>
    2
-------------
  0000 1111
```
The result is `15` because shifting right by 2 bits is equivalent to performing integer division by \(2^2\) (or 4). 

### Summary of Bitwise Operations
- **Bitwise AND (`&`)**: Returns 1 if both bits are 1.
- **Bitwise OR (`|`)**: Returns 1 if at least one bit is 1.
- **Bitwise XOR (`^`)**: Returns 1 if exactly one of the bits is 1.
- **Bitwise NOT (`~`)**: Flips the bits (1 becomes 0 and 0 becomes 1).
- **Bitwise Left Shift (`<<`)**: Shifts bits to the left, filling with 0s on the right.
- **Bitwise Right Shift (`>>`)**: Shifts bits to the right, discarding bits on the right.

These bitwise operations are useful in various applications, such as low-level programming, graphics, cryptography, and performance optimization tasks where direct manipulation of bits is required.

## Membershipship operation
**What are Python membership operations?**  
The membership operators in Python help us determine whether an item is present in a given container type object, or in other words, whether an item is a member of the given container type object.

**What is the "in" operator?**  
The "in" operator is used to check whether a substring is present in a bigger string, any item is present in a list or tuple, or a sub-list or sub-tuple is included in a list or tuple.

**What is the "not in" operator?**  
The "not in" operator is used to check if a sequence with the given value is not present in the object like a string, list, tuple, etc.



## Identity operation
**What are Python identity operations?**  
The identity operators compare the objects to determine whether they share the same memory and refer to the same object type (data type).

**What is the "is" operator?**  
The 'is' operator evaluates to True if both the operand objects share the same memory location. The memory location of the object can be obtained by the "id()" function. If the "id()" of both variables is the same, the "is" operator returns True.

**What is the "is not" operator?**  
The 'is not' operator evaluates to True if both the operand objects do not share the same memory location or if both operands are not the same objects.

## Precedence operation
**What is Python Operator Precedence?**  
An expression may have multiple operators to be evaluated. The operator precedence defines the order in which operators are evaluated. In other words, the order of operator evaluation is determined by the operator precedence.

**What is the BODMAS rule?**  
The BODMAS rule states that brackets are evaluated first, followed by division and multiplication operators, and finally addition and subtraction operators.

**What is the importance of operator associativity?**  
Associativity determines the order of evaluation for operators with the same precedence, typically left to right for most operators.

**Operator Precedence in Python:**  
The following table lists all the operators in Python in their decreasing order of precedence. Operators in the same cell under the Operators column have the same precedence.

The following table lists all the operators in Python in their decreasing order of precedence. Operators in the same cell under the Operators column have the same precedence
Sr.No.	    Operator & Description
1	        (), [], {} - Parentheses and braces
2	        [index], [index:index] - Subscription, slicing
3	        await x - Await expression
4	        ** - Exponentiation
5	        +x, -x, ~x - Positive, negative, bitwise NOT
6	        *, @, /, //, % - Multiplication, matrix multiplication, division, floor division, remainder
7	        +, - - Addition and subtraction
8	        <<, >> - Left Shifts, Right Shifts
9	        & - Bitwise AND
10	        ^ - Bitwise XOR
11	        in, not in, is, is not, <, <=, >, >=, !=, == - Comparisons, membership tests, identity tests
12	        not x - Boolean NOT
13	        and - Boolean AND
14	        or - Boolean OR
15	        if else - Conditional expression
16	        lambda - Lambda expression
17          := - Walrus operator



## Comments
**What are comments?**  
Python comments are programmer-readable explanations or annotations in the Python source code. They are added to make the source code easier for humans to understand and are ignored by the Python interpreter. Comments enhance the readability of the code and help programmers understand the code more carefully.

**What are the types of comments supported by Python?**  
- **Single-line comments**  
- **Multi-line comments**  
- **Docstring comments**  

**What are single-line comments?**  
Single-line comments in Python start with a hash symbol (#) and extend to the end of the line. They are used to provide short explanations or notes about the code. They can be placed on their own line above the code they describe or at the end of a line of code (known as an inline comment) to provide context or clarification about that specific line. A standalone single-line comment occupies an entire line by itself, starting with a hash symbol (#).

**What are multi-line comments?**  
In Python, multi-line comments are used to provide longer explanations or notes that span multiple lines. While Python does not have a specific syntax for multi-line comments, there are two common ways to achieve this: consecutive single-line comments and triple-quoted strings.

**What are consecutive single-line comments?**  
Consecutive single-line comments refer to using the hash symbol (#) at the beginning of each line. This method is often used for longer explanations or to section off parts of the code.  
**Example:**  
```python
# This function calculates the factorial of a number
# using an iterative approach. The factorial of a number
# n is the product of all positive integers less than or
# equal to n. For example, factorial(5) is 5*4*3*2*1 = 120
```

**What are triple-quoted comments?**  
Triple-quoted strings (''' or """) can be used to create multi-line comments. These strings are technically string literals but can be used as comments if they are not assigned to any variable or used in expressions. This pattern is often used for block comments or when documenting sections of code that require detailed explanations.  
**Example:**  
```python
"""
This function calculates the greatest common divisor (GCD)
of two numbers using the Euclidean algorithm. The GCD of
two numbers is the largest number that divides both of them
without leaving a remainder.
"""
```

**What are Docstring comments?**  
Documentation comments, also known as docstrings, provide a way to incorporate documentation within your code. This can be useful for explaining the purpose and usage of modules, classes, functions, and methods. Effective use of documentation comments helps other developers understand your code and its purpose without needing to read through all the details of the implementation. Docstrings are a special type of comment that is written using triple quotes (''' or """) and are placed immediately after the definition of the entity they document. Docstrings can be accessed programmatically, making them an integral part of Python's built-in documentation tools.

**How to access docstrings?**  
Docstrings can be accessed using the `.__doc__` attribute or the `help()` function. This makes it easy to view the documentation for any module, class, function, or method directly from the interactive Python shell or within the code.  
**Example:**  
```python
def greet(name):
    """
    This function greets the person whose name is passed as a parameter.

    Parameters:
    name (str): The name of the person to greet

    Returns:
    None
    """
print(greet.__doc__)

# OR 

help(greet)
```


## User input
**Why is user input important in computer applications?**  
User input makes the application interactive, allowing users to engage with the software while it is running.

**What are the common forms of user input in applications?**  
Applications may accept user input in the following forms:  
- Text entered in the console (using `sys.stdin`)  
- Graphical user interface (GUI)  
- Web-based interface  

**What is the purpose of Python's input() function?**  
The `input()` function allows you to assign different values to a variable at runtime, while the program is running.

**What is the syntax for using the input() function?**  
```python
var = input()
```

**How does the input() function work?**  
When the interpreter encounters the `input()` function, it waits for the user to enter data from the keyboard until the Enter key is pressed. The entered characters are stored as a string variable for further use.

**What happens after the Enter key is pressed?**  
After the Enter key is pressed, the program proceeds to the next statement.

**How can you provide a prompt in the input() function?**  
You can include a prompt text inside the `input()` function, which will appear before the cursor when the code is run.

**What is the syntax for using a prompt with the input() function?**  
```python
var = input("Enter your prompt text here: ")
```

**What is the benefit of using a prompt in the input() function?**  
A prompt helps guide the user on what information to enter, making the application more user-friendly.

**How can you combine input and type casting in one line?**  
You can directly use the `int()` function with the `input()` function.  
**Example:**  
```python
width = int(input("Enter width: "))
height = int(input("Enter height: "))
area = width * height
print("Area of rectangle =", area)
```

**What is the purpose of the print() function in Python?**  
The `print()` function displays the value of Python expressions on the console or standard output.

**How can you print multiple values using the print() function?**  
Separate the values with commas inside the parentheses.  
**Example:**  
```python
a = "Hello World"
b = 100
c = 25.50
print(a, b, c)
```

**How can you change the separator in the print() function?**  
Use the `sep` parameter to define a custom separator.  
**Example:**  
```python
print(city, state, country, sep=',')
```

**How can you prevent print() from adding a newline at the end?**  
Use the `end` parameter to specify what to print at the end instead of a newline.  
**Example:**  
```python
print("City:", city, end=" ")
print("State:", state)
```

## Numbers
**What are the built-in number types available in Python?**  
- **Integers (int)**  
- **Floating-point numbers (float)**  
- **Complex numbers (complex)**  

**What is the Boolean data type in Python?**  
The `bool` type can be treated as a sub-type of `int`, with values `True` (1) and `False` (0).

**How is an integer defined in Python?**  
An integer is a whole number without a fractional part. Examples include 1234, 0, and -55.

**How can you create an integer in Python?**  
- **Literal representation:** `a = 10`  
- **Expression evaluating to an integer:** `c = a + b`  
- **Using `int()` function:** `a = int(10.5)`, `b = int("100")`  

**How can you represent binary, octal, and hexadecimal numbers in Python?**  
- **Binary:** Prefix with `0b` (e.g., `a = 0b101`)  
- **Octal:** Prefix with `0o` (e.g., `a = 0o107`)  
- **Hexadecimal:** Prefix with `0x` (e.g., `a = 0xA2`)  

**What defines a floating-point number in Python?**  
A floating-point number has an integer part and a fractional part, separated by a decimal point (e.g., 9.99, -0.999).

**How can you create a float in Python?**  
- **Literal notation:** `a = 9.99`  
- **Result of an expression:** `c = a / b`  
- **Using `float()` function:** `a = float("123.45")`  

**What is scientific notation in floating-point numbers?**  
It represents numbers in the form of a coefficient and an exponent (e.g., `1.23E+3`).

**What is a complex number in Python?**  
A complex number consists of a real part and an imaginary part, represented as `x + yi` (or `x + yj` in Python).

**How can you create a complex number in Python?**  
- **Literal representation:** `a = 5 + 6j`  
- **Using `complex()` function:** `a = complex(5.3, 6)`  

**What attributes does a complex number have?**  
- **real:** Returns the real part.  
- **imag:** Returns the coefficient of the imaginary part.  

**What is the purpose of the `conjugate()` method in complex numbers?**  
It returns a complex number with the sign of the imaginary component reversed (e.g., `a.conjugate()`).

**How can you convert between integers and complex?**  
- `complex(x)`: Convert to a complex number with real part `x` and imaginary part `0`.  
- `complex(x, y)`: Convert to a complex number with real part `x` and imaginary part `y`.

## Bolleans
**What is the bool type in Python?**  
The `bool` type is a sub-type of `int` that has two possible values: `True` and `False`.

**How do Boolean values convert to other types in Python?**  
- `int(True)` returns `1`  
- `int(False)` returns `0`  
- `float(True)` returns `1.0`  
- `float(False)` returns `0.0`  
- `complex(True)` returns `(1 + 0j)`  
- `complex(False)` returns `(0 + 0j)`  

**What is a Boolean expression in Python?**  
A Boolean expression evaluates to a Boolean value (`True` or `False`), often involving comparison operators.

**What is the purpose of the bool() function?**  
The `bool()` function returns the truth value of an expression. It returns `True` if the expression evaluates to true; otherwise, it returns `False`. Without parameters, it returns `False`.