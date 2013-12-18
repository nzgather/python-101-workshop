[<img src="../assets/gather_workshops_logo.svg" alt="Gather Workshops" style="width:15em" />](http://gathergather.co.nz/workshops/)
[<img src="../assets/python-logo-generic.svg" alt="Gather Workshops" style="width:20em; margin-left:2em;" />](http://www.python.org)

# Welcome to the Tutorial!

This tutorial covers several core programming concepts that we'll build upon during the following interactive lecture. It will take 1-2 hours to complete. There's a break in the middle, and exercises at the middle and end to help review the material.

This is an interactive tutorial! As you go through this tutorial, any time you see something that looks like this:

<pre>
a = "Hello"
</pre>

you should type the expression at a Python prompt, hitting Return after every line and noting the output.

No copying and pasting! You'll learn the concepts better if you type them out yourself.

## Math

Math in Python looks a lot like math you type into a calculator. A Python prompt makes a great calculator if you need to crunch some numbers and don't have a good calculator handy.

### Addition

<pre>
2 + 2
1.5 + 2.25
</pre>

### Subtraction

<pre>
4 - 2
100 - .5
0 - 2
</pre>

### Multiplication

<pre>
2 * 3
</pre>

### Division

<pre>
4 / 2
1 / 2
</pre>

Hey now! That last result is probably not what you expected. What's going on here is that integer divison produces an integer. You need a number that knows about the decimal point to get a decimal out of division:

<pre>
1.0 / 2
</pre>

This means you have to be careful when manipulating fractions. If you were doing some baking and needed to add 3/4 of a cup of flour and 1/4 of a cup of flour, we know in our heads that 3/4 + 1/4 = 1 cup. But try that at the Python prompt:

<pre>
3/4 + 1/4
</pre>

What do you need to do to get the right answer? Use data types that understand decimals for each of the divisions:

<pre>
3.0/4 + 1.0/4
3.0/4.0 + 1.0/4.0
</pre>

The two previous expressions produce the same result. You only need to make one of the numbers in each fraction have a decimal. When the Python interpreter goes to do the division, it notices that one of the numbers in the fraction cares about decimals and says "that means I have to make the other number care about decimals too".

## Types

There's a helpful <b>function</b> (more on what a function is in a second) called <code>type</code> that tells you what kind of thing -- what <b>data type</b> -- Python thinks something is. We can check for ourselves that Python considers '1' and '1.0' to be different data types:

<pre>
type(1)
type(1.0)
</pre>

So now we've seen two data types: <b>integers</b> and <b>floats</b>.

I used the term 'function' without explaining what it is -- we'll talk about functions more in a bit, and write our own, but for now know these things:

* Functions encapsulate some useful bit of work. We save that useful bit of work inside the function so we don't have to type it over and over again every time we want to use it. So, for example, some nice person decided that being able to determine the type of an object was useful, so he or she put the Python code that figures out an object's type into the function <code>type</code>, and now we all get to use it, instead of having to write it ourselves.
* Functions are sort of like functions in math class. You provide input to a function and it produces output. The <code>type</code> function takes data as an input, and produces what type of data the data is (e.g. an integer or a float) as output.
* To use a function, write the name of the function followed by an open parenthesis, what the function takes as input (we call that input the <b>arguments</b> to the function), and then a close parenthesis.

So in this case 'type' is the name of the function, and it takes one argument; in the example we first give <code>type</code> an argument of 1 and then give it an argument of 1.0.

### Command history

Stop here and try hitting the Up arrow on your keyboard a few times. The Python <b>interpreter</b> saves a history of what you've entered, so you can arrow up to old commands and hit Return to re-run them!

## Variables

A lot of work gets done in Python using variables. Variables are a lot like the variables in math class, except that in Python variables can be of any data type, not just numbers.

<pre>
type(4)
x = 4
x
type(x)
2 * x
</pre>

Giving a name to something, so that you can refer to it by that name, is called <b>assignment</b>. Above, we assigned the name 'x' to 4, and after that we can use <code>x</code> wherever we want to use the number 4.

Variables can't have spaces or other special characters, and they need to start with a letter. Here are some valid variable names:

<code>magic_number = 1500</code><br />
<code>amountOfFlour = .75</code><br />
<code>my_name = "Jessica"</code>

Projects develop naming conventions: maybe multi-word variable names use underscores (like <code>magic_number</code>), or "camel case" (like <code>amountOfFlour</code>). The most
important thing is to be consistent within a project, because it makes the code more readable.

## Output

Notice how if you type a 4 and hit enter, the Python interpreter spits a 4 back
out:

<pre>
4
</pre>

But if you assign 4 to a variable, nothing is printed:

<pre>
x = 4
</pre>

You can think of it as that something needs to get the output. Without an assignment, the winner is the screen. With assignment, the output goes to the variable.

You can reassign variables if you want:

<pre>
x = 4
x
x = 5
x
</pre>

Sometimes reassigning a variable is an accident and causes bugs in programs.

<pre>
x = 3
y = 4
x * y
x * x
2 * x - 1 * y
</pre>

Order of operations works pretty much like how you learned in school. If you're unsure of an ordering, you can add parentheses like on a calculator:

<pre>
(2 * x) - (1 * y)
</pre>

Note that the spacing doesn't matter:

<pre>
x = 4
</pre>

and

<pre>
x=4
</pre>

are both valid Python and mean the same thing.

<pre>
(2 * x) - (1 * y)
</pre>

and

<pre>
(2*x)-(1*y)
</pre>

are also both valid and mean the same thing. You should strive to be consistent with whatever spacing you like or a job requires, since it makes reading the code easier.

You aren't cheating and skipping typing these exercises out, are you? Good! :)

## Strings

So far we've seen two data types: <b>integers</b> and <b>floats</b>. Another useful data type is a <b>string</b>, which is just what Python calls a bunch of characters (like numbers, letters, whitespace, and punctuation) put together. Strings are indicated by being surrounded by quotes:

<pre>
"Hello"
"Python, I'm your #1 fan!"
</pre>

Like with the math data types above, we can use the <code>type</code> function to check the type of strings:

<pre>
type("Hello")
type(1)
type("1")
</pre>

### String Concatenation

You can smoosh strings together (called "concatenation") using the '+' sign:

<pre>
"Hello" + "World"
</pre>

<pre>
name = "Jessica"
print "Hello " + name
</pre>

### Printing

You can print strings using <code>print</code>:

<pre>
h = "Hello"
w = "World"
print h + w
</pre>

<pre>
my_string = "Alpha " + "Beta " + "Gamma " + "Delta"
print my_string
</pre>

How about printing different data types together?

<pre>
print "Hello" + 1
</pre>

Hey now! The output from the previous example was really different and interesting; let's break down exactly what happened:

<pre>
>>> print "Hello" + 1
Traceback (most recent call last):
  File "&lt;stdin>", line 1, in &lt;module>
TypeError: cannot concatenate 'str' and 'int' objects
</pre>

Python is giving us a <b>traceback</b>. A traceback is details on what was happening when Python encountered an Exception or Error -- something it doesn't know how to handle.

There are many kinds of Python errors, with descriptive names to help us humans understand what went wrong. In this case we are getting a <code>TypeError</code>: we tried to do some operation on a data type that isn't supported for that data type.

Python gives us a helpful error message as part of the TypeError:

<code>"cannot concatenate 'str' and 'int' objects"</code>

We saw above the we can concatenate strings:

<pre>
print "Hello" + "World"
</pre>

works just fine.

However,

<pre>
print "Hello" + 1
</pre>

produces a <code>TypeError</code>. We are telling Python to concatenate a string and an integer, and that's not something Python understands how to do.

We can convert an integer into a string ourselves, using the <code>str</code> function:

<pre>
print "Hello" + str(1)
</pre>

Like the <code>type</code> function from before, the <code>str</code> function takes 1 argument. In the above example it took the integer 1. <code>str</code> takes a Python object as input and produces a string version of that input as output.

### String length

There's another useful function that works on strings called <code>len</code>. <code>len</code> returns the length of a string as an integer:

<pre>
print len("Hello")
print len("")
fish = "humuhumunukunukuapuaʻa"
length = str(len(fish))
print fish + " is a Hawaiian fish whose name is " + length + " characters long."
</pre>

### Quotes

We've been using double quotes around our strings, but you can use either double or single quotes:

<pre>
print 'Hello'
print "Hello"
</pre>

Like with spacing above, use whichever quotes make the most sense for you, but be consistent.

You do have to be careful about using quotes inside of strings:

<pre>
print 'I'm a happy camper'
</pre>

This gives us another <b>traceback</b>, for a new kind of error, a <code>SyntaxError</code>. When Python looks at that expression, it sees the string 'I' and then

<code>m a happy camper'</code>

which it doesn't understand -- it's not 'valid' Python. Those letters aren't variables (we haven't assigned them to anything), and that trailing quote isn't balanced. So it raises a <code>SyntaxError</code>.

We can use double quotes to avoid this problem:

<pre>
print "I'm a happy camper"
</pre>

or we can <b>escape</b> the quote with a backslash:

<pre>
print 'I\'m a happy camper'
print 'Ada Lovelace is often called the world\'s first programmer.'
print "Computer scientist Grace Hopper popularized the term \"debugging\"."
</pre>

One fun thing about strings in Python is that you can multiply them:

<pre>
print "A" * 40
print "ABC" * 12
h = "Happy"
b = "Birthday"
print (h + b) * 10
</pre>

## Part 1 Practice

Read the following expressions, but don't execute them. Guess what the output will be. After you've made a guess, copy and paste the expressions at a Python prompt and check your guess.

1.
<pre>
total = 1.5 - 1/2 + ((-2.0/2) - (1.0/2))
print total
type(total)
</pre>

2.
<pre>
a = "quick"
b =  "brown"
c = "fox jumps over the lazy dog"
print "The " +  a * 3 + " " +  b * 3 + " " + c
</pre>

3.
<pre>
print 2.0 * 123 + str(2.0) * 123
</pre>

4.

(Remember, copying and pasting is fine here in this practice section -- we'll go back to typing out the code for part 2)

<pre>
a = "| (_|   -()-  -()-   -()-   -()- | -()-  -()-  -()-   -()-   ||\n"
b = "|_\_|_/___|__|__|__|___|__|___|__|___________________________||\n"
c = "|________________________________|__|__()_|__()_|__()__|_____||\n"
d = " ___|)_______________________________________________________\n"
e = "|_/(|,\____/_|___/_|____/_|______|___________________________||\n"
f = "|___/____________________________|___________________________||\n"
g = "|   |     | ()  | ()   | ()   |  |                           ||\n"
h = "|__\___|.________________________|___\_|___\_|___\_|___|_____||\n"
i = "|__/|_______/|____/|_____/|______|___________________________||\n"
j = "|_____/__________________________|____\|____\|____\|_________||\n"
k = "|____/___________________________|___________________________||\n"
l = "|__/___\_._______________________|__|__|__|__|__|__|___|_____||\n"

print d + f + i + e + b + g + a + c + l + h + j + k
</pre>

## End of Part 1

Congratulations! You've learned about and practiced math, strings, variables, data types, exceptions, tracebacks, and executing Python from the Python prompt.

Take a break, stretch, meet some neighbors, and ask the staff if you have any questions about this material.

## Python scripts

Until now we've been executing commands at the Python prompt. This is great for math, short bits of code, and testing. For longer ideas, it's easier to store the code in a file.

<ol>
<li>Download the file [nobel.py](http://mit.edu/jesstess/www/BostonPythonWorkshop6/nobel.py) by right-clicking on it and saying to save it as a ".py" file to your Desktop. The ".py" extension hints that this is a Python script.</li>
<li>Open a command prompt, and use the navigation commands (<code>dir</code> and <code>cd</code> on Windows, <code>ls</code>, <code>pwd</code>, and <code>cd</code> on OS X and Linux) to navigate to your home directory. See [navigating from a command prompt](https://openhatch.org/wiki/Boston_Python_Workshop_6/Friday#Goal_.234:_practice_navigating_the_computer_from_a_command_prompt) for a refresher on those commands.</li>
<li>Once you are in your home directory, execute the contents of <code>nobel.py</code> by typing

<pre>
python nobel.py
</pre>

at a command prompt.

<code>nobel.py</code> introduces two new concepts: comments and multiline strings.</li>

<li>Open <code>nobel.py</code> in your text editor (see [preparing your text editor](https://openhatch.org/wiki/Boston_Python_Workshop_6/Friday#Goal_.232:_prepare_a_text_editor) for a refresher on starting the editor).</li>
<li>Read through the file in your text editor carefully and check your understanding of both the comments and the code.</li>
</ol>

Study the script until you can answer these questions:
<ol>
<li>How do you comment code in Python?</li>
<li>How do you print just a newline?</li>
<li>How do you print a multi-line string so that whitespace is preserved?</li>
</ol>

Let's get back to some interactive examples. Keep typing them out! You'll thank yourself tomorrow. :)

## Booleans

So far, the code we've written has been <i>unconditional</i>: no choice is getting made, and the code is always run. Python has another data type called a <b>boolean</b> that is helpful for writing code that makes decisions. There are two booleans: <code>True</code> and <code>False</code>.

<pre>
True
</pre>

<pre>
type(True)
</pre>

<pre>
False
</pre>

<pre>
type(False)
</pre>

You can test if Python objects are equal or unequal. The result is a boolean:

<pre>
0 == 0
</pre>

<pre>
0 == 1
</pre>

Use <code>==</code> to test for equality. Recall that <code>=</code> is used for <i>assignment</i>.

This is an important idea and can be a source of bugs until you get used to it: <b>= is assignment, == is comparison</b>.

Use <code>!=</code> to test for inequality:

<pre>
"a" != "a"
</pre>

<pre>
"a" != "A"
</pre>

<code>&lt;</code>, <code>&lt;=</code>, <code>&gt;</code>, and <code>&gt;=</code> have the same meaning as in math class. The result of these tests is a boolean:

<pre>
1 > 0
</pre>

<pre>
2 >= 3
</pre>

<pre>
-1 &lt; 0
</pre>

<pre>
.5 &lt;= 1
</pre>

You can check for containment with the <code>in</code> keyword, which also results in a boolean:

<pre>
"H" in "Hello"
</pre>

<pre>
"X" in "Hello"
</pre>

Or check for a lack of containment with <code>not in</code>:

<pre>
"a" not in "abcde"
</pre>

<pre>
"Perl" not in "Boston Python Workshop"
</pre>

## Flow Control

#### if statements

We can use these expressions that <i>evaluate</i> to booleans to make decisions and conditionally execute code:

<pre>
if 6 > 5:
     print "Six is greater than five!"
</pre>

That was our first multi-line piece of code, and the way to enter it at a Python prompt is a little different. First, type the <code>if 6 > 5:</code> part, and hit enter. The next line will have <code>...</code> as a prompt, instead of the usual <code>&gt;&gt;&gt;</code>. This is Python telling us that we are in the middle of a <b>code block</b>, and so long as we indent our code it should be a part of this code block.

Type 4 spaces, and then type <code>print "Six is greater than five!"</code>. Hit enter to end the line, and hit enter again to tell Python you are done with this code block. All together, it will look like this:

<pre>
>>> if 6 > 5:
...      print "Six is greater than five!"
...
Six is greater than five!
</pre>

So what is going on here? When Python encounters the <code>if</code> keyword, it <i>evaluates</i> the <i>expression</i> following the keyword and before the colon. If that expression is <b>True</b>, Python executes the code in the indented code block under the <code>if</code> line. If that expression is <b>False</b>, Python skips over the code block.

In this case, because 6 really is greater than 5, Python executes the code block under the if statement, and we see "Six is greater than five!" printed to the screen. Guess what will happen with these other expressions, then type them out and see if your guess was correct:

<pre>
if 0 > 2:
     print "Zero is greater than two!"
</pre>

<pre>
if "banana" in "bananarama":
    print "I miss the 80s."
</pre>

#### more choices: <code>if</code> and <code>else</code>

You can use the <code>else</code> keyword to execute code only when the <code>if</code> expression isn't True:

<pre>
sister_age = 15
brother_age = 12
if sister_age > brother_age:
    print "sister is older"
else:
    print "brother is older"
</pre>

Like with <code>if</code>, the code block under the <code>else</code> statement must be indented so Python knows that it is a part of the <code>else</code> block.

#### compound conditionals: <code>and</code> and <code>or</code>

You can check multiple expressions together using the <code>and</code> and <code>or</code> keywords. If two expressions are joined by an <code>and</code>, they <b>both</b> have to be True for the overall expression to be True. If two expressions are joined by an <code>or</code>, as long as <b>at least one</b> is True, the overall expression is True.

Try typing these out and see what you get:

<pre>
1 > 0 and 1 &lt; 2
</pre>

<pre>
1 &lt; 2 and "x" in "abc"
</pre>

<pre>
"a" in "hello" or "e" in "hello"
</pre>

<pre>
1 &lt;= 0 or "a" not in "abc"
</pre>

Guess what will happen when you enter these next two examples, and then type them out and see if you are correct. If you have trouble with the indenting, call over a staff member and practice together. It is important to be comfortable with indenting for tomorrow.

<pre>
temperature = 32
if temperature > 60 and temperature &lt; 75:
    print "It's nice and cozy in here!"
else:
    print "Too extreme for me."
</pre>

<pre>
hour = 11
if hour &lt; 7 or hour > 23:
    print "Go away!"
    print "I'm sleeping!"
else:
    print "Welcome to the cheese shop!"
    print "Can I interest you in some choice gouda?"
</pre>

You can have as many lines of code as you want in <code>if</code> and <code>else</code> blocks; just make sure to indent them so Python knows they are a part of the block.

#### even more choices: <code>elif</code>

If you have more than two cases, you can use the <code>elif</code> keyword to check more cases. You can have as many <code>elif</code> cases as you want; Python will go down the code checking each <code>elif</code> until it finds a True condition or reaches the default <code>else</code> block.

<pre>
sister_age = 15
brother_age = 12
if sister_age > brother_age:
    print "sister is older"
elif sister_age == brother_age:
    print "sister and brother are the same age"
else:
    print "brother is older"
</pre>

You don't have to have an <code>else</code> block, if you don't need it. That just means there isn't default code to execute when none of the <code>if</code> or <code>elif</code> conditions are True:

<pre>
color = "orange"
if color == "green" or color == "red":
  print "Christmas color!"
elif color == "black" or color == "orange":
  print "Halloween color!"
elif color == "pink":
  print "Valentine's Day color!"
</pre>

If color had been "purple", that code wouldn't have printed anything.

<b>Remember that  '=' is for assignment and '==' is for comparison.</b>

## Writing Functions

We talked a bit about functions when we introduced the <code>type()</code> function. Let's review what we know about functions:

* They do some useful bit of work.
* They let us re-use code without having to type it out each time.
* They take input and possibly produce output (we say they <b>return</b> a value). You can assign a variable to this output.
* You call a function by using its name followed by its <b>arguments</b> in parenthesis.

For example:

<pre>
length = len("Mississippi")
</pre>

Executing this code assigns the length of the string "Mississippi" to the variable <code>length</code>.

We can write our own functions to encapsulate bits of useful work so we can reuse them. Here's how you do it:

<b>Step 1: write a function signature</b>

A <b>function signature</b> tells you how the function will be called. It starts with the keyword <code>def</code>, which tells Python that you are defining a function. Then comes a space, the name of your function, an open parenthesis, the comma-separated input <b>parameters</b> for your function, a close parenthesis, and a colon. Here's what a function signature looks like for a function that takes no arguments:

<code>def myFunction():</code>

Here's what a function signature looks like for a function that takes one argument called <code>string</code>:

<code>def myFunction(string):</code>

And one for a function that takes two arguments:

<code>def myFunction(myList, myInteger):</code>

Parameters should have names that usefully describe what they are used for in the function.

We've used the words <b>parameters</b> and <b>arguments</b> seemingly interchangeably to reference the input to functions. The distinction isn't really important right now, but if you're curious: in function signatures the input is called parameters, and when you are calling the function the input is called arguments.

<b>Step 2: do useful work inside the function</b>

Underneath the function signature you do your useful work. Everything inside the function is indented, just like with if/else blocks, so Python knows that it is a part of the function.

You can use the variables passed into the function as parameters, just like you can use variables once you define them outside of functions.

<pre>
def add(x, y):
    result = x + y
</pre>

<b>Step 3: return something</b>

If you want to be able to assign a variable to the output of a function, the function has to <b>return that output</b> using the <code>return</code> keyword.

<pre>
def add(x, y):
    result = x + y
    return result
</pre>

or, even shorter:

<pre>
def add(x, y):
    return x + y
</pre>

You can return any Python object: numbers, strings, booleans ... even other functions!

Once you execute a return, you are done with the function -- you don't get to do any more work. That means if you have a function like this:

<pre>
def absoluteValue(number):
    if number &lt; 0:
        return number * -1
    return number
</pre>

if <code>number</code> is less than 0, you return <code>number * -1</code> and never even get to the last line of the function. However, if <code>number</code> is greater than or equal to 0, the <code>if</code> expression evaluates to <code>False</code>, so we skip the code in the <code>if</code> block and return <code>number</code>.

We could have written the above function like this if we wanted. It's the same logic, just more typing:

<pre>
def absoluteValue(number):
    if number &lt; 0:
        return number * -1
    else:
        return number
</pre>

<b>Step 4: use the function</b>

Once you define a function you can use it as many times as you want:

<pre>
def add(x, y):
    return x + y

result = add(1234, 5678)
print result
result = add(-1.5, .5)
print result
</pre>

Functions don't have to return anything, if you don't want them to. They usually return something because we usually want to be able to assign variables to their output.

## End of Part 2

Congratulations! You've learned about and practiced executing Python scripts, booleans, conditionals, and if/else blocks, and you've written your own Python functions. This is a huge, huge accomplishment!

Take a break, stretch, meet some neighbors, and ask the staff if you have any questions about this material.

## Extra Practise

If you're bored, have extra time, or want to have some more practise, there are some exercises on CodingBat to explore what we've learned further.

* [CodingBat exercises](https://openhatch.org/wiki/Boston_Python_Workshop_6/Friday/CodingBat_Using_Codingbat) (bit.ly/1ghX8IU)
* [More CodingBat exercises](http://codingbat.com/home/bostonpythonworkshop@gmail.com/SaturdayMorning) (bit.ly/1aLXlM9)
* A quick [guide to using CodingBat](https://openhatch.org/wiki/Boston_Python_Workshop_6/Friday/CodingBat_Using_Codingbat) (bit.ly/1fafrfX)


---------------------------------------

Adapted from [Boston Python Workshop](https://openhatch.org/wiki/Boston_Python_Workshop_6/Data_types) content
by [Gather](https://github.com/organizations/nzgather). CC-BY
