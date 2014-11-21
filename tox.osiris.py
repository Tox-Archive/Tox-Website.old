def runonce():
    return {}


def reply(msg):

    try:
        lang = msg['header']['Accept-Language'].split(',')[0].split('-')[0]
    except:
        lang = 'en'

    if msg['header']['PATH'] == '/ip_stats':
        dat = "<p>"
        for ip in msg['runonce']:
            dat = dat + \
                '%s has visited this page %s times<br>' % (
                    ip, msg['runonce'][ip])
        dat += "</p><br>" + \
            str(msg['runonce'])
        return {"code": 200, "msg": dat}

    if msg['header']['PATH'] == '/downloads':
        return {"code": 301, "msg": "wiki", "header": {"Location": "https://wiki.tox.im/Binaries"}}

    if msg['header']['PATH'] == '/tox.pdf':
        return {"code": 301, "msg": "Jenkins forward", "header": {"Location": "https://jenkins.libtoxcore.so/job/Technical_Report/lastSuccessfulBuild/artifact/tox.pdf/"}}

    if msg['header']['PATH'].startswith('/request301/'):
        loc = msg['header']['PATH'].split('/', 2)[2]
        return {"code": 200, "msg": "About to view a site off Tox.im, are you sure you'd like to <a href='/forward/" + loc + "'>continue?</a>", "header": {"Content-Type": 'text/html'}}

    if msg['header']['PATH'].startswith('/forward/'):
        loc = msg['header']['PATH'].split('/', 2)[2]
        return {"code": 301, "msg": "wiki", "header": {"Location": loc}}

    if msg['header']['PATH'] != '/assets':
        if msg['header']['PATH'] != '/':
            lang = msg['header']['PATH'].split('/', 1)[1]

    if msg['header']['PATH'].startswith('/assets'):
        return {"code": 200, "file": msg['header']['PATH'].split('/', 1)[1]}
    else:
        return {"code": 200, "file": "site/" + lang + ".html", "header": {"Content-Type": 'text/html', "X-Powered-By": 'OSIRIS Mach/4'}}
