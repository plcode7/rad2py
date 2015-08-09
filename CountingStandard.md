# Introduction #

Python has built-in code Tokenizer suitable to parse and count logical lines.

This automated strategy will be adopted to measure software size precisely and repeatable, needed for performance evaluation (LOC/hour), assessing quality (defect density) and planning (product estimation).

The following token are used to count Source Lines of Code (SLOC):
  * NEWLINE: token indicates the end of a logical line of Python code
  * COMMENT: token value used to indicate a comment

Comment to code ratio: _TBD_

## Clarifications ##

The following statement types are counted as logical lines (SLOC):
  * executable lines
  * docstrings (triple-quote `"""` are counted as a single line)
  * shebang `#!/usr/bin/env python`, probably because BOM

Other considerations:
  * Comments are counted separately (with no distinction between own lines, with source or banners)
  * Blank lines are not counted at all
  * Python languaje doesn't has nonexecutable statements (declarations, compiler directives, begin/ends blocks)

## Counting Anomalies ##

Although Python Tokenizer can detect more tokens (like COLON `;` used as the statement separator) and could be used to further parse and detect compound statements (multiple assignments, nested functions call, list comprehension, etc.), initially for simplicity there will be no further code analysis and that anomalies will be counted as 1 LOC (see bellow).

The following examples will be counted as 1 LOC although it could be decomposed in separate statements:

```
x_avg = mean(values); n = len(values);
```

```
return math.sqrt(sum([(x_i - x_avg)**2 
                      for x_i in values]) / float(n - 1))
```

Note that using colon to separate statements is a violation to the CodingStandard: _E701 multiple statements on one line (colon)_

# Example #

## Physical Source Code ##

Sample python source code (physical file program1A.py):
```
﻿#!/usr/bin/env python
# coding:utf-8

"PSP Program 1A - Standard Deviation"

__author__ = "Mariano Reingart (reingart@gmail.com)"
__copyright__ = "Copyright (C) 2011 Mariano Reingart"
__license__ = "GPL 3.0"

import math


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


def stddev(values):
    """Calculate the standard deviation of a list of number values:
    
    >>> stddev([160, 591, 114, 229, 230, 270, 128, 1657, 624, 1503])
    572.026844746915
    >>> stddev([186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601])
    625.6339806770231
    >>> stddev([15.0, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2])
    62.25583060601187
    """
    x_avg = mean(values)
    n = len(values)
    return math.sqrt(sum([(x_i - x_avg)**2 
                          for x_i in values]) / float(n - 1))


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

## Logical Source Code ##

For the previous physical source code, the token detects the following logical lines (NEWLINE token) that get counted:

```
ï»¿ (BOM) #!/usr/bin/env python
"PSP Program 1A - Standard Deviation"
__author__ = "Mariano Reingart (reingart@gmail.com)"
__copyright__ = "Copyright (C) 2011 Mariano Reingart"
__license__ = "GPL 3.0"
import math
def mean(values):
    'docstring - 1 SLOC'
    return sum(values) / float(len(values))
def stddev(values):
    'docstring - 1 SLOC'
    x_avg = mean(values)
    n = len(values)
    return math.sqrt(sum([(x_i - x_avg)**2for x_i in values]) / float(n - 1))
if __name__ == "__main__":
    sd = stddev([160, 591, 114, 229, 230, 270, 128, 1657, 624, 1503])
    assert round(sd, 2) == 572.03
    sd = stddev([186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601])
    assert round(sd, 2) == 625.63
    sd = stddev([15.0, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2])
    assert round(sd, 2) == 62.26
```

## Results ##
  * Total LOC count: 21
  * Comments couunt: 5