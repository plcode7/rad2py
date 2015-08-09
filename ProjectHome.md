<a href='https://github.com/reingart/rad2py'><img src='https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png' alt='Fork me on GitHub' border='0' align='right' /></a>

## rad2py Features ##

**Updated!:** for more info see wiki RoadMap, ScreenShots, InstallationGuide, ResearchThesis, CodingStandard and CountingStandard


### ide2py ###

This project aims to provide a modern, cross-platform, fully-featured and totally integrated development environment ([IDE](http://en.wikipedia.org/wiki/Integrated_development_environment) - [CASE](http://en.wikipedia.org/wiki/Computer-aided_software_engineering)) for Python, including:
  * Interactive Shell with Introspection
  * Stylized Code Editor (based on [Scintilla](http://www.scintilla.org/)):
    * Autocompletion & Calltips (thanks [jedi](http://jedi.jedidjah.ch/en/latest/)!)
    * Highlight Syntax error, style issues ([pep8](http://www.python.org/dev/peps/pep-0008/)), static checks ([pyflakes](https://launchpad.net/pyflakes)) and doctests
  * Incorporated QdbRemotePythonDebugger
    * Remote Shell with introspection & Console redirection
    * Edit and continue (fix small typo errors on the fly!)
    * Quick inspect variables on mouse hover
    * Call stack and locals/globals pane
  * Repository support ([mercurial](http://mercurial.selenic.com/) by now)
    * File browser and local edition
    * Commands: Add, Remove, Commit, etc.
  * Visual side-by-side Diff, using [wxpydiff](http://code.google.com/p/wxpydiff/)
  * Visual Unittest integration, using [pytong](http://code.google.com/p/pytong/)
  * Fluid GUI Interface designer (HTML like) [gui2py](http://code.google.com/p/gui2py/)
  * Deployment Tools support (py2exe or similar) _pending_
  * Legacy Visual Basic application migration, using [vb2py](http://code.google.com/p/vb2py/) _experimental_

![https://rad2py.googlecode.com/hg/screenshots/ide2py-0.05-ubuntu.png](https://rad2py.googlecode.com/hg/screenshots/ide2py-0.05-ubuntu.png)

### psp2py ###
Optional application to support the Carnnegie Mellon's SEI  [Personal Software Process](http://en.wikipedia.org/wiki/Personal_software_process) (TM) for automatic metric recollection and continuous improvement:
  * Storage of historical metric for statistical analysis (defect, times, LOCs)
  * Estimation tools and performance reports
  * Simple Project Management (wiki & issues) tracking system

## Research, Motivation and Goals ##

This work is done initially as my degree thesis (see this [initial article](http://docs.google.com/View?id=0Af_UYqYT4LNaZGQ5Ym04MmdfOWhkeHI1d2hj),  [progress report](https://docs.google.com/document/pub?id=1xG1_6AZaJenYeYhZcvWoGXxWA1jd4qzyECVuDNDzsJM), [full degree thesis document](http://t.co/SsMfYDGJ), [academic paper](http://41jaiio.sadio.org.ar/sites/default/files/17_EST_2012.pdf) and ongoing [master's thesis project](https://docs.google.com/document/d/1Jo-_Nf_vMeKvszEuWA24yrfrqGGU-T73cczMPSBZ9ss/edit?usp=sharing)), based on my personal experience and academic research, and it is intended to be used either for educational purposes and in real world commercial applications.

This project was motivated by the lack of a simple VB-like tool for python (knowing its drawbacks and lesson learned after using it) , but mostly by Python "IDEs" annoyances (specially by IDLE gotchas in the teaching room trying to teach Python, and also by the loss of productivity of such tools in my professional work for IT companies as freelancer).

The goal of this project is to be as simple as possible (i.e. an overhauled IDLE), so there is no plans to developed a plugin system (I think being python-based and open source is extensible enough) and no other language, web framework, ORM or GUI toolkit will be integrated (altough this project tools may be used to develop general python programs).
There are plenty of other good specific tools that already support them.


While ide2py can be useful with other frameworks and toolkits, DAL and other gluon ([web2py base libraries](http://en.wikipedia.org/wiki/Web2py)) will be adopted to unify and enable development of data-centric applications (relational model, and [PostgreSQL](http://www.postgresql.org/) will be the preferred backend for production):
  * Command line interface scripts
  * Visual interfaces using [gui2py](http://code.google.com/p/gui2py/) (wxPython based)
  * Web applications using [web2py](http://code.google.com/p/web2py/) (WSGI compilant)
  * Legacy application migration from VB using [vb2py](http://code.google.com/p/vb2py/) (EBNF tool)

Additionally, to prevent common pitfalls of [RAD](http://en.wikipedia.org/wiki/Rapid_application_development) regarding software quality, this aproach will follow [Personal Software Process](http://en.wikipedia.org/wiki/Personal_Software_Process) guidelines:
  * Planning, Design, Code, Review, Postmortem phases
  * Automatic Code size counting (LOC), time and defect log recording
  * Task Estimation and reporting

To avoid developer overload, this project will explore [task-focused interfaces](http://en.wikipedia.org/wiki/Task-focused_interface) like [Eclipse Mylyn](https://www.eclipse.org/mylyn/), and [Agile Application Lifecycle Management](http://en.wikipedia.org/wiki/Application_lifecycle_management)

## Status ##

The initial proof-of-concept is based on wx examples (demo skeletons), and many parts were inspired/influenced by activegrid wx sample (pyide), wxpydev, pyragua, picalo, SPE, pythonwin, Ninja-IDE, DrPython and IDLE

The **previous status** (2012-01-13) is a working experimental prototype that support an integrated editor, debugger, interactive shell, repository explorer and PSP metric collection tools (some rough edges but totally functional, including support to web2py)

gui2py integration is underway (started on 2013), see the [screenshot of gui2py visual tools in ide2py](https://gui2py.googlecode.com/hg/screenshots/win8/rad2py_ide2py_gui2py_integration.png)

vb2py project integration will be started on 2014

Final integrated prototype is expected to be available on January, 2015

## News ##

  * [Academic paper](http://www.41jaiio.org.ar/sites/default/files/17_EST_2012.pdf) & Poster (Spanish) presented at [JAIIO 2012](http://www.41jaiio.org.ar/) [students works symposium](http://www.41jaiio.org.ar/sites/default/files/ProgramaEST.pdf)
  * [Poster (English)](http://4.bp.blogspot.com/-jYxb1QphXHI/T3MGLFDrXOI/AAAAAAAAANE/ouFgCr7Umxg/s1600/rad2py.png) at [PyCon US 2012](https://us.pycon.org/2012/schedule/presentation/147/)
  * [Full degree thesis document](http://t.co/SsMfYDGJ) (Dec. 2011)
  * Article at [PyAr Magazine](http://revista.python.org.ar/4/es/html/rad2py.html) 4th ed., distributed at [PyCon Argentina 2011](http://ar.pycon.org/2011) ([presentation talk](http://ar.pycon.org/2011/activity/accepted/1))
  * Ongoing [Master's Thesis Project Plan](https://docs.google.com/document/d/1Jo-_Nf_vMeKvszEuWA24yrfrqGGU-T73cczMPSBZ9ss/edit?usp=sharing) (Open University of Catalonia, Master's degree program on Free Software) **New!**