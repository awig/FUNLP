# Getting Setup with Python

There are 2 major branches of Python, Python 2 and Python 3\. Python 2.7 is widely used but is not being actively enhanced. Python 3+ (latest version is 3.6) is the future so we'll stick to using it.

## Installation

### Linux

Linux already comes with Python, but you should upgrade to the latest version with the following commands from the terminal:

```
sudo apt update
sudo apt upgrade python3
```

Now type,

```
python3 --version
Python 3.5.2
```

Check that the version is 3.5.x.

### Windows

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

## Navigating Your Python Environment

The best way to get started is to learn the fundamental programming concepts. But, that is not always practical. So, start by just diving into some code, which is what we are doing.

I can add recommendations if you like for resources.

### Package Management

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

### Python Virtual Environments

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
