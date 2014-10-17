"""
This is the OSIRIS model currently powering tox.im.
How to use: move me to app/tox.py
git clone this
mv this to app/tox
run buildsite.py like normal
add mod = tox to a domain and restart
"""

def reply(msg):

	try:
		lang = msg['header']['Accept-Language'].split(',')[0].split('-')[0]
	except:
		lang = 'en'
		
	if msg['header']['PATH'] != '/assets':
		if msg['header']['PATH'] != '/':
			lang = msg['header']['PATH'].split('/',1)[1]

	if msg['header']['PATH'].startswith('/assets'):
		return { "code": 200, "file": msg['header']['PATH'].split('/',1)[1] }
	else:
		return { "code": 200, "file": "site/" + lang + ".html" }
