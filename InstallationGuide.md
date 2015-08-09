ASAP there will be installation packages for download, sorry for the
inconvenience.

In the meantime, follow the following steps to install the components.

# ide2py Quick Install #

ide2py is the main desktop application to edit and debug python scripts and web2py application.

The basic installation steps are:

  * Get [python 2.7+](http://python.org/download/) and [wxPython 3.0+](http://www.wxpython.org/download.php) (the latest, 3.0.2 recommended)
  * Install [jedi](https://github.com/davidhalter/jedi#installation) (autocompletion library)
  * Optionally dependencies:
    * For repository browser, get [mercurial](http://mercurial.selenic.com/downloads/)
    * For psp support  install
      * [simplejson](http://pypi.python.org/pypi/simplejson/) (only for python2.5)
      * [OpenCV](http://www.opencv.org/) + [NumPy](http://www.numpy.org/) (only for face recognition to track timing autommatically)
    * For statical checkers install:
      * [pep8.py](http://pypi.python.org/pypi/pep8)
      * [pyflakes](http://pypi.python.org/pypi/pyflakes/)
    * For the GitHub connector install [githubpy](https://github.com/michaelliao/githubpy/blob/master/github.py)
  * [Download](http://code.google.com/p/rad2py/downloads/list) or Clone rad2py repository: `hg clone https://code.google.com/p/rad2py/`
  * Download and unzip [web2py](http://www.web2py.com/examples/static/web2py_src.zip) into rad2py folder. **NOTE**: you should replace gluon/contrib/qdb.py (shipped with web2py) with the ide2py updated version ([qdb.py](https://rad2py.googlecode.com/hg/ide2py/qdb.py)) if to be able to debug properly (until web2py master trunk gets updated)
  * Change directory to rad2py/ide2py
  * Execute `python main.py`

**Important:** Remember to configure ide2py.ini after the first run (basic settings are in ide2py.ini.dist)

# psp2py Quick Install #

psp2py is a web2py application to store your personal metrics and do reporting and estimates.

The installation steps are:

  * Download and unzip web2py (may be the same used by ide2py)
  * Copy or symlink rad2py/psp2py to web2py/applications folder
  * Start a separate standalone server `python web2py.py`

**Note:** this webapp is optional, you can run ide2py without it (of course, some PSP extensions features will not work in that case).

# Tested Environments #

These are the known compatible versions of python and wxPython:

Ubuntu 14.04:
```
Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import wx
w>>> wx.version()
'3.0.2.0 gtk2 (classic)'
```

Windows 8.1:
```
Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)] on win
32
Type "help", "copyright", "credits" or "license" for more information.
>>> import wx
>>> wx.version()
'3.0.2.0 msw (classic)'
```