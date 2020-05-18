import os
import subprocess
import sys

import click

from guild import ipy

from main import base_train


@click.command()
@click.option("--epochs", default=10, help="Epochs to train.")
def main(**kw):
    ipy.run(base_train, **kw)


if __name__ == "__main__":
    main()
