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
atom-beautify
atomic-emacs
auto-detect-indentation
autoclose-html
autocomplete-python
file-icons
git-time-machine
highlight-selected
language-restructuredtext
linter
linter-flake8
markdown-scroll-sync
minimap
minimap-highlight-selected
open-recent
python-jedi
python-nosetests
python-tools
rst-preview
todo-show
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
