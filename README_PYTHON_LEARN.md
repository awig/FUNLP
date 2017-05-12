# Basics of Using Python

Python is both a high-level, general purpose language, so it is good for many tasks although not the most efficient.<br>
It is often used as "glue" between distinct systems since it has widely supported on different platforms and systems as it is easily extensible

A core concept behind the design of Python is for it to be easy for a human read and hopefully with fewer lines needed.

There are many programming concepts built-in to Python. These include object-oriented, imperative, and functional programming.

Another benefit of Python is that it can be used interpretively (kind of like the command line), scripting, or creating large packages that have many classes and methods.

## Using an Interpreter

The easy way to get started with Python after installing it is just to type `python` from the terminal/command-line. This starts the python interpreter and then you can run a command like `2+6` and it will interpret the code in real-time without having to explicitly run it through a compiler (like you would need to do in C or Fortran).

```
(env3) adam@case:~/dylan/nlp/funlp$ python
Python 3.5.2 (default, Sep 10 2016, 08:21:44)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 2+6
8
>>>
```

I prefer using `ipython` for the interactive python environment instead of just the default you get with `python`. You can start it with just typing `ipython` instead:

```
(env3) adam@case~/dylan/nlp/funlp$ ipython
Python 3.5.2 (default, Oct 11 2016, 05:05:28)
Type "copyright", "credits" or "license" for more information.

IPython 5.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.
```

As you can see there are some useful commands and macros that can be run instantly. Try typing `?` and `%quickref` as it suggests. For instance, now you can list the elements of the current directory from within the interactive prompt by typing `%ls` or even just `ls`. You may also notice that changes the prompt colors and has autocomplete. These are wonderful time savers to have.

## Python Package Management

A package manager is a program for a language or system that manages the install, uninstall and record keeping of non-standard library packages.

For Python, `pip` is the _de-facto_ package manager that you need to get familiar with. It can be used to install packages from the different distribution methods for Python libraries or will search the official online repository of python packages called the [Python Package Index (PyPI)](https://pypi.python.org/pypi). There are literally 10's of thousands or even 100s of thousands of packages available there.

For example, to install the Natural Language Toolkit (NLTK) we will be using run this command from the command prompt:

```

pip install nltk
```

To uninstall this same package is it as easy as executing:

```

pip uninstall nltk
```

## Python Scripts

Python files have the extension `.py`. Create a file named `example.py` and copy the following code into it.

```
# !/usr/bin/env python

# This first line is for Unix systems, it tells the system to use the current environment's python
# to run this program if none is specified. You may easily ignore it in Window.

"""
This is an example python script that calculates the size of each subdirectory in a given directory and prints a summary graphic.
It simply runs from the start of the file to the end. This is often just referred to as a \"script\".

Run this command with an argument that is the directory you would like to analyze. If none is given it defaults to the current directory. Be careful which directory you select or it may take awhile or even crash.

An example of how to run it from the command prompt with two directories back selected.
  python graph_dir_size.py "../.."

A copy of this file is provided in the repo.
"""

# first import packages you will use
import os           # operating system tools/interfaces
import numpy        # we need this for arrays
import networkx     # we need this for creating graph structures
import matplotlib   # we need this for creating visual graphics
```

## Python Methods and Classes

TODO

## About Lists

TODO

## Structure of a Python Package

TODO

## Further Reading

There is far too much to learn about Python than I can put here. Some useful references are:

- TODO

# Python Library Structure

TODO

/funlp/ /fake-news/ /_.py_ /data/ /_.csv_, _.txt_ /tests/ /docs/ _setup.py_ _README.md_ _CHANGELOG.md_
