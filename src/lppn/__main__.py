#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
import sys

# https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/#running-a-command-line-interface-from-source-with-src-layout
if not __package__:
    # Make CLI runnable from source tree with
    #    python src/package
    package_source_path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, package_source_path)

import argparse
from lppn import lppn

def main():
    parser = argparse.ArgumentParser(description='Print the latest Python patch number of a given major and minor version')
    parser.add_argument('--full-version', '-f', action='store_true', help='Print full version')
    parser.add_argument('major', type=int, help='Major Python version e.g. 3')
    parser.add_argument('minor', type=int, help='Minor Python version e.g. 12')
    args = parser.parse_args()

    patch = lppn.get(args.major, args.minor)
    if args.full_version:
        print(f'{args.major}.{args.minor}.{patch}')
    else:
        print(patch)

if __name__ == "__main__":
    main()

