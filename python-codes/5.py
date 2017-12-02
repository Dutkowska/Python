Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> pliczek=open('plik').read()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    pliczek=open('plik').read()
FileNotFoundError: [Errno 2] No such file or directory: 'plik'
>>> pliczek=open(C:\Users\Paula\Documents\python\plik.txt).read()
SyntaxError: invalid syntax
>>> pliczek=open('C:\Users\Paula\Documents\python\plik.txt').read()
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> pliczek=open('C:\Users\Paula\Documents\python\plik').read()
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> help(open)
Help on built-in function open in module io:

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    Open file and return a stream.  Raise IOError upon failure.
    
    file is either a text or byte string giving the name (and the path
    if the file isn't in the current working directory) of the file to
    be opened or an integer file descriptor of the file to be
    wrapped. (If a file descriptor is given, it is closed when the
    returned I/O object is closed, unless closefd is set to False.)
    
    mode is an optional string that specifies the mode in which the file
    is opened. It defaults to 'r' which means open for reading in text
    mode.  Other common values are 'w' for writing (truncating the file if
    it already exists), 'x' for creating and writing to a new file, and
    'a' for appending (which on some Unix systems, means that all writes
    append to the end of the file regardless of the current seek position).
    In text mode, if encoding is not specified the encoding used is platform
    dependent: locale.getpreferredencoding(False) is called to get the
    current locale encoding. (For reading and writing raw bytes use binary
    mode and leave encoding unspecified.) The available modes are:
    
    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================
    
    The default mode is 'rt' (open for reading text). For binary random
    access, the mode 'w+b' opens and truncates the file to 0 bytes, while
    'r+b' opens the file without truncation. The 'x' mode implies 'w' and
    raises an `FileExistsError` if the file already exists.
    
    Python distinguishes between files opened in binary and text modes,
    even when the underlying operating system doesn't. Files opened in
    binary mode (appending 'b' to the mode argument) return contents as
    bytes objects without any decoding. In text mode (the default, or when
    't' is appended to the mode argument), the contents of the file are
    returned as strings, the bytes having been first decoded using a
    platform-dependent encoding or using the specified encoding if given.
    
    'U' mode is deprecated and will raise an exception in future versions
    of Python.  It has no effect in Python 3.  Use newline to control
    universal newlines mode.
    
    buffering is an optional integer used to set the buffering policy.
    Pass 0 to switch buffering off (only allowed in binary mode), 1 to select
    line buffering (only usable in text mode), and an integer > 1 to indicate
    the size of a fixed-size chunk buffer.  When no buffering argument is
    given, the default buffering policy works as follows:
    
    * Binary files are buffered in fixed-size chunks; the size of the buffer
      is chosen using a heuristic trying to determine the underlying device's
      "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.
      On many systems, the buffer will typically be 4096 or 8192 bytes long.
    
    * "Interactive" text files (files for which isatty() returns True)
      use line buffering.  Other text files use the policy described above
      for binary files.
    
    encoding is the name of the encoding used to decode or encode the
    file. This should only be used in text mode. The default encoding is
    platform dependent, but any encoding supported by Python can be
    passed.  See the codecs module for the list of supported encodings.
    
    errors is an optional string that specifies how encoding errors are to
    be handled---this argument should not be used in binary mode. Pass
    'strict' to raise a ValueError exception if there is an encoding error
    (the default of None has the same effect), or pass 'ignore' to ignore
    errors. (Note that ignoring encoding errors can lead to data loss.)
    See the documentation for codecs.register or run 'help(codecs.Codec)'
    for a list of the permitted encoding error strings.
    
    newline controls how universal newlines works (it only applies to text
    mode). It can be None, '', '\n', '\r', and '\r\n'.  It works as
    follows:
    
    * On input, if newline is None, universal newlines mode is
      enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
      these are translated into '\n' before being returned to the
      caller. If it is '', universal newline mode is enabled, but line
      endings are returned to the caller untranslated. If it has any of
      the other legal values, input lines are only terminated by the given
      string, and the line ending is returned to the caller untranslated.
    
    * On output, if newline is None, any '\n' characters written are
      translated to the system default line separator, os.linesep. If
      newline is '' or '\n', no translation takes place. If newline is any
      of the other legal values, any '\n' characters written are translated
      to the given string.
    
    If closefd is False, the underlying file descriptor will be kept open
    when the file is closed. This does not work when a file name is given
    and must be True in that case.
    
    A custom opener can be used by passing a callable as *opener*. The
    underlying file descriptor for the file object is then obtained by
    calling *opener* with (*file*, *flags*). *opener* must return an open
    file descriptor (passing os.open as *opener* results in functionality
    similar to passing None).
    
    open() returns a file object whose type depends on the mode, and
    through which the standard file operations such as reading and writing
    are performed. When open() is used to open a file in a text mode ('w',
    'r', 'wt', 'rt', etc.), it returns a TextIOWrapper. When used to open
    a file in a binary mode, the returned class varies: in read binary
    mode, it returns a BufferedReader; in write binary and append binary
    modes, it returns a BufferedWriter, and in read/write mode, it returns
    a BufferedRandom.
    
    It is also possible to use a string or bytearray as a file for both
    reading and writing. For strings StringIO can be used like a file
    opened in a text mode, and for bytes a BytesIO can be used like a file
    opened in a binary mode.

>>> f=open('plik', 'r')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    f=open('plik', 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'plik'
>>> f=open('C:\Users\Paula\Documents\python\plik', 'r')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> path='C:\Users\Paula\Documents\python\plik.txt'
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> path = 'C:\Users\Paula\Documents\python\plik.txt'
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> path = '/Users/Paula/Documents/python/plik.txt'
>>> plik = open(path,'r')
>>> plik.read()
'123456789'
>>> plik[1:2]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    plik[1:2]
TypeError: '_io.TextIOWrapper' object is not subscriptable
>>> plik(1:2)
SyntaxError: invalid syntax
>>> plik[2]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    plik[2]
TypeError: '_io.TextIOWrapper' object is not subscriptable
>>> plik[[2]]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    plik[[2]]
TypeError: '_io.TextIOWrapper' object is not subscriptable
>>> plik.readline()
''
>>> plik.readlines()
[]
>>> plik.close()
>>> plik.read()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    plik.read()
ValueError: I/O operation on closed file.
>>> plik = open(path, 'r')
>>> plik.read()
'123456789\nabcdefghi'
>>> plik.readline()
''
>>> plik.readlines()
[]
>>> zmienna=plik.read()
>>> zmienna[2:3]
''
>>> plik.close()
>>> plik = open(path, 'w').write('tekst')
>>> plik.read()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    plik.read()
AttributeError: 'int' object has no attribute 'read'
>>> plik.close()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    plik.close()
AttributeError: 'int' object has no attribute 'close'
>>> plik = open(path,'r')
>>> plik.read()
'tekst'
>>> plik.close()
>>> plik=open(path, 'w')
>>> plik.write('text')
4
>>> plik.close()
>>> plik=open(path, 'r')
>>> plik.open()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    plik.open()
AttributeError: '_io.TextIOWrapper' object has no attribute 'open'
>>> plik.read()
'text'
>>> plik.close()
>>> lista=['1','2','3']
>>> plik=open(path, 'w')
>>> plik.writelines(lista)
>>> plik.close()
>>> plik=open(path, 'r')
>>> plik.read()
'123'
>>> lista=["1", "2", "3"]
>>> plik=open(path, 'w')
>>> plik.writelines(lista)
>>> plik.readline()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    plik.readline()
io.UnsupportedOperation: not readable
>>> plik.close()
>>> plik = open(path, 'r')
>>> plik.readlines()
['123']
>>> plik.readline()
''
>>> plik.read()
''
>>> plik.close()
>>> plik=open(path, 'r')
>>> plik.read()
'123'
>>> plik.close()
>>> plik = open(path, 'a')
>>> plik.write('abc')
3
>>> plik.close()
>>> plik=open(path, 'a')
>>> plik.read()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    plik.read()
io.UnsupportedOperation: not readable
>>> plik.close()
>>> plik=open(path, 'r')
>>> plik.read()
'123abc'
>>> plik.close()
>>> plik=open(path, 'a')
>>> plik.write('\n987zyx')
7
>>> plik.close()
>>> plik=open(path, 'r')
>>> plik.read()
'123abc\n987zyx'
>>> plik.close()
>>> plik=open(path, 'r')
>>> plik.readlines()
['123abc\n', '987zyx']
>>> plik.readline(1)
''
>>> plik.readline(0)
''
>>> plik.readline()
''
>>> plik.close()
>>> plik=open(path, 'r')
>>> plik.readline()
'123abc\n'
>>> plik.readline()
'987zyx'
>>> plik.close()
>>> plik=open(path).readlines()
>>> cel=open(path, 'w')
>>> for s in plik:
	cel.write(s.replace("abc", "ABC"))
cel.close()
SyntaxError: invalid syntax
>>> for s in plik:
	cel.write(s.replace("abc", "ABC"))

	
7
6
>>> cel.close()
>>> cel=open(path, 'r').read()
>>> cel.read()
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    cel.read()
AttributeError: 'str' object has no attribute 'read'
>>> cel.close()
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    cel.close()
AttributeError: 'str' object has no attribute 'close'
>>> pathcel='C:\Users\Paula\Documents\python\cel.txt'
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> pathcel = '/Users/Paula/Documents/python/cel.txt'
>>> plik.close()
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    plik.close()
AttributeError: 'list' object has no attribute 'close'
>>> plik=open(path).readlines()
>>> cel=open(pathcel, 'w')
>>> for s in plik:
	cel.write(s.replace("ab", "jk"))

	
7
6
>>> cel.close()
>>> cel=open(pathcel, 'r')
>>> cel.read()
'123ABC\n987zyx'
>>> cel.close()
>>> plik.open(path).readlines()
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    plik.open(path).readlines()
AttributeError: 'list' object has no attribute 'open'
>>> plik=open(path).readlines()
>>> cel=open(pathcel, 'w')
>>> for s in plik:
	cel.write(s.replace("12", "00"))

	
7
6
>>> cel.close()
>>> cel=open(pathcel, 'r')
>>> cel.read()
'003ABC\n987zyx'
>>> cel.close()
>>> plik=open(path, 'r')
>>> import linecache
>>> wiersz=linecache.getline(path, 1)
>>> print(wiersz)
123ABC

>>> wiersz=linecache.getline(path, 2)
>>> print(wiersz)
987zyx

>>> print(linecache.getline(path,2))
987zyx

>>> count=len(open(path, 'rU').readlines())
>>> print(count)
2
>>> print(len(open(path, 'rU').readlines()))
2
>>> 
