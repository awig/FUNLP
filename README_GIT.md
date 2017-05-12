# Basics of Git with GitHub

Since we'll be using `git` as our version control software. I'll give you the basics for using it. I will expand it as we use new features. Basically, a version control software helps keep track of committing changes to code and helping organize those changes among multiple developers.

There are other version source control tools like `svn`, `mercurial`, or whatever Team Foundation Server (Microsoft). However, git has become the de-facto standard in almost all new open source projects and all the cool kids do it :P! But practically I have found it to work really well and very helpful when merging code and keeping track of commits. It also doesn't hurt that we use Github to host all our open source code and they add a lot of nice features on top of it, such as the concept of forking (note: this is not a standard git term).

## Overview of versioning

One important concept to understand is that you will have a local and remote repository. Each "contributor" to a project has their own local repository where they commit and make changes while they are developing/working on the project. The remote repository (in this case hosted on GitHub) is the central location that all code from the "contributors" gets committed to in order to maintain a main repository. Multiple "contributors" are usually working the code base at any time, so it is important to keep track of all commits (versions of the code) and be able to merge them together quickly. If this is not done correctly things become a huge mess quickly! It is easier to understand with examples, but important concepts will be to understand will be _branching_, _pushing_, _pulling_, and _merging_ that help us keep things managed nicely.

Fun fact Linus Torvalds, the creator of Linux, also originally designed git.

## Further resources

1. Instead of using the command line, you can use the user interface program `gitk`.

2. A simple guide to using git and a good reference to quickly find commonly used commands. <http://rogerdudler.github.io/git-guide/>

3. GitHub's guides to using git and github. <https://guides.github.com/>

4. CodeAcademy course for git. <https://www.codecademy.com/learn/learn-git>

## Installation

### Windows

My recommendation is to use the solution from this website <https://git-for-windows.github.io/>.

### Linux

Just make sure it is installed with

```
sudo apt install git
```

## Cloning this repo

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

## Understanding branches

A _branch_ in git is basically a copy of the code that can be worked on without changing the code other contributors are working on. All repositories have a default branch called _master_. To see which branch of this repository you are on run:

```
git branch
> * master
```

There is probably only going to be the master branch shown. It is also often useful to see which remote repository each branch points to, which can be done with `git branch -vv`. It will list the latest commit as well as the name of the remote repository, which will be `origin/master`. `origin` is just the default name given to the remote repository. You can link to different remote repositories so it is often good to give them helpful names, but we won't worry about that now.

A very simple idea of the workflow for branching can be found here <http://rogerdudler.github.io/git-guide/img/branches.png>.

In general, you create a separate branch when you are working on a new feature (in this case _feature_x_). After you have developed and tested it, you can then _merge_ it back into the _master_ branch. It can get much more complicated, but it all boils down to these basic steps. Now let's try it out.

## Pulling the latest commits

First, it is always a good idea to make sure you have the latest code, this is accomplished by running a _pull_ command which goes and fetches and checks out the latest remote repository branch:

```
git pull
```

You should see `Already up-to-date.` as the response for the obvious reason.

## Creating a new branch

Now create a new branch called `dylans_feature`:

```
git checkout -b dylans_feature
```

The `-b` tells it to create and checkout this new branch. It is important to know that this new branch is only created locally at first and any changes we make will not automatically get committed to the remote repository.

If you run `git branch -vv`, you will see that this new branch has no remote repository connected to it and that the asterisk `*` now points to this new branch.

## Adding a new branch to remote repository

Now let's add this new branch to the remote repository. This is simple _push_ command with the structure `git push <repo> <branch>`, where `<repo>` is the name of the remote repository, which for this case is just _origin_, and `<branch>` is the name of the branch you want to add to the repository, which for this case is _dylans_feature_.

```
git push origin dylans_feature
```

## Committing to the repo

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

## Merging branches

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

### Pull requests on GitHub

GitHub allows you to do a _pull request_ (PR for short) instead of doing a merge right away. The good point of doing PRs is so that maintainer gets notified about you wanting to merge your code and can review it before approving it. We'll use pull requests before merging big changes, as it is good practice.

See <https://help.github.com/articles/creating-a-pull-request/> how to do a pull request.

## Deleting branches

It is easy to delete a branch if it is only local with `git branch -d <branch>`. Ff it is on the remote repository you must be careful not to remove someone else's work, but is basically the same but adding the remote repository name before the branch name.

Let's create a new local branch `delete-me` and delete it. Note that you can't delete a branch you are currently on, so you have to be on a different branch.

```
git branch -b delete-me
git checkout master
git branch -d delete-me
```

## Removing changes and resetting

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
