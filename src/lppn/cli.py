#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import lppn


def parse():
    parser = argparse.ArgumentParser(
        description=(
            "Print the latest Python patch number of a given major and minor"
            " version"
        )
    )
    parser.add_argument(
        "--full-version", "-f", action="store_true", help="Print full version"
    )
    parser.add_argument("major", type=int, help="Major Python version e.g. 3")
    parser.add_argument("minor", type=int, help="Minor Python version e.g. 12")
    args = parser.parse_args()

    patch = lppn.get(args.major, args.minor)
    if args.full_version:
        print(f"{args.major}.{args.minor}.{patch}")
    else:
        print(patch)