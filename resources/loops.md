[Gather Workshops](http://gathergather.co.nz/workshops/) - [Python](http://www.python.org)

# Loops Cheat Sheet

##  For loops

Use a <code>for</code> loop to do something to every element in a list.

<pre>
>>> names = ["Jessica", "Adam", "Liz"]
>>> for name in names:
...     print name
...
Jessica
Adam
Liz</pre>

<pre>
>>> names = ["Jessica", "Adam", "Liz"]
>>> for name in names:
...     print "Hello " + name
...
Hello Jessica
Hello Adam
Hello Liz</pre>

###  <code>if</code> statements inside <code>for</code> loop

<pre>
>>> for name in ["Alice", "Bob", "Cassie", "Deb", "Ellen"]:
...     if name[0] in "AEIOU":
...         print name + " starts with a vowel."
...
Alice starts with a vowel.
Ellen starts with a vowel.</pre>

Sometimes you want to start with a new empty list, and only add to that list if some condition is true:

<pre>
>>> vowel_names = []
>>> for name in ["Alice", "Bob", "Cassie", "Deb", "Ellen"]:
...     if name[0] in "AEIOU":
...         vowel_names.append(name)
...
>>> print vowel_names
['Alice', 'Ellen']</pre>

###  <code>for</code> loops inside <code>for</code> loops

You can put <code>for</code> loops inside <code>for</code> loops. The indentation dictates which <code>for</code> loop a line is in.

<pre>
>>> letters = ["a", "b", "c"]
>>> numbers = [1, 2, 3]
>>> for letter in letters:
...     for number in numbers:
...         print letter * number
...
a
aa
aaa
b
bb
bbb
c
cc
ccc</pre>

The order of the <code>for</code> loops matters. Compare the above example with this one:

<pre>
>>> for number in numbers:
...     for letter in letters:
...         print number * letter
...
a
b
c
aa
bb
cc
aaa
bbb
ccc</pre>

##  Useful functions related to lists and for loops

####  sorting lists

Use <code>.sort()</code> to sort a list:

<pre>
>>> names = ["Eliza", "Joe", "Henry", "Harriet", "Wanda", "Pat"]
>>> names.sort()
>>> names
['Eliza', 'Harriet', 'Henry', 'Joe', 'Pat', 'Wanda']
</pre>

####  Getting the maximum and minimum values from a list

<pre>
>>> numbers = [0, 3, 10, -1]
>>> max(numbers)
10
>>> min(numbers)
-1
</pre>

####  Generating a list of numbers easily with <code>range()</code>

The <code>range()</code> function returns a list of numbers. This is handy for when you want to generate a list of numbers on the fly instead of creating the list yourself.

<pre>
>>> range(5)
[0, 1, 2, 3, 4]
</pre>

Use <code>range</code> when you want to loop over a bunch of numbers in a list:

<pre>
>>> numbers = range(5)
>>> for number in numbers:
...     print number * number
...
0
1
4
9
16
</pre>

We could rewrite the above example like this:

<pre>
>>> for number in range(5):
...     print number * number
...
0
1
4
9
16
</pre>

##  <code>while</code> loops

Use a <code>while</code> loop to loop so long as a condition is <code>True</code>.

<pre>>>> i = 0
>>> while i < 10:
...     print i
...     i = i + 1
...
0
1
2
3
4
5
6
7
8
9</pre>

###  <code>break</code> keyword

Use the <code>break</code> keyword to break out of a loop early:

<pre>
>>> i = 0
>>> while True:
...     print i
...     i = i + 1
...     if i > 10:
...         break
...
0
1
2
3
4
5
6
7
8
9
10</pre>

###  Get user input with <code>raw_input()</code>

<pre>
>>> while True:
...     input = raw_input("Please type something> ")
...     if input == "Quit":
...         print "Goodbye!"
...         break
...     else:
...         print "You said: " + input
...
Please type something> Hello
You said: Hello
Please type something> How are you?
You said: How are you?
Please type something> Quit
Goodbye!
>>> </pre>

---------------------------------------

Adapted from [Boston Python Workshop](https://openhatch.org/wiki/Boston_Python_Workshop_6/Data_types) content
by [Gather](https://github.com/organizations/nzgather). CC-BY