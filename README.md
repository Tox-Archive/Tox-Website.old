ProjectTox-Website
==================

Source code for the Tox.im website

Building the site
=================

Building the site requires Python 3 and the pystache library.  
In the main directory, run ``python3 buildsite.py``.  
The site will be in the new ``site/`` directory.

Translations
============

As well as new translations, improvement of translations we already have is welcome too. Just copy ``index.en.json`` to ``index.??.json``, where ``??`` is your language's [ISO 639 code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).  
If the language you are translating to has more than one dialect (for example: Brazilian Portuguese vs Portuguese Portuguese), you can add ``-??`` before ``.json``, where ``??`` is a unique code for your dialect. A full example: ``index.pt-br.json``

Language file metadata
----------------------

The JSON files used by buildsite.py have some special names which are used by the script to build the bar of languages in the footer. The names are:

``_language``: The (native) name of your language. Example: *Français*  
``_ind``: Leave this as it is.  
``_comment``: A comment about the language file. Optional.  
``_author``: The creator(s) of the file.

What we have so far
===================

**Verified**:

(A strong and trustworthy method for verification is in the process of formulation. As of yet, no translation is 100% approved.)

**Needing verification (from someone who isn't the original translator)**:

- English
- German
- Russian
- Italian
- Dutch
- Polish
- Brazilian Portuguese
- Portuguese Portuguese
- Swedish
- Turkish
- Spanish
- French
- Arabic
- Norwegian
- Chinese
- Lithuanian
- Croatian
- Finnish
