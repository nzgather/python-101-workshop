[<img src="../assets/gather_workshops_logo.svg" alt="Gather Workshops" style="width:15em" />](http://gathergather.co.nz/workshops/)
[<img src="../assets/python-logo-generic.svg" alt="Gather Workshops" style="width:20em; margin-left:2em;" />](http://www.python.org)

# Data Types Cheat Sheet

## Numbers: integers and floats

* Integers don't have a decimal place.
* Floats have a decimal place.
* Math mostly works the way it does on a calculator, and you can use parentheses to override the order of operations.

#### Math: addition, subtraction, multiplication

<b>addition</b>: 2 + 2<br />
<b>subtraction</b>: 0 - 2<br />
<b>multiplication</b>: 2 * 3<br />

#### Math: division

<pre>
>>> 4 / 2
2
>>> 1 / 2
0
</pre>

* Integer division produces an integer. You need a number that knows about the decimal point to get a decimal out of division:

<pre>
>>> 1.0 / 2
0.5
>>> float(1) / 2
0.5
</pre>

#### Types

<pre>
>>> type(1)
&lt;type 'int'>
>>> type(1.0)
&lt;type 'float'>
</pre>

## Strings

* Strings are bits of text, and contain characters like numbers, letters, whitespace, and punctuation.
* String are surrounded by quotes.
* Use triple-quotes (""") to create whitespace-preserving multi-line strings.

<pre>
>>> "Hello"
'Hello'
</pre>

#### String concatenation

<pre>
>>> "Hello" + "World"
HelloWorld
>>> "Hello" + "World" + 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot concatenate 'str' and 'int' objects
>>> "Hello" + "World" + str(1)
'HelloWorld1'
</pre>

#### Printing strings

<pre>
>>> print "Hello" + "World"
HelloWorld
</pre>

<pre>
>>> name = "Jessica"
>>> print "Hello " + name
Hello Jessica
</pre>

<pre>
>>> print """In 2009,
...     The monetary component of the Nobel Prize
...         was US $1.4 million."""
In 2009,
    The monetary component of the Nobel Prize
        was US $1.4 million.
</pre>

#### Types

<pre>
>>> type("Hello")
&lt;type 'str'>
</pre>

## Booleans

* There are two booleans, <code>True</code> and <code>False</code>.
* Use booleans to make decisions.

#### Containment with 'in' and 'not in'

<pre>
>>> "H" in "Hello"
True
>>> "a" not in ["a", "b", "c"]
False
</pre>

#### Equality

* <code>==</code> tests for equality
* <codE>!=</code> tests for inequality
* <code>&lt;</code>, <code>&lt;=</code>, <code>&gt;</code>, and <code>&gt;=</code> have the same meaning as in math class.

<pre>
>>> 0 == 0
True
>>> 0 == 1
False
</pre>

<pre>
"a" != "a"
</pre>

<pre>
"a" != "A"
</pre>

#### Use with if/else blocks

* When Python encounters the <code>if</code> keyword, it evaluates the expression following the keyword and before the colon. If that expression is <code>True</code>, Python executes the code in the indented code block under the if line. If that expression is <code>False</code>, Python skips over the code block.

<pre>
temperature = 32
if temperature > 60 and temperature &lt; 75:
    print "It's nice and cozy in here!"
else:
    print "Too extreme for me."
</pre>

#### Types

<pre>
>>> type(True)
&lt;type 'bool'>
>>> type(False)
&lt;type 'bool'>
</pre>

## Lists

* Use lists to store data where order matters.
* Lists are indexed starting with 0.

#### List initialization

<pre>
>>> my_list = []
>>> my_list
[]
>>> your_list = ["a", "b", "c", 1, 2, 3]
>>> your_list
['a', 'b', 'c', 1, 2, 3]
</pre>

#### Access and adding elements to a list

<pre>
>>> len(my_list)
0
>>> my_list[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> my_list.append("Alice")
>>> my_list
['Alice']
>>> len(my_list)
1
>>> my_list[0]
'Alice'
>>> my_list.insert(0, "Amy")
>>> my_list
['Amy', 'Alice']
</pre>

<pre>
>>> my_list = ['Amy', 'Alice']
>>> 'Amy' in my_list
True
>>> 'Bob' in my_list
False
</pre>

#### Changing elements in a list

<pre>
>>> your_list = []
>>> your_list.append("apples")
>>> your_list[0]
'apples'
>>> your_list[0] = "bananas"
>>> your_list
['bananas']
</pre>

#### Slicing lists

<pre>
>>> her_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
>>> her_list[0]
'a'
>>> her_list[0:3]
['a', 'b', 'c']
>>> her_list[:3]
['a', 'b', 'c']
>>> her_list[-1]
'h'
>>> her_list[5:]
['f', 'g', 'h']
>>> her_list[:]
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
</pre>

#### Strings are a lot like lists

<pre>
>>> my_string = "Hello World"
>>> my_string[0]
'H'
>>> my_string[:5]
'Hello'
>>> my_string[6:]
'World'
>>> my_string = my_string[:6] + "Jessica"
>>> my_string
'Hello Jessica'
</pre>

* One big way in which strings are different from lists is that lists are mutable (you can change them), and strings are immutable (you can't change them). To "change" a string you have to make a copy:

<pre>
>>> h = "Hello"
>>> h[0] = "J"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> h = "J" + h[1:]
>>> h
'Jello'
</pre>

#### Types

<pre>
>>> type(my_list)
&lt;type 'list'>
</pre>

## Dictionaries

* Use dictionaries to store key/value pairs.
* Dictionaries do not guarantee ordering.
* A given key can only have one value, but multiple keys can have the same value.

#### Initialization

<pre>
>>> my_dict = {}
>>> my_dict
{}
>>> your_dict = {"Alice" : "chocolate", "Bob" : "strawberry", "Cara" : "mint chip"}
>>> your_dict
{'Bob': 'strawberry', 'Cara': 'mint chip', 'Alice': 'chocolate'}
</pre>

#### Adding elements to a dictionary

<pre>
>>> your_dict["Dora"] = "vanilla"
>>> your_dict
{'Bob': 'strawberry', 'Cara': 'mint chip', 'Dora': 'vanilla', 'Alice': 'chocolate'}
</pre>

#### Accessing elements of a dictionary

<pre>
>>> your_dict["Alice"]
'chocolate'
>>> your_dict.get("Alice")
'chocolate'
</pre>

<pre>
>>> your_dict["Eve"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Eve'
>>> "Eve" in her_dict
False
>>> "Alice" in her_dict
True
>>> your_dict.get("Eve")
>>> person = your_dict.get("Eve")
>>> print person
None
>>> print type(person)
&lt;type 'NoneType'>
>>> your_dict.get("Alice")
'coconut'
</pre>

#### Changing elements of a dictionary

<pre>
>>> your_dict["Alice"] = "coconut"
>>> your_dict
{'Bob': 'strawberry', 'Cara': 'mint chip', 'Dora': 'vanilla', 'Alice': 'coconut'}
</pre>

#### Types

<pre>
>>> type(my_dict)
&lt;type 'dict'>
</pre>

---------------------------------------

Adapted from [Boston Python Workshop](https://openhatch.org/wiki/Boston_Python_Workshop_6/Data_types) content 
by [Gather](https://github.com/organizations/nzgather). CC-BY