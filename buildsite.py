#!/usr/bin/env python3
from __future__ import print_function
import json
import os
import pystache
import re
import shutil
import sys

def do_format_template(name, template):
    basename = ".".join(name.split(".")[:-1])
    if not basename:
        return
    print("Enumerating languages... ", end="")
    language_files = [lf for lf in os.listdir(os.getcwd())
                      if lf.endswith(".json") and lf.startswith(basename + ".")]
    print("{0} found.".format(len(language_files)))
    renderer = pystache.renderer.Renderer()
    lang_values = {}
    lang_list = []
    for language in language_files:
        language = language.split(".")[-2]
        if not re.match(r"^[a-z0-9\-]+$", language):
            continue
        if not os.path.isdir(os.path.join("site", language)):
            os.mkdir(os.path.join("site", language))
        with open("{0}.{1}.json".format(basename, language), "r") as lf:
            values = json.load(lf)
        for key in values:
            if isinstance(values[key], str):
                values[key] = values[key].replace("\n", "<br>")
        lang_list.append({"lang_name": values["_language"],
                          "lang_shortcode": language,
                          "ind": values["_ind"]})
        lang_values[language] = values
    lang_list.sort(key=lambda x: x["ind"])
    for language in language_files:
        language = language.split(".")[-2]
        with open("site/{1}/{0}.html".format(basename, language), "w") as outfile:
            outfile.write(renderer.render(template, lang_values[language], languages=lang_list))

def main():
    if not os.path.isdir(os.path.join(os.getcwd(), "site")):
        os.mkdir("site")
    if os.path.isdir(os.path.join("site", "assets")):
        shutil.rmtree(os.path.join("site", "assets"))
    shutil.copytree("assets", os.path.join("site", "assets"))
    templates = [tp_name for tp_name in os.listdir(os.getcwd())
                 if tp_name.endswith(".mustache")]
    for template_name in templates:
        with open(template_name) as tmp_file:
            print("Building template {0}.".format(template_name))
            do_format_template(template_name, tmp_file.read())

if __name__ == "__main__":
    main()