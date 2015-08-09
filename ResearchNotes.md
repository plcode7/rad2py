# Introduction #

Notes taken from Oct. / Nov. / Dec. 2014 for my research master thesis, for more info see [project plan](https://docs.google.com/document/d/1Jo-_Nf_vMeKvszEuWA24yrfrqGGU-T73cczMPSBZ9ss/edit?usp=sharing)


# Ideas / Issues #

  * Turn off camera when psp phase is stopped (privacy?)
  * ~~Integrated Browser for planning!~~
  * PSP defect not marked as resolved after load
  * Better integrated method for psp planning? spreadshet? (summing times per method, like psp2py)
  * Sum columns in PSP timetable (totals)
  * Design via wiki?
  * Issue comments!!!!
  * In design mode, do not mark syntax errors?...
  * Text file editor / Blank scratch par for taking notes
  * Automatic change planning -> design -> code -> compile...
  * Store fold and unfold events
  * Mark resolved syntax error once file is saved correctly
  * Integrated visual diff is broken!!! (needs update)
  * Integrated mercurial support is broken!!! (needs update)
  * PSP defect line is not detected correctly (escalate the traceback upside to avoid marking errors in third-party libraries)
  * Automatic fix pep8 / pyflakes errors?
  * Adjust line number in defects when source code changes (maybe using uuid to track source code line in metadata/editor)
  * Investigate some dubious "defects" detected by pyflakes, how to ignore? (i.e. trivial or unrelated defects in other parts of the program -check fold/unfold?-)
  * Add spell-checker! (for comments, commit messages and maybe variable names)
  * IDE doesn't close cleanly if not correctly if a browser tab is open
  * Also, open browser tabs un-blocking mode (background thread?)
  * Copy PSP data between project (planed times!)
  * Assign Issue automatically when start planning
  * Issue description is insuficient to do any real requeriment planification & analisis (GitHub doesn't support attachments...)
  * ~~Fix Issue automatic resizing (down border)~~
  * ~~Allow to deactivate a task... (not selecting anyone from the choice...)~~
  * When starting a new task, select "planning" and close open files
  * When suspending or closing, avoid asking the interruption comment: "phone call"
  * When selecting task, show title!!!!
  * On task change, repository is not correctly updated? (check)
  * How to detect internal errors defects (i.e. catched by try/except block)
  * Fix syntax error detection in the same line -currently ignored as not fixed- (compare the string?), or reopen the defect?
  * Add defect doesn't work with accents (unicode...)
  * ~~Reduce startup time (don't fetch issue from GitHub, avoid PSP webservice)~~ _this also allows multiple sessions open of the IDE at once_

# Documentation #

## Installation ##

  * Add webkit dependencies: `sudo apt-get install python-webkit libwebkit-dev`
  * Add python dependencies: `sudo apt-get install python pep8 pyflakes`