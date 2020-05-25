# create admin with username and password

import re
import sys

import requests

import gitlab


URL = 'http://localhost'
SIGN_IN_URL = 'http://localhost/users/sign_in'
LOGIN_URL = 'http://localhost/users'

session = requests.Session()

sign_in_page = session.get(SIGN_IN_URL).content
count = 0
token = None
for l in sign_in_page.split('\n'):
    m = re.search('name="authenticity_token" value="([^"]+)"', l)
    if m:
	count += 1
	if count == 1:
		break 

if m:
    token = m.group(1)

if not token:
    print('Unable to find the authenticity token')
    sys.exit(1)

data = {'new_user[name]': 'Yuqi',
	'new_user[username]': 'root2',
	'new_user[email]': 'jinyq1997@gmail.com',
	'new_user[email_confirmation]': 'jinyq1997@gmail.com',	
	'new_user[password]': 'password',
	'authenticity_token': token}
        
r = session.post(LOGIN_URL, data=data)
if r.status_code != 200:
    print('Failed to register')
    sys.exit(1)







