# Unclosed File Resource Leak in Python

This repository demonstrates a common but easily overlooked error in Python: failing to close a file after opening it. This can lead to resource exhaustion and unexpected behavior.

## The Bug

The `bug.py` file contains a function `function_with_unclosed_file` which opens a file for reading but neglects to close it. This leaves the file open, consuming system resources. The longer the program runs and more files opened in this way the worse this becomes. 

## The Solution

The `bugSolution.py` demonstrates the correct way to handle file operations: using a `with` statement. The `with` statement guarantees that the file will be closed automatically, even if exceptions occur.