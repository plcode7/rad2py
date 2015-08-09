# Qdb: a really simple remote client/server debugger for Python #

## What? ##

  * Python Bdb (stdlib) based debugger
  * Remote: attachable from external processes (even on other machines)
  * Client/Server: a backend designed to run with several frontends (wx,  web2py, etc.)
  * Simple & Small: just a enhanced Pdb

## Why? ##

  * pdb is text only (and local process), this causes big troubles with wx and web servers
  * [rpdb2](http://code.google.com/p/winpdb/source/browse/rpdb2.py) (winpdb) is too complex to use/extend in my case (rpdb2 is 14500 LOC against ~700 LOC of this script)
  * I need this for a totally integrated IDE I'm writing (see [rad2py](http://code.google.com/p/rad2py/))
  * IPC/RPC Flexibility: supports Threading Queues, Multiprocessing Pipes and Sockets
  * Cross-Version (py2.6+ & py3k), Cross-Platform (win/linux/mac interoperability)  _(work in progress)_

## How? ##

  * [bdb](http://docs.python.org/library/bdb.html):  Python Debugger framework
  * [multiprocessing](http://docs.python.org/library/multiprocessing.html): [listeners/clients](http://docs.python.org/library/multiprocessing.html#multiprocessing-listeners-clients): queue/pipe communication (serialization w/ pickle) **requires python 2.6+**
  * [JSON-RPC](http://json-rpc.org/wiki/specification): JSON-like Remote Procedure Call protocol over stream connections (see also [simplejsonrpc.py](http://code.google.com/p/rad2py/source/browse/ide2py/simplejsonrpc.py) in this project)
  * [Cmd](http://docs.python.org/library/cmd.html): cmd — Support for line-oriented command interpreters
  * [wxpython](http://www.wxpython.org): toolkit for visual interface

## Download ##

Just one file: [qdb.py](http://code.google.com/p/rad2py/source/browse/ide2py/qdb.py) (download [raw file](http://rad2py.googlecode.com/hg/ide2py/qdb.py))


## Commands ##

The Command Line Interface accepts is very similar to [pdb](http://docs.python.org/library/pdb.html):

  * `c`: Continue execution, only stop when a breakpoint is encountered.
  * `s`: Execute the current line, stop at the first possible occasion
  * `n`: Execute the current line, do not stop at function calls
  * `r`: Continue execution until the current function returns
  * `p`: Inspect the value of the expression
  * `w`: Print a stack trace, with the most recent frame at the bottom.
  * `l [from:to]`: List source code for the current file
  * `j lineno`: Set the next line that will be executed.
  * `b filename:lineno`: Set a breakpoint at filename:breakpoint
  * `h`: help
  * `q`: Quit from the debugger. The program being executed is aborted.

For more information, see: [pdb debugger commands](http://docs.python.org/library/pdb.html#debugger-commands)

## Usage ##

### Standalone ###

First, ensure you have qdb.py installed in your python path (or in the current directory).

The call the python interpreter with the option `-m qdb` and your script name. This will load your program under qdb debugging.

Sample Session in the backend:

```
reingart@desktop:~/rad2py/ide2py$ python -m qdb hola.py
qdb debugger backend: waiting for connection at ('localhost', 6000)
qdb debugger backend: connected to ('127.0.0.1', 52322)
```

Then, in other terminal, run the python interpreter with the option `-m qdb` only. This will launch the qdb attached to the debugging session.

Sample session in the frontend (Command Line Interface):
```
reingart@desktop:~/rad2py/ide2py$ python -m qdb
qdb debugger fronted: waiting for connection to ('localhost', 6000)
running   hola.py
> hola.py(3)
-> name = raw_input("please write your name:")
(Cmd) n
please write your name: mariano
> hola.py(4)
-> print "hello", name
(Cmd) !name = 'Mariano'
None
> hola.py(4)
-> print "hello", name
(Cmd) n
hello   Mariano
> hola.py(6)
-> def factorial(n):
(Cmd) l
hola.py:   1    # sample file to test shell & debugger
hola.py:   2
hola.py:   3    name = raw_input("please write your name:")
hola.py:   4    print "hello", name
hola.py:   5
hola.py:   6->  def factorial(n):
hola.py:   7        """This is the "factorial" function
hola.py:   8        >>> factorial(5)
hola.py:   9        120
hola.py:  10
hola.py:  11        """
```

Note: `(Cmd)` is the prompt, just type your command (i.e. `n`) and hit enter.

### Web2py / Django ###

First, copy qdb.py to your system path, in web2py copy it to the modules directory of the application:
```
copy qdb.py C:\web2py\applications\welcome\modules
```

Then, edit the controller or the model script inserting `import qdb; qdb.set_trace()`:
```
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html
    """
    response.flash = "Welcome to web2py!"
    import qdb; qdb.set_trace()
    return dict(message=T('Hello World'))
```

Finally, open the webpage, for example http://localhost:8000/welcome/default/index. The browser will wait until you open a terminal and issue `python -m qdp`:
```
C:\rad2py\ide2py>python qdb.py
qdb debugger fronted: waiting for connection to ('localhost', 6000)
> C:\web2py\applications\welcome\controllers/default.py(19)
->     return dict(message=T('Hello World'))
(Cmd) p response.flash
Welcome to web2py!
> C:\web2py\applications\welcome\controllers/default.py(19)
->     return dict(message=T('Hello World'))
(Cmd) c
```

For django and others web frameworks, it should be similar, just import qdb and call set\_trace.

**Note**: you can change the address / port and password to connect to remote servers over the internet. See the qdb source.

For a full web user interface, see this blog post:

http://reingart.blogspot.com/2012/02/new-web2py-online-python-debugger.html

### Visual interface ###

_Comming soon_

See ScreenShots for early development.

## Py3k ##

You can convert this to Python 3.2 using 2to3:
```
C:>c:\Python32\python.exe c:\python32\Tools\Scripts\2to3.py -w qdb.py
```

Remember to change `authkey=b'secret password'` as in python3 it requires bytes for the authentication key.

Then, you can run it:
```
C:\rad2py\ide2py>c:\Python32\python.exe qdb.py
waiting for connection to ('192.168.248.3', 6000)
running   hola.py
 hola.py:   3   name = raw_input("please write your name:")
 (Cmd) l
```

Interoperability between operating systems works (tested a Windows 7 32 bits connected to Ubuntu 11.10 64 bits), but py2 to py3 debug fails because the new picke protocol version 3:
```
reingart@desktop:~/rad2py/ide2py$ python2.7 qdb.py hola.py
waiting for connection at ('192.168.248.3', 6000)
connection accepted from ('192.168.248.8', 57649)
Traceback (most recent call last):
  File "/home/reingart/tesis/rad2py/ide2py/qdb.py", line 60, in user_line
    self.interaction(frame)
  File "/home/reingart/tesis/rad2py/ide2py/qdb.py", line 137, in interaction
    request = self.pipe.recv()
ValueError: unsupported pickle protocol: 3
```


**TODO**: changing to multiprocessing.connection.XmlClient and multiprocessing.connection.XmlListener would do the trick (or developing a JSON client/listener would be even better)