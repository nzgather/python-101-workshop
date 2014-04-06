[Gather Workshops](http://gathergather.co.nz/workshops/) - [Python](http://www.python.org)

# Welcome to the Tutorial!

This tutorial covers several core programming concepts that we'll build upon during the following interactive lecture. It will take 1-2 hours to complete. There's a break in the middle, and exercises at the middle and end to help review the material.

This is an interactive tutorial! As you go through this tutorial, any time you see something that looks like this:

```
a = "Hello"
```

you should type the expression at a Python prompt, hitting Return after every line and noting the output.

No copying and pasting! You'll learn the concepts better if you type them out yourself.

## Math

Math in Python looks a lot like math you type into a calculator. A Python prompt makes a great calculator if you need to crunch some numbers and don't have a good calculator handy.

### Addition

```
2 + 2
1.5 + 2.25
```

### Subtraction

```
4 - 2
100 - .5
0 - 2
```

### Multiplication

```
2 * 3
```

### Division

```
4 / 2
1 / 2
3/4 + 1/4
```

What do you need to do to get the right answer? Use data types that understand decimals for each of the divisions:

```
3.0/4 + 1.0/4
3.0/4.0 + 1.0/4.0
```

The two previous expressions produce the same result. You only need to make one of the numbers in each fraction have a decimal. When the Python interpreter goes to do the division, it notices that one of the numbers in the fraction cares about decimals and says "that means I have to make the other number care about decimals too".

## Types

There's a helpful **function** (more on what a function is in a second) called `type` that tells you what kind of thing -- what **data type** -- Python thinks something is. We can check for ourselves that Python considers '1' and '1.0' to be different data types:

```
type(1)
type(1.0)
```

So now we've seen two data types: **integers** and **floats**.

By the way, what is a "function"? Here are the important ideas about functions:

* A function encapsulates a useful bit of work and gives that work a name.
You provide input to a function and it produces output. For example, the `type` function takes data as an input, and produces what type of data the data is (e.g. an integer or a float) as output.
* To use a function, write the name of the function, followed by an open parenthesis, then what the function needs as input (we call that input the **arguments** to the function), and then a close parenthesis.
* Programmers have a lot of slang around functions. They'll say that functions "take" arguments, or that they "give" or "pass" arguments to a function. "call" and "invoke" are both synonyms for using a function.

In the example above, "type" was the name of the function. `type`code> takes one argument; we first gave type an argument of 1 and then gave it an argument of 1.0.



### Command history

Stop here and try hitting the Up arrow on your keyboard a few times. The Python **interpreter** saves a history of what you've entered, so you can arrow up to old commands and hit Return to re-run them!

## Variables

A lot of work gets done in Python using variables. Variables are a lot like the variables in math class, except that in Python variables can be of any data type, not just numbers.

```
type(4)
x = 4
x
type(x)
2 * x
```

Giving a name to something, so that you can refer to it by that name, is called **assignment**. Above, we assigned the name 'x' to 4, and after that we can use `x` wherever we want to use the number 4.

Variables can't have spaces or other special characters, and they need to start with a letter. Here are some valid variable names:

`magic_number = 1500`<br />
`amountOfFlour = .75`<br />
`my_name = "Jessica"`

Projects develop naming conventions: maybe multi-word variable names use underscores (like `magic_number`), or "camel case" (like `amountOfFlour`). The most important thing is to be consistent within a project, because it makes the code more readable.

## Output

Notice how if you type a 4 and hit enter, the Python interpreter spits a 4 back
out:

```
4
```

But if you assign 4 to a variable, nothing is printed:

```
x = 4
```

You can think of it as that something needs to get the output. Without an assignment, the winner is the screen. With assignment, the output goes to the variable.

You can reassign variables if you want:

```
x = 4
x
x = 5
x
```

Sometimes reassigning a variable is an accident and causes bugs in programs.

```
x = 3
y = 4
x * y
x * x
2 * x - 1 * y
```

Order of operations works pretty much like how you learn in school. If you're unsure of an ordering, you can add brackets like on a calculator:

```
(2 * x) - (1 * y)
```

Note that the spacing doesn't matter:

```
x = 4
```

and

```
x=4
```

are both valid Python and mean the same thing.

```
(2 * x) - (1 * y)
```

and

```
(2*x)-(1*y)
```

are also both valid and mean the same thing. You should strive to be consistent with whatever spacing you like or a job requires, since it makes reading the code easier.

You aren't cheating and skipping typing these exercises out, are you? Good! :)

## Strings

So far we've seen two data types: **integers** and **floats**. Another useful data type is a **string**, which is just what Python calls a bunch of characters (like numbers, letters, whitespace, and punctuation) put together. Strings are indicated by being surrounded by quotes:

```
"Hello"
"Python, I'm your #1 fan!"
```

Like with the math data types above, we can use the `type` function to check the type of strings:

```
type("Hello")
type(1)
type("1")
```

### String Concatenation

You can smoosh strings together (called "concatenation") using the '+' sign:

```
"Hello" + "World"
```

```
name = "Jessica"
"Hello " + name
```

How about concatenating different data types?

```
"Hello" + 1
```

Hey now! The output from the previous example was really different and interesting; let's break down exactly what happened:

```
>>> "Hello" + 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
```

Python is giving us a **traceback**. A traceback is details on what was happening when Python encountered an Exception or Error -- something it doesn't know how to handle.

There are many kinds of Python errors, with descriptive names to help us humans understand what went wrong. In this case we are getting a `TypeError`: we tried to do some operation on a data type that isn't supported for that data type.

Python gives us a helpful error message as part of the TypeError:

`"Can't convert 'int' object to str implicitly"`

We saw above the we can concatenate strings:

```
print("Hello" + "World")
```

works just fine.

However,

```
print("Hello" + 1)
```

produces a `TypeError`. We are telling Python to concatenate a string and an integer, and that's not something Python understands how to do.

We can convert an integer into a string ourselves, using the `str` function:

```
"Hello" + str(1)
```

Like the `type` function from before, the `str` function takes one argument. In the above example it took the integer 1. `str` takes a Python object as input and produces a string version of that input as output.

### String length

There's another useful function that works on strings called `len`. `len` returns the length of a string as an integer:

```
len("Hello")
len("")
fish = "humuhumunukunukuapuaʻa"
name_length = len(fish)
fish + " is a Hawaiian fish whose name is " + str(name_length) + " characters long."
```

### Quotes

We've been using double quotes around our strings, but you can use either double or single quotes:

```
'Hello'
"Hello"
```

Like with spacing above, use whichever quotes make the most sense for you, but be consistent.

You do have to be careful about using quotes inside of strings:

```
'I'm a happy camper'
```

This gives us another **traceback**, for a new kind of error, a `SyntaxError`. When Python looks at that expression, it sees the string '`I`'' and then

`m a happy camper'`

which it doesn't understand -- it's not 'valid' Python. Those letters aren't variables (we haven't assigned them to anything), and that trailing quote isn't balanced. So it raises a `SyntaxError`.

We can use double quotes to avoid this problem:

```
"I'm a happy camper"
```

One fun thing about strings in Python is that you can multiply them:

```
"A" * 40
"ABC" * 12
h = "Happy"
b = "Birthday"
(h + b) * 10
```

## Part 1 Practice

Read the following expressions, but don't execute them. Guess what the output will be. After you've made a guess, copy and paste the expressions at a Python prompt and check your guess.

1.
```
total = 1.5 - 1/2 + ((-2.0/2) - (1.0/2))
total
type(total)
```

2.
```
a = "quick"
b =  "brown"
c = "fox jumps over the lazy dog"
"The " +  a * 3 + " " +  b * 3 + " " + c
```


## End of Part 1

Congratulations! You've learned about and practiced math, strings, variables, data types, exceptions, tracebacks, and executing Python from the Python prompt.

Take a break, stretch, meet some neighbors, and ask the mentors if you have any questions about this material.

## Printing

So far we've been learning at the interactive Python interpreter. When you are working at the interpreter, any work that you do gets printed to the screen. For example:

```
h = "Hello"
w = "World"
h + w
```

will display "HelloWorld".

Another place that we will be writing Python code is in a file. When we run Python code from a file instead of interactively, we don't get work printed to the screen for free. We have to tell Python to print(the information to the screen. The way we do this is with the **print** function. Here's how it works:)

```
h = "Hello"
w = "World"
print(h + w)
```

```
my_string = "Alpha " + "Beta " + "Gamma " + "Delta"
print(my_string)
```

The string manipulation is exactly the same as before. The only difference is that you need to use **print** to print(results to the screen:)

```
h + w
```

becomes

```
print(h + w)
```

We'll see more examples of the print(function in the next section.)


## Python scripts

Until now we've been executing commands at the Python prompt. This is great for math, short bits of code, and testing. For longer ideas, it's easier to store the code in a file.

1. Download the file [nobel.py](http://mit.edu/jesstess/www/BostonPythonWorkshop8/nobel.py) by right-clicking on it and saying to save it as a ".py" file to your Desktop. The ".py" extension hints that this is a Python script.
2. Open a command prompt, and use the navigation commands (`dir` and `cd` on Windows, `ls`, `pwd`, and `cd` on OS X and Linux) to navigate to your home directory. See [navigating from a command prompt](https://openhatch.org/wiki/Boston_Python_Workshop_8/Friday#Goal_.234:_practice_navigating_the_computer_from_a_command_prompt) for a refresher on those commands.
3. Once you are in your home directory, execute the contents of `nobel.py` by typing

   ```
python3 nobel.py
```

   at a command prompt.

   `nobel.py` introduces two new concepts: comments and multiline strings.

4. Open `nobel.py` in your text editor (see [preparing your text editor](https://openhatch.org/wiki/Boston_Python_Workshop_8/Friday#Goal_.232:_prepare_a_text_editor) for a refresher on starting the editor).
5. Read through the file in your text editor carefully and check your understanding of both the comments and the code.</li>

Study the script until you can answer these questions:

1. How do you comment code in Python?
2. How do you print(just a newline?)
3. How do you print(a multi-line string so that spaces (whitespace) are preserved?)



## Booleans

Please return to the interactive Python interpreter for the rest of the tutorial. And remember: type out the examples. You'll thank yourself tomorrow. :)

So far, the code we've written has been *unconditional*: no choice is getting made, and the code is always run. Python has another data type called a **boolean** that is helpful for writing code that makes decisions. There are two booleans: `True` and `False`.

```
True
```

```
type(True)
```

```
False
```

```
type(False)
```

You can test if Python objects are equal or unequal. The result is a boolean:

```
0 == 0
```

```
0 == 1
```

Use `==` to test for equality. Recall that `=` is used for *assignment*.

This is an important idea and can be a source of bugs until you get used to it: **= is assignment, == is comparison**.

Use `!=` to test for inequality:

```
"a" != "a"
```

```
"a" != "A"
```

`<`, `<=`, `>`, and `>=` have the same meaning as in math class. The result of these tests is a boolean:

```
1 > 0
```

```
2 >= 3
```

```
-1 < 0
```

```
.5 <= 1
```

You can check for containment with the `in` keyword, which also results in a boolean:

```
"H" in "Hello"
```

```
"X" in "Hello"
```

Or check for a lack of containment with `not in`:

```
"a" not in "abcde"
```

```
"PHP" not in "Gather Python Workshop"
```

## Making choices

We can use these expressions that _evaluate_ to booleans to make decisions and conditionally execute code:

#### if statements

The simplest way to make a choice in Python is with the `if` keyword. Here's an example (don't try to type this one, just look at it for now):

```
if 6 > 5:
     print("Six is greater than five!")
```

This is our first multi-line piece of code, and the way to enter it at a Python prompt is a little different. First, type the `if 6 > 5:` part, and hit enter. The next line will have `...` as a prompt, instead of the usual `>>>`. This is Python telling us that we are in the middle of a **code block**, and so long as we indent our code it should be a part of this code block.

Type 4 spaces, and then type `print("Six is greater than five!"`. Hit enter to end the line, and hit enter again to tell Python you are done with this code block. All together, it will look like this:)

```
>>> if 6 > 5:
...      print("Six is greater than five!")
...
Six is greater than five!
```

So what is going on here? When Python encounters the `if` keyword, it _evaluates_ the _expression_ following the keyword and before the colon. If that expression is **True**, Python executes the code in the indented code block under the `if` line. If that expression is **False**, Python skips over the code block.

In this case, because 6 really is greater than 5, Python executes the code block under the if statement, and we see "Six is greater than five!" printed to the screen. Guess what will happen with these other expressions, then type them out and see if your guess was correct:

```
if 0 > 2:
     print("Zero is greater than two!")
```

```
if "banana" in "bananarama":
    print("I miss the 80s.")
```

#### more choices: `if` and `else`

You can use the `else` keyword to execute code only when the `if` expression isn't True:

```
sister_age = 15
brother_age = 12
if sister_age > brother_age:
    print("sister is older")
else:
    print("brother is older")
```

Like with `if`, the code block under the `else` statement must be indented so Python knows that it is a part of the `else` block.

#### compound conditionals: `and` and `or`

You can check multiple expressions together using the `and` and `or` keywords. If two expressions are joined by an `and`, they **both** have to be True for the overall expression to be True. If two expressions are joined by an `or`, as long as **at least one** is True, the overall expression is True.

Try typing these out and see what you get:

```
1 > 0 and 1 < 2
```

```
1 < 2 and "x" in "abc"
```

```
"a" in "hello" or "e" in "hello"
```

```
1 <= 0 or "a" not in "abc"
```

Guess what will happen when you enter these next two examples, and then type them out and see if you are correct. If you have trouble with the indenting, call over a staff member and practice together. It is important to be comfortable with indenting for tomorrow.

```
temperature = 9
if temperature > 18 and temperature < 24:
    print("It's nice and cozy in here!")
else:
    print("Too extreme for me.")
```

```
hour = 11
if hour < 7 or hour > 23:
    print("Go away!")
    print("I'm sleeping!")
else:
    print("Welcome to the cheese shop!")
    print("Can I interest you in some choice gouda?")
```

You can have as many lines of code as you want in `if` and `else` blocks; just make sure to indent them so Python knows they are a part of the block.

#### even more choices: `elif`

If you have more than two cases, you can use the `elif` keyword to check more cases. You can have as many `elif` cases as you want; Python will go down the code checking each `elif` until it finds a True condition or reaches the default `else` block.

```
sister_age = 15
brother_age = 12
if sister_age > brother_age:
    print("sister is older")
elif sister_age == brother_age:
    print("sister and brother are the same age")
else:
    print("brother is older")
```

You don't have to have an `else` block, if you don't need it. That just means there isn't default code to execute when none of the `if` or `elif` conditions are True:

```
color = "orange"
if color == "green" or color == "red":
  print("Christmas color!")
elif color == "black" or color == "orange":
  print("Halloween color!")
elif color == "pink":
  print("Valentine's Day color!")
```

If color had been "purple", that code wouldn't have printed anything.

**Remember that '=' is for assignment and '==' is for comparison.**

### In summary: the structure of if/elif/else

Here's a diagram of `if/elif/else`:

```
if [some condition A is True]:
   [work that gets done if condition A is True]
elif [some condition B is True]:
   [work that gets done if condition B is True]
else:
   [work that gets done only if none of the above conditions was True]
```
_Indent_ the work that gets done under a condition.

Do you understand the difference between `elif` and `else`? When do you indent? When do you use a colon? If you're not sure, talk about it with a neighbor or mentor.

<!--
## Writing Functions

We talked a bit about functions when we introduced the `type()` function. Let's review what we know about functions:

* They do some useful bit of work.
* They let us re-use code without having to type it out each time.
* They take input and possibly produce output (we say they **return** a value). You can assign a variable to this output.
* You call a function by using its name followed by its **arguments** in parenthesis.

For example:

```
length = len("Mississippi")
```

Executing this code assigns the length of the string "Mississippi" to the variable `length`.

We can write our own functions to encapsulate bits of useful work so we can reuse them. Here's how you do it:

**Step 1: write a function signature**

A **function signature** tells you how the function will be called. It starts with the keyword `def`, which tells Python that you are defining a function. Then comes a space, the name of your function, an open parenthesis, the comma-separated input **parameters** for your function, a close parenthesis, and a colon. Here's what a function signature looks like for a function that takes no arguments:

`def myFunction():`

Here's what a function signature looks like for a function that takes one argument called `string`:

`def myFunction(string):`

And one for a function that takes two arguments:

`def myFunction(myList, myInteger):`

Parameters should have names that usefully describe what they are used for in the function.

We've used the words **parameters** and **arguments** seemingly interchangeably to reference the input to functions. The distinction isn't really important right now, but if you're curious: in function signatures the input is called parameters, and when you are calling the function the input is called arguments.

**Step 2: do useful work inside the function**

Underneath the function signature you do your useful work. Everything inside the function is indented, just like with if/else blocks, so Python knows that it is a part of the function.

You can use the variables passed into the function as parameters, just like you can use variables once you define them outside of functions.

```
def add(x, y):
    result = x + y
```

**Step 3: return something**

If you want to be able to assign a variable to the output of a function, the function has to **return that output** using the `return` keyword.

```
def add(x, y):
    result = x + y
    return result
```

or, even shorter:

```
def add(x, y):
    return x + y
```

You can return any Python object: numbers, strings, booleans ... even other functions!

Once you execute a return, you are done with the function -- you don't get to do any more work. That means if you have a function like this:

```
def absoluteValue(number):
    if number < 0:
        return number * -1
    return number
```

if `number` is less than 0, you return `number * -1` and never even get to the last line of the function. However, if `number` is greater than or equal to 0, the `if` expression evaluates to `False`, so we skip the code in the `if` block and return `number`.

We could have written the above function like this if we wanted. It's the same logic, just more typing:

```
def absoluteValue(number):
    if number < 0:
        return number * -1
    else:
        return number
```

**Step 4: use the function**

Once you define a function you can use it as many times as you want:

```
def add(x, y):
    return x + y

result = add(1234, 5678)
print(result)
result = add(-1.5, .5)
print(result)
```

Functions don't have to return anything, if you don't want them to. They usually return something because we usually want to be able to assign variables to their output.
-->

## End of Part 2

Congratulations! You've learned about and practiced executing Python scripts, booleans, conditionals, and making choices with if, elif, and else. This is a huge, huge accomplishment!

Take a break, stretch, and ask the mentors if you have any questions about this material.

If you have extra time or want to have some more practise, there are some exercises on CodeAcademy to explore what we've learned further.

* [CodeAcademy exercises](http://www.codecademy.com/courses/python-beginner-en-kSQwt) (bit.ly/1kd3MTJ)


---------------------------------------

Adapted from [Boston Python Workshop](https://openhatch.org/wiki/Boston_Python_Workshop_8/Friday/Tutorial) content
by [Gather](https://github.com/organizations/nzgather). CC-BY
