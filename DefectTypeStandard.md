# Introduction #

The Defect Type Standard purpose is to facilitate cause analysis and defect prevention.

This document is based in the PSP Defect Type Standard (Humprey 1997, "A discipline for software enginering", pp38, 260, 262, 661), modeled on the work at IBM Research by types were taken from R. Chillarege, I. Bhandari, J. Chaar, M. Halliday, D. Moebus, B. Ray and M. Y. Wong: "Orthogonal Defect Classification - A Concept of In-Process Measurements" _IEEE Transactions on Software Engineering_, vol. 18., no. 11 (November 1992): 943-956.

The standard has been adapted to follow the python programming language built-in exception types, using conventions from the [Python Language Reference](http://docs.python.org/library/exceptions.html), and its automatic checker, pep8.py

**NOTE**: Type 30 (Build/Package) was moved inside Type 100 (Environment), so Type 30 is used to automatically classificate PEP8 format defect (Type 22 in the detailed standard from the book)

Some python exceptions are not considered errors (StopIteration and GeneratorExit) so they are not categorized as defects.
Other python exceptions were moved to better categories to maintain consistency with the python exception hierachy (IOError) or for a easier classification/balance (EOFError, BufferError, ImportError)

# Details #

| Defect Type Number | Type Name | Description |
|:-------------------|:----------|:------------|
| 10                 | Documentation | Errors in docstrings and comments |
| 20                 | Syntax    | SyntaxError (spelling, punctuation, format) and IndentationError (block delimitation) |
| 30                 | Coding standard | PEP8 format warnings and errors (long lines, missing spaces, etc.) |
| 40                 |Assignment | NameError (undefined), unused variables, IndexError/KeyError (range/limits LookupError), UnboundLocalError (scope), ImportError |
| 50                 |Interface  | TypeError, AttributeError: wrong parameters and methods |
| 60                 | Checking  | AssertionError (failed assert) and failed tests (doctests or unittest) |
| 70                 | Data      | ValueError (wrong data), ArithmeticError (overflow, zero-division, floating-point), EOFError and BufferError |
| 80                 | Function  | RuntimeError and logic errors |
| 90                 | System	   | SystemError (including MemoryError, ReferenceError) and Libraries or package unexpected errors |
| 100                | Enviroment | EnvironmentError: Operating system and build/third party unexpected errors (including IOError) |