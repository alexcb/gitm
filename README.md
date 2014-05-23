gitm
====

Git'm -- a tool for dealing with multiple git repos.

Requirements
============

Python3
blessings library

In development
==============

This is still under initial development, commands that work are:

    alexcb$ python3.4 gitm status
    ~/Desktop/funproject                  3 modified
    ~/Documents/git/tracker               10 untracked
    ~/github/alexcb/python_utils          Clean

or run any command across all repos with:

    python3.4 gitm -- <user command>

for example

    python3.4 gitm -- pwd

    python3.4 gitm -- git checkout -b new_branch_everywhere
