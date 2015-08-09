# Introduction #

While programs must be correct, the source code should be understandable, this requires that it be well structurd and clearly commented.

This document is based in the PSP Coding Standard (Humprey, "A discipline for software enginering", pp670-672), that was largely drawn from a standard developed by Jim Murphy of the University of Massachusetts.

The standard has been adapted to follow the python programming language syntax and rules, using conventions from the ["PEP 8 -- Style Guide for Python Code"](http://www.python.org/dev/peps/pep-0008/), and it automatically checker, pep8.py

# General Guidelines #

## Program Headers ##

Begin all programs with a descriptive header, including:
  * Python interpreter requeriments (_shebang_)
  * Character set (utf8 for unicode)
  * Module docstring (general description)
  * Author, copyright and license
  * Version and/or start date (optional, could be provided by the repository)

Example:
```
﻿#!/usr/bin/env python
# coding:utf-8

"PSP Program 1A - Standard Deviation"

__author__ = "Mariano Reingart (reingart@gmail.com)"
__copyright__ = "Copyright (C) 2011 Mariano Reingart"
__license__ = "GPL 3.0"
__version__ = "
```

## Listing Contents ##

Provide a summary of the program contents (TOC if necessary).
This can be automatically done if each function or class has their python docstring (documentation string) attached.

Examples:

```
def mean(values):
    "Calculate the average of the numbers given:"
    return sum(values) / float(len(values))

def stddev(values):
    "Calculate the standard deviation of a list of number values"
    x_avg = mean(values); n = len(values)
    return math.sqrt(sum([(x_i - x_avg)**2 for 
                           x_i in values]) / float(n - 1))
```

## Documentation Tests ##

Include documentation test whenever possible, to show use case and expected results.
Example:
```
def mean(values):
    """Calculate the average of the numbers given:
    
    >>> mean([1, 2, 3])
    2.0
    >>> mean([1, 2])
    1.5
    >>> mean([1, 3])
    2.0
    """
    return sum(values) / float(len(values))
```
## Identifiers ##

Use descriptive names for all variables, function names, contastans, and other identifiers.
Avoid abbreviations or single-letter variables.

Example:
```
number_of_students = 0    # This is GOOD
x4 = j = ftave = 0        # These  are BAD
```

## Comments ##

  * Document the code so that the reader can understand its operation
  * Comments should explain both the purpose and behavior of the code
  * Comment variable definition to indicate their purpose.

Good Comment:
```
if record_count > limit: # have all the records been processed? 
```
Bad Comment:
```
if record_count > limit: # check if record_count greater than limit 
```


## Major Sections ##

Precede major program sections by a block comment that describes the processing that is done in the next section:

```
# ******************************************************
# this program section will ...
# ******************************************************
```

## Blank Spaces ##

  * Write programs with sufficient spacing so that they do not appear crowded
  * Separate every program construct with at least one space

## Indenting ##

Python is sensitive to indentation, so:
  * 4 spaces for each indent
  * Indent every block (do not use single line multiple statement)

## Capitalization ##

  * Capitalize all constants (global variables)
  * Use CamelCase for class names
  * Lowercase all other identifiers

Example:
```
DEFAULT_NUMBER_OF_STUDENTS = 14
class_size = DEFAULT_NUMBER_OF_STUDENTS
```


## Assertions ##

If possible, include in the main section basic assertions to check sample data and expected results (basic unit test implementation):

```
if __name__ == "__main__":
    # Table D5 "Object LOC" column
    sd = stddev([160, 591, 114, 229, 230, 270, 128, 1657, 624, 1503])
    assert round(sd, 2) == 572.03
    # Table D5 "New and Changed LOC" column
    sd = stddev([186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601])
    assert round(sd, 2) == 625.63
    # Table D5 "Development Hours" column
    sd = stddev([15.0, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2])
    assert round(sd, 2) == 62.26
```

# PEP8 Guidelines #

Checking tool provides two kind of messages: E (errors) and W (warnings):
  * 100 indentation
  * 200 whitespace
  * 300 blank lines
  * 400 imports
  * 500 line length
  * 600 deprecation
  * 700 statements

Special character conventions:
  * \s is used for whitespaces
  * \n for new lines
  * \t for tabulations

The following section describes automatic checks done by pep8.py

The example format uses "Okay" (when code is correct) or error/warning code followed by colon and space, the rest of the line is example source code.

## Indentation ##

Use 4 spaces per indentation level.
```
Okay: a = 1
Okay: if a == 0:\n    a = 1
E111:   a = 1

Okay: for item in items:\n    pass
E112: for item in items:\npass

Okay: a = 1\nb = 2
E113: a = 1\n    b = 2
```

## Never mix tabs or spaces for Indentation ##

```
Okay: if a == 0:\n        a = 1\n        b = 1
E101: if a == 0:\n        a = 1\n\tb = 1
```

## Tabs are obsolete for Indentation, use spaces ##

```
Okay: if True:\n    return
W191: if True:\n\treturn
```

## Trailing whitespace is superfluous ##

```
Okay: spam(1)
W291: spam(1)\s
```

## Trailing blank lines are superfluous ##

```
Okay: spam(1)
W391: spam(1)\n
```

## The last line should have a newline ##

```
W292 no newline at end of file
```

## Limit all lines to a maximum of 79 characters ##

```
E501 line too long (79 characters)
```

## Imports on separate lines ##

```
Okay: import os\nimport sys
E401: import sys, os

Okay: from subprocess import Popen, PIPE
Okay: from myclas import MyClass
Okay: from foo.bar.yourclass import YourClass
Okay: import myclass
Okay: import foo.bar.yourclass
```

## Compound Statements ##

Compound statements (multiple statements on the same line) are
generally discouraged.

While sometimes it's okay to put an if/for/while with a small body
on the same line, never do this for multi-clause statements. Also
avoid folding such long lines!

```
Okay: if foo == 'blah':\n    do_blah_thing()
Okay: do_one()
Okay: do_two()
Okay: do_three()

E701: if foo == 'blah': do_blah_thing()
E701: for x in lst: total += x
E701: while t < 10: t = delay()
E701: if foo == 'blah': do_blah_thing()
E701: else: do_non_blah_thing()
E701: try: something()
E701: finally: cleanup()
E701: if foo == 'blah': one(); two(); three()

E702: do_one(); do_two(); do_three()
```

### Blank Lines ###

  * Separate top-level function and class definitions with two blank lines.
  * Method definitions inside a class are separated by a single blank line.
  * Extra blank lines may be used (sparingly) to separate groups of related functions.  Blank lines may be omitted between a bunch of related one-liners (e.g. a set of dummy implementations).
  * Use blank lines in functions, sparingly, to indicate logical sections.

```
Okay: def a():\n    pass\n\n\ndef b():\n    pass
E301: class Foo:\n    def bar():\n        pass
E302: def a():\n    pass\n\ndef b(n):\n    pass
E302: def a():\n    pass\n\n\n\ndef b(n):\n    pass
E303: def a():\n\n\n\n    pass
E304: @decorator\n\ndef a():\n    pass
```

## Avoid extraneous whitespace ##

  * Immediately inside parentheses, brackets or braces.
  * Immediately before a comma, semicolon, or colon.

```
Okay: spam(ham[1], {eggs: 2})
E201: spam( ham[1], {eggs: 2})
E201: spam(ham[ 1], {eggs: 2})
E201: spam(ham[1], { eggs: 2})
E202: spam(ham[1], {eggs: 2} )
E202: spam(ham[1 ], {eggs: 2})
E202: spam(ham[1], {eggs: 2 })

E203: if x == 4: print x, y; x, y = y , x
E203: if x == 4: print x, y ; x, y = y, x
E203: if x == 4 : print x, y; x, y = y, x
```

## Missing whitespace ##
Each comma, semicolon or colon should be followed by whitespace:
```
Okay: [a, b]
Okay: (3,)
Okay: a[1:4]
Okay: a[:4]
Okay: a[1:]
Okay: a[1:4:2]
E231: ['a','b']
E231: foo(bar,baz)
```

## (Extra) Whitespace before parameters ##

Avoid extraneous whitespace in the following situations:
  * Immediately before the open parenthesis that starts the argument   list of a function call.
  * Immediately before the open parenthesis that starts an indexing or slicing.

```
Okay: spam(1)
E211: spam (1)

Okay: dict['key'] = list[index]
E211: dict ['key'] = list[index]
E211: dict['key'] = list [index]
```

## (Extra) Whitespace around operator ##

Avoid extraneous whitespace in the following situations:

  * More than one space around an assignment (or other) operator to align it with another.

```
Okay: a = 12 + 3
E221: a = 4  + 5
E222: a = 4 +  5
E223: a = 4\t+ 5
E224: a = 4 +\t5
```

## Missing whitespace around operator ##

  * Always surround these binary operators with a single space on either side: assignment (=), augmented assignment (+=, -= etc.), comparisons (==, <, >, !=, <>, <=, >=, in, not in, is, is not), Booleans (and, or, not).
  * Use spaces around arithmetic operators.

```
Okay: i = i + 1
Okay: submitted += 1
Okay: x = x * 2 - 1
Okay: hypot2 = x * x + y * y
Okay: c = (a + b) * (a - b)
Okay: foo(bar, key='word', *args, **kwargs)
Okay: baz(**kwargs)
Okay: negative = -1
Okay: spam(-1)

E225: i=i+1
E225: submitted +=1
E225: x = x*2 - 1
E225: hypot2 = x*x + y*y
E225: c = (a+b) * (a-b)
```

## (Extra) Whitespace around comma ##

Avoid extraneous whitespace in the following situations:

  * More than one space around an assignment (or other) operator to align it with another.

```
E241 multiple spaces after '%s'"
E242 tab after '%s'
```

## (Extra) Whitespace around named parameter equals ##

Don't use spaces around the '=' sign when used to indicate a keyword argument or a default parameter value.

```
Okay: def complex(real, imag=0.0):
Okay: return magic(r=real, i=imag)
Okay: boolean(a == b)
Okay: boolean(a != b)
Okay: boolean(a <= b)
Okay: boolean(a >= b)

E251: def complex(real, imag = 0.0):
E251: return magic(r = real, i = imag)
```

## Python 3000 has\_key deprecated ##

```
Okay: x in {...}
W601: {}.has_key(x) 
```

## Python 3000 raise comma deprecated ##

```
Okay: aise ValueError('message') 
W602: raise ValueError, 'message'
```