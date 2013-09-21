Tox.im
==================

Source code for the Tox.im website

Building the site
=================

Building the site requires Python 3 and the pystache library.  
In the main directory, run ``python3 buildsite.py``.  
The site will be in the new ``site/`` directory.

Translations
============

As well as new translations, improvement of translations we already have is welcome too. Just copy ``index.en.json`` to ``index.??.json``, where ``??`` is your language's [Zend locale name](http://framework.zend.com/manual/1.12/en/zend.locale.appendix.html).  
If the language you are translating to has more than one dialect (for example: Brazilian Portuguese vs Portuguese Portuguese), you can add ``_??`` before ``.json``, where ``??`` is a unique code for your dialect. A full example: ``index.pt_BR.json`` Capitalization **does** matter!

#### Please **use LF (Unix) line endings in your json files**, or **else Kud will never forgive you**. Even on Windows, a decent editor like Notepad++ will let you do this!

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
- English
- French

(A strong and trustworthy method for verification is in the process of formulation. As of yet, no translation is 100% approved.)

**Needing verification (from someone who isn't the original translator)**:

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
- Arabic
- Norwegian
- Chinese
- Lithuanian
- Croatian
- Finnish
