Tox.im
==================

Source code for the Tox.im website

Building the site
=================

Building the site requires Python 2 or Python 3 and the pystache library.  
In the main directory, run ``python buildsite2.py`` for python 2 and run ``python3 buildsite.py`` for python 3.  
The site will be in the new ``site/`` directory.

To make the folder layout do the following:  
Move in to the site folder ``cd site``  
Make a list of all the languages ``ls | tr ' ' '\n' | grep html | tr '.' '\n' | grep -v 'html' > list``.  
Make a folder for every language ``cat list | xargs mkdir``.  
Move a language in to a folder ``cat list | xargs -I % mv %.html %/index.html``.  
Make an index page ``ln -s en/index.html .`` Change en to a default language  
cat list | xargs -I % ln -s assets %
Remove the list file ``rm list``  

Translations
============

As well as new translations, improvement of translations we already have is welcome too. Just copy ``index.en.json`` to ``index.??.json``, where ``??`` is your language's [Zend locale name](http://framework.zend.com/manual/1.12/en/zend.locale.appendix.html).  
If the language you are translating to has more than one dialect (for example: Brazilian Portuguese vs Portuguese Portuguese), you can add ``_??`` before ``.json``, where ``??`` is a unique code for your dialect. A full example: ``index.pt_BR.json`` Capitalization **does** matter!

#### Please **use LF (Unix) line endings in your json files**. Even on Windows, a decent editor like Notepad++ will let you do this!

Language file metadata
----------------------

The JSON files used by buildsite.py have some special names which are used by the script to build the bar of languages in the footer. The names are:

``_language``: The (native) name of your language. Example: *Français*  
``_ind``: Leave this as it is.  
``_comment``: A comment about the language file. Optional.  
``_author``: The creator(s) of the file.  
``_direction``: ``rtl`` or ``ltr`` only. Specifies the text direction of the language. If you leave this key out, it will be left-to-right.

What we have so far
===================

**Verified**:
- English
- French (@irungentoo)
- German (@sudden6)
- Russian (@stqism)
- Hebrew (@GreenLunar)
- Arabic (@Tanjoodo)

*Note: You can still submit pull requests for verified languages.*

**Needing verification (from someone who isn't the original translator)**:

*everything else not listed above*
