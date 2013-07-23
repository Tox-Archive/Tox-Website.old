#!/usr/bin/env python
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
        if not re.match(r"^[A-Za-z0-9_.]+$", language):
            continue
        with open("{0}.{1}.json".format(basename, language), "r") as lf:
            try:
                values = json.load(lf)
            except ValueError:
                print("Error in {0}.{1}.json!".format(basename, language))
                raise
        for key in values:
            if isinstance(values[key], str):
                values[key] = values[key].replace("\n", "<br>")
        lang_list.append({"lang_name": values["_language"],
                          "lang_shortcode": language,
                          "ind": values["_ind"]})
        lang_values[language] = values
    lang_list.sort(key=lambda x: x["lang_shortcode"])
    lang_list[-1]["last"] = 1
    for language in language_files:
        language = language.split(".")[-2]
        with open("site/{1}.html".format(basename, language), "w") as outfile:
            if sys.version_info.major == 2:
                outfile.write(renderer.render(template, lang_values[language],
                              languages=lang_list).encode("utf-8"))
            else:
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
            if sys.version_info.major == 2:
                do_format_template(template_name, tmp_file.read().decode("utf-8"))
            else:
                do_format_template(template_name, tmp_file.read())

if __name__ == "__main__":
    main()