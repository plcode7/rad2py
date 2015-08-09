# Timeline & Milestones #

Although this research started a long time ago (mid 2006 as a degree thesis plan) only planning and bibliographic references tasks were done, and most development work started in early 2011:
  * ~~Proof-of-Concept (pre-alpha): Jun 2011~~ **DONE**
  * ~~Working Prototype (alpha): Aug 2011~~ **DONE**
  * ~~Experimental Design (beta1): Nov 2011~~ **DONE**
  * Tentative Complete design (beta2): Jul 2013 (est.)
  * Tentative First release candidate: Dec 2013 (est.)
  * Tentative First stable release: Jun 2014 (est.)

# Assignments #

The IDE and support tools will be used to develop programming assignments suggested by the PSP Book (Humprey, "A discipline for Software Enginering" pp752-769) to gather metrics in order to do a basic empirical validation of the hypothesis of this research:
  * ~~[Program 1A](http://code.google.com/p/rad2py/source/browse/assignments/program1A.py): Std Deviation~~ **DONE**
  * ~~[Program 2A](http://code.google.com/p/rad2py/source/browse/assignments/program2A.py): Count logical lines~~ **DONE**
  * ~~[Program 3A](http://code.google.com/p/rad2py/source/browse/assignments/program3A.py): Count LOC, LOC per object and method count~~ **DONE**
  * ~~[Program 4A](http://code.google.com/p/rad2py/source/browse/assignments/program4A.py): Linear regression (size estimation)~~ **DONE**
  * ~~[Program 5A](http://code.google.com/p/rad2py/source/browse/assignments/program5A.py): Simpson's rule integration and normal distribution~~ **DONE**
  * ~~[Program 6A](http://code.google.com/p/rad2py/source/browse/assignments/program6A.py): LOC estimation (90/70 prediction interval)~~ **DONE**
  * ~~Program 7A: Correlation and significance~~ **NOT MANDATORY**
  * ~~Program 8A: Sort a linked list~~ **UNNECESSARY**
  * ~~Program 9A: Calculate the degree of a normal distribution~~ **NOT MANDATORY**
  * Program 10A: Three-variable multiple regression estimation

Program 1B to 9B enhance previous programs to allow data storage and user iteration (they are optional for this research due to time and scope limitations)

Some trade-off were made for the sake of simplicity regarding python compared to other traditional languages like ADA, C++ or Pascal used in the book (i.e. high-level data structures -no linked list implementation needed-, PEP8 for codification standard, using python as pseudocode for design, stdlib to tokenize code automatically, pyclbr to inspect functions and objects, etc.)

Extensive field work would be made once validated the initial hypothesis to gather more metrics, enhancing a actual project and porting two other projects from Visual Basic to Python:
  * http://code.google.com/p/pyafipws/wiki/PyRece: Electronic Invoice Application
  * http://code.google.com/p/ampatu/: 911 Emergency management system
  * http://code.google.com/p/gestionlibre/: Simple ERP System

# Documents/Reports #

  * ~~CodingStandard (a.k.a. C29)~~ **DONE**
  * ~~CountingStandard (logical SLOC count a.k.a. [R1](https://code.google.com/p/rad2py/source/detail?r=1))~~ **DONE**
  * ~~DefectTypeStandard analysis~~ **DONE**
  * ~~CodeReview~~ **DONE**

# TO DO list #

Following is a list of problem founds that should be corrected before finishing the initial research:

## PSP phases ##
  * ~~automatic change to next phase when done (tick button)~~ **DONE** (it was working, added warning message if no editor open)
  * ~~load/save metric is not intuitive (stop in pm should save it)~~ **DONE**
  * ~~do not allow close pm phase with open defects !~~ **DONE**

## PSP defects ##
  * ~~bind DEL key to delete action~~  **DONE**
  * ~~fix DBNotFoundError issues (deleting selected defect?)~~ **FIXED**
  * ~~refresh selected item on deletions~~ **DONE**
  * ~~detect inject phase from metadata~~ **DONE**
  * ~~fix error when defect has no program file~~  **FIXED**
  * ~~fix defects number sequence~~  **FIXED**
  * ~~add summary (ex description)~~ **DONE**
  * ~~sort defects by number (when loading)~~ **DONE**
  * ~~TypeError when creating a defect and then double clicking it~~ **FIXED**
  * ~~checker detected wrong inject phase (postmortem)~~ **FIXED**

## PSP checks ##
  * ~~syntax errors do not show correctly summary~~ **FIXED**
  * ~~add exception text as description~~ **DONE** (only useful for syntax errors)
  * ~~add traceback field?~~ **WONTFIX** (tested, but not useful)
  * ~~do not report IDE exceptions as defects~~ **DONE?** (direct or indirect)
  * better categorization of python exceptions (defect types)
  * avoid pep8 false-positives (fails in shebang/BOM and doctests, is it broken?)
  * ~~avoid duplicates and allow wontfix status~~ **DONE**
  * ~~separate doctest from syntax checking (see phase)~~  **DONE**
  * "doctest for mean([1, 3]) failed, want 2.0 got 2.0 " WTF ???????
  * ~~compile vs check is not clear, review the button at toolbar~~  **DONE**

## Debugger ##
  * when pressing stop, do not start debugger if already stopped
  * fix wx event handler debugging (gui2py recipe)
  * find a workaround for wx.App singleton to debug simple wx
  * [issue 7](https://code.google.com/p/rad2py/issues/detail?id=7): fix incorrect lineno in traceback after exec'ing in main module
  * ~~fix dangerous locals + globals inspection~~

## Shell ##
  * fix annoying Copy/Paste issues (not working using the keyboard)
  * ~~clean local namespace dictionary before running a script~~

## Editor ##
  * fix wx.STC styling issues when highlight searchs/errors
  * ~~enhance find to search selected text~~ **DONE**
  * ~~remove asterisk at notebook title when the file is just opened and not modified~~ **DONE**
  * fix erroneous/bogous repaint on ubuntu
  * ~~[issue 4](https://code.google.com/p/rad2py/issues/detail?id=4): fix undo CTRL+Z~~ **FIXED**
  * ~~highligh errors/defect lines~~ **DONE**
  * automatically inspect the text under cursor
  * ~~fix IOError when opening a nonexistent file~~ **FIXED**

## Repository ##
  * fix folder separator under windows
  * ~~show unversioned files by default (new repos)~~ **DONE**
  * append all files when creating a local repo?

## Main ##
  * ~~correctly close files~~ **DONE**
  * test running/debugging multiple files
  * [issue 5](https://code.google.com/p/rad2py/issues/detail?id=5): wx.SafeYield blocks the app in rare occasions
  * ~~[issue 6](https://code.google.com/p/rad2py/issues/detail?id=6): misterious exception on AUIFrame  (filehistory, and other attribs)~~ **DONE**
  * ~~preserve session (open files)~~ **DONE**
  * fix not closing issue after using debugger (horphan thread?)
  * fix help system (enhance html pydoc)
  * internationalization T()

# Remarks #

Some insights and comments:
  * a program skeleton should be useful, a start-up wizard will be great!
  * design phase using python as "pseudocode" greatly reduces code phase
  * doctest are not useful right now (dificult to debug), using assert instead (or maybe unittest...)
  * integrated debuger/shell were useful to make doctest and stop at asserts!
  * reviews and checklists seems a must-have, replace compile phase?

Some facts:
  * Program 1A (Std Dev) was almost trivial (around 50 LOC, reduced to 6 SLOC excluding comments, documentation and tests) but 16 errors were found (13 automatic -most minor issues-, 3 added manually, discarding false positivies and duplicates, some repeated) and took ~2m for planning, ~20m for design+code, 25m for testing and ~5m for postmortem phase (53m total actual time, my 60m guess estimate was ok, but time spent in each phases was wrong)
  * Program 2A (SLOC count) was not so trivial (around 116 LOC, reduced to 59 SLOC excluding comments, documentation and tests), 31 errors were found,  and took ~5m for planning, ~47m for design, ~60m for code, 3m for "compile", 32m for testing and ~1m for postmortem phase (148m total actual time, exceeded my 96m guess estimate, mostly in coding phase)

**NOTE**: as no previous historical data, first planning estimated time is my best "guess" (as the book suggests)

**Exit Criteria**: The programs must be thoroughly tested, assertions and docstrings must exist and not fail (run without error) and all defects found should be fixed (or marked wontfix if they are not real defects), including pep8 warnings/errors and statics checks (pyflakes).

# Future Steps #

Long term efforts (once finished initial RAD/PSP research) are:
  * ~~Stack trace and variable inspection window (debugger/shell)~~ **DONE**
  * ~~a GUI visual design tool~~ **DONE** (partially using [gui2py](https://code.google.com/p/gui2py/), integration needs improvements)
  * ~~fix debugger issues and/or make/use a Remote Debugger~~ **DONE** see QdbRemotePythonDebugger
  * support web2py remote file edition, debugging and ticket support (started, work ahead...)