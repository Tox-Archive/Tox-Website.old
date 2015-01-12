import os.path

def reply(msg):

    try:
        lang = msg['header']['Accept-Language'].split(',')[0].split('-')[0]
    except:
        try:
            lang = msg['header']['accept-language'].split(',')[0].split('-')[0]
        except:
            lang = 'en'

    if msg['header']['PATH'] == '/downloads':
        return {"code": 302, "msg": "wiki", "header": {"Location": "https://wiki.tox.im/Binaries"}}

    if msg['header']['PATH'] == '/tox.pdf':
        return {"code": 302, "msg": "Jenkins forward", "header": {"Location": "https://jenkins.libtoxcore.so/job/Technical_Report/lastSuccessfulBuild/artifact/tox.pdf/"}}

    if msg['header']['PATH'].startswith('/f/'):
        loc = msg['header']['PATH'].split('/', 2)[2]
        return {"code": 200, "msg": "About to view a site off Tox.im, are you sure you'd like to <a href='/forward/" + loc + "'>continue?</a>"}

    if msg['header']['PATH'].startswith('/forward/'):
        loc = msg['header']['PATH'].split('/', 2)[2]
        return {"code": 302, "msg": "wiki", "header": {"Location": loc}}

    if msg['header']['PATH'] != '/assets':
        if msg['header']['PATH'] != '/':
            lang = msg['header']['PATH'].split('/', 1)[1]
            if os.path.isfile("/etc/osiris/app/tox/site/" + lang + ".html") == False:
                lang = "en"

    if msg['header']['PATH'].startswith('/assets'):
        return {"code": 200, "file": msg['header']['PATH'].split('/', 1)[1]}
    else:
        return {"code": 200, "file": "site/" + lang + ".html", "header": {"X-Powered-By": 'OSIRIS Mach/4'}}
