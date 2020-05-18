# Guild Experiments

This project illustrates running a simple [MNIST training
operation](main.py) using Guild in two ways:

- Run as an operation defined in a [Guild file](guild.yml)
- Run using a Python [wrapper script](wrapper.py)

Run the operation defined in the Guild file, use the `guild` command:

    $ guild run main

Run the operation using the Python wrapper:

    $ python wrapper.py

Both approaches generate a run that can be viewed using the various
Guild commands or the `ipy` interface.

Command line:

    $ guild runs

Using Python shell

    >>> from guild import ipy as guild
    >>> guild.runs()
