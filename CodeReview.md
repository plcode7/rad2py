# Purpose #

To guide you in conducting an effective code review.

Based on Table 8.3, "C++ Code Review Guideline and checklist" of the PSP book  (Humprey, "A discipline for software enginering", p242).

# General #

As you complete each review step, check off that item in the box to the right.

Complete the checklist for one program unit before you start to review the next

# Complete #

Verify that the code covers all the design and requisites.

# Imports #

Verify that import statements:

  * for included libraries are complete
  * there are no unused libraries
  * import lines are ordered alphabetically

# Initialization #

Check variable and parameter initialization:

  * at program initiation
  * at start of every loop
  * at function/procedure entry

# Calls #

Check function call formats:

  * parameters
  * immutable/mutable types

# Names #

Check name spelling and use:

  * is it consistent?
  * is it within the declared scope?

# String #

Check that all string are:
  * correctly encoded/decoded

# Output Format #

Check the output format:

  * line stepping is proper
  * spacing is proper

# (), {}, [.md](.md) Pairs #

Ensure the tuple, dict and list delimiters are proper and matched

# Logic Operators #

Verify the proper use of ==, =, ||, and so on.

Check every logic function for proper ().

# Line-by-line check #

Check every line of code for:

  * instruction syntax and
  * proper punctuation

# Standars #

Ensure the code conforms to the coding standards.

# File Open and Close #

Verify that all files are:

  * poperly declared (read/write mode, text/binary, etc.)
  * opened, and
  * closed