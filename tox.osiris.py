def runonce():
    return {}


def reply(msg):
    print msg['header']
    try:
        lang = msg['header']['Accept-Language'].split(',')[0].split('-')[0]
    except:
        lang = 'en'

    ip = msg['ip']
    try:
        msg['runonce'][ip] += 1
    except:
        msg['runonce'][ip] = 1

    if msg['header']['PATH'] == '/ip_stats':
        dat = "<p>"
        for ip in msg['runonce']:
            dat = dat + \
                '%s has visited this page %s times<br>' % (
                    ip, msg['runonce'][ip])
        dat += "</p><br>" + str(msg['runonce'])
        print msg['runonce']
        return {"code": 200, "msg": dat}

    if msg['header']['PATH'] == '/downloads':
        return {"code": 301, "msg": "wiki", "header": {"Location": "https://wiki.tox.im/Binaries"}}

    if msg['header']['PATH'] != '/assets':
        if msg['header']['PATH'] != '/':
            lang = msg['header']['PATH'].split('/', 1)[1]

    if msg['header']['PATH'].startswith('/assets'):
        return {"code": 200, "file": msg['header']['PATH'].split('/', 1)[1]}
    else:
        return {"code": 200, "file": "site/" + lang + ".html", "header": {"Content-Type": 'text/html', "X-Powered-By": 'OSIRIS Mach/4'}}
