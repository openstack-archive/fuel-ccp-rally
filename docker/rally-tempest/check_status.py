#!/usr/bin/env python

from __future__ import print_function

import json
import sys


def main():
    with open(sys.argv[1]) as f:
        data = json.load(f)
    failures = data["verifications"].values()[0]["failures"]
    if failures == 0:
        print("Tests succeeded!")
        sys.exit(0)
    else:
        print("Tests failed: %d." % failures)
        sys.exit(1)


if __name__ == "__main__":
    main()
