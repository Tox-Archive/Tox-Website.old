#!/usr/bin/env python
# quality.py - check up-to-dateness of TLs.
# Author: stal (at) zodiaclabs.org, July 2014
# Copyright (c) 2014 Zodiac Labs.

from __future__ import print_function
from __future__ import unicode_literals
import sys
import os

try:
    import simplejson
except ImportError:
    import json as simplejson

def do_tlc(name, lang):
    name = name[:name.rfind(".mustache")]
    print("Beginning TLC on {0}.".format(name))
    print("Using {0}.{1}.json as a base.".format(name, lang))
    with open("{0}.{1}.json".format(name, lang), "r") as master:
        master_kvlist = simplejson.load(master)

    others = [lf for lf in os.listdir(os.getcwd())
              if lf.endswith(".json") and lf.startswith(name + ".")]
    others.remove("{0}.{1}.json".format(name, lang))
    for lf in others:
        with open(lf, "r") as sf:
            check_values = simplejson.load(sf)

        warnings = []
        def cw(b, s):
            b.append(s)

        for key in master_kvlist:
            if key not in check_values:
                cw(warnings, "\033[32mmissing key\033[0m: \"{0}\".".format(
                   key, master_kvlist[key].replace("\n", "\\n")))
                cw(warnings, "Please translate the string: \"{0}\" "
                             "and insert it into the file.".format(
                   master_kvlist[key]))

        for key in check_values:
            if key not in master_kvlist:
                cw(warnings, "\033[31mextraneous key\033[0m: \"{0}\": {1}".format(
                      key, check_values[key].replace("\n", "\\n")))
                cw(warnings, "You should remove it from the file.")

        if warnings:
            print("----- {0} warnings for {1}. -----".format(len(warnings), lf))
            for w in warnings:
                print(w)
            print("")
    print("TLC on {0} complete.".format(name))

def main(master):
    templates = [tp_name for tp_name in os.listdir(os.getcwd())
                 if tp_name.endswith(".mustache")]
    for template_name in templates:
        print("Checking {0}.".format(template_name))
        if sys.version_info.major == 2:
            do_tlc(template_name, master)
        else:
            do_tlc(template_name, master)

if __name__ == '__main__':
    main(sys.argv[1])
