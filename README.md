# FUNLP

Sandbox for messing around with Natural Language Processing (NLP).

# Getting Setup

Dylan, this section describes how to get started by setting up your environment and some other useful tips that I use when doing development. We'll mainly be using Python, so I'll be focusing on it. I'll provide instructions for Linux/Mac right now and I can try and help you get it setup on Windows sometime.

## Operating System

**Ubuntu Linux**

I use this distribution of Linux. It is well supported and maintained with a new stable release every 2 years.

The latest stable release is 16.04\. It can be downloaded from: [Ubuntu 16.04.1](https://www.ubuntu.com/download/desktop) [Follow this link for the instructions](https://www.ubuntu.com/download/desktop/install-ubuntu-desktop). You have to make sure the device you put the `.iso` image that you download on a DVD or USB and then boot from that device from the BIOS. You may have to change the BIOS settings which can be accessed on startup by pressing a certain key (often F10 or F12).

You could have it installed side-by-side with Windows or in a virtual machine. There are a couple of nice free ones:

- [Oracle's VirtualBox](https://www.virtualbox.org/wiki/Downloads) (this is the one that I use)
- [VMWare's Workstation Player](http://www.vmware.com/products/player/playerpro-evaluation.html)

## Editors

### Atom

I use atom all the time. It is "hackable", so there are plenty of great plugins for autocompletion, minimaps, syntax highlighting for different languages, and so on. It is available for all OSs.

[Download Atom](https://atom.io/) run it through a compiler The plugins can be accessed from `Edit` in the menu bar and then `Preferences`. Some useful plugins that I use are:

```
(env3) adam@case:~/dylan/nlp$ apm list --installed --bare
atom-beautify@0.29.13
atomic-emacs@0.9.2
auto-detect-indentation@1.3.0
autoclose-html@0.23.0
autocomplete-python@1.8.11
file-icons@1.7.25
git-time-machine@1.5.4
highlight-selected@0.11.2
language-restructuredtext@1.0.1
linter@1.11.18
linter-flake8@2.0.2
markdown-scroll-sync@2.1.2
minimap@4.25.6
minimap-highlight-selected@4.4.0
open-recent@5.0.0
python-jedi@0.3.8
python-nosetests@0.2.0
python-tools@0.6.8
rst-preview@1.3.1
todo-show@1.8.0
```

### Notepad++

This is a nice cross-platform text editor that doesn't have the learning curve you might experience with Atom. It is basically a significantly enhanced Notepad for developers.

[Download Notepad++](https://notepad-plus-plus.org/)

### IDEs

Alternative to more basic text editors you can also use an integrated development environment. I started out using different IDEs in college. While they may be easier to use at the start, they don't force you to learn some useful features or ideas of languages like compiler flags and build tools.

Some popular ones include:

- [Eclipse](https://eclipse.org/downloads/) has support for many languages
- [Thonny](http://thonny.cs.ut.ee/) looks like a good tool for beginning programmers and python learners (my recommendation if you want help understanding the python language and essential programming concepts)
- [Komodo Edit](http://www.activestate.com/komodo-edit) multi-language support, free version is "Edit"

## Python

There are 2 major branches of Python, Python 2 and Python 3\. Python 2.7 is widely used but is not being actively enhanced. Python 3+ (latest version is 3.5) is the future so we'll stick to using it.

### Installation

#### Linux

Linux already comes with Python, but you should upgrade to the latest version with the following commands from the terminal:

```
sudo apt update
sudo apt upgrade python3
```

Now type

```
python3 --version
Python 3.5.2
```

Check that the version is 3.5.x.

#### Windows

I think you'll have to download from their website or you can download from a well maintained distribution.

[See a list of them here.](https://wiki.python.org/moin/PythonDistributions)

I've tried a few of them. [Anaconda Python](https://www.continuum.io/downloads) is probably the best for our purposes.

Download and install the Python 3.5 version (make sure to choose the proper byte size) using the defaults. It will install python as well as a package manager called `conda`. Open up the Anaconda command prompt (should be installed in the start menu or the Desktop). Then run:

```
conda list
```

If successfully installed, this will list the python packages it already has installed. First, make sure your current packages are up to date. Remember these commands and run it often:

```
conda update conda
conda update anaconda   # updates all packages
```

Be sure the packages we want to use will be installed, so run the following commands and install those that are missing and any dependencies that need to be installed:

```
conda install git
conda install pip
conda install jupyter
conda install ipython
conda install wget
conda install curl
conda install numpy
conda install scipy
conda install scikit-learn
conda install setuptools
conda install nltk
conda install pandas
conda install matplotlib
conda install networkx
```

This should be plenty to get us started. Most of the tools you see later on will now be available on Windows as well, but let me know if you have any trouble.

### Learning Python

The best way to get started is to learn the fundamental programming concepts. But, that is not always practical. So, start by just diving into some code, which is what we are doing.

I can add recommendations if you like for resources.

### Managing Packages

To manage your python packages, use Python's package manager `pip`. It is extremely useful, and keeps things nice and neat for you rather than having to install a bunch of packages from their source files. It actually goes and grabs the latest version from a website that maintains all the latest version of distributed python packages called PyPI (the Python Package Index). `pip` should be already installed for you.

For example to install the useful `ipython` for enhanced use of interactive python.

```
pip install ipython
```

Then to remove it you can do:

```
pip uninstall ipython
```

Most command line programs like python, pip, etc. will list their use if you use the `--help` flag.

```
pip --help

Usage:   
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  ...
```

### Virtual environments

I recommend getting use to using virtual environments because you may have multiple projects where it is useful to isolate their environment settings from each other. For Python, the most common virtual environment tool is `virtualenv`.

Install it with `pip`.

```
pip install virtualenv
```

#### Creating the virtualenv

To create a virtual environment go to the directory you want to install it in and run

```
virtualenv --python=python3 env3
```

The `--python=python3` just specifies the python executable to be used in this virtual environment instance. `env3` is just my convention for naming Python3 virtual environments. You can use any name you want.

It will take a few seconds for the new virtual environment to be setup. There will now be a folder in the directory named `env3`. This hosts all the information for the virtual environment and deleting this folder removes it.

#### Starting the virtualenv

To start the virtual environment you need to run:

```
source env3/bin/active
```

You'll notice a `(env3)` added to the beginning of your terminal prompt when you are in the virtual environment.

#### Exiting the virtualenv

To get out of the virtual environment just run:

```
deactivate
```

### Basics of Using Python

Python is both a high-level, general purpose language, so it is good for many tasks although not the most efficient.<br>
It is often used as "glue" between distinct systems since it has widely supported on different platforms and systems as it is easily extensible

A core concept behind the design of Python is for it to be easy for a human read and hopefully with fewer lines needed.

There are many programming concepts built-in to Python. These include object-oriented, imperative, and functional programming.

Another benefit of Python is that it can be used interpretively (kind of like the command line), scripting, or creating large packages that have many classes and methods.

#### Using an Interpreter

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

#### Python Package Management

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

#### Python Scripts

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

#### Python Methods and Classes

TODO

#### About Lists

TODO

#### Structure of a Python Package

TODO

#### Further Reading

There is far too much to learn about Python than I can put here. Some useful references are:

- TODO

## Basics of Git with GitHub

Since we'll be using `git` as our version control software. I'll give you the basics for using it. I will expand it as we use new features. Basically, a version control software helps keep track of committing changes to code and helping organize those changes among multiple developers.

There are other version source control tools like `svn`, `mercurial`, or whatever Team Foundation Server (Microsoft). However, git has become the de-facto standard in almost all new open source projects and all the cool kids do it :P! But practically I have found it to work really well and very helpful when merging code and keeping track of commits. It also doesn't hurt that we use Github to host all our open source code and they add a lot of nice features on top of it, such as the concept of forking (note: this is not a standard git term).

### Overview of versioning

One important concept to understand is that you will have a local and remote repository. Each "contributor" to a project has their own local repository where they commit and make changes while they are developing/working on the project. The remote repository (in this case hosted on GitHub) is the central location that all code from the "contributors" gets committed to in order to maintain a main repository. Multiple "contributors" are usually working the code base at any time, so it is important to keep track of all commits (versions of the code) and be able to merge them together quickly. If this is not done correctly things become a huge mess quickly! It is easier to understand with examples, but important concepts will be to understand will be _branching_, _pushing_, _pulling_, and _merging_ that help us keep things managed nicely.

Fun fact Linus Torvalds, the creator of Linux, also originally designed git.

### Further resources

1. Instead of using the command line, you can use the user interface program `gitk`.

2. A simple guide to using git and a good reference to quickly find commonly used commands. <http://rogerdudler.github.io/git-guide/>

3. GitHub's guides to using git and github. <https://guides.github.com/>

4. CodeAcademy course for git. <https://www.codecademy.com/learn/learn-git>

### Installation

#### Windows

My recommendation is to use the solution from this website <https://git-for-windows.github.io/>.

#### Linux

Just make sure it is installed with

```
sudo apt install git
```

### Cloning this repo

There are a few different ways to do this, but the basic syntax is: `git clone <repo> [<dir>]`. The `<repo>` is usually the website for the project, which for GitHub projects is located on the homepage of the project. See the image below.

![GitHub Cloning](https://github.com/awig/FUNLP/blob/master/images/GitHub_cloning.png)

The `[<dir>]` is the directory to which the repository will be installed, which defaults to the name of the repository. I highly recommend you leave the name the same, unless you have a very good reason to do otherwise.

As you can see the home for this repo in SSH format (don't worry about what this means at this time) `git@github.com:awig/FUNLP.git` or in HTTPS format `https://github.com/awig/FUNLP.git`. Therefore, we can use one of the following commands to clone this repo:

Using the SSH format:

```
git clone git@github.com:awig/FUNLP.git
```

or using the HTTPS format:

```
git clone https://github.com/awig/FUNLP.git
```

Since we left the `[<dir>]` optional argument off, it will download everything to the default repository _FUNLP_.

Now change to this directory and check the contents of the folder look somewhat similar to what I show below:

```
cd FUNLP
ls   # in windows use "dir" instead of "ls"
> README.md                    hangman.py                   install_nltk_data.py     images/                      run_nltk_examples.py
```

### Understanding branches

A _branch_ in git is basically a copy of the code that can be worked on without changing the code other contributors are working on. All repositories have a default branch called _master_. To see which branch of this repository you are on run:

```
git branch
> * master
```

There is probably only going to be the master branch shown. It is also often useful to see which remote repository each branch points to, which can be done with `git branch -vv`. It will list the latest commit as well as the name of the remote repository, which will be `origin/master`. `origin` is just the default name given to the remote repository. You can link to different remote repositories so it is often good to give them helpful names, but we won't worry about that now.

A very simple idea of the workflow for branching can be found here <http://rogerdudler.github.io/git-guide/img/branches.png>.

In general, you create a separate branch when you are working on a new feature (in this case _feature_x_). After you have developed and tested it, you can then _merge_ it back into the _master_ branch. It can get much more complicated, but it all boils down to these basic steps. Now let's try it out.

### Pulling the latest commits

First, it is always a good idea to make sure you have the latest code, this is accomplished by running a _pull_ command which goes and fetches and checks out the latest remote repository branch:

```
git pull
```

You should see `Already up-to-date.` as the response for the obvious reason.

### Creating a new branch

Now create a new branch called `dylans_feature`:

```
git checkout -b dylans_feature
```

The `-b` tells it to create and checkout this new branch. It is important to know that this new branch is only created locally at first and any changes we make will not automatically get committed to the remote repository.

If you run `git branch -vv`, you will see that this new branch has no remote repository connected to it and that the asterisk `*` now points to this new branch.

### Adding a new branch to remote repository

Now let's add this new branch to the remote repository. This is simple _push_ command with the structure `git push <repo> <branch>`, where `<repo>` is the name of the remote repository, which for this case is just _origin_, and `<branch>` is the name of the branch you want to add to the repository, which for this case is _dylans_feature_.

```
git push origin dylans_feature
```

### Committing to the repo

Now create a new file _boring.py_ and copy and paste the code below in it.

```python3
# !/usr/bin/env python3

print("Adam, these instructions are so boring and slow. Let's get to something fun!")
```

Save it and run the script.

Okay, so now we need to add this file to the remote repository. This is a 3 step process:

1. _add_ the files or changed files, known as _staging_
2. _commit_ the additions (don't worry about the details of this for now) and it is important to always put a message when committing using `-m`.
3. _push_ the commitments to the remote repository (similar to what we already did for the branch)

```
git add boring.py
git commit -m "first commit of boring.py"
git push
```

That should be it, you've now have the new branch on the repository. It is a good idea, if you are ever not sure if you committed something or what you have added, to run `git status` to check.

```
git status
```

### Merging branches

Once you have gone through the trouble of testing that the code on your branch is working, documented, and tested well. You can merge the changes back into the master branch. This is an important step, as there may be conflicts in the code that need to be resolved.

To merge your branch you must do the following steps

1. Checkout the branch (we call it the up-stream branch) we want to merge with, in this case it is _master_.
2. Run the merge command. It will notify you of conflicts in the code or you can run `git status` to check.
3. Resolve conflicts that are found. They will need to changed then added and committed as before in [Committing to the repo](#Committing-to-the-repo).

```
git checkout master
git merge dylans_feature
# resolve conflicts here
git push
```

#### Pull requests on GitHub

GitHub allows you to do a _pull request_ (PR for short) instead of doing a merge right away. The good point of doing PRs is so that maintainer gets notified about you wanting to merge your code and can review it before approving it. We'll use pull requests before merging big changes, as it is good practice.

See <https://help.github.com/articles/creating-a-pull-request/> how to do a pull request.

### Deleting branches

It is easy to delete a branch if it is only local with `git branch -d <branch>`. Ff it is on the remote repository you must be careful not to remove someone else's work, but is basically the same but adding the remote repository name before the branch name.

Let's create a new local branch `delete-me` and delete it. Note that you can't delete a branch you are currently on, so you have to be on a different branch.

```
git branch -b delete-me
git checkout master
git branch -d delete-me
```

### Removing changes and resetting

If you accidentally added something and want to undo it, take this command `git checkout -- <file>`, where `<file>` is the name of the file you want to revert to last committed change.

For example to remove any changes you made to the README file:

```
git checkout -- README.md
```

If you want to revert your whole working tree to a different commit and remove _ALL_ local changes you can run the command `git reset --hard <repo>/<branch>`. Only do this if you are absolutely sure that you don't need any of your local changes.

For example, to revert everything back to the remote repository's master branch:

```
git reset --hard origin/master
```

# Natural Language Processing

# License

No license

# Contributors

- Adam Wigington
- Dylan Fuhs
